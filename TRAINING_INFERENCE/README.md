# 训练与推理系统

从单请求逐 token 执行进入缓存、调度、算子优化、分布式训练和后训练，解释实际系统瓶颈。

本轮完成资料准备和导读整理。共登记 15 项，取得 15 项；综合报告与实验按专题另行推进。

## 资料入口

[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)

## 建议阅读顺序

- **推理入门与服务**：[AI001](sources/AI001-wechat-prefill-decode.md) → [AI002](sources/AI002-wechat-kv-cache.md) → [AI065](../MODELS/sources/AI065-qwen3-implementation.md) → [AI024](sources/AI024-pagedattention.md) → [AI032](sources/AI032-vllm-architecture.md)。
- **性能与执行**：[AI063](sources/AI063-go-brrr.md) → [AI023](sources/AI023-flashattention.md) → [AI029](sources/AI029-speculative-decoding.md) → [AI030](sources/AI030-sglang.md) → [AI034](sources/AI034-tensorrt-llm.md) → [AI031](sources/AI031-mlir.md)。
- **分布式训练与后训练**：[AI005](../ALGORITHMS/sources/AI005-adam.md) → [AI025](sources/AI025-zero.md) → [AI026](sources/AI026-megatron-lm.md) → [AI039](../CLOUD_ACCELERATORS/sources/AI039-nccl.md) → [AI033](sources/AI033-rlhf.md) → [AI027](sources/AI027-dpo.md) → [AI028](sources/AI028-deepseek-math.md)。

## 研究时应回答的问题

- Prefill 与 Decode 的输入、缓存访问和资源需求怎样不同？
- 吞吐、首 token 延迟和每 token 延迟怎样受批量、调度与存储影响？
- 训练状态怎样分片？计算与通信是否重叠？优化的收益如何验证？

## 后续连接

[代表性大模型](../MODELS/README.md) · [云端芯片与集群架构](../CLOUD_ACCELERATORS/README.md) · [端侧模型与芯片架构](../EDGE_AI/README.md)
