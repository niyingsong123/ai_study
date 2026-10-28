# AI048：llama.cpp: local LLM inference (selected repository files)

主归属：[端侧模型与芯片架构](../README.md)。来源性质：固定提交的选定源码。

- 原始来源：[原文或固定版本仓库](https://github.com/ggml-org/llama.cpp/tree/1fb7ef3e3327f18f1e99d294115b8493d54e196a)
- 版本：1fb7ef3e3327f18f1e99d294115b8493d54e196a
- 归档日期：2026-10-02
- 发布日期：本次未可靠提取；归档日期不代表发布日期。

## 归档与阅读状态

已固定提交、保存并定位选定源文件；未编译、安装或运行模型。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [commit.json](../../original_file/code/AI048-llama-cpp/commit.json) | 固定提交元数据 |
| [README.md](../../original_file/code/AI048-llama-cpp/README.md) | 选定原始源码 |
| [llama-kv-cache.cpp](../../original_file/code/AI048-llama-cpp/src/llama-kv-cache.cpp) | 选定原始源码 |
| [llama-model.cpp](../../original_file/code/AI048-llama-cpp/src/llama-model.cpp) | 选定原始源码 |

## 入选理由与研究用途

为 CPU/GPU 本地推理、GGUF 和低比特模型运行建立实现入口，配合选定模型及 KV Cache 代码查执行路径。

## 建议阅读定位

README；supported backends；selected model and KV cache source files。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

GGUF 是模型文件组织格式，量化类型、算子支持和设备性能分别核实；未下载模型权重。

## 交叉阅读

- [AI011：AWQ: Activation-aware Weight Quantization for On-Device LLM Compression and Acceleration](../../ALGORITHMS/sources/AI011-awq.md)
- [AI013：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../ALGORITHMS/sources/AI013-gqa.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
