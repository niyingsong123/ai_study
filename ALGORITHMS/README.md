# AI 算法与基础技术

理解算法解决的问题、关键数学关系与计算过程，为模型、系统和硬件研究提供共同基础。

本轮完成资料准备和导读整理。共登记 15 项，取得 14 项；综合报告与实验按专题另行推进。

## 资料入口

[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)

## 建议阅读顺序

- **Transformer 主线**：[AI058](sources/AI058-illustrated-transformer.md) → [AI003](sources/AI003-attention-is-all-you-need.md) → [AI014](sources/AI014-roformer.md) → [AI013](sources/AI013-gqa.md) → [AI008](sources/AI008-switch-transformer.md) → [AI007](sources/AI007-mamba.md)。
- **训练与压缩**：[AI005](sources/AI005-adam.md) → [AI009](sources/AI009-lora.md) → [AI010](sources/AI010-knowledge-distillation.md) → [AI012](sources/AI012-gptq.md) → [AI011](sources/AI011-awq.md)。
- **视觉与生成分支**：[AI004](sources/AI004-resnet.md) → [AI006](sources/AI006-ddpm.md) → [AI061](sources/AI061-lilian-diffusion.md)。

待补入口：[AI064：Transformer升级之路：2、博采众长的旋转式位置编码 — 苏剑林](sources/AI064-su-rope.md)。可先采用对应已下载原始资料。

## 研究时应回答的问题

- 注意力、前馈层和状态更新分别执行什么计算？张量形状怎样变化？
- 优化方法改变了训练目标、模型结构还是数值表示？有什么代价？
- 计算复杂度、参数量、缓存大小与实际设备性能怎样关联？

## 后续连接

[代表性大模型](../MODELS/README.md) · [训练与推理系统](../TRAINING_INFERENCE/README.md) · [端侧模型与芯片架构](../EDGE_AI/README.md)
