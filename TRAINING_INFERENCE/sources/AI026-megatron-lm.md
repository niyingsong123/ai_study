# AI026：Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism

主归属：[训练与推理系统](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/1909.08053)
- 版本：1909.08053v4
- 归档日期：2026-10-02
- 作者/团队：Shoeybi, Mohammad；Patwary, Mostofa；Puri, Raul；LeGresley, Patrick；Casper, Jared；Catanzaro, Bryan
- arXiv 首次提交日期：2019/09/17

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI026-megatron-lm.metadata.html](../../original_file/papers/AI026-megatron-lm.metadata.html) | 论文元数据页 |
| [AI026-megatron-lm.pdf](../../original_file/papers/AI026-megatron-lm.pdf) | 15 页 PDF |

## 入选理由与研究用途

从 Transformer 的矩阵切分和通信位置理解张量并行，为多卡训练及推理中的计算通信映射提供基础。

## 建议阅读定位

Model Parallelism；Transformer layers；scaling evaluation。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

这是早期方法论文；现代 Megatron 的流水、序列及专家并行需补版本文档。

## 交叉阅读

- [AI025：ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](AI025-zero.md)
- [AI039：NCCL User Guide: Collective Operations](../../CLOUD_ACCELERATORS/sources/AI039-nccl.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
