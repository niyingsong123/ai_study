"""Curated acquisition catalog; source IDs start after the two existing WeChat links."""

SOURCES = []

def add(group, slug, title, locator, guide, reading, limits, related=(), kind='paper', extras=()):
    SOURCES.append(dict(source_id=f'AI{len(SOURCES)+3:03d}', group=group, slug=slug,
        title=title, locator=locator, kind=kind, guide=guide, recommended_reading=reading,
        limits=limits, related_slugs=list(related), extras=list(extras)))

add('ALGORITHMS','attention-is-all-you-need','Attention Is All You Need','1706.03762',
    'Transformer 的基础来源，适合建立注意力、前馈层、残差与位置编码的整体认识，并把模型结构映射成矩阵运算和张量流。',
    'Model Architecture；Scaled Dot-Product Attention；Multi-Head Attention；Positional Encoding。',
    '原论文主要是 encoder-decoder 翻译模型；现代 decoder-only 大模型的归一化、位置编码和缓存机制需另查实现。')
add('ALGORITHMS','resnet','Deep Residual Learning for Image Recognition','1512.03385',
    '研究残差连接为何改善深层网络训练，以及卷积网络中分辨率、通道数和计算量的关系；也是理解端侧视觉负载的基础。',
    'Residual Learning；Identity Mapping；Network Architectures。',
    '图像分类实验的网络与训练条件不能直接推广到语言模型或所有视觉任务。')
add('ALGORITHMS','adam','Adam: A Method for Stochastic Optimization','1412.6980',
    '解释训练中一阶与二阶矩估计、自适应步长及偏差修正，为分析优化器状态显存和后续训练系统提供基础。',
    'Algorithm 1；bias correction；experimental setup。',
    'Adam 与 AdamW 的权重衰减处理不同；现代训练配方及超参数需要结合目标实现。')
add('ALGORITHMS','ddpm','Denoising Diffusion Probabilistic Models','2006.11239',
    '理解前向加噪、反向去噪和训练目标的对应关系，建立生成式视觉模型的计算过程与多步采样成本认识。',
    'Background；Diffusion models and denoising autoencoders；Algorithms 1/2。',
    '该来源是基础 DDPM；潜空间扩散、DiT 和加速采样属于后续扩展。')
add('ALGORITHMS','mamba','Mamba: Linear-Time Sequence Modeling with Selective State Spaces','2312.00752',
    '从选择性状态空间模型理解 Transformer 之外的序列建模路线，关注状态更新、扫描实现与长序列资源代价。',
    'Selective State Space Models；Hardware-aware algorithm；architecture。',
    '线性序列复杂度不直接等于任何硬件上的端到端优势；混合架构需另查模型报告。')
add('ALGORITHMS','switch-transformer','Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity','2101.03961',
    '作为 MoE 基础来源，研究 token 路由、专家容量和负载均衡，并区分总参数量、激活参数量与执行成本。',
    'Switch Routing；capacity factor；load balancing；distributed implementation。',
    '单专家路由及实验设置有明确边界，不等同于所有现代 MoE 配方。',('deepseek-v3','qwen3'))
add('ALGORITHMS','lora','LoRA: Low-Rank Adaptation of Large Language Models','2106.09685',
    '研究低秩更新如何减少可训练参数和优化器状态，理解适配器训练、加载和权重合并的基本取舍。',
    'Low-rank-parametrized update matrices；Applying LoRA to Transformer。',
    '参数节省与速度提升不是同一指标；rank、作用层和训练任务均需注明。')
add('ALGORITHMS','knowledge-distillation','Distilling the Knowledge in a Neural Network','1503.02531',
    '理解教师模型、学生模型、soft targets 和温度，作为小模型构建、端侧压缩及推理模型蒸馏的基础。',
    'Distillation；temperature；specialist models。',
    '基础分类蒸馏与大模型序列生成、推理轨迹蒸馏的目标和数据组织有所不同。',('deepseek-r1','mobilellm'))
add('ALGORITHMS','awq','AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration','2306.00978',
    '研究激活感知的权重量化和缩放处理，连接低精度误差、模型容量、访存需求与端侧执行效率。',
    'Activation-aware Weight Quantization；hardware implementation；evaluation。',
    '论文量化算法、具体低比特格式和运行时 kernel 支持需分开核对。',('gptq','llama-cpp'))
add('ALGORITHMS','gptq','GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers','2210.17323',
    '研究训练后权重量化如何利用校准与二阶信息处理误差，并与 AWQ 的关注点和实施条件比较。',
    'Optimal Brain Quantization；GPTQ algorithm；quantization experiments。',
    '量化位数不足以描述格式和性能；校准数据、分组策略及设备实现都需记录。',('awq',))
add('ALGORITHMS','gqa','GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints','2305.13245',
    '理解查询头与键值头的分组关系，分析多头注意力、MQA、GQA 对 KV Cache 规模和模型质量的影响。',
    'Method；GQA variants；quality and speed experiments。',
    '缓存容量估算需使用模型实际 KV head 数、精度、层数与序列长度。',('qwen3','llama3'))
add('ALGORITHMS','roformer','RoFormer: Enhanced Transformer with Rotary Position Embedding','2104.09864',
    '研究旋转位置编码如何把位置信息融入注意力，连接位置表示、相对位置关系和长上下文扩展问题。',
    'Rotary Position Embedding；properties；experimental setup。',
    '原始 RoPE 不直接规定现代模型的外推或缩放策略；具体参数应查模型配置。')

add('MODELS','qwen3','Qwen3 Technical Report','2505.09388',
    '同时包含稠密与 MoE 模型，适合选取稠密模型作为推理基线，并研究思考模式、训练阶段和小模型知识迁移。',
    'Model Architecture；Pre-training；Post-training；model size tables。',
    '报告中的 Qwen3 是明确代际；它不自动代表截至归档日所有 Qwen 产品的最新能力。',('gqa','switch-transformer','lora'))
add('MODELS','deepseek-v3','DeepSeek-V3 Technical Report','2412.19437',
    '串起 MLA、MoE、低精度训练、多 token 预测及分布式执行，适合研究模型结构如何改变内存和通信需求。',
    'Architecture；Infrastructure；Pre-Training；Post-Training。',
    '总参数与每 token 激活参数分别记录；论文成本数字只在其统计范围内引用。',('switch-transformer','deepseek-hardware'))
add('MODELS','deepseek-r1','DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning','2501.12948',
    '研究强化学习、冷启动数据与蒸馏在推理模型构建中的作用，并区分模型骨干结构和后训练产生的能力。',
    'DeepSeek-R1-Zero；DeepSeek-R1；Distillation；limitations。',
    '推理能力与具体硬件映射是不同层次；生成长度和评测条件影响质量及推理成本。',('deepseek-math','knowledge-distillation'))
add('MODELS','llama3','The Llama 3 Herd of Models','2407.21783',
    '作为 decoder-only 稠密模型的对照，覆盖结构、预训练、后训练和扩展任务，为完整推理流程研究提供参照。',
    'Model Architecture；Pre-training；Post-training；inference。',
    '报告篇幅较长，初期只选读结构与相关章节；不能把一个尺寸的配置推广到全系列。',('gqa','roformer'))
add('MODELS','qwen25-vl','Qwen2.5-VL Technical Report','2502.13923',
    '连接视觉编码、语言骨干和动态分辨率输入，研究多模态模型的 token、编码成本与端到端执行。',
    'Model Architecture；dynamic resolution；training；evaluation。',
    '视觉输入尺寸、视频帧数和处理流程都会改变资源需求，不能只按文字 token 数比较。',('vit','clip'))
add('MODELS','qwen38-next','On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability','2608.30320',
    '作为近期架构研究补充，关注混合序列结构、稀疏专家及外部容量设计，并将质量、训练效率和稳定性放在一起观察。',
    'Architecture and ablations；efficiency；training stability。',
    '属于明确版本的近期研究来源；结构和配置须以下载正文核对，不视为所有模型的通用路线。',('mamba','deepseek-v3'))
add('MODELS','gemma3','Gemma 3 Technical Report','2503.19786',
    '研究不同规模模型、视觉语言支持与局部/全局注意力设计，作为稠密结构和缓存取舍的对照。',
    'Model Architecture；attention design；training and evaluation。',
    '不同尺寸的多模态和结构支持须分别核对；局部注意力不等于任意长上下文均无代价。',('gqa','qwen25-vl'))
add('MODELS','deepseek-hardware','Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures','2505.09343',
    '直接连接 MLA、MoE、FP8 与集群网络，适合从算法选择推导硬件和通信需求，形成云端研究的问题清单。',
    'Model architecture；FP8；network topology；hardware reflections。',
    '实现经验和硬件建议保留适用场景，不作为其他厂商芯片的已验证规格。',('deepseek-v3','nccl','cdna4'))

add('TRAINING_INFERENCE','flashattention','FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness','2205.14135',
    '研究分块、在线 softmax 和减少高带宽内存读写的机制，说明数学结果相同的算子可以有不同的数据搬运成本。',
    'IO complexity；FlashAttention algorithm；kernel evaluation。',
    'IO 分析与目标 GPU kernel 性能分别核实；不从理论复杂度直接推定全模型加速。',('attention-is-all-you-need',))
add('TRAINING_INFERENCE','pagedattention','Efficient Memory Management for Large Language Model Serving with PagedAttention','2309.06180',
    '解释 KV Cache 分页、映射、共享和内存碎片，连接请求调度、并发和推理服务吞吐。',
    'PagedAttention；KV cache management；serving and evaluation。',
    '论文时期 vLLM 与当前版本存在差异；页表类比不代表它与 CPU/GPU 地址翻译机制完全相同。',('vllm-architecture','gqa'))
add('TRAINING_INFERENCE','zero','ZeRO: Memory Optimizations Toward Training Trillion Parameter Models','1910.02054',
    '按优化器状态、梯度和参数理解训练内存，并研究不同分片阶段的存储节省和通信代价。',
    'Memory consumption；ZeRO stages；communication analysis。',
    '训练状态分片与推理 KV Cache 是不同问题；具体 offload 和实现能力需查对应版本。',('adam','megatron-lm'))
add('TRAINING_INFERENCE','megatron-lm','Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism','1909.08053',
    '从 Transformer 的矩阵切分和通信位置理解张量并行，为多卡训练及推理中的计算通信映射提供基础。',
    'Model Parallelism；Transformer layers；scaling evaluation。',
    '这是早期方法论文；现代 Megatron 的流水、序列及专家并行需补版本文档。',('zero','nccl'))
add('TRAINING_INFERENCE','dpo','Direct Preference Optimization: Your Language Model is Secretly a Reward Model','2305.18290',
    '研究偏好数据如何用于直接优化语言模型，比较奖励模型、策略优化和参考模型在后训练中的职责。',
    'Derivation；DPO algorithm；preference learning experiments。',
    '算法推导的目标和数据假设需保留；DPO 不等同于所有强化学习或推理能力训练。',('rlhf',))
add('TRAINING_INFERENCE','deepseek-math','DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models','2402.03300',
    '作为 GRPO 的方法来源，研究组内相对奖励、训练组织及数学推理任务，补充推理模型后训练的基础。',
    'Group Relative Policy Optimization；reinforcement learning；ablation。',
    '本文任务、奖励和模型设置与 R1 等后续工作不同；使用时分别注明。',('deepseek-r1','dpo'))
add('TRAINING_INFERENCE','speculative-decoding','Fast Inference from Transformers via Speculative Decoding','2211.17192',
    '研究草稿模型与目标模型验证如何并行产生候选 token，以及接受率、额外计算和延迟之间的关系。',
    'Speculative sampling；correctness；latency analysis。',
    '分布保持结论依赖特定采样/接受过程；不同推测实现及硬件速度另行核实。')
add('TRAINING_INFERENCE','sglang','SGLang: Efficient Execution of Structured Language Model Programs','2312.07104',
    '把结构化模型程序与运行时连接起来，研究前缀复用、执行调度及程序级效率，作为推理服务的另一条路线。',
    'Programming interface；RadixAttention；runtime and evaluation。',
    '论文与当前 SGLang 功能并非完全一致；实验模型、并发和命中条件需保留。',('pagedattention','react'))
add('TRAINING_INFERENCE','mlir','MLIR: A Compiler Infrastructure for the End of Moore\'s Law','2002.11054',
    '为模型到算子、图优化及设备代码的映射建立编译器基础，理解多层中间表示与不同抽象层的优化。',
    'Design principles；dialects；progressive lowering。',
    '基础设施论文不表示任何特定 NPU 的编译流程和算子支持已验证。',('executorch','onnx-qnn'))
add('TRAINING_INFERENCE','vllm-architecture','vLLM Architecture Overview (v0.10.2)','https://docs.vllm.ai/en/v0.10.2/design/arch_overview.html',
    '采用固定版本文档核对引擎、调度器、执行器与模型运行器的关系，把 PagedAttention 论文落实到软件系统位置。',
    'Architecture overview；LLM engine；scheduler；executor and model runner。',
    '固定 v0.10.2 作为可追溯基线；并不标为归档日最新版，具体功能以该版本为准。',('pagedattention','sglang'),kind='official')
add('TRAINING_INFERENCE','rlhf','Training language models to follow instructions with human feedback','2203.02155',
    '理解监督微调、偏好标注、奖励模型和策略优化的基本流程，为后训练方法比较建立共同语言。',
    'Methods；SFT；reward model；PPO；limitations。',
    '研究报告中的模型与标注设置具有历史条件，不据此推定当前商用模型内部训练细节。',('dpo','deepseek-r1'))
add('TRAINING_INFERENCE','tensorrt-llm','TensorRT-LLM Overview (v0.20.0)','https://nvidia.github.io/TensorRT-LLM/0.20.0/overview.html',
    '核对 NVIDIA 推理软件栈中的模型执行、运行接口和优化组件，作为跨框架比较的官方入口。',
    'Overview；execution workflow；supported features and examples。',
    '固定 v0.20.0 文档作为基线；依赖特定 GPU、精度和 kernel 的功能逐项核实。',('vllm-architecture',),kind='official')

add('CLOUD_ACCELERATORS','blackwell','NVIDIA Blackwell Architecture (official snapshot)','https://www.nvidia.com/en-us/data-center/technologies/blackwell-architecture/',
    '连接 Tensor Core、Transformer Engine、低精度计算、NVLink 与机架系统，作为 NVIDIA 云端架构的官方入口。',
    'Transformer Engine；NVLink/NVLink Switch；system organization；technical brief link。',
    '产品概述和厂商性能声明与微架构规格分别理解；不同 Blackwell/Ultra 产品配置不能混用。',('tensorrt-llm','deepseek-hardware'),kind='official')
add('CLOUD_ACCELERATORS','cdna4','AMD CDNA 4 Architecture White Paper','https://www.amd.com/content/dam/amd/en/documents/instinct-tech-docs/white-papers/amd-cdna-4-architecture-whitepaper.pdf',
    '研究计算单元、矩阵核心、数值格式、chiplet 和 HBM，结合模型算子分析 AMD 云端加速器的数据流。',
    'Architecture overview；compute units；matrix operations；memory subsystem。',
    'CDNA 4 与 MI350 的具体代际适用；不推广为所有 AMD GPU 规格。',('blackwell','deepseek-hardware'),kind='official_pdf')
add('CLOUD_ACCELERATORS','tpu-v4','TPU v4: An Optically Reconfigurable Supercomputer for Machine Learning with Hardware Support for Embeddings','2304.01433',
    '连接专用矩阵计算、SparseCore 与集群拓扑，研究硬件如何同时支持大模型和 embedding 负载。',
    'TPU v4 architecture；SparseCore；optical circuit switches；system evaluation。',
    'TPU v4 是有充分论文资料的架构基线，不作为归档日最新 TPU；性能比较保留工作负载和系统条件。',('tpu-first','dlrm'))
add('CLOUD_ACCELERATORS','tpu-first','In-Datacenter Performance Analysis of a Tensor Processing Unit','1704.04760',
    '研究专用矩阵加速器、片上存储与数据流组织，并理解实际推理延迟需求如何影响硬件设计。',
    'Architecture；matrix multiply unit；memory；performance analysis。',
    '属于早期 TPU 推理架构；代际差异必须与 TPU v4 等后续资料分开。',('tpu-v4',))
add('CLOUD_ACCELERATORS','nccl','NCCL User Guide: Collective Operations','https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/usage/collectives.html',
    '理解 AllReduce、AllGather、ReduceScatter 等集合通信的语义，用来定位训练及模型并行中的通信需求。',
    'AllReduce；Broadcast；ReduceScatter；AllGather。',
    '此页是 API/通信语义文档；环树算法、拓扑和带宽需查具体版本实现。',('megatron-lm','zero'),kind='official')
add('CLOUD_ACCELERATORS','mlperf-inference','MLPerf Inference Benchmark','1911.02549',
    '为云端和端侧比较建立任务质量、延迟约束、部署场景与可复现性的基础认识。',
    'Benchmark principles；scenarios；quality and latency constraints。',
    '历史论文不包含当前全部 benchmark 与规则；正式比较需再核对相应版本。',('mobilellm','blackwell'))

add('EDGE_AI','qualcomm-npu','Unlocking on-device generative AI with an NPU and heterogeneous computing','https://www.qualcomm.com/content/dam/qcomm-martech/dm-assets/documents/Unlocking-on-device-generative-AI-with-an-NPU-and-heterogeneous-computing.pdf',
    '解释 NPU、CPU、GPU 与存储子系统的协作，建立端侧生成式 AI 的性能、能效和持续功耗问题。',
    'NPU and heterogeneous computing；memory；software stack；platform examples。',
    '厂商白皮书侧重公开结构与价值说明，未公开的精确流水、存储容量和调度细节保留未知。',('onnx-qnn','mobilellm'),kind='official_pdf')
add('EDGE_AI','hexagon-2026','Qualcomm Hexagon NPU: mobile architecture for agentic AI (2026-09)','https://www.qualcomm.com/news/onq/2026/09/hexagon-npu-agentic-ai-architecture',
    '补充近期端侧 NPU 对 Transformer、混合专家、共享存储与多任务的公开说明，用于发现新一代架构研究问题。',
    'Element Accelerator；shared memory；MoE；precision and workloads。',
    '官方博客是公开概述，性能及百分比有厂商条件；尚不能据此补全未公开微架构。',('qualcomm-npu','switch-transformer'),kind='official')
add('EDGE_AI','mobilellm','MobileLLM: Optimizing Sub-billion Parameter Language Models for On-Device Applications','2402.14905',
    '研究小模型的深度、宽度、embedding 和共享设计，说明端侧模型结构本身也需要围绕资源约束选择。',
    'Architecture design；embedding sharing；layer sharing；evaluation。',
    '小模型任务效果与真实设备能效分别验证；模型大小不直接表示部署成功。',('knowledge-distillation','awq'))
add('EDGE_AI','mcunet','MCUNet: Tiny Deep Learning on IoT Devices','2007.10319',
    '把模型搜索与小型执行引擎结合，研究微控制器上 SRAM/Flash 约束及模型运行时共同设计。',
    'TinyNAS；TinyEngine；memory constraints；device experiments。',
    '微控制器视觉场景与手机大模型差异很大，用于扩展端侧类型和方法，不直接互推性能。',('resnet','mlir'))
add('EDGE_AI','onnx-qnn','ONNX Runtime QNN Execution Provider','https://onnxruntime.ai/docs/execution-providers/QNN-ExecutionProvider.html',
    '从官方执行后端文档理解模型如何落到 Qualcomm 平台，关注编译、量化、算子支持、后端选项和设备条件。',
    'Requirements；configuration；quantization；supported operators；examples。',
    '此页随项目更新，归档日快照需与目标版本及 QNN SDK 对应；未运行设备验证。',('qualcomm-npu','awq'),kind='official')
add('EDGE_AI','executorch','ExecuTorch documentation: Overview','https://docs.pytorch.org/executorch/stable/intro-how-it-works.html',
    '理解从 PyTorch 导出到边缘运行时与设备后端的流程，关注图转换、内存规划、算子和 delegate 的边界。',
    'Export；edge dialect；backend delegation；runtime。',
    'stable 地址是归档日快照；不同后端覆盖与性能需要固定版本和目标设备验证。',('mlir','onnx-qnn'),kind='official')
add('EDGE_AI','mlx','MLX: array framework for Apple silicon (selected repository files)','github:ml-explore/mlx:main:README.md',
    '作为 Apple silicon 统一内存和数组执行的软件入口，结合选定代码与文档研究 CPU/GPU 数据共享及运行方式。',
    'README；unified memory；lazy evaluation；selected source files。',
    'MLX 的 Apple silicon 执行不表示已研究或控制 Apple Neural Engine；代码文件未编译运行。',('llama-cpp',),kind='code',extras=('python/mlx/nn/layers/quantized.py',))
add('EDGE_AI','llama-cpp','llama.cpp: local LLM inference (selected repository files)','github:ggml-org/llama.cpp:master:README.md',
    '为 CPU/GPU 本地推理、GGUF 和低比特模型运行建立实现入口，配合选定模型及 KV Cache 代码查执行路径。',
    'README；supported backends；selected model and KV cache source files。',
    'GGUF 是模型文件组织格式，量化类型、算子支持和设备性能分别核实；未下载模型权重。',('awq','gqa'),kind='code',extras=('src/llama-model.cpp','src/llama-kv-cache.cpp'))

add('APPLICATIONS','rag','Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks','2005.11401',
    '研究检索器、外部知识与生成器的配合，区分检索、上下文处理和生成的成本与质量问题。',
    'RAG model；retrieval；RAG-Sequence/RAG-Token；evaluation。',
    '基础 RAG 论文与现代工程流水、重排序或 Agentic RAG 不完全相同。')
add('APPLICATIONS','react','ReAct: Synergizing Reasoning and Acting in Language Models','2210.03629',
    '理解模型如何交替推理、行动并接收观测，作为 Agent 与工具调用循环的基础。',
    'ReAct prompting；reasoning and acting；task evaluation。',
    '论文提示策略不代表任意 Agent 的可靠性；环境、工具和任务条件需要说明。',('rag','toolformer'))
add('APPLICATIONS','toolformer','Toolformer: Language Models Can Teach Themselves to Use Tools','2302.04761',
    '研究模型如何形成工具调用训练样本，并从语言建模损失角度选择工具使用机会。',
    'API call sampling；filtering；model finetuning；tools。',
    '训练式工具使用与仅在提示中定义工具接口不同；外部 API 成本和正确性需单独评估。',('react',))
add('APPLICATIONS','vit','An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale','2010.11929',
    '理解图像 patch 如何变成 Transformer token，连接视觉输入分辨率、序列长度与计算存储需求。',
    'Vision Transformer；patch embeddings；training and evaluation。',
    '图像分类 ViT 与多模态模型的视觉编码器存在具体实现差异。',('attention-is-all-you-need','qwen25-vl'))
add('APPLICATIONS','clip','Learning Transferable Visual Models From Natural Language Supervision','2103.00020',
    '研究图文对比学习和双编码器，理解视觉语言对齐、embedding 与零样本任务的基本机制。',
    'Contrastive pretraining；zero-shot classification；limitations。',
    'CLIP 本身不是自回归多模态生成模型，相关能力边界需要保留。',('vit','qwen25-vl'))
add('APPLICATIONS','whisper','Robust Speech Recognition via Large-Scale Weak Supervision','2212.04356',
    '研究语音输入的表示、序列到序列建模和大规模弱监督，扩展 AI 负载到语音识别。',
    'Approach；model and training；evaluation；limitations。',
    '语音识别和语音生成是不同任务；数据、语言及任务指标分别记录。',('qwen3-tts',))
add('APPLICATIONS','dlrm','Deep Learning Recommendation Model for Personalization and Recommendation Systems','1906.00091',
    '把 embedding lookup、稀疏特征与稠密 MLP 联系起来，理解推荐模型与大语言模型不同的存储访问模式。',
    'Model architecture；embedding；feature interaction；parallelism。',
    '基础 DLRM 与现代推荐模型并非全部相同；工作负载和 embedding 表规模需明确。',('tpu-v4',))
add('APPLICATIONS','rt2','RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control','2307.15818',
    '研究视觉语言模型如何将动作表示为输出，作为具身智能和模型到控制任务的扩展入口。',
    'Vision-language-action；action tokenization；co-finetuning；evaluation。',
    '论文机器人体、数据和环境条件不能直接推定其他设备的控制能力。',('qwen25-vl','react'))
add('APPLICATIONS','qwen3-tts','Qwen3-TTS Technical Report','2601.15621',
    '补充较近期的语音生成模型、语音 tokenizer 和流式合成结构，研究首包延迟与连续输出的约束。',
    'Model architecture；speech tokenizers；streaming synthesis；evaluation。',
    '语音质量、克隆条件和延迟依赖任务及实现，不能仅使用单个最佳数字比较。',('whisper',))

add('ALGORITHMS','illustrated-transformer','The Illustrated Transformer — Jay Alammar','https://jalammar.github.io/illustrated-transformer/',
    '以结构图、矩阵图和逐步解释建立 Transformer 直觉，适合在阅读原论文前后查清 Q/K/V 和多头计算。',
    'Self-attention；multi-headed attention；positional encoding；encoder/decoder。',
    '属于技术教学文章，图中简化与现代 decoder-only 模型的具体配置需回原论文及实现核对。',('attention-is-all-you-need',),kind='blog')
add('MODELS','illustrated-gpt2','The Illustrated GPT-2 — Jay Alammar','https://jalammar.github.io/illustrated-gpt2/',
    '用图示解释 decoder-only、自回归生成及输出采样，帮助从原始 encoder-decoder Transformer 过渡到语言模型。',
    'GPT-2 structure；masked attention；token generation；sampling。',
    'GPT-2 的历史结构和数值不是现代模型通用配置，学习时与 Qwen/Llama 等基线交叉核对。',('qwen3','llama3'),kind='blog')
add('APPLICATIONS','lilian-agents','LLM Powered Autonomous Agents — Lilian Weng','https://lilianweng.github.io/posts/2023-06-23-agent/',
    '按规划、记忆和工具使用组织 Agent 的知识地图，带有论文参考及案例，适合选择深入研究的问题。',
    'Agent system overview；planning；memory；tool use；challenges。',
    '属于 2023 年的综合解读，案例和工程生态有时效性；机制与可靠性结论回查对应原始研究。',('react','rag','toolformer'),kind='blog')
add('ALGORITHMS','lilian-diffusion','What are Diffusion Models? — Lilian Weng','https://lilianweng.github.io/posts/2021-07-11-diffusion-models/',
    '通过公式和不同方法之间的关系解释扩散模型，适合补充 DDPM 推导以及采样加速的学习路线。',
    'Denoising diffusion；parameterization；sampling；references。',
    '博客可能持续更新，采用归档日版本；精确推导和实验结论回原始论文核对。',('ddpm',),kind='blog')
add('MODELS','raschka-comparison','The Big LLM Architecture Comparison — Sebastian Raschka','https://magazine.sebastianraschka.com/p/the-big-llm-architecture-comparison',
    '把多种开放模型的注意力、专家、归一化和结构图放在共同视角下比较，适合寻找架构差异及后续阅读入口。',
    'DeepSeek；Llama；Qwen；architecture figures；source and implementation links。',
    '以实际取得的公开正文为范围；模型事实回查官方报告和配置，最新内容及未获取部分不计已读。',('qwen3','deepseek-v3','llama3'),kind='blog')
add('TRAINING_INFERENCE','go-brrr','Making Deep Learning Go Brrrr From First Principles — Horace He','https://horace.io/brrr_intro.html',
    '用计算、内存带宽和执行开销理解深度学习性能，适合作为算子分析、融合和硬件映射的直觉入口。',
    'Compute；memory bandwidth；overhead；operation fusion and batching。',
    '解释性性能模型有简化假设；目标硬件上的瓶颈需使用具体 shape 和测量验证。',('flashattention','blackwell'),kind='blog')
add('ALGORITHMS','su-rope','Transformer升级之路：2、博采众长的旋转式位置编码 — 苏剑林','https://kexue.fm/archives/8265',
    '中文作者文章解释旋转式位置编码的设计与推导，可与 RoFormer 原论文配合学习位置编码和相对位置关系。',
    '旋转矩阵；相对位置；性质与实现；原论文链接。',
    '保留作者博客的版本和推导范围；长上下文改进、精度和模型配置仍需另外核实。',('roformer',),kind='blog')

add('MODELS','qwen3-implementation','Transformers Qwen3 implementation (v4.55.4 selected files)','github:huggingface/transformers:v4.55.4:src/transformers/models/qwen3/modeling_qwen3.py',
    '为首个推理专题保存固定版本的 Qwen3 注意力、前馈层、decoder 与配置代码，可与微信缓存示例及模型报告交叉核对。',
    'Qwen3Attention；Qwen3MLP；Qwen3DecoderLayer；Qwen3Config；cache update。',
    '仅保存并定位选定源文件，未安装该版本或运行模型；缓存 API 及具体模型参数须对应版本。',('qwen3','gqa'),kind='code',extras=('src/transformers/models/qwen3/configuration_qwen3.py',))
