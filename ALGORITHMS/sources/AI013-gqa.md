# AI013：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints

主归属：[AI 算法与基础技术](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2305.13245)
- 版本：2305.13245v3
- 归档日期：2026-10-02
- 作者/团队：Ainslie, Joshua；Lee-Thorp, James；de Jong, Michiel；Zemlyanskiy, Yury；Lebrón, Federico；Sanghai, Sumit
- arXiv 首次提交日期：2023/05/22

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI013-gqa.metadata.html](../../original_file/papers/AI013-gqa.metadata.html) | 论文元数据页 |
| [AI013-gqa.pdf](../../original_file/papers/AI013-gqa.pdf) | 7 页 PDF |

## 入选理由与研究用途

理解查询头与键值头的分组关系，分析多头注意力、MQA、GQA 对 KV Cache 规模和模型质量的影响。

## 建议阅读定位

Method；GQA variants；quality and speed experiments。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

缓存容量估算需使用模型实际 KV head 数、精度、层数与序列长度。

## 交叉阅读

- [AI015：Qwen3 Technical Report](../../MODELS/sources/AI015-qwen3.md)
- [AI018：The Llama 3 Herd of Models](../../MODELS/sources/AI018-llama3.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
