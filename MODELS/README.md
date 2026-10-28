# 代表性大模型

以公开报告和固定版本实现为依据，比较稠密、MoE、推理及多模态模型的设计取舍。

本轮完成资料准备和导读整理。共登记 11 项，取得 11 项；综合报告与实验按专题另行推进。

## 资料入口

[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)

## 建议阅读顺序

- **稠密模型基线**：[AI059](sources/AI059-illustrated-gpt2.md) → [AI015](sources/AI015-qwen3.md) → [AI065](sources/AI065-qwen3-implementation.md) → [AI018](sources/AI018-llama3.md) → [AI021](sources/AI021-gemma3.md)。
- **MoE 与推理能力**：[AI008](../ALGORITHMS/sources/AI008-switch-transformer.md) → [AI016](sources/AI016-deepseek-v3.md) → [AI017](sources/AI017-deepseek-r1.md) → [AI028](../TRAINING_INFERENCE/sources/AI028-deepseek-math.md) → [AI022](sources/AI022-deepseek-hardware.md)。
- **扩展与架构比较**：[AI019](sources/AI019-qwen25-vl.md) → [AI020](sources/AI020-qwen38-next.md) → [AI062](sources/AI062-raschka-comparison.md)。

## 研究时应回答的问题

- Attention、归一化、位置编码和前馈层的具体配置是什么？
- 总参数、每 token 激活参数和训练/推理状态各自占用多少资源？
- 能力变化来自结构、数据、训练目标还是后训练？公开证据支持到哪一步？

## 后续连接

[AI 算法与基础技术](../ALGORITHMS/README.md) · [训练与推理系统](../TRAINING_INFERENCE/README.md) · [云端芯片与集群架构](../CLOUD_ACCELERATORS/README.md) · [应用机制与扩展专题](../APPLICATIONS/README.md)
