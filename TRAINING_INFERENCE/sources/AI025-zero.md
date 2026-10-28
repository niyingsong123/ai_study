# AI025：ZeRO: Memory Optimizations Toward Training Trillion Parameter Models

主归属：[训练与推理系统](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/1910.02054)
- 版本：1910.02054v3
- 归档日期：2026-10-02
- 作者/团队：Rajbhandari, Samyam；Rasley, Jeff；Ruwase, Olatunji；He, Yuxiong
- arXiv 首次提交日期：2019/10/04

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI025-zero.metadata.html](../../original_file/papers/AI025-zero.metadata.html) | 论文元数据页 |
| [AI025-zero.pdf](../../original_file/papers/AI025-zero.pdf) | 24 页 PDF |

## 入选理由与研究用途

按优化器状态、梯度和参数理解训练内存，并研究不同分片阶段的存储节省和通信代价。

## 建议阅读定位

Memory consumption；ZeRO stages；communication analysis。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

训练状态分片与推理 KV Cache 是不同问题；具体 offload 和实现能力需查对应版本。

## 交叉阅读

- [AI005：Adam: A Method for Stochastic Optimization](../../ALGORITHMS/sources/AI005-adam.md)
- [AI026：Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](AI026-megatron-lm.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
