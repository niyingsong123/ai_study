# AI047：MLX: array framework for Apple silicon (selected repository files)

主归属：[端侧模型与芯片架构](../README.md)。来源性质：固定提交的选定源码。

- 原始来源：[原文或固定版本仓库](https://github.com/ml-explore/mlx/tree/25532871329fe4cafdada9fa0941a1cdbfb3a9f2)
- 版本：25532871329fe4cafdada9fa0941a1cdbfb3a9f2
- 归档日期：2026-10-02
- 发布日期：本次未可靠提取；归档日期不代表发布日期。

## 归档与阅读状态

已固定提交、保存并定位选定源文件；未编译、安装或运行模型。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [commit.json](../../original_file/code/AI047-mlx/commit.json) | 固定提交元数据 |
| [quantized.py](../../original_file/code/AI047-mlx/python/mlx/nn/layers/quantized.py) | 选定原始源码 |
| [README.md](../../original_file/code/AI047-mlx/README.md) | 选定原始源码 |

## 入选理由与研究用途

作为 Apple silicon 统一内存和数组执行的软件入口，结合选定代码与文档研究 CPU/GPU 数据共享及运行方式。

## 建议阅读定位

README；unified memory；lazy evaluation；selected source files。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

MLX 的 Apple silicon 执行不表示已研究或控制 Apple Neural Engine；代码文件未编译运行。

## 交叉阅读

- [AI048：llama.cpp: local LLM inference (selected repository files)](AI048-llama-cpp.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
