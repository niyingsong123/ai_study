# AI023：FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness

主归属：[训练与推理系统](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2205.14135)
- 版本：2205.14135v2
- 归档日期：2026-10-02
- 作者/团队：Dao, Tri；Fu, Daniel Y.；Ermon, Stefano；Rudra, Atri；Ré, Christopher
- arXiv 首次提交日期：2022/05/27

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI023-flashattention.metadata.html](../../original_file/papers/AI023-flashattention.metadata.html) | 论文元数据页 |
| [AI023-flashattention.pdf](../../original_file/papers/AI023-flashattention.pdf) | 34 页 PDF |

## 入选理由与研究用途

研究分块、在线 softmax 和减少高带宽内存读写的机制，说明数学结果相同的算子可以有不同的数据搬运成本。

## 建议阅读定位

IO complexity；FlashAttention algorithm；kernel evaluation。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

IO 分析与目标 GPU kernel 性能分别核实；不从理论复杂度直接推定全模型加速。

## 交叉阅读

- [AI003：Attention Is All You Need](../../ALGORITHMS/sources/AI003-attention-is-all-you-need.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
