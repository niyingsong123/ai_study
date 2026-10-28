"""Retry incomplete public downloads and record original WeChat availability."""
import json, re
from pathlib import Path
from acquire_materials import ROOT, RAW, CACHE, RESULT_PATH, download, readable, analyze_pdf, get_meta

payload=json.loads(RESULT_PATH.read_text(encoding='utf-8'))
records=payload['records']

for row in records:
    if row['slug'] not in ('mlx','llama-cpp'): continue
    commit=row['version'] if row.get('version','').startswith(('2026',)) is False and len(row.get('version',''))==40 else ''
    if not commit:
        commit_files=[f for f in row['files'] if f['path'].endswith('commit.json')]
        if commit_files: commit=json.loads((ROOT/commit_files[0]['path']).read_text(encoding='utf-8'))['sha']
    if not commit: continue
    _,repo,branch,rel=row['locator'].split(':',3)
    for name in [rel]+row['extras']:
        if any(f['path'].endswith('/'+name) for f in row['files']): continue
        try:
            file=download(f'https://raw.githubusercontent.com/{repo}/{commit}/{name}',RAW/'code'/(row['source_id']+'-'+row['slug'])/name,120)
            row['files'].append(file)
        except Exception as exc: print(row['source_id'],name,str(exc),flush=True)
    paths=[rel]+row['extras']
    missing=[name for name in paths if not any(f['path'].endswith('/'+name) for f in row['files'])]
    row['errors']=[dict(url=name,error='selected file not retrieved after retry') for name in missing]
    row['status']='archived' if not missing else ('archived_with_gaps' if rel not in missing else 'failed')
    row.update(version=commit,source_url=f'https://github.com/{repo}/tree/{commit}',verified_title=row['title'])
    if rel not in missing:
        content=(RAW/'code'/(row['source_id']+'-'+row['slug'])/rel).read_text(encoding='utf-8',errors='replace')
        (CACHE/(row['source_id']+'-'+row['slug']+'.txt')).write_text(content,encoding='utf-8')
        row['verification_excerpt']=content[:1900]
    print(row['source_id'],row['status'],flush=True)

for row in records:
    if row['slug']!='su-rope': continue
    try:
        url='https://spaces.ac.cn/archives/8265'
        file=download(url,RAW/'blogs'/(row['source_id']+'-'+row['slug']+'.html'),60)
        raw=(ROOT/file['path']).read_text(encoding='utf-8',errors='replace')
        content,title=readable(raw)
        if len(content)<1000 or '旋转' not in content: raise RuntimeError('no verified article body')
        file['readable_characters']=len(content)
        row.update(files=[file],source_url=url,verified_title=title,version='2026-10-02 snapshot',
                   status='archived',errors=[],verification_excerpt=content[:1900])
        (CACHE/(row['source_id']+'-'+row['slug']+'.txt')).write_text(content,encoding='utf-8')
    except Exception as exc: row['errors'].append(dict(url=url,error=str(exc)))
    print(row['source_id'],row['status'],flush=True)

# Retrieve the public NVIDIA document viewer and discover its PDF link.
for row in records:
    if row['slug']!='blackwell': continue
    try:
        viewer=download('https://resources.nvidia.com/en-us-blackwell-architecture',RAW/'official'/(row['source_id']+'-blackwell-document-viewer.html'),60)
        row['files'].append(viewer)
        raw=(ROOT/viewer['path']).read_text(encoding='utf-8',errors='replace').replace('\\/','/')
        candidates=re.findall(r'https?://[^\s\"\x27<>]+\.pdf(?:\?[^\s\"\x27<>]*)?',raw,re.I)
        candidates=[u for u in candidates if 'nvidia' in u.lower() and 'blackwell' in u.lower()]
        row['document_viewer_pdf_candidates']=list(dict.fromkeys(candidates))
        for index,url in enumerate(row['document_viewer_pdf_candidates'][:1]):
            file=download(url,RAW/'papers'/(row['source_id']+'-blackwell-technical-brief.pdf'),90)
            row['files'].append(file); analyze_pdf(file)
        print(row['source_id'],'technical brief candidates',len(candidates),flush=True)
    except Exception as exc: row['supplementary_download_error']=str(exc)

wechat=[]
for ident,url in [('AI001','https://mp.weixin.qq.com/s/dId6qeAjZpzAkke2JjLdfg'),('AI002','https://mp.weixin.qq.com/s/qADtdc_tAdkX1dRKFG50DQ')]:
    result=dict(source_id=ident,url=url,checked_date='2026-10-02',status='link_only')
    try:
        file=download(url,CACHE/(ident+'-wechat-response.html'),60)
        raw=(ROOT/file['path']).read_text(encoding='utf-8',errors='replace')
        text,title=readable(raw)
        result['response_title']=title
        if re.search(r'id=[\"\x27]js_content',raw) and len(text)>1000:
            target=RAW/'wechat'/(ident+'-article.html')
            target.write_bytes((ROOT/file['path']).read_bytes())
            result.update(status='body_archived',file=target.relative_to(ROOT).as_posix(),title=get_meta(raw,'og:title') or title)
        else: result['reason']='No js_content article body; verification or unavailable response'
    except Exception as exc: result['reason']=str(exc)
    wechat.append(result); print(ident,result['status'],flush=True)

payload['wechat_recheck']=wechat
RESULT_PATH.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
