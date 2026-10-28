# 云端芯片与集群架构

比较 GPU、TPU 的公开计算与存储结构，并把模型负载、HBM、互连和集群通信联系起来。

本轮完成资料准备和导读整理。共登记 6 项，取得 6 项；综合报告与实验按专题另行推进。

## 资料入口

[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)

## 建议阅读顺序

- **架构入口**：[AI035](sources/AI035-blackwell.md) → [AI036](sources/AI036-cdna4.md) → [AI038](sources/AI038-tpu-first.md) → [AI037](sources/AI037-tpu-v4.md)。
- **负载与集群**：[AI022](../MODELS/sources/AI022-deepseek-hardware.md) → [AI026](../TRAINING_INFERENCE/sources/AI026-megatron-lm.md) → [AI039](sources/AI039-nccl.md) → [AI040](sources/AI040-mlperf-inference.md)。

## 研究时应回答的问题

- 矩阵单元、向量计算、片上存储和 HBM 怎样参与模型执行？
- 单芯片、单机和多机分别受到什么容量、带宽或通信限制？
- 硬件性能声明的精度、稀疏性、模型与测量条件是否可比？

## 后续连接

[训练与推理系统](../TRAINING_INFERENCE/README.md) · [代表性大模型](../MODELS/README.md) · [端侧模型与芯片架构](../EDGE_AI/README.md)
