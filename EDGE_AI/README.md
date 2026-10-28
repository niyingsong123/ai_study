# 端侧模型与芯片架构

围绕手机、PC 和微控制器的容量、带宽、持续功耗与工具链约束，研究模型和执行系统共同设计。

本轮完成资料准备和导读整理。共登记 8 项，取得 7 项；综合报告与实验按专题另行推进。

## 资料入口

[全部来源与逐篇导读](sources/README.md) · [全项目资料集](../sources.md) · [总体阅读路线](../materials-reading-guide.md)

## 建议阅读顺序

- **端侧约束与小模型**：[AI041](sources/AI041-qualcomm-npu.md) → [AI043](sources/AI043-mobilellm.md) → [AI010](../ALGORITHMS/sources/AI010-knowledge-distillation.md) → [AI011](../ALGORITHMS/sources/AI011-awq.md)。
- **部署与执行**：[AI045](sources/AI045-onnx-qnn.md) → [AI046](sources/AI046-executorch.md) → [AI048](sources/AI048-llama-cpp.md) → [AI047](sources/AI047-mlx.md)。
- **微控制器分支**：[AI004](../ALGORITHMS/sources/AI004-resnet.md) → [AI044](sources/AI044-mcunet.md)。

待补入口：[AI042：Qualcomm Hexagon NPU: mobile architecture for agentic AI (2026-09)](sources/AI042-hexagon-2026.md)。可先采用对应已下载原始资料。

## 研究时应回答的问题

- 目标设备支持哪些精度、算子、动态形状和模型规模？
- CPU、GPU、NPU 和存储之间怎样划分任务与共享数据？
- 短时性能与持续性能有什么差异？内存、功耗和任务效果如何一起比较？

## 后续连接

[AI 算法与基础技术](../ALGORITHMS/README.md) · [训练与推理系统](../TRAINING_INFERENCE/README.md) · [云端芯片与集群架构](../CLOUD_ACCELERATORS/README.md)
