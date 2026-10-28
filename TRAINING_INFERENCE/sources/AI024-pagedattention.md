# AI024：Efficient Memory Management for Large Language Model Serving with PagedAttention

主归属：[训练与推理系统](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2309.06180)
- 版本：2309.06180v1
- 归档日期：2026-10-02
- 作者/团队：Kwon, Woosuk；Li, Zhuohan；Zhuang, Siyuan；Sheng, Ying；Zheng, Lianmin；Yu, Cody Hao；Gonzalez, Joseph E.；Zhang, Hao；Stoica, Ion
- arXiv 首次提交日期：2023/09/12

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI024-pagedattention.metadata.html](../../original_file/papers/AI024-pagedattention.metadata.html) | 论文元数据页 |
| [AI024-pagedattention.pdf](../../original_file/papers/AI024-pagedattention.pdf) | 16 页 PDF |

## 入选理由与研究用途

解释 KV Cache 分页、映射、共享和内存碎片，连接请求调度、并发和推理服务吞吐。

## 建议阅读定位

PagedAttention；KV cache management；serving and evaluation。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

论文时期 vLLM 与当前版本存在差异；页表类比不代表它与 CPU/GPU 地址翻译机制完全相同。

## 交叉阅读

- [AI032：vLLM Architecture Overview (v0.10.2)](AI032-vllm-architecture.md)
- [AI013：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../ALGORITHMS/sources/AI013-gqa.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
