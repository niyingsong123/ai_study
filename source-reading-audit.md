# 首批资料归档与阅读核查

批次：AI-MATERIALS-20261002。归档日：2026-10-02。

## 资料规模

共登记 65 项稳定编号，取得 63 项可用原文；2 项保留链接、待补正文。

| 类型 | 已取得来源数 | 保存范围 |
| --- | --- | --- |
| 原始论文/技术报告 | 44 | arXiv 元数据页与固定 vN 的 PDF |
| 官方白皮书 | 2 | 原始 PDF |
| 官方文档与架构页面 | 6 | 指定 HTML 页面；不是整个站点的离线镜像 |
| 作者技术文章 | 8 | 原始 HTML、正文阅读副本及可取得图示，含用户提供的两篇微信文章 |
| 选定源码 | 3 | MLX、llama.cpp 与 Transformers Qwen3 的固定提交及指定文件 |

合计 46 份 PDF、1196 页；229 个独立图像文件、8 个派生阅读副本。原始文件与图像约 184.7 MiB（不含派生阅读副本、总清单和临时检查文件）。

## 本轮实际检查

- 下载文件均记录原始 URL、本地路径、字节数和 SHA-256；整理时重新读取文件核对大小与哈希。论文元数据记录题名、作者、首次提交日期和下载版本。
- 46 份 PDF 均通过文件头、页树和全页文字提取检查；已渲染并逐一目视检查全部 PDF 的第 1 页，确认不是验证页面、空白或明显错题文件。
- 首页检查不等于逐页阅读，也不等于全文图表的视觉核对。论文导读依据题名、摘要/导言及选读信息建立；推荐章节仍待具体专题精读。
- 博主文章检查实际取得的正文、章节入口及选定段落；保存原始 HTML，另生成阅读副本。本批未把原文表格转换成 Markdown 表格。
- 代码按提交固定，仅保存选定文件；未编译运行，未执行下载的仓库脚本。模型权重、训练数据集和完整仓库不在本批范围。
- 六个方向均建立入口、分类索引与逐篇导读。同一来源只有一篇主导读，其他方向通过编号交叉引用。

最终离线核查通过：352 个归档/派生文件的大小与 SHA-256 相符，229 个图像文件可解析，84 份入口与导读中的 775 个本地链接可定位。8 篇文章原始 HTML 与阅读副本中的全部 5 个表格，已对照单元格文字、顺序及显式合并属性；这是结构与文字核对，未进行完整网页或表格的视觉核对。

## 作者文章图示与外部依赖

| 来源 | 本地图像/正文独立图像地址 | 状态 |
| --- | --- | --- |
| [AI001：学习大模型推理的两个阶段：Prefill 与 Decode](TRAINING_INFERENCE/sources/AI001-wechat-prefill-decode.md) | 8/8 | 图像地址均已取得 |
| [AI002：学习大模型推理的 KV Cache](TRAINING_INFERENCE/sources/AI002-wechat-kv-cache.md) | 6/6 | 图像地址均已取得 |
| [AI058：The Illustrated Transformer — Jay Alammar](ALGORITHMS/sources/AI058-illustrated-transformer.md) | 35/37 | 2 个地址未取得，阅读副本保留在线引用 |
| [AI059：The Illustrated GPT-2 — Jay Alammar](MODELS/sources/AI059-illustrated-gpt2.md) | 62/64 | 2 个地址未取得，阅读副本保留在线引用 |
| [AI060：LLM Powered Autonomous Agents — Lilian Weng](APPLICATIONS/sources/AI060-lilian-agents.md) | 12/13 | 1 个地址未取得，阅读副本保留在线引用 |
| [AI061：What are Diffusion Models? — Lilian Weng](ALGORITHMS/sources/AI061-lilian-diffusion.md) | 18/19 | 1 个地址未取得，阅读副本保留在线引用 |
| [AI062：The Big LLM Architecture Comparison — Sebastian Raschka](MODELS/sources/AI062-raschka-comparison.md) | 75/75 | 图像地址均已取得 |
| [AI063：Making Deep Learning Go Brrrr From First Principles — Horace He](TRAINING_INFERENCE/sources/AI063-go-brrr.md) | 13/13 | 图像地址均已取得 |

图像数按不同 URL 去重，不等于文中引用次数；动画文件按原格式保存。页面中的数学排版、交互、嵌入内容、样式或未下载外部文件仍可能依赖网络。原始 HTML 和在线原文保留为对照依据，本批不宣称完整网页已离线复现。

未取得的图像地址：

- AI058：[在线图像](https://jalammar.github.io/images/t/transformer_decoding_1.gif)。
- AI058：[在线图像](https://jalammar.github.io/images/t/transformer_decoding_2.gif)。
- AI059：[在线图像](https://jalammar.github.io/images/xlnet/gpt-2-autoregression-2.gif)。
- AI059：[在线图像](https://jalammar.github.io/images/gpt2/gpt2-mlp-2.gif)。
- AI060：[在线图像](https://lilianweng.github.io/posts/2023-06-23-agent/sea-otter.png)。
- AI061：[在线图像](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/diffusion-example.png)。

## 已知内容辨析

[AI002](TRAINING_INFERENCE/sources/AI002-wechat-kv-cache.md) 将 KV Cache 的收益概括为总计算量 O(n²)→O(n)。应拆开投影/MLP 与全注意力扫描：缓存避免历史 token 重复投影，但每个新 token 仍访问历史 K/V，累计注意力计算与访存随序列增长。该表述不能当作完整生成过程的总复杂度结论。

[AI001](TRAINING_INFERENCE/sources/AI001-wechat-prefill-decode.md) 的“Prefill 计算密集、Decode 访存密集”用于常见场景的直觉；批量、序列长度、稠密/MoE 结构和执行实现会改变瓶颈。低精度指令和权重访问方式也需对应具体硬件、模型与实现。

## 待补入口与边界

- [AI042：Qualcomm Hexagon NPU: mobile architecture for agentic AI (2026-09)](EDGE_AI/sources/AI042-hexagon-2026.md)：站点返回验证页面；只保留原始链接，未将返回页计入可用资料。
- [AI064：Transformer升级之路：2、博采众长的旋转式位置编码 — 苏剑林](ALGORITHMS/sources/AI064-su-rope.md)：作者站及备用域名返回 HTTP 403；正文未取得。RoPE 可先读已归档的 RoFormer 原论文。
- [AI035：NVIDIA Blackwell Architecture (official snapshot)](CLOUD_ACCELERATORS/sources/AI035-blackwell.md)：已保存官方架构概述和文档入口 HTML；补充 PDF 下载失败，未计入白皮书。
- 各方向的综合研究报告、推导验证、代码复现和设备测量尚未开展；本批是资料集与导读准备。

## 可追溯文件

- [正式归档清单](source-manifest.json)：稳定编号、版本、来源文件与图示路径、字节数、SHA-256、阅读范围及已知限制。
- [下载尝试记录](original_file/acquisition-20261002.json)：本批的原始抓取结果及错误信息。
- [核查结果](material-validation.json)：文件完整性、图像可解析性、索引链接与阅读副本结构核查。
- [阅读路线](materials-reading-guide.md)：根据研究问题选择资料。
