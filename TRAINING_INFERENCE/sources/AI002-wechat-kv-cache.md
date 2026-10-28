# AI002：学习大模型推理的 KV Cache

主归属：[训练与推理系统](../README.md)。来源性质：作者技术文章。

- 原始来源：[原文或固定版本仓库](https://mp.weixin.qq.com/s/qADtdc_tAdkX1dRKFG50DQ)
- 版本：2026-10-02 snapshot
- 归档日期：2026-10-02
- 作者/团队：aneasystone
- 发布账号：日习一技
- 发布日期：本次未可靠提取；归档日期不代表发布日期。

## 归档与阅读状态

已检查取得的正文、章节入口及选定段落；未逐段核验全部推导、示例和结论。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

优先打开：[本地正文阅读副本](../../original_file/blogs/AI002-wechat-kv-cache.reader.html)。

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI002-article.html](../../original_file/wechat/AI002-article.html) | 原始网页 HTML |

正文图像：已保存 6/6 个独立图像地址；重复使用的图像只保存一份。
原始 HTML 完整保留；本地阅读副本保留正文、可取得图示和原始表格，移除页面导航与脚本。数学排版、交互及外部依赖可能仍需打开在线原文。

## 入选理由与研究用途

中文 KV Cache 入门文章，包含因果注意力、逐 token 追加、缓存容量公式及 Qwen3 小模型示例，适合建立缓存结构和资源估算的直觉。

## 建议阅读定位

正文中的工作流程、瓶颈或缓存容量说明，以及代码示例；结合交叉引用的原始资料阅读。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

文中 O(n²)→O(n) 是对重复计算的简化说法，不应作为完整自注意力总复杂度结论；全注意力解码仍访问历史 K/V，累计注意力计算和访存随序列增长。示例 cache API 需核对 Transformers 版本。
辨析时应分别统计投影/MLP 与注意力。对于固定模型、固定初始 prompt、全注意力逐步生成，缓存后的每步注意力仍扫描增长的历史；不能将新 token 的投影计算量直接当作整个生成过程的总计算量。示例中的 KB/KiB 也需采用统一单位。

## 交叉阅读

- [AI013：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../ALGORITHMS/sources/AI013-gqa.md)
- [AI024：Efficient Memory Management for Large Language Model Serving with PagedAttention](AI024-pagedattention.md)
- [AI065：Transformers Qwen3 implementation (v4.55.4 selected files)](../../MODELS/sources/AI065-qwen3-implementation.md)
- [AI063：Making Deep Learning Go Brrrr From First Principles — Horace He](AI063-go-brrr.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
