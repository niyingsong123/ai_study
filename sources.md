# 资料集与来源

归档批次：2026-10-02。共登记 65 项稳定来源编号，已取得 63 项可用原文；2 项保留链接、待补正文。每份来源只维护一篇主导读，跨方向通过编号复用。

已取得资料：44 篇原始论文/技术报告、2 份官方白皮书 PDF、6 份官方网页文档、3 组固定提交的选定源码、8 篇作者技术文章。共 46 份 PDF（1196 页），另保存 8 个文章阅读副本及 229 个独立图像文件。

[建议阅读路线](materials-reading-guide.md) · [原始文件入口](original_file/README.md) · [归档与阅读核查](source-reading-audit.md) · [机器可读清单](source-manifest.json)

## 六个研究方向

| 方向 | 已取得/登记 | 分类索引 | 核心覆盖 |
| --- | --- | --- | --- |
| [AI 算法与基础技术](ALGORITHMS/README.md) | 14/15 | [全部来源](ALGORITHMS/sources/README.md) | Transformer、CNN、扩散、SSM、MoE、优化、LoRA、量化、蒸馏 |
| [代表性大模型](MODELS/README.md) | 11/11 | [全部来源](MODELS/sources/README.md) | Qwen、DeepSeek、Llama、Gemma、多模态与选定实现 |
| [训练与推理系统](TRAINING_INFERENCE/README.md) | 15/15 | [全部来源](TRAINING_INFERENCE/sources/README.md) | 缓存、调度、Attention IO、编译、分布式训练及后训练 |
| [云端芯片与集群](CLOUD_ACCELERATORS/README.md) | 6/6 | [全部来源](CLOUD_ACCELERATORS/sources/README.md) | GPU/TPU、存储层次、互连、通信、评估口径 |
| [端侧模型与芯片](EDGE_AI/README.md) | 7/8 | [全部来源](EDGE_AI/sources/README.md) | 小模型、移动/PC/MCU、NPU、异构执行及部署工具链 |
| [应用机制与扩展](APPLICATIONS/README.md) | 10/10 | [全部来源](APPLICATIONS/sources/README.md) | RAG、Agent、工具、视觉、语音、推荐与具身智能 |

分类索引列出全部来源；逐篇导读提供原始 URL、本地文件、版本、建议阅读定位、适用边界及相关来源。固定的软件版本用于建立基线，不代表归档日的最新版本；公开报告中的性能结论仍需保留原实验条件。

## 用户提供的原始学习资料

首次收录：2026-10-01。2026-10-02 重新访问成功，以下题名与作者已从取得的原文核实；未可靠提取发布日期。

### AI001：学习大模型推理的两个阶段：Prefill 与 Decode

- 原始链接：[打开微信原文](https://mp.weixin.qq.com/s/dId6qeAjZpzAkke2JjLdfg)
- 本地链接文件：[AI001-dId6qeAjZpzAkke2JjLdfg.url](original_file/wechat/AI001-dId6qeAjZpzAkke2JjLdfg.url)
- 来源：用户提供。
- 作者：aneasystone；发布账号：日习一技。
- 归档状态：[原始 HTML](original_file/wechat/AI001-article.html)、[本地正文阅读副本](original_file/blogs/AI001-wechat-prefill-decode.reader.html)及 8 个正文图像地址均已保存。
- 阅读状态：已检查正文与选定段落，完成[入选导读](TRAINING_INFERENCE/sources/AI001-wechat-prefill-decode.md)；未复现文中的性能示例。常见瓶颈描述须对应批量、序列长度和实际实现。

### AI002：学习大模型推理的 KV Cache

- 原始链接：[打开微信原文](https://mp.weixin.qq.com/s/qADtdc_tAdkX1dRKFG50DQ)
- 本地链接文件：[AI002-qADtdc_tAdkX1dRKFG50DQ.url](original_file/wechat/AI002-qADtdc_tAdkX1dRKFG50DQ.url)
- 来源：用户提供。
- 作者：aneasystone；发布账号：日习一技。
- 归档状态：[原始 HTML](original_file/wechat/AI002-article.html)、[本地正文阅读副本](original_file/blogs/AI002-wechat-kv-cache.reader.html)及 6 个正文图像地址均已保存。
- 阅读状态：已检查正文与选定段落，完成[入选导读](TRAINING_INFERENCE/sources/AI002-wechat-kv-cache.md)；示例代码未运行。导读已标明总复杂度简化、缓存 API 版本和单位核对事项。

## 作者文章精选

作者文章按研究主题归属，用于图解、推导和阅读路线；模型事实、实现及性能结论与原始论文或官方资料交叉核对。优先选择作者原站、有清晰参考和具体技术内容的文章。

| 来源 | 作者 | 阅读用途 | 本地状态 |
| --- | --- | --- | --- |
| [AI058：The Illustrated Transformer](ALGORITHMS/sources/AI058-illustrated-transformer.md) | Jay Alammar | Attention、多头和 Transformer 结构图解 | 正文与可取得图示已归档 |
| [AI059：The Illustrated GPT-2](MODELS/sources/AI059-illustrated-gpt2.md) | Jay Alammar | 自回归语言模型与逐 token 生成 | 正文与可取得图示已归档 |
| [AI060：LLM Powered Autonomous Agents](APPLICATIONS/sources/AI060-lilian-agents.md) | Lilian Weng | 规划、记忆、工具与挑战的资料地图 | 正文与可取得图示已归档 |
| [AI061：What are Diffusion Models?](ALGORITHMS/sources/AI061-lilian-diffusion.md) | Lilian Weng | 扩散模型公式及方法关系 | 正文与可取得图示已归档 |
| [AI062：The Big LLM Architecture Comparison](MODELS/sources/AI062-raschka-comparison.md) | Sebastian Raschka | 开放模型结构比较与原始实现入口 | 取得的公开正文及图示已归档 |
| [AI063：Making Deep Learning Go Brrrr From First Principles](TRAINING_INFERENCE/sources/AI063-go-brrr.md) | Horace He | 计算、访存、执行开销和融合的性能直觉 | 正文与图示已归档 |
| [AI064：旋转式位置编码](ALGORITHMS/sources/AI064-su-rope.md) | 苏剑林 | RoPE 中文推导候选入口 | **待补正文，HTTP 403** |

用户提供的 AI001、AI002 同样属于作者技术文章，列于上一节。部分图像、数学排版或交互仍依赖在线原文，具体缺口见[核查记录](source-reading-audit.md)。

## 待补资料

- [AI042：Qualcomm Hexagon NPU 新架构文章](EDGE_AI/sources/AI042-hexagon-2026.md)：返回站点验证页面，未取得可用正文。先采用已下载的 [AI041 异构计算白皮书](EDGE_AI/sources/AI041-qualcomm-npu.md)。
- [AI064：苏剑林 RoPE 文章](ALGORITHMS/sources/AI064-su-rope.md)：正文未取得。先采用已下载的 [AI014 RoFormer 论文](ALGORITHMS/sources/AI014-roformer.md)。
- [AI035：Blackwell 官方资料](CLOUD_ACCELERATORS/sources/AI035-blackwell.md)：架构概述及文档入口 HTML 已保存，补充 PDF 下载失败；未计作白皮书。

## 归档记录

2026-10-01：尝试访问两篇微信原文，浏览工具无法打开，本地访问也未成功。本次保存的是链接，不是文章全文；未据此生成摘要、学习笔记或主题分类。

2026-10-02：用户授权按六个主要研究方向下载整理资料，并允许纳入高质量博主文章。完成本批下载、原始版本保存、六方向索引、逐篇导读、阅读路线及文件核查；原两篇微信链接保留稳定编号，补齐正文及图示。

当前阅读状态为资料筛选、归档与导读准备。未将推荐章节登记为全文精读完成，也未将资料整理登记为综合研究报告或设备验证完成。
