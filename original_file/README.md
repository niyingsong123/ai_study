# 原始学习资料

本目录参照 soc_study 的 `original_file/` 保存原始资料。原始文件保留原件；网页链接按来源保存，正文是否已归档在[总资料索引](../sources.md)中注明。

## 归档结构

| 目录/文件 | 保存内容 |
| --- | --- |
| `papers/` | 44 篇 arXiv 原始论文/技术报告 PDF 与元数据页；下载版本固定为 vN |
| `official/` | AMD CDNA 4、Qualcomm NPU 两份白皮书 PDF，以及指定官方 HTML 文档和架构页面 |
| `blogs/` | 作者原站 HTML、派生正文阅读副本及 `assets/<来源编号>/` 下的可取得图示 |
| `code/` | MLX、llama.cpp、Transformers Qwen3 的提交元数据及选定源文件 |
| `wechat/` | 用户提供的原始 `.url` 链接和后续取得的文章 HTML |
| `pending/` | 未取得正文的来源链接；验证页面不计入可用原文 |
| [acquisition-20261002.json](acquisition-20261002.json) | 本批下载结果、版本、路径、哈希和失败原因 |

完整来源与逐篇入口见[总索引](../sources.md)，正式文件清单见[source-manifest.json](../source-manifest.json)。原始 PDF 共 46 份、1196 页；HTML 是指定页面的归档快照，不是整站镜像。阅读副本为派生文件，原始 HTML 同时保留。

## 微信公众号资料

- AI001《学习大模型推理的两个阶段：Prefill 与 Decode》：[原始链接文件](wechat/AI001-dId6qeAjZpzAkke2JjLdfg.url) · [原始 HTML](wechat/AI001-article.html) · [本地阅读副本](blogs/AI001-wechat-prefill-decode.reader.html) · [导读](../TRAINING_INFERENCE/sources/AI001-wechat-prefill-decode.md)。
- AI002《学习大模型推理的 KV Cache》：[原始链接文件](wechat/AI002-qADtdc_tAdkX1dRKFG50DQ.url) · [原始 HTML](wechat/AI002-article.html) · [本地阅读副本](blogs/AI002-wechat-kv-cache.reader.html) · [导读](../TRAINING_INFERENCE/sources/AI002-wechat-kv-cache.md)。

两个 `.url` 文件可在 Windows 中双击打开原始网页。首次收录于 2026-10-01；2026-10-02 已补齐正文，作者为 aneasystone（「日习一技」），两文 14 个正文图像地址均已保存。阅读副本放在 `blogs/`，便于统一复用图示归档。

## 归档边界

来源文件以原始下载内容保存，逐篇导读位于对应研究方向的 `sources/`。代码只归档指定文件，不代表完整仓库；未下载模型权重或训练数据集。数学排版、交互及未取得的图像可能仍需在线原文，详见[实际核查范围与缺口](../source-reading-audit.md)。
