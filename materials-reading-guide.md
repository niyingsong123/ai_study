# 首批 AI 资料阅读路线

资料快照：2026-10-02。从[总索引](sources.md)或[六个方向入口](README.md#分类资料集)查找原文与逐篇导读。

论文用于建立机制与证据，作者文章用于图解和组织问题，官方文档与固定源码用于核对实现。阅读路线按问题选择，不要求逐份顺序读完。

## 首条路线：从输入 token 到云端与端侧执行

| 步骤 | 阅读资料 | 应形成的认识 |
| --- | --- | --- |
| 1. Transformer 与自回归 | [AI058](ALGORITHMS/sources/AI058-illustrated-transformer.md)、[AI003](ALGORITHMS/sources/AI003-attention-is-all-you-need.md)、[AI059](MODELS/sources/AI059-illustrated-gpt2.md) | 建立 Embedding、Attention、前馈层、因果掩码与输出采样的整体过程。 |
| 2. Prefill、Decode 与缓存 | [AI001](TRAINING_INFERENCE/sources/AI001-wechat-prefill-decode.md)、[AI002](TRAINING_INFERENCE/sources/AI002-wechat-kv-cache.md)、[AI013](ALGORITHMS/sources/AI013-gqa.md) | 解释两阶段输入、缓存追加、KV 头数和资源需求；留意微信文章中的复杂度简化。 |
| 3. 公开模型与实现 | [AI015](MODELS/sources/AI015-qwen3.md)、[AI065](MODELS/sources/AI065-qwen3-implementation.md) | 选择报告中的稠密成员，核对结构及代码；正式复现时补齐具体检查点配置与 tokenizer。 |
| 4. 服务与算子优化 | [AI024](TRAINING_INFERENCE/sources/AI024-pagedattention.md)、[AI032](TRAINING_INFERENCE/sources/AI032-vllm-architecture.md)、[AI023](TRAINING_INFERENCE/sources/AI023-flashattention.md)、[AI063](TRAINING_INFERENCE/sources/AI063-go-brrr.md) | 区分缓存组织、请求调度和算子 IO 优化，连接延迟、吞吐及访存瓶颈。 |
| 5. 云端硬件映射 | [AI035](CLOUD_ACCELERATORS/sources/AI035-blackwell.md)、[AI036](CLOUD_ACCELERATORS/sources/AI036-cdna4.md)、[AI037](CLOUD_ACCELERATORS/sources/AI037-tpu-v4.md)、[AI022](MODELS/sources/AI022-deepseek-hardware.md) | 把算子、权重、缓存与矩阵单元、HBM、互连和集群联系起来。 |
| 6. 端侧约束与运行时 | [AI041](EDGE_AI/sources/AI041-qualcomm-npu.md)、[AI011](ALGORITHMS/sources/AI011-awq.md)、[AI043](EDGE_AI/sources/AI043-mobilellm.md)、[AI045](EDGE_AI/sources/AI045-onnx-qnn.md)、[AI048](EDGE_AI/sources/AI048-llama-cpp.md) | 说明低比特、小模型、算子覆盖、异构执行和持续功耗的取舍。 |

这条路线准备了原文与导读；完整推理报告、资源估算和设备实测尚未开展。软件文档中的固定版本用于建立可追溯基线，不代表归档日的最新发布。

## 根据问题选择分支

| 问题 | 推荐入口 |
| --- | --- |
| MoE 为什么节省激活计算，又增加通信？ | [AI008](ALGORITHMS/sources/AI008-switch-transformer.md)、[AI016](MODELS/sources/AI016-deepseek-v3.md)、[AI022](MODELS/sources/AI022-deepseek-hardware.md) |
| 后训练如何形成指令遵循与推理能力？ | [AI033](TRAINING_INFERENCE/sources/AI033-rlhf.md)、[AI027](TRAINING_INFERENCE/sources/AI027-dpo.md)、[AI028](TRAINING_INFERENCE/sources/AI028-deepseek-math.md)、[AI017](MODELS/sources/AI017-deepseek-r1.md) |
| 训练显存和多卡通信怎样组织？ | [AI005](ALGORITHMS/sources/AI005-adam.md)、[AI025](TRAINING_INFERENCE/sources/AI025-zero.md)、[AI026](TRAINING_INFERENCE/sources/AI026-megatron-lm.md)、[AI039](CLOUD_ACCELERATORS/sources/AI039-nccl.md) |
| 量化、蒸馏与小模型怎样适应端侧？ | [AI012](ALGORITHMS/sources/AI012-gptq.md)、[AI011](ALGORITHMS/sources/AI011-awq.md)、[AI010](ALGORITHMS/sources/AI010-knowledge-distillation.md)、[AI043](EDGE_AI/sources/AI043-mobilellm.md)、[AI044](EDGE_AI/sources/AI044-mcunet.md) |
| 扩散模型与 Transformer 生成有什么不同？ | [AI006](ALGORITHMS/sources/AI006-ddpm.md)、[AI061](ALGORITHMS/sources/AI061-lilian-diffusion.md) |
| RAG 与 Agent 增加了哪些系统环节？ | [AI049](APPLICATIONS/sources/AI049-rag.md)、[AI050](APPLICATIONS/sources/AI050-react.md)、[AI051](APPLICATIONS/sources/AI051-toolformer.md)、[AI060](APPLICATIONS/sources/AI060-lilian-agents.md) |
| 视觉、语音、推荐与机器人有哪些新负载？ | [AI052](APPLICATIONS/sources/AI052-vit.md)、[AI053](APPLICATIONS/sources/AI053-clip.md)、[AI019](MODELS/sources/AI019-qwen25-vl.md)、[AI054](APPLICATIONS/sources/AI054-whisper.md)、[AI057](APPLICATIONS/sources/AI057-qwen3-tts.md)、[AI055](APPLICATIONS/sources/AI055-dlrm.md)、[AI056](APPLICATIONS/sources/AI056-rt2.md) |

## 博主文章的使用方法

本批纳入 Jay Alammar、Lilian Weng、Sebastian Raschka、Horace He，以及用户提供的 aneasystone 微信文章。优先采用作者原站，选择有清晰推导、结构图、代码或原始参考的文章，并与论文及实现交叉阅读。苏剑林 RoPE 文章保留为待补入口。

作者文章中的示意参数、历史模型和性能简化需保留其条件。原文观点、导读辨析与后续实测分别记录；对已取得的文章保存原始 HTML、正文阅读副本及可取得图示。

## 阅读记录与产出

每次精读把实际页码/章节、张量形状、公式假设、实现位置和未解决问题补入该来源的唯一主笔记。跨来源结论再写入具体专题报告；复现先固定模型检查点、依赖、硬件与输入条件。

[归档与阅读核查记录](source-reading-audit.md)记录本轮完成范围和剩余缺口。
