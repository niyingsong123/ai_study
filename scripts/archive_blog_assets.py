"""Preserve blog figures and create a local reader while retaining original HTML."""
import concurrent.futures, hashlib, html, json, re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from acquire_materials import ROOT, RAW, CACHE, RESULT_PATH, download

VOID={'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}
class Node:
    def __init__(self,tag='',attrs=(),parent=None): self.tag=tag;self.attrs=dict(attrs);self.children=[];self.parent=parent
    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child,Node): yield from child.walk()
    def text(self): return ''.join(c.text() if isinstance(c,Node) else c for c in self.children)

class Tree(HTMLParser):
    def __init__(self): super().__init__(convert_charrefs=True);self.root=Node('root');self.current=self.root
    def handle_starttag(self,tag,attrs):
        node=Node(tag,attrs,self.current);self.current.children.append(node)
        if tag not in VOID: self.current=node
    def handle_startendtag(self,tag,attrs): self.handle_starttag(tag,attrs);self.handle_endtag(tag)
    def handle_endtag(self,tag):
        node=self.current
        while node.parent:
            if node.tag==tag: self.current=node.parent;return
            node=node.parent
    def handle_data(self,data): self.current.children.append(data)

def serialize(node,base,assets,reader_dir):
    if isinstance(node,str): return html.escape(node)
    if node.tag in ('script','style','noscript','nav','header','footer','iframe','form','button'): return ''
    attrs={k:v for k,v in node.attrs.items() if not k.startswith('on') and k not in ('srcset','loading')}
    tag=node.tag
    # Some older blog pages use HTML <image src="..." />; browsers treat it as img.
    if node.tag=='image' and attrs.get('src'): tag='img'
    if tag=='img':
        src=attrs.get('data-src') or attrs.get('src') or attrs.get('data-original')
        if src:
            absolute=urljoin(base,src)
            if absolute in assets:
                import os
                attrs['src']=PathString(ROOT/assets[absolute]['path'],reader_dir)
            else: attrs['src']=absolute
        for key in ('data-src','data-original'): attrs.pop(key,None)
    if attrs.get('href') and not attrs['href'].startswith('#'): attrs['href']=urljoin(base,attrs['href'])
    rendered=''.join(' '+k+'="'+html.escape(v or '',quote=True)+'"' for k,v in attrs.items())
    if tag=='root': return ''.join(serialize(c,base,assets,reader_dir) for c in node.children)
    if tag in VOID: return '<'+tag+rendered+'>'
    return '<'+tag+rendered+'>'+''.join(serialize(c,base,assets,reader_dir) for c in node.children)+'</'+tag+'>'

def PathString(path,start):
    import os
    return os.path.relpath(path,start).replace('\\','/')

payload=json.loads(RESULT_PATH.read_text(encoding='utf-8'))
for row in payload['records']:
    if row['kind']!='blog' or row['status']!='archived': continue
    source=next(f for f in row['files'] if f['path'].endswith('.html'))
    raw=(ROOT/source['path']).read_text(encoding='utf-8',errors='replace')
    tree=Tree();tree.feed(raw)
    nodes=list(tree.root.walk())
    articles=[n for n in nodes if n.attrs.get('id')=='js_content']
    if not articles: articles=[n for n in nodes if n.tag=='article']
    if not articles:
        articles=[n for n in nodes if re.search(r'post-content|entry-content|body markup|main-content',n.attrs.get('class','')+' '+n.attrs.get('id',''))]
    if not articles: articles=[n for n in nodes if n.tag=='main']
    if not articles: articles=[n for n in nodes if n.tag=='body']
    selected=max(articles,key=lambda n:len(n.text())) if articles else tree.root
    # Preserve a usable text checkpoint separately from the local HTML reader.
    (CACHE/(row['source_id']+'-'+row['slug']+'.article.txt')).write_text(selected.text(),encoding='utf-8')
    urls=[]
    for node in selected.walk():
        if node.tag=='img' or (node.tag=='image' and node.attrs.get('src')):
            src=node.attrs.get('data-src') or node.attrs.get('src') or node.attrs.get('data-original')
            if src and not src.startswith('data:'):
                url=urljoin(row['source_url'],src)
                if url.startswith('https://') or url.startswith('http://'): urls.append(url)
    urls=list(dict.fromkeys(urls))
    def fetch(url):
        suffix=urlparse(url).path.rsplit('.',1)[-1].lower()
        suffix='.'+suffix if suffix in ('png','jpg','jpeg','gif','svg','webp','avif') else '.img'
        name=hashlib.sha256(url.encode()).hexdigest()[:18]+suffix
        try: return url,download(url,RAW/'blogs'/'assets'/row['source_id']/name,45),None
        except Exception as exc: return url,None,str(exc)
    assets={};failures=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        for url,file,error in pool.map(fetch,urls):
            if file: assets[url]=file
            else: failures.append(dict(url=url,error=error))
    row['image_files']=list(assets.values());row['image_download_failures']=failures
    row['article_image_count']=len(urls)
    target=RAW/'blogs'/(row['source_id']+'-'+row['slug']+'.reader.html')
    header='<html><head><meta charset="utf-8"><title>'+html.escape(row['title'])+'</title><style>body{max-width:1000px;margin:36px auto;padding:0 24px;font:18px/1.65 system-ui;color:#222}img{max-width:100%;height:auto}pre{overflow:auto;background:#f4f4f4;padding:16px}table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:6px}a{color:#0864ad}.archive{background:#eef5fa;padding:16px;font-size:15px}</style></head><body>'
    banner='<div class="archive">本地阅读副本，归档日 2026-10-02。<a href="'+html.escape(row['source_url'],quote=True)+'">原文</a>。原始 HTML 另存。保留正文和可取得的图像；部分数学排版、交互内容或外部依赖仍需在线原文。</div>'
    target.write_text(header+banner+serialize(selected,row['source_url'],assets,target.parent)+'</body></html>',encoding='utf-8')
    row['reader_path']=target.relative_to(ROOT).as_posix()
    row['reader_sha256']=hashlib.sha256(target.read_bytes()).hexdigest()
    row['reader_note']='Derived reading copy, original HTML unchanged; images localized where retrieved; math/interactive/external dependencies not fully offline.'
    print(row['source_id'],row['slug'],'images',len(assets),'/',len(urls),'errors',len(failures),flush=True)

RESULT_PATH.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
