# AI039：NCCL User Guide: Collective Operations

主归属：[云端芯片与集群架构](../README.md)。来源性质：官方网页文档。

- 原始来源：[原文或固定版本仓库](https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html)
- 版本：页面标注 NCCL 2.32.3；2026-10-02 快照
- 归档日期：2026-10-02
- 发布日期：本次未可靠提取；归档日期不代表发布日期。

## 归档与阅读状态

已检查取得的页面及相关章节入口；仅归档指定页面，未离线保存整个文档站。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI039-nccl.html](../../original_file/official/AI039-nccl.html) | 原始网页 HTML |

## 入选理由与研究用途

理解 AllReduce、AllGather、ReduceScatter 等集合通信的语义，用来定位训练及模型并行中的通信需求。

## 建议阅读定位

AllReduce；Broadcast；ReduceScatter；AllGather。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

此页是 API/通信语义文档；环树算法、拓扑和带宽需查具体版本实现。

## 交叉阅读

- [AI026：Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism](../../TRAINING_INFERENCE/sources/AI026-megatron-lm.md)
- [AI025：ZeRO: Memory Optimizations Toward Training Trillion Parameter Models](../../TRAINING_INFERENCE/sources/AI025-zero.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
