import hashlib, json, re
from acquire_materials import ROOT, RAW, CACHE, RESULT_PATH, download, analyze_pdf, acquire
from materials_catalog import SOURCES

payload=json.loads(RESULT_PATH.read_text(encoding='utf-8'))
rows=payload['records']
for spec in SOURCES:
    if any(r['source_id']==spec['source_id'] for r in rows): continue
    rows.append(acquire(spec))

for row in rows:
    if row['slug']!='qwen3-implementation' or row['status']=='archived': continue
    name='src/transformers/models/qwen3/configuration_qwen3.py'
    try:
        file=download('https://raw.githubusercontent.com/huggingface/transformers/'+row['version']+'/'+name,
            RAW/'code'/(row['source_id']+'-'+row['slug'])/name,120)
        row['files'].append(file);row['errors']=[];row['status']='archived'
    except Exception as exc: print('AI065 configuration retry',str(exc),flush=True)

for row in rows:
    if row['slug']!='blackwell': continue
    if any(f['path'].endswith('blackwell-technical-brief.pdf') for f in row['files']): continue
    try:
        url='https://resources.nvidia.com/pdf/601206'
        file=download(url,RAW/'papers'/'AI035-blackwell-technical-brief.pdf',90)
        text=analyze_pdf(file);file['discovered_via']='https://resources.nvidia.com/en-us-blackwell-architecture'
        row['files'].append(file);row['technical_brief_excerpt']=text[:2200]
        print('AI035 official technical brief',file['pages'],'pages',flush=True)
    except Exception as exc: row['supplementary_download_error']=str(exc)

for check in payload.get('wechat_recheck',[]):
    if check['status']!='body_archived': continue
    ident=check['source_id']
    if any(r['source_id']==ident for r in rows): continue
    path=ROOT/check['file'];raw=path.read_text(encoding='utf-8',errors='replace')
    author_match=re.search(r'(?:var\s+)?author\s*=\s*[\"\x27]([^\"\x27]+)',raw)
    date_match=re.search(r'(?:var\s+)?publish_time\s*=\s*[\"\x27]([^\"\x27]+)',raw)
    nickname=re.search(r'(?:var\s+)?nickname\s*=\s*(?:htmlDecode\()?\s*[\"\x27]([^\"\x27]+)',raw)
    title=check['title']
    guide=('中文推理入门文章，用流程图和算术强度解释 Prefill、Decode、TTFT、TPOT 与计算/访存瓶颈，适合连接模型过程与性能指标。' if ident=='AI001' else
           '中文 KV Cache 入门文章，包含因果注意力、逐 token 追加、缓存容量公式及 Qwen3 小模型示例，适合建立缓存结构和资源估算的直觉。')
    limits=('Prefill 计算密集、Decode 访存密集是常见情形；batch、序列长度、模型类型和实现会改变瓶颈。文章关于权重访问和低精度硬件的概括需结合具体架构核对。' if ident=='AI001' else
            '文中 O(n²)→O(n) 是对重复计算的简化说法，不应作为完整自注意力总复杂度结论；全注意力解码仍访问历史 K/V，累计注意力计算和访存随序列增长。示例 cache API 需核对 Transformers 版本。')
    rows.append(dict(source_id=ident,group='TRAINING_INFERENCE',slug='wechat-prefill-decode' if ident=='AI001' else 'wechat-kv-cache',
        title=title,verified_title=title,locator=check['url'],source_url=check['url'],kind='blog',guide=guide,
        recommended_reading='正文中的工作流程、瓶颈或缓存容量说明，以及代码示例；结合交叉引用的原始资料阅读。',
        limits=limits,related_slugs=['gqa','pagedattention','qwen3-implementation','go-brrr'],extras=[],
        version='2026-10-02 snapshot',archive_date='2026-10-02',authors=[author_match.group(1) if author_match else 'aneasystone'],
        publisher=nickname.group(1) if nickname else '日习一技',published_date=date_match.group(1) if date_match else '',
        status='archived',errors=[],files=[dict(url=check['url'],final_url=check['url'],path=check['file'],bytes=path.stat().st_size,
        sha256=hashlib.sha256(path.read_bytes()).hexdigest())]))

payload['records']=sorted(rows,key=lambda r:r['source_id'])
RESULT_PATH.write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
