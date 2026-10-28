# AI016：DeepSeek-V3 Technical Report

主归属：[代表性大模型](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2412.19437)
- 版本：2412.19437v2
- 归档日期：2026-10-02
- 作者/团队：DeepSeek-AI；Liu, Aixin；Feng, Bei；Xue, Bing；Wang, Bingxuan；Wu, Bochao；Lu, Chengda；Zhao, Chenggang；Deng, Chengqi；Zhang, Chenyu；Ruan, Chong；Dai, Damai；Guo, Daya；Yang, Dejian；Chen, Deli；Ji, Dongjie；Li, Erhang；Lin, Fangyun；Dai, Fucong；Luo, Fuli；Hao, Guangbo；Chen, Guanting；Li, Guowei；Zhang, H.；Bao, Han；Xu, Hanwei；Wang, Haocheng；Zhang, Haowei；Ding, Honghui；Xin, Huajian；Gao, Huazuo；Li, Hui；Qu, Hui；Cai, J. L.；Liang, Jian；Guo, Jianzhong；Ni, Jiaqi；Li, Jiashi；Wang, Jiawei；Chen, Jin；Chen, Jingchang；Yuan, Jingyang；Qiu, Junjie；Li, Junlong；Song, Junxiao；Dong, Kai；Hu, Kai；Gao, Kaige；Guan, Kang；Huang, Kexin；Yu, Kuai；Wang, Lean；Zhang, Lecong；Xu, Lei；Xia, Leyi；Zhao, Liang；Wang, Litong；Zhang, Liyue；Li, Meng；Wang, Miaojun；Zhang, Mingchuan；Zhang, Minghua；Tang, Minghui；Li, Mingming；Tian, Ning；Huang, Panpan；Wang, Peiyi；Zhang, Peng；Wang, Qiancheng；Zhu, Qihao；Chen, Qinyu；Du, Qiushi；Chen, R. J.；Jin, R. L.；Ge, Ruiqi；Zhang, Ruisong；Pan, Ruizhe；Wang, Runji；Xu, Runxin；Zhang, Ruoyu；Chen, Ruyi；Li, S. S.；Lu, Shanghao；Zhou, Shangyan；Chen, Shanhuang；Wu, Shaoqing；Ye, Shengfeng；Ye, Shengfeng；Ma, Shirong；Wang, Shiyu；Zhou, Shuang；Yu, Shuiping；Zhou, Shunfeng；Pan, Shuting；Wang, T.；Yun, Tao；Pei, Tian；Sun, Tianyu；Xiao, W. L.；Zeng, Wangding；Zhao, Wanjia；An, Wei；Liu, Wen；Liang, Wenfeng；Gao, Wenjun；Yu, Wenqin；Zhang, Wentao；Li, X. Q.；Jin, Xiangyue；Wang, Xianzu；Bi, Xiao；Liu, Xiaodong；Wang, Xiaohan；Shen, Xiaojin；Chen, Xiaokang；Zhang, Xiaokang；Chen, Xiaosha；Nie, Xiaotao；Sun, Xiaowen；Wang, Xiaoxiang；Cheng, Xin；Liu, Xin；Xie, Xin；Liu, Xingchao；Yu, Xingkai；Song, Xinnan；Shan, Xinxia；Zhou, Xinyi；Yang, Xinyu；Li, Xinyuan；Su, Xuecheng；Lin, Xuheng；Li, Y. K.；Wang, Y. Q.；Wei, Y. X.；Zhu, Y. X.；Zhang, Yang；Xu, Yanhong；Xu, Yanhong；Huang, Yanping；Li, Yao；Zhao, Yao；Sun, Yaofeng；Li, Yaohui；Wang, Yaohui；Yu, Yi；Zheng, Yi；Zhang, Yichao；Shi, Yifan；Xiong, Yiliang；He, Ying；Tang, Ying；Piao, Yishi；Wang, Yisong；Tan, Yixuan；Ma, Yiyang；Liu, Yiyuan；Guo, Yongqiang；Wu, Yu；Ou, Yuan；Zhu, Yuchen；Wang, Yuduan；Gong, Yue；Zou, Yuheng；He, Yujia；Zha, Yukun；Xiong, Yunfan；Ma, Yunxian；Yan, Yuting；Luo, Yuxiang；You, Yuxiang；Liu, Yuxuan；Zhou, Yuyang；Wu, Z. F.；Ren, Z. Z.；Ren, Zehui；Sha, Zhangli；Fu, Zhe；Xu, Zhean；Huang, Zhen；Zhang, Zhen；Xie, Zhenda；Zhang, Zhengyan；Hao, Zhewen；Gou, Zhibin；Ma, Zhicheng；Yan, Zhigang；Shao, Zhihong；Xu, Zhipeng；Wu, Zhiyu；Zhang, Zhongyu；Li, Zhuoshu；Gu, Zihui；Zhu, Zijia；Liu, Zijun；Li, Zilin；Xie, Ziwei；Song, Ziyang；Gao, Ziyi；Pan, Zizheng
- arXiv 首次提交日期：2024/12/27

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI016-deepseek-v3.metadata.html](../../original_file/papers/AI016-deepseek-v3.metadata.html) | 论文元数据页 |
| [AI016-deepseek-v3.pdf](../../original_file/papers/AI016-deepseek-v3.pdf) | 53 页 PDF |

## 入选理由与研究用途

串起 MLA、MoE、低精度训练、多 token 预测及分布式执行，适合研究模型结构如何改变内存和通信需求。

## 建议阅读定位

Architecture；Infrastructure；Pre-Training；Post-Training。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

总参数与每 token 激活参数分别记录；论文成本数字只在其统计范围内引用。

## 交叉阅读

- [AI008：Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity](../../ALGORITHMS/sources/AI008-switch-transformer.md)
- [AI022：Insights into DeepSeek-V3: Scaling Challenges and Reflections on Hardware for AI Architectures](AI022-deepseek-hardware.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
