# AI008：Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity

主归属：[AI 算法与基础技术](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2101.03961)
- 版本：2101.03961v3
- 归档日期：2026-10-02
- 作者/团队：Fedus, William；Zoph, Barret；Shazeer, Noam
- arXiv 首次提交日期：2021/01/11

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI008-switch-transformer.metadata.html](../../original_file/papers/AI008-switch-transformer.metadata.html) | 论文元数据页 |
| [AI008-switch-transformer.pdf](../../original_file/papers/AI008-switch-transformer.pdf) | 40 页 PDF |

## 入选理由与研究用途

作为 MoE 基础来源，研究 token 路由、专家容量和负载均衡，并区分总参数量、激活参数量与执行成本。

## 建议阅读定位

Switch Routing；capacity factor；load balancing；distributed implementation。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

单专家路由及实验设置有明确边界，不等同于所有现代 MoE 配方。

## 交叉阅读

- [AI016：DeepSeek-V3 Technical Report](../../MODELS/sources/AI016-deepseek-v3.md)
- [AI015：Qwen3 Technical Report](../../MODELS/sources/AI015-qwen3.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
