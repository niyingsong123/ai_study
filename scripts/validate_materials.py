"""Independently check saved files, navigation, and local article copies offline."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlparse
import hashlib
import json
import re
import xml.etree.ElementTree as ET

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'source-manifest.json'
OUTPUT = ROOT / 'material-validation.json'
manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
records = manifest['sources']
errors = []
checks = {'batch': manifest['batch'], 'scope': 'Archive integrity, local navigation, image parsing, source/reader table text and merge markup; no full HTML visual audit.',
          'files': [], 'images': [], 'articles': [], 'links': [], 'errors': errors}


def require(condition, message):
    if not condition:
        errors.append(message)


class ArticleParser(HTMLParser):
    """Independent parser, deliberately separate from the reader generator."""
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.active_tables = []
        self.active_cells = []
        self.images = []
        self.heading = None
        self.headings = []
        self.script_depth = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag in ('script', 'style'):
            self.script_depth += 1
        if self.script_depth:
            return
        if tag == 'table':
            table = {'rows': []}
            self.tables.append(table)
            self.active_tables.append(table)
        if tag == 'tr' and self.active_tables:
            self.active_tables[-1]['rows'].append([])
        if tag in ('td', 'th') and self.active_tables:
            if not self.active_tables[-1]['rows']:
                self.active_tables[-1]['rows'].append([])
            cell = {'tag': tag, 'rowspan': attrs.get('rowspan', '1'), 'colspan': attrs.get('colspan', '1'), 'text': ''}
            self.active_tables[-1]['rows'][-1].append(cell)
            self.active_cells.append(cell)
        if tag == 'br':
            for cell in self.active_cells:
                cell['text'] += ' '
        if tag == 'img' or (tag == 'image' and attrs.get('src')):
            self.images.append(attrs.get('data-src') or attrs.get('src') or attrs.get('data-original') or '')
        if tag in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            self.heading = {'tag': tag, 'text': ''}

    def handle_startendtag(self, tag, attributes):
        self.handle_starttag(tag, attributes)
        if tag not in ('img', 'br', 'hr', 'meta', 'link', 'source', 'input', 'image'):
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.script_depth = max(0, self.script_depth - 1)
            return
        if self.script_depth:
            return
        if tag in ('td', 'th') and self.active_cells:
            self.active_cells.pop()
        if tag == 'table' and self.active_tables:
            self.active_tables.pop()
        if self.heading and tag == self.heading['tag']:
            self.headings.append(re.sub(r'\s+', ' ', self.heading['text']).strip())
            self.heading = None

    def handle_data(self, data):
        if self.script_depth:
            return
        for cell in self.active_cells:
            cell['text'] += data
        if self.heading:
            self.heading['text'] += data

    def normalized_tables(self):
        for table in self.tables:
            for row in table['rows']:
                for cell in row:
                    cell['text'] = re.sub(r'\s+', ' ', cell['text']).strip()
        return self.tables


require(len(records) == 65, 'Expected 65 registered stable source IDs')
require(len({row['source_id'] for row in records}) == len(records), 'Duplicate source ID')
require(len({row['note_path'] for row in records}) == len(records), 'Duplicate source note path')
require(sorted(row['source_id'] for row in records) == [f'AI{i:03d}' for i in range(1, 66)], 'Missing source ID')
require(sum(row['status'] == 'archived' for row in records) == manifest['summary']['archived_sources'], 'Archived count mismatch')
require(Counter(row['kind'] for row in records if row['status'] == 'archived') == manifest['summary']['by_kind_archived'], 'Source kind counts mismatch')

owned_docs = {ROOT / name for name in ('README.md', 'sources.md', 'project-context.md', 'research-roadmap.md', 'materials-reading-guide.md', 'source-reading-audit.md', 'original_file/README.md')}
for group, group_counts in manifest['summary']['groups'].items():
    require(sum(row['group'] == group for row in records) == group_counts['registered'], 'Group registration count mismatch: ' + group)
    require(sum(row['group'] == group and row['status'] == 'archived' for row in records) == group_counts['archived'], 'Group archive count mismatch: ' + group)
    owned_docs.update((ROOT / group).rglob('*.md'))

for row in records:
    require((ROOT / row['note_path']).is_file(), 'Missing main note: ' + row['source_id'])
    if row['status'] != 'archived':
        require(not row['files'], 'Failed response counted as an archived original: ' + row['source_id'])
        require((ROOT / row['link_file']).is_file(), 'Missing pending URL file: ' + row['source_id'])
    files = row['files'] + row.get('image_files', [])
    if row.get('reader_file'):
        files.append(row['reader_file'])
    for item in files:
        path = (ROOT / item['path']).resolve()
        require(path.is_relative_to(ROOT), 'Saved file path outside workspace: ' + item['path'])
        if not path.is_file():
            errors.append('Missing saved file: ' + item['path'])
            continue
        content = path.read_bytes()
        ok = len(content) == item['bytes'] and hashlib.sha256(content).hexdigest() == item['sha256']
        require(ok, 'Hash/size mismatch: ' + item['path'])
        checks['files'].append({'path': item['path'], 'sha256_matches': ok, 'bytes': len(content)})
    for item in row.get('image_files', []):
        path = ROOT / item['path']
        try:
            if path.suffix == '.svg' or path.read_bytes().lstrip().startswith((b'<svg', b'<?xml')):
                xml = ET.parse(path)
                require(xml.getroot().tag.endswith('svg'), 'Downloaded XML is not SVG: ' + item['path'])
                result = {'format': 'SVG', 'parsed': True}
            else:
                with Image.open(path) as image:
                    result = {'format': image.format, 'width': image.width, 'height': image.height, 'parsed': True}
                    image.verify()
            checks['images'].append({'path': item['path'], **result})
        except Exception as exc:
            errors.append('Unreadable image: ' + item['path'] + ': ' + str(exc))
    if row.get('reader_path'):
        original_file = next(file for file in row['files'] if file['path'].endswith('.html'))
        source = ArticleParser()
        source.feed((ROOT / original_file['path']).read_text(encoding='utf-8', errors='replace'))
        reader = ArticleParser()
        reader_path = ROOT / row['reader_path']
        reader.feed(reader_path.read_text(encoding='utf-8'))
        original_tables = source.normalized_tables()
        reader_tables = reader.normalized_tables()
        tables_ok = original_tables == reader_tables
        require(tables_ok, 'Source/reader table text or merge markup differs: ' + row['source_id'])
        local_images = 0
        remote_images = set()
        for src in reader.images:
            if src.startswith(('https://', 'http://')):
                remote_images.add(src)
            elif src and not src.startswith('data:'):
                target = (reader_path.parent / unquote(src)).resolve()
                require(target.is_file(), 'Broken local article image: ' + row['source_id'] + ' ' + src)
                local_images += 1
        expected_remote = {failure['url'] for failure in row.get('image_download_failures', [])}
        require(remote_images == expected_remote, 'Unrecorded or missing remote image reference: ' + row['source_id'])
        require(bool(reader.headings), 'Reader has no article headings: ' + row['source_id'])
        require(all(heading in source.headings for heading in reader.headings), 'Reader heading absent from source: ' + row['source_id'])
        checks['articles'].append({'source_id': row['source_id'], 'source_tables': len(original_tables), 'reader_tables': len(reader_tables), 'table_cells_text_order_and_merge_markup_match': tables_ok,
                                   'source_headings': len(source.headings), 'reader_headings': len(reader.headings), 'local_image_references': local_images, 'recorded_remote_images': len(remote_images), 'full_visual_audit': False})


def headings_in(path):
    text = path.read_text(encoding='utf-8')
    headings = []
    for title in re.findall(r'^#{1,6}\s+(.+)$', text, re.M):
        title = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', title).replace('`', '').replace('*', '').lower()
        slug = re.sub(r'[^\w\-\s\u4e00-\u9fff]', '', title).replace(' ', '-')
        headings.append(slug)
    return set(headings)


# The audit links to this result. Create the artifact before checking that link.
OUTPUT.write_text(json.dumps({'batch': manifest['batch'], 'status': 'checking'}, ensure_ascii=False) + '\n', encoding='utf-8')
for document in sorted(owned_docs):
    require(document.is_file(), 'Missing collection entry: ' + str(document))
    if not document.is_file():
        continue
    text = document.read_text(encoding='utf-8')
    for target in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', text):
        target = target.strip().split(' "', 1)[0].strip('<>')
        parsed = urlparse(target)
        if parsed.scheme or target.startswith('//'):
            continue
        local = (document.parent / unquote(parsed.path)).resolve() if parsed.path else document
        exists = local.exists()
        require(exists, f'Broken Markdown link: {document.relative_to(ROOT)} -> {target}')
        if parsed.fragment and exists and local.suffix == '.md':
            require(unquote(parsed.fragment) in headings_in(local), f'Broken Markdown heading link: {document.relative_to(ROOT)} -> {target}')
        checks['links'].append({'from': document.relative_to(ROOT).as_posix(), 'target': target, 'exists': exists})

for name in ('AI001-dId6qeAjZpzAkke2JjLdfg.url', 'AI002-qADtdc_tAdkX1dRKFG50DQ.url'):
    require((ROOT / 'original_file/wechat' / name).is_file(), 'Original user URL file missing: ' + name)
require(len(checks['images']) == manifest['summary']['downloaded_images'], 'Image count mismatch')
checks['summary'] = {'registered_sources': len(records), 'checked_files': len(checks['files']), 'parsed_images': len(checks['images']),
                     'checked_documents': len(owned_docs), 'checked_local_links': len(checks['links']), 'checked_article_tables': sum(row['reader_tables'] for row in checks['articles']),
                     'pdf_first_pages_visually_reviewed': sum(bool(row.get('pdf_visual_check', {}).get('visually_reviewed')) for row in records), 'errors': len(errors)}
checks['passed'] = not errors
OUTPUT.write_text(json.dumps(checks, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(checks['summary'], ensure_ascii=False, indent=2))
for error in errors:
    print('ERROR:', error)
raise SystemExit(1 if errors else 0)
