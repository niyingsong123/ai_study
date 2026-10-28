"""Build the first curated collection from verified acquisition records.

New user-facing files are written once. Existing project documentation is edited
separately, so rerunning this script cannot silently replace user annotations.
"""
from collections import Counter
from datetime import datetime
from pathlib import Path
import hashlib
import html
import json
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
DATE = '2026-10-02'
INPUT = ROOT / 'original_file/acquisition-20261002.json'
CACHE = ROOT / 'tmp/materials-20261002'

GROUPS = {
    'ALGORITHMS': {
        'name': 'AI 算法与基础技术',
        'purpose': '理解算法解决的问题、关键数学关系与计算过程，为模型、系统和硬件研究提供共同基础。',
        'routes': [
            ('Transformer 主线', ['illustrated-transformer', 'attention-is-all-you-need', 'roformer', 'gqa', 'switch-transformer', 'mamba']),
            ('训练与压缩', ['adam', 'lora', 'knowledge-distillation', 'gptq', 'awq']),
            ('视觉与生成分支', ['resnet', 'ddpm', 'lilian-diffusion']),
        ],
        'questions': ['注意力、前馈层和状态更新分别执行什么计算？张量形状怎样变化？', '优化方法改变了训练目标、模型结构还是数值表示？有什么代价？', '计算复杂度、参数量、缓存大小与实际设备性能怎样关联？'],
        'followups': ['MODELS', 'TRAINING_INFERENCE', 'EDGE_AI'],
    },
    'MODELS': {
        'name': '代表性大模型',
        'purpose': '以公开报告和固定版本实现为依据，比较稠密、MoE、推理及多模态模型的设计取舍。',
        'routes': [
            ('稠密模型基线', ['illustrated-gpt2', 'qwen3', 'qwen3-implementation', 'llama3', 'gemma3']),
            ('MoE 与推理能力', ['switch-transformer', 'deepseek-v3', 'deepseek-r1', 'deepseek-math', 'deepseek-hardware']),
            ('扩展与架构比较', ['qwen25-vl', 'qwen38-next', 'raschka-comparison']),
        ],
        'questions': ['Attention、归一化、位置编码和前馈层的具体配置是什么？', '总参数、每 token 激活参数和训练/推理状态各自占用多少资源？', '能力变化来自结构、数据、训练目标还是后训练？公开证据支持到哪一步？'],
        'followups': ['ALGORITHMS', 'TRAINING_INFERENCE', 'CLOUD_ACCELERATORS', 'APPLICATIONS'],
    },
    'TRAINING_INFERENCE': {
        'name': '训练与推理系统',
        'purpose': '从单请求逐 token 执行进入缓存、调度、算子优化、分布式训练和后训练，解释实际系统瓶颈。',
        'routes': [
            ('推理入门与服务', ['wechat-prefill-decode', 'wechat-kv-cache', 'qwen3-implementation', 'pagedattention', 'vllm-architecture']),
            ('性能与执行', ['go-brrr', 'flashattention', 'speculative-decoding', 'sglang', 'tensorrt-llm', 'mlir']),
            ('分布式训练与后训练', ['adam', 'zero', 'megatron-lm', 'nccl', 'rlhf', 'dpo', 'deepseek-math']),
        ],
        'questions': ['Prefill 与 Decode 的输入、缓存访问和资源需求怎样不同？', '吞吐、首 token 延迟和每 token 延迟怎样受批量、调度与存储影响？', '训练状态怎样分片？计算与通信是否重叠？优化的收益如何验证？'],
        'followups': ['MODELS', 'CLOUD_ACCELERATORS', 'EDGE_AI'],
    },
    'CLOUD_ACCELERATORS': {
        'name': '云端芯片与集群架构',
        'purpose': '比较 GPU、TPU 的公开计算与存储结构，并把模型负载、HBM、互连和集群通信联系起来。',
        'routes': [
            ('架构入口', ['blackwell', 'cdna4', 'tpu-first', 'tpu-v4']),
            ('负载与集群', ['deepseek-hardware', 'megatron-lm', 'nccl', 'mlperf-inference']),
        ],
        'questions': ['矩阵单元、向量计算、片上存储和 HBM 怎样参与模型执行？', '单芯片、单机和多机分别受到什么容量、带宽或通信限制？', '硬件性能声明的精度、稀疏性、模型与测量条件是否可比？'],
        'followups': ['TRAINING_INFERENCE', 'MODELS', 'EDGE_AI'],
    },
    'EDGE_AI': {
        'name': '端侧模型与芯片架构',
        'purpose': '围绕手机、PC 和微控制器的容量、带宽、持续功耗与工具链约束，研究模型和执行系统共同设计。',
        'routes': [
            ('端侧约束与小模型', ['qualcomm-npu', 'mobilellm', 'knowledge-distillation', 'awq']),
            ('部署与执行', ['onnx-qnn', 'executorch', 'llama-cpp', 'mlx']),
            ('微控制器分支', ['resnet', 'mcunet']),
        ],
        'questions': ['目标设备支持哪些精度、算子、动态形状和模型规模？', 'CPU、GPU、NPU 和存储之间怎样划分任务与共享数据？', '短时性能与持续性能有什么差异？内存、功耗和任务效果如何一起比较？'],
        'followups': ['ALGORITHMS', 'TRAINING_INFERENCE', 'CLOUD_ACCELERATORS'],
    },
    'APPLICATIONS': {
        'name': '应用机制与扩展专题',
        'purpose': '把检索、工具、视觉、语音、推荐和机器人任务的新需求映射到模型过程与系统资源。',
        'routes': [
            ('RAG 与 Agent', ['lilian-agents', 'rag', 'react', 'toolformer']),
            ('视觉与语音', ['vit', 'clip', 'qwen25-vl', 'whisper', 'qwen3-tts']),
            ('推荐与具身智能', ['dlrm', 'rt2']),
        ],
        'questions': ['任务引入了哪些输入、外部状态、工具和输出？', '任务质量、可靠性与时延怎样评估？基础模型能力和应用能力如何区分？', '新序列长度、embedding 查表或连续控制怎样改变计算与访存模式？'],
        'followups': ['MODELS', 'TRAINING_INFERENCE', 'CLOUD_ACCELERATORS'],
    },
}
KINDS = {'paper': '原始论文/技术报告', 'official': '官方网页文档', 'official_pdf': '官方白皮书 PDF', 'blog': '作者技术文章', 'code': '固定提交的选定源码'}


def write_new(relative, text):
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        raise FileExistsError(f'Refusing to overwrite existing notes: {relative}')
    path.write_text(text.rstrip() + '\n', encoding='utf-8')


def link_to(target, from_file):
    return os.path.relpath(ROOT / target, (ROOT / from_file).parent).replace('\\', '/')


def table_text(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


payload = json.loads(INPUT.read_text(encoding='utf-8'))
rows = sorted(payload['records'], key=lambda row: row['source_id'])
by_slug = {row['slug']: row for row in rows}

# A download challenge is a diagnostic response, not an archived article.
diagnostics = CACHE / 'download-diagnostics'
for row in rows:
    if row['status'] != 'failed':
        continue
    row['source_url'] = row.get('source_url') or row['locator']
    for file in row.get('files', []):
        original = (ROOT / file['path']).resolve()
        if not original.is_relative_to(ROOT / 'original_file'):
            raise ValueError('Diagnostic path outside original_file')
        if original.exists():
            diagnostics.mkdir(parents=True, exist_ok=True)
            destination = diagnostics / original.name
            if destination.exists():
                raise FileExistsError(destination)
            shutil.move(str(original), str(destination))
            file['path'] = destination.relative_to(ROOT).as_posix()
    row['diagnostic_files'] = row.get('files', [])
    row['files'] = []
    url_path = ROOT / 'original_file/pending' / (row['source_id'] + '-' + row['slug'] + '.url')
    url_path.parent.mkdir(parents=True, exist_ok=True)
    if not url_path.exists():
        url_path.write_text('[InternetShortcut]\nURL=' + row['source_url'] + '\n', encoding='utf-8')
    row['link_file'] = url_path.relative_to(ROOT).as_posix()

# Move task-generated unfinished transfer fragments out of the usable archive.
partials = []
for partial in (ROOT / 'original_file').rglob('*.part'):
    original = partial.resolve()
    if not original.is_relative_to(ROOT / 'original_file'):
        raise ValueError('Partial file outside archive')
    target = diagnostics / original.relative_to(ROOT / 'original_file')
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        raise FileExistsError(target)
    shutil.move(str(original), str(target))
    partials.append(target.relative_to(ROOT).as_posix())

AUTHORS = {'illustrated-transformer': 'Jay Alammar', 'illustrated-gpt2': 'Jay Alammar', 'lilian-agents': 'Lilian Weng', 'lilian-diffusion': 'Lilian Weng', 'raschka-comparison': 'Sebastian Raschka', 'go-brrr': 'Horace He', 'su-rope': '苏剑林'}
VERSION_LABELS = {
    'vllm-architecture': 'v0.10.2 文档；2026-10-02 归档',
    'tensorrt-llm': 'v0.20.0 文档；2026-10-02 归档',
    'nccl': '页面标注 NCCL 2.32.3；2026-10-02 快照',
    'executorch': '页面标注 ExecuTorch 1.5；2026-10-02 快照',
}
for row in rows:
    row['note_path'] = f"{row['group']}/sources/{row['source_id']}-{row['slug']}.md"
    row['kind_label'] = KINDS[row['kind']]
    row['version_label'] = VERSION_LABELS.get(row['slug'], row.get('version', '未取得正文，版本待核实'))
    if row['slug'] in AUTHORS:
        row['authors'] = [AUTHORS[row['slug']]]
    if row['kind'] in ('official', 'blog') and row['status'] == 'archived':
        content_file = next((f for f in row['files'] if f['path'].endswith('.html')), None)
        if content_file:
            original = (ROOT / content_file['path']).read_text(encoding='utf-8', errors='replace')
            title = re.search(r'<title[^>]*>(.*?)</title>', original, re.I | re.S)
            if title:
                row['verified_title'] = html.unescape(re.sub(r'<[^>]+>', '', title.group(1))).strip()
    row['reading_status'] = (
        '未取得正文；只登记来源入口，不生成正文结论。' if row['status'] != 'archived'
        else '已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。' if row['kind'] == 'paper'
        else '已核对文件主题和首页，完成可读性检查；架构细节及全文待专题精读。' if row['kind'] == 'official_pdf'
        else '已检查取得的正文、章节入口及选定段落；未逐段核验全部推导、示例和结论。' if row['kind'] == 'blog'
        else '已检查取得的页面及相关章节入口；仅归档指定页面，未离线保存整个文档站。' if row['kind'] == 'official'
        else '已固定提交、保存并定位选定源文件；未编译、安装或运行模型。'
    )

preview_path = CACHE / 'pdf-preview-checks.json'
previews = json.loads(preview_path.read_text(encoding='utf-8'))
# All six contact sheets have been inspected by the agent, covering every PDF.
for item in previews['records']:
    if not item['rendered']:
        raise ValueError('Unrendered PDF: ' + item['source_id'])
    item['visually_reviewed'] = True
    item['review_scope'] = 'Page 1 only, visually reviewed in contact sheets 01-06; no full-page visual audit.'
preview_path.write_text(json.dumps(previews, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
pdf_checks = {item['source_id']: item for item in previews['records']}

archive_files = []
for row in rows:
    for file in row['files'] + row.get('image_files', []):
        path = ROOT / file['path']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != file['sha256'] or path.stat().st_size != file['bytes']:
            raise ValueError('Archive integrity mismatch: ' + file['path'])
        archive_files.append(file)
    if row.get('reader_path'):
        path = ROOT / row['reader_path']
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        if digest != row['reader_sha256']:
            raise ValueError('Reader integrity mismatch: ' + row['source_id'])
        row['reader_file'] = {'path': row['reader_path'], 'bytes': path.stat().st_size, 'sha256': digest, 'derived': True}
    if row['source_id'] in pdf_checks:
        row['pdf_visual_check'] = {k: v for k, v in pdf_checks[row['source_id']].items() if k in ('rendered_pages', 'visually_reviewed', 'review_scope')}

counts = Counter(row['kind'] for row in rows if row['status'] == 'archived')
pdfs = [file for row in rows if row['status'] == 'archived' for file in row['files'] if file['path'].endswith('.pdf')]
images = [file for row in rows for file in row.get('image_files', [])]
image_failures = [failure for row in rows for failure in row.get('image_download_failures', [])]
archived_count = sum(row['status'] == 'archived' for row in rows)
summary = {
    'registered_sources': len(rows), 'archived_sources': archived_count,
    'pending_sources': len(rows) - archived_count, 'by_kind_archived': dict(counts),
    'pdf_files': len(pdfs), 'pdf_pages': sum(file['pages'] for file in pdfs),
    'blog_reader_files': sum(bool(row.get('reader_path')) for row in rows),
    'downloaded_images': len(images), 'image_download_failures': len(image_failures),
    'original_bytes_excluding_readers_and_metadata_manifests': sum(file['bytes'] for file in archive_files),
    'groups': {group: {'registered': sum(row['group'] == group for row in rows), 'archived': sum(row['group'] == group and row['status'] == 'archived' for row in rows)} for group in GROUPS},
}


def source_link(slug, from_file, with_title=False):
    row = by_slug[slug]
    label = row['source_id'] + ('：' + row['title'] if with_title else '')
    return f"[{label}]({link_to(row['note_path'], from_file)})"


for row in rows:
    target = row['note_path']
    body = [f"# {row['source_id']}：{row['title']}", '',
            f"主归属：[{GROUPS[row['group']]['name']}](../README.md)。来源性质：{row['kind_label']}。", '',
            f"- 原始来源：[原文或固定版本仓库]({row['source_url']})",
            f"- 版本：{row['version_label']}", f"- 归档日期：{DATE}"]
    if row.get('authors'):
        body.append('- 作者/团队：' + '；'.join(row['authors']))
    if row.get('publisher'):
        body.append('- 发布账号：' + row['publisher'])
    if row.get('published_date'):
        label = 'arXiv 首次提交日期' if row['kind'] == 'paper' else '页面提供的发布日期'
        body.append(f"- {label}：{row['published_date']}")
    else:
        body.append('- 发布日期：本次未可靠提取；归档日期不代表发布日期。')
    body.extend(['', '## 归档与阅读状态', '', row['reading_status'], ''])
    if row['status'] != 'archived':
        reason = '返回验证页面，未取得可用正文。' if row['slug'] == 'hexagon-2026' else '作者站及备用域名返回 HTTP 403，未取得正文。'
        body.extend(['**状态：待补正文。** ' + reason,
                     f"[已保存的原始链接]({link_to(row['link_file'], target)})。", '',
                     '## 预期用途与替代资料', '',
                     '此条目用于保存后续追踪入口。题名和来源背景仅作为候选信息，本次不据此整理正文摘要或确认具体机制。'])
        if row['slug'] == 'hexagon-2026':
            body.append('近期新代际信息待补；当前可先阅读 Qualcomm 异构计算白皮书，建立端侧 NPU 的基础问题。')
        else:
            body.append('RoPE 推导先以已下载的 RoFormer 原论文为依据；作者文章取得正文后再补充导读。')
    else:
        body.append('**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**')
        if row.get('reader_path'):
            body.extend(['', f"优先打开：[本地正文阅读副本]({link_to(row['reader_path'], target)})。"])
        body.extend(['', '| 本地原始文件 | 文件说明 |', '| --- | --- |'])
        for file in row['files']:
            path = file['path']
            label = Path(path).name
            detail = str(file['pages']) + ' 页 PDF' if path.endswith('.pdf') else '论文元数据页' if path.endswith('.metadata.html') else '固定提交元数据' if path.endswith('commit.json') else '原始网页 HTML' if path.endswith('.html') else '选定原始源码'
            body.append(f"| [{table_text(label)}]({link_to(path, target)}) | {detail} |")
        if row.get('image_files'):
            body.extend(['', f"正文图像：已保存 {len(row['image_files'])}/{row['article_image_count']} 个独立图像地址；重复使用的图像只保存一份。"])
        if row.get('image_download_failures'):
            body.append(f"其中 {len(row['image_download_failures'])} 个地址未取得，本地副本保留在线地址。详见[归档核查]({link_to('source-reading-audit.md', target)})。")
        if row.get('reader_path'):
            body.append('原始 HTML 完整保留；本地阅读副本保留正文、可取得图示和原始表格，移除页面导航与脚本。数学排版、交互及外部依赖可能仍需打开在线原文。')
        body.extend(['', '## 入选理由与研究用途', '', row['guide'], '', '## 建议阅读定位', '', row['recommended_reading'], '',
                     '建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。', '', '## 适用边界与核对事项', '', row['limits']])
        if row['slug'] == 'blackwell':
            body.append('本次保存的是官方架构概述 HTML 和技术文档入口 HTML；入口所指 PDF 下载返回错误，未作为白皮书归档。')
        if row['slug'] == 'qwen3-implementation':
            body.append('Qwen3Config 的默认值不等于任意 Qwen3 检查点的配置。复现微信中的 Qwen3-0.6B 示例前，还需固定该检查点的 config、tokenizer 和运行依赖。')
        if row['slug'] == 'wechat-kv-cache':
            body.append('辨析时应分别统计投影/MLP 与注意力。对于固定模型、固定初始 prompt、全注意力逐步生成，缓存后的每步注意力仍扫描增长的历史；不能将新 token 的投影计算量直接当作整个生成过程的总计算量。示例中的 KB/KiB 也需采用统一单位。')
    if row.get('related_slugs'):
        body.extend(['', '## 交叉阅读', ''])
        for slug in row['related_slugs']:
            if slug in by_slug:
                body.append('- ' + source_link(slug, target, True))
    body.extend(['', f"[分类资料索引](README.md) · [全项目资料索引]({link_to('sources.md', target)})"])
    write_new(target, '\n'.join(body))

for group, settings in GROUPS.items():
    group_rows = [row for row in rows if row['group'] == group]
    target = f'{group}/sources/README.md'
    body = [f"# {settings['name']}：资料索引", '',
            f"登记 {len(group_rows)} 项，已取得 {sum(row['status'] == 'archived' for row in group_rows)} 项。每份来源只维护一篇主导读，跨方向按链接复用。", '',
            '| 编号与导读 | 类型 | 版本/日期 | 归档状态 |', '| --- | --- | --- | --- |']
    for row in group_rows:
        status = '原文已归档' if row['status'] == 'archived' else '**待补正文**'
        version = row['version_label']
        if row['kind'] == 'code':
            version = row['version'][:12] + '（固定提交）'
        body.append(f"| [{row['source_id']}：{table_text(row['title'])}]({Path(row['note_path']).name}) | {row['kind_label']} | {table_text(version)} | {status} |")
    body.extend(['', '[方向入口与阅读顺序](../README.md) · [全项目索引](../../sources.md)'])
    write_new(target, '\n'.join(body))
    target = f'{group}/README.md'
    body = [f"# {settings['name']}", '', settings['purpose'], '',
            f"本轮完成资料准备和导读整理。共登记 {len(group_rows)} 项，取得 {sum(row['status'] == 'archived' for row in group_rows)} 项；综合报告与实验按专题另行推进。", '',
            '## 资料入口', '', '[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)', '',
            '## 建议阅读顺序', '']
    for label, route in settings['routes']:
        body.append('- **' + label + '**：' + ' → '.join(source_link(slug, target) for slug in route) + '。')
    pending = [row for row in group_rows if row['status'] != 'archived']
    if pending:
        body.extend(['', '待补入口：' + '；'.join(source_link(row['slug'], target, True) for row in pending) + '。可先采用对应已下载原始资料。'])
    body.extend(['', '## 研究时应回答的问题', ''])
    body.extend('- ' + question for question in settings['questions'])
    body.extend(['', '## 后续连接', '', ' · '.join(f"[{GROUPS[other]['name']}](../{other}/README.md)" for other in settings['followups'])])
    write_new(target, '\n'.join(body))

manifest_rows = []
for row in rows:
    clean = {key: value for key, value in row.items() if key not in ('verification_excerpt', 'diagnostic_files', 'retrieved_at_utc')}
    if row.get('retrieved_at_utc'):
        clean['retrieved_at'] = row['retrieved_at_utc']
    manifest_rows.append(clean)
manifest = {'schema_version': 1, 'batch': payload['batch'], 'archive_date': DATE,
            'scope': 'AI reference materials, not model weights or training datasets',
            'summary': summary, 'sources': manifest_rows}
write_new('source-manifest.json', json.dumps(manifest, ensure_ascii=False, indent=2))
INPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

target = 'materials-reading-guide.md'
body = ['# 首批 AI 资料阅读路线', '',
        f"资料快照：{DATE}。从[总索引](sources.md)或[六个方向入口](README.md#分类资料集)查找原文与逐篇导读。", '',
        '论文用于建立机制与证据，作者文章用于图解和组织问题，官方文档与固定源码用于核对实现。阅读路线按问题选择，不要求逐份顺序读完。', '',
        '## 首条路线：从输入 token 到云端与端侧执行', '',
        '| 步骤 | 阅读资料 | 应形成的认识 |', '| --- | --- | --- |']
routes = [
    ('1. Transformer 与自回归', ['illustrated-transformer', 'attention-is-all-you-need', 'illustrated-gpt2'], '建立 Embedding、Attention、前馈层、因果掩码与输出采样的整体过程。'),
    ('2. Prefill、Decode 与缓存', ['wechat-prefill-decode', 'wechat-kv-cache', 'gqa'], '解释两阶段输入、缓存追加、KV 头数和资源需求；留意微信文章中的复杂度简化。'),
    ('3. 公开模型与实现', ['qwen3', 'qwen3-implementation'], '选择报告中的稠密成员，核对结构及代码；正式复现时补齐具体检查点配置与 tokenizer。'),
    ('4. 服务与算子优化', ['pagedattention', 'vllm-architecture', 'flashattention', 'go-brrr'], '区分缓存组织、请求调度和算子 IO 优化，连接延迟、吞吐及访存瓶颈。'),
    ('5. 云端硬件映射', ['blackwell', 'cdna4', 'tpu-v4', 'deepseek-hardware'], '把算子、权重、缓存与矩阵单元、HBM、互连和集群联系起来。'),
    ('6. 端侧约束与运行时', ['qualcomm-npu', 'awq', 'mobilellm', 'onnx-qnn', 'llama-cpp'], '说明低比特、小模型、算子覆盖、异构执行和持续功耗的取舍。'),
]
for label, slugs, outcome in routes:
    body.append('| ' + label + ' | ' + '、'.join(source_link(slug, target) for slug in slugs) + ' | ' + outcome + ' |')
body.extend(['', '这条路线准备了原文与导读；完整推理报告、资源估算和设备实测尚未开展。软件文档中的固定版本用于建立可追溯基线，不代表归档日的最新发布。', '',
             '## 根据问题选择分支', '', '| 问题 | 推荐入口 |', '| --- | --- |'])
branches = [
    ('MoE 为什么节省激活计算，又增加通信？', ['switch-transformer', 'deepseek-v3', 'deepseek-hardware']),
    ('后训练如何形成指令遵循与推理能力？', ['rlhf', 'dpo', 'deepseek-math', 'deepseek-r1']),
    ('训练显存和多卡通信怎样组织？', ['adam', 'zero', 'megatron-lm', 'nccl']),
    ('量化、蒸馏与小模型怎样适应端侧？', ['gptq', 'awq', 'knowledge-distillation', 'mobilellm', 'mcunet']),
    ('扩散模型与 Transformer 生成有什么不同？', ['ddpm', 'lilian-diffusion']),
    ('RAG 与 Agent 增加了哪些系统环节？', ['rag', 'react', 'toolformer', 'lilian-agents']),
    ('视觉、语音、推荐与机器人有哪些新负载？', ['vit', 'clip', 'qwen25-vl', 'whisper', 'qwen3-tts', 'dlrm', 'rt2']),
]
for question, slugs in branches:
    body.append('| ' + question + ' | ' + '、'.join(source_link(slug, target) for slug in slugs) + ' |')
body.extend(['', '## 博主文章的使用方法', '',
             '本批纳入 Jay Alammar、Lilian Weng、Sebastian Raschka、Horace He，以及用户提供的 aneasystone 微信文章。优先采用作者原站，选择有清晰推导、结构图、代码或原始参考的文章，并与论文及实现交叉阅读。苏剑林 RoPE 文章保留为待补入口。', '',
             '作者文章中的示意参数、历史模型和性能简化需保留其条件。原文观点、导读辨析与后续实测分别记录；对已取得的文章保存原始 HTML、正文阅读副本及可取得图示。', '',
             '## 阅读记录与产出', '',
             '每次精读把实际页码/章节、张量形状、公式假设、实现位置和未解决问题补入该来源的唯一主笔记。跨来源结论再写入具体专题报告；复现先固定模型检查点、依赖、硬件与输入条件。', '',
             '[归档与阅读核查记录](source-reading-audit.md)记录本轮完成范围和剩余缺口。'])
write_new(target, '\n'.join(body))

target = 'source-reading-audit.md'
body = ['# 首批资料归档与阅读核查', '', f"批次：{payload['batch']}。归档日：{DATE}。", '',
        '## 资料规模', '',
        f"共登记 {len(rows)} 项稳定编号，取得 {archived_count} 项可用原文；{len(rows)-archived_count} 项保留链接、待补正文。", '',
        '| 类型 | 已取得来源数 | 保存范围 |', '| --- | --- | --- |',
        f"| 原始论文/技术报告 | {counts['paper']} | arXiv 元数据页与固定 vN 的 PDF |",
        f"| 官方白皮书 | {counts['official_pdf']} | 原始 PDF |",
        f"| 官方文档与架构页面 | {counts['official']} | 指定 HTML 页面；不是整个站点的离线镜像 |",
        f"| 作者技术文章 | {counts['blog']} | 原始 HTML、正文阅读副本及可取得图示，含用户提供的两篇微信文章 |",
        f"| 选定源码 | {counts['code']} | MLX、llama.cpp 与 Transformers Qwen3 的固定提交及指定文件 |", '',
        f"合计 {len(pdfs)} 份 PDF、{summary['pdf_pages']} 页；{len(images)} 个独立图像文件、{summary['blog_reader_files']} 个派生阅读副本。原始文件与图像约 {summary['original_bytes_excluding_readers_and_metadata_manifests']/1024/1024:.1f} MiB（不含派生阅读副本、总清单和临时检查文件）。", '',
        '## 本轮实际检查', '',
        '- 下载文件均记录原始 URL、本地路径、字节数和 SHA-256；整理时重新读取文件核对大小与哈希。论文元数据记录题名、作者、首次提交日期和下载版本。',
        f"- {len(pdfs)} 份 PDF 均通过文件头、页树和全页文字提取检查；已渲染并逐一目视检查全部 PDF 的第 1 页，确认不是验证页面、空白或明显错题文件。",
        '- 首页检查不等于逐页阅读，也不等于全文图表的视觉核对。论文导读依据题名、摘要/导言及选读信息建立；推荐章节仍待具体专题精读。',
        '- 博主文章检查实际取得的正文、章节入口及选定段落；保存原始 HTML，另生成阅读副本。本批未把原文表格转换成 Markdown 表格。',
        '- 代码按提交固定，仅保存选定文件；未编译运行，未执行下载的仓库脚本。模型权重、训练数据集和完整仓库不在本批范围。',
        '- 六个方向均建立入口、分类索引与逐篇导读。同一来源只有一篇主导读，其他方向通过编号交叉引用。', '',
        '## 作者文章图示与外部依赖', '', '| 来源 | 本地图像/正文独立图像地址 | 状态 |', '| --- | --- | --- |']
for row in rows:
    if row['kind'] == 'blog' and row['status'] == 'archived':
        failures = len(row.get('image_download_failures', []))
        detail = '图像地址均已取得' if not failures else f'{failures} 个地址未取得，阅读副本保留在线引用'
        body.append(f"| {source_link(row['slug'], target, True)} | {len(row.get('image_files', []))}/{row['article_image_count']} | {detail} |")
body.extend(['', '图像数按不同 URL 去重，不等于文中引用次数；动画文件按原格式保存。页面中的数学排版、交互、嵌入内容、样式或未下载外部文件仍可能依赖网络。原始 HTML 和在线原文保留为对照依据，本批不宣称完整网页已离线复现。'])
if image_failures:
    body.extend(['', '未取得的图像地址：', ''])
    for row in rows:
        for failure in row.get('image_download_failures', []):
            body.append(f"- {row['source_id']}：[在线图像]({failure['url']})。")
body.extend(['', '## 已知内容辨析', '',
             source_link('wechat-kv-cache', target) + ' 将 KV Cache 的收益概括为总计算量 O(n²)→O(n)。应拆开投影/MLP 与全注意力扫描：缓存避免历史 token 重复投影，但每个新 token 仍访问历史 K/V，累计注意力计算与访存随序列增长。该表述不能当作完整生成过程的总复杂度结论。', '',
             source_link('wechat-prefill-decode', target) + ' 的“Prefill 计算密集、Decode 访存密集”用于常见场景的直觉；批量、序列长度、稠密/MoE 结构和执行实现会改变瓶颈。低精度指令和权重访问方式也需对应具体硬件、模型与实现。', '',
             '## 待补入口与边界', '',
             '- ' + source_link('hexagon-2026', target, True) + '：站点返回验证页面；只保留原始链接，未将返回页计入可用资料。',
             '- ' + source_link('su-rope', target, True) + '：作者站及备用域名返回 HTTP 403；正文未取得。RoPE 可先读已归档的 RoFormer 原论文。',
             '- ' + source_link('blackwell', target, True) + '：已保存官方架构概述和文档入口 HTML；补充 PDF 下载失败，未计入白皮书。',
             '- 各方向的综合研究报告、推导验证、代码复现和设备测量尚未开展；本批是资料集与导读准备。', '',
             '## 可追溯文件', '',
             '- [正式归档清单](source-manifest.json)：稳定编号、版本、来源文件与图示路径、字节数、SHA-256、阅读范围及已知限制。',
             '- [下载尝试记录](original_file/acquisition-20261002.json)：本批的原始抓取结果及错误信息。',
             '- [核查结果](material-validation.json)：文件完整性、图像可解析性、索引链接与阅读副本结构核查。',
             '- [阅读路线](materials-reading-guide.md)：根据研究问题选择资料。'])
write_new(target, '\n'.join(body))
print(json.dumps(summary, ensure_ascii=False, indent=2))
