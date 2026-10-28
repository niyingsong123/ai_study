# AI 学习项目

本项目是长期维护的 AI 技术与架构研究库，用于研究 AI 算法、关键技术、代表性大模型、训练与推理系统，以及云端和端侧芯片架构。参照 soc_study 的方式组织学习资料，保留原始来源，积累可追溯、可复用的研究成果。

研究主线：**应用需求 → 算法与模型 → 算子和数据流 → 训练与推理系统 → 云端或端侧硬件 → 性能与效果评估。**

## 阅读入口

- [项目上下文](project-context.md)：已确认的项目定位、研究范围、研究方法与长期约定。
- [研究路线图](research-roadmap.md)：阶段安排、专题依赖、近期切入点与完成条件。
- [资料集与来源](sources.md)：已收录资料、原始链接、本地位置及归档状态。
- [资料阅读路线](materials-reading-guide.md)：从推理入门进入模型、系统、云端与端侧，并按问题选择分支。
- [原始学习资料](original_file/README.md)：原始文件和网页链接的保存说明。
- [归档与阅读核查](source-reading-audit.md)：本批检查范围、版本限制和待补资料。

## 当前研究安排

2026-10-02，用户确认研究计划 v0.1，现已保存为[项目上下文](project-context.md)和[研究路线图](research-roadmap.md) v1.0。范围覆盖算法与基础技术、代表性大模型、训练与推理系统、云端芯片与集群、端侧模型与芯片，以及应用机制与扩展专题。

近期建议从《大模型推理的完整过程：从输入 token 到云端与端侧执行》切入，先围绕一个公开的稠密 Transformer 模型串起计算过程和资源需求，再研究 MoE、推理框架、云端加速器与端侧 NPU。首批已准备 Qwen3 报告、固定版本实现、推理入门文章及相关系统资料；具体模型检查点和实验条件在专题启动时核实。当前完成规划、资料集和导读准备，各阶段的综合研究及实验尚未开展。

## 分类资料集

2026-10-02，登记 65 项来源，已取得 63 项可用原文，另 2 项待补正文。资料包含 44 篇原始论文/技术报告、2 份官方白皮书、6 份官方网页文档、3 组固定提交的选定源码和 8 篇作者文章。原始 PDF 共 46 份、1196 页；文章另保存 229 个独立图像文件。

| 方向 | 已取得/登记 | 代表性资料 |
| --- | --- | --- |
| [AI 算法与基础技术](ALGORITHMS/README.md) | 14/15 | Transformer、ResNet、Adam、DDPM、Mamba、MoE、LoRA、量化与蒸馏 |
| [代表性大模型](MODELS/README.md) | 11/11 | Qwen、DeepSeek、Llama、Gemma、视觉语言模型与架构图解 |
| [训练与推理系统](TRAINING_INFERENCE/README.md) | 15/15 | Prefill/Decode、KV Cache、FlashAttention、vLLM、ZeRO、后训练 |
| [云端芯片与集群](CLOUD_ACCELERATORS/README.md) | 6/6 | NVIDIA Blackwell、AMD CDNA 4、Google TPU、NCCL、MLPerf |
| [端侧模型与芯片](EDGE_AI/README.md) | 7/8 | Qualcomm NPU、MobileLLM、MCUNet、ONNX QNN、ExecuTorch、MLX、llama.cpp |
| [应用机制与扩展](APPLICATIONS/README.md) | 10/10 | RAG、Agent、工具调用、视觉、语音、推荐与机器人 |

每份来源均有唯一编号和主导读，记录版本、本地原文、建议阅读章节、适用边界与交叉引用。作者文章包含 Jay Alammar、Lilian Weng、Sebastian Raschka、Horace He，以及用户提供的两篇微信文章。阅读状态与下载状态分别登记，详见[资料总索引](sources.md)。

## 目录组织

- `project-context.md`：长期研究约定。
- `research-roadmap.md`：阶段安排与专题依赖。
- `original_file/`：按论文、官方文档、作者文章、选定源码、微信及待补入口保存原始学习资料。
- `sources.md`：维护全项目资料索引。
- 六个方向已按 `<方向>/README.md` 与 `<方向>/sources/` 建立入口、分类索引和逐篇导读。具体专题启动时，再按需要建立 `research-plan.md`、报告及实验。完整用途见[项目上下文](project-context.md#目录组织)。
- `source-manifest.json`：记录全部来源的版本、文件路径、SHA-256、阅读范围和下载状态。

## 当前资料

2026-10-01 收录用户提供的两篇微信公众号文章链接，保留编号 AI001、AI002。2026-10-02 已成功取得正文及图示，核实为 aneasystone（「日习一技」）的《学习大模型推理的两个阶段：Prefill 与 Decode》和《学习大模型推理的 KV Cache》，纳入[训练与推理资料集](TRAINING_INFERENCE/sources/README.md)。原始链接文件继续保留。

## GitHub 同步与本地资料

GitHub 仓库保存项目文档、六方向资料索引与导读、来源清单、归档核查记录及维护脚本。`original_file/README.md` 作为原件目录说明一并保存；其余下载原文、网页副本、源码快照和图像，以及 `tmp/` 和 Python 缓存，仅在本地保留，由 `.gitignore` 排除。

导读和清单中的原件相对路径用于完整本地资料库，GitHub 副本不包含这些文件。在线阅读请使用各来源导读中的原始链接；需要运行 `scripts/validate_materials.py` 核查原件时，须先具备与清单版本一致的本地资料。归档核查记录说明当时实际检查范围，不代表每次同步都重新精读或完成视觉审核。
