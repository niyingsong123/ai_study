"""Download immutable source snapshots and record results without touching existing notes."""
import concurrent.futures, hashlib, html, json, os, re, subprocess, time
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin, urlparse
from pypdf import PdfReader
from materials_catalog import SOURCES

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / 'original_file'
CACHE = ROOT / 'tmp' / 'materials-20261002'
CACHE.mkdir(parents=True, exist_ok=True)
RESULT_PATH = RAW / 'acquisition-20261002.json'

class ReadableHTML(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0; self.title=False; self.titles=[]
    def handle_starttag(self, tag, attrs):
        if tag in ('script','style','noscript'): self.skip+=1
        if tag=='title': self.title=True
        if tag in ('p','h1','h2','h3','h4','li','div','section','tr','br'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style','noscript'): self.skip=max(0,self.skip-1)
        if tag=='title': self.title=False
    def handle_data(self, data):
        if not self.skip:
            self.parts.append(data)
            if self.title: self.titles.append(data)
    def text(self):
        return re.sub(r'\n[ \t]*\n+', '\n', ''.join(self.parts)).strip()

def readable(content):
    parser=ReadableHTML(); parser.feed(content)
    return parser.text(), ''.join(parser.titles).strip()

def download(url, dest, timeout=60):
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 100:
        return dict(url=url, final_url=url, path=dest.relative_to(ROOT).as_posix(),
                    bytes=dest.stat().st_size, sha256=hashlib.sha256(dest.read_bytes()).hexdigest(), cache_reused=True)
    partial=dest.with_suffix(dest.suffix+'.part')
    args=['curl.exe','--silent','--show-error','--location','--fail','--connect-timeout','12',
          '--max-time',str(timeout),'--user-agent','Mozilla/5.0 (AI study source archiver)',
          '--output',str(partial),'--write-out','%{http_code}\t%{url_effective}\t%{content_type}',url]
    process=subprocess.run(args,capture_output=True,text=True,encoding='utf-8',errors='replace')
    if process.returncode:
        raise RuntimeError(process.stderr.strip()[-400:] or f'curl exit {process.returncode}')
    if not partial.exists() or partial.stat().st_size<100:
        raise RuntimeError('empty or undersized response')
    fields=process.stdout.split('\t',2)
    os.replace(partial,dest)
    return dict(url=url,final_url=fields[1] if len(fields)>1 else url,
        content_type=fields[2] if len(fields)>2 else '',http_status=fields[0],
        path=dest.relative_to(ROOT).as_posix(),bytes=dest.stat().st_size,
        sha256=hashlib.sha256(dest.read_bytes()).hexdigest())

def analyze_pdf(file):
    path=ROOT/file['path']
    if path.read_bytes()[:5]!=b'%PDF-': raise RuntimeError('response is not a PDF')
    reader=PdfReader(path)
    texts=[]
    for index,page in enumerate(reader.pages):
        texts.append(f'\n=== PDF page {index+1} ===\n'+(page.extract_text() or ''))
    joined='\n'.join(texts)
    file.update(pages=len(reader.pages), pdf_title=str((reader.metadata or {}).get('/Title','')),
                extracted_characters=len(joined),validation='PDF header, page tree, all-page text extraction')
    (CACHE/(path.stem+'.txt')).write_text(joined,encoding='utf-8')
    return joined

def get_meta(content,name):
    for match in re.finditer(r'<meta\b[^>]*>',content,re.I):
        attrs=dict((m.group(1).lower(),html.unescape(m.group(3))) for m in re.finditer(r'([\w:-]+)\s*=\s*([\"\x27])(.*?)\2',match.group(),re.S))
        if attrs.get('name')==name or attrs.get('property')==name: return attrs.get('content','')
    return ''

def acquire(spec):
    row=dict(spec); row.update(files=[],errors=[],retrieved_at_utc=datetime.now(timezone.utc).isoformat(),archive_date='2026-10-02')
    ident=spec['source_id']+'-'+spec['slug']
    try:
        if spec['kind']=='paper':
            url='https://arxiv.org/abs/'+spec['locator']
            file=download(url,RAW/'papers'/(ident+'.metadata.html'),35)
            row['files'].append(file)
            content=(ROOT/file['path']).read_text(encoding='utf-8',errors='replace')
            title=get_meta(content,'citation_title')
            if not title: raise RuntimeError('arXiv metadata missing citation_title')
            row['verified_title']=title
            row['published_date']=get_meta(content,'citation_date')
            row['authors']=re.findall(r'<meta\s+name="citation_author"\s+content="([^"]+)"',content)
            versions=[int(v) for v in re.findall(r'\[v(\d+)\]',content)]
            if not versions: versions=[int(v) for v in re.findall(re.escape(spec['locator'])+r'v(\d+)',content)]
            version=max(versions) if versions else 1
            row['version']=spec['locator']+f'v{version}'
            row['source_url']=url
            pdf=download('https://arxiv.org/pdf/'+row['version'],RAW/'papers'/(ident+'.pdf'),90)
            row['files'].append(pdf)
            text=analyze_pdf(pdf)
            row['verification_excerpt']=text[:1900]
        elif spec['kind']=='code':
            _,repo,branch,rel=spec['locator'].split(':',3)
            commit_file=download(f'https://api.github.com/repos/{repo}/commits/{branch}',RAW/'code'/ident/'commit.json',35)
            row['files'].append(commit_file)
            commit=json.loads((ROOT/commit_file['path']).read_text(encoding='utf-8'))['sha']
            row.update(version=commit,source_url=f'https://github.com/{repo}/tree/{commit}',verified_title=spec['title'])
            for path in [rel]+spec['extras']:
                try:
                    file=download(f'https://raw.githubusercontent.com/{repo}/{commit}/{path}',RAW/'code'/ident/path,45)
                    row['files'].append(file)
                except Exception as exc: row['errors'].append(dict(url=path,error=str(exc)))
            main=next(f for f in row['files'] if f['path'].endswith(rel))
            content=(ROOT/main['path']).read_text(encoding='utf-8',errors='replace')
            (CACHE/(ident+'.txt')).write_text(content,encoding='utf-8')
            row['verification_excerpt']=content[:1900]
        else:
            category='papers' if spec['kind']=='official_pdf' else ('blogs' if spec['kind']=='blog' else 'official')
            suffix='.pdf' if spec['kind']=='official_pdf' else '.html'
            file=download(spec['locator'],RAW/category/(ident+suffix),90 if suffix=='.pdf' else 45)
            row['files'].append(file); row['source_url']=spec['locator']
            if suffix=='.pdf':
                content=analyze_pdf(file); row['verified_title']=file['pdf_title'] or spec['title']
            else:
                raw=(ROOT/file['path']).read_text(encoding='utf-8',errors='replace')
                content,title=readable(raw); row['verified_title']=title or spec['title']
                if len(content)<500 or re.search(r'^\s*(Just a moment|Access Denied|Attention Required)',content,re.I):
                    raise RuntimeError('response is a challenge or insufficient readable content')
                file['readable_characters']=len(content)
                row['published_date']=get_meta(raw,'article:published_time') or get_meta(raw,'date')
                (CACHE/(ident+'.txt')).write_text(content,encoding='utf-8')
            row['version']=row.get('version') or '2026-10-02 snapshot'
            row['verification_excerpt']=content[:1900]
        row['status']='archived' if not row['errors'] else 'archived_with_gaps'
    except Exception as exc:
        row['status']='failed'; row['errors'].append(dict(error=str(exc)))
    print(json.dumps(dict(source_id=row['source_id'],slug=row['slug'],status=row['status'],files=len(row['files']),errors=row['errors']),ensure_ascii=False),flush=True)
    return row

def main():
    previous={}
    if RESULT_PATH.exists():
        previous={r['source_id']:r for r in json.loads(RESULT_PATH.read_text(encoding='utf-8'))['records']}
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        tasks={pool.submit(acquire,spec):spec for spec in SOURCES if previous.get(spec['source_id'],{}).get('status') not in ('archived','archived_with_gaps')}
        results.extend(r for r in previous.values() if r.get('status') in ('archived','archived_with_gaps'))
        for future in concurrent.futures.as_completed(tasks):
            results.append(future.result())
            payload=dict(batch='AI-MATERIALS-20261002',archive_date='2026-10-02',records=sorted(results,key=lambda x:x['source_id']))
            RESULT_PATH.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('COMPLETED '+json.dumps({s:sum(r['status']==s for r in results) for s in ('archived','archived_with_gaps','failed')}),flush=True)

if __name__=='__main__': main()
