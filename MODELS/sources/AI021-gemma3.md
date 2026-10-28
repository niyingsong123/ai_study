# AI021：Gemma 3 Technical Report

主归属：[代表性大模型](../README.md)。来源性质：原始论文/技术报告。

- 原始来源：[原文或固定版本仓库](https://arxiv.org/abs/2503.19786)
- 版本：2503.19786v1
- 归档日期：2026-10-02
- 作者/团队：Gemma Team；Kamath, Aishwarya；Ferret, Johan；Pathak, Shreya；Vieillard, Nino；Merhej, Ramona；Perrin, Sarah；Matejovicova, Tatiana；Ramé, Alexandre；Rivière, Morgane；Rouillard, Louis；Mesnard, Thomas；Cideron, Geoffrey；Grill, Jean-bastien；Ramos, Sabela；Yvinec, Edouard；Casbon, Michelle；Pot, Etienne；Penchev, Ivo；Liu, Gaël；Visin, Francesco；Kenealy, Kathleen；Beyer, Lucas；Zhai, Xiaohai；Tsitsulin, Anton；Busa-Fekete, Robert；Feng, Alex；Sachdeva, Noveen；Coleman, Benjamin；Gao, Yi；Mustafa, Basil；Barr, Iain；Parisotto, Emilio；Tian, David；Eyal, Matan；Cherry, Colin；Peter, Jan-Thorsten；Sinopalnikov, Danila；Bhupatiraju, Surya；Agarwal, Rishabh；Kazemi, Mehran；Malkin, Dan；Kumar, Ravin；Vilar, David；Brusilovsky, Idan；Luo, Jiaming；Steiner, Andreas；Friesen, Abe；Sharma, Abhanshu；Sharma, Abheesht；Gilady, Adi Mayrav；Goedeckemeyer, Adrian；Saade, Alaa；Feng, Alex；Kolesnikov, Alexander；Bendebury, Alexei；Abdagic, Alvin；Vadi, Amit；György, András；Pinto, André Susano；Das, Anil；Bapna, Ankur；Miech, Antoine；Yang, Antoine；Paterson, Antonia；Shenoy, Ashish；Chakrabarti, Ayan；Piot, Bilal；Wu, Bo；Shahriari, Bobak；Petrini, Bryce；Chen, Charlie；Lan, Charline Le；Choquette-Choo, Christopher A.；Carey, CJ；Brick, Cormac；Deutsch, Daniel；Eisenbud, Danielle；Cattle, Dee；Cheng, Derek；Paparas, Dimitris；Sreepathihalli, Divyashree Shivakumar；Reid, Doug；Tran, Dustin；Zelle, Dustin；Noland, Eric；Huizenga, Erwin；Kharitonov, Eugene；Liu, Frederick；Amirkhanyan, Gagik；Cameron, Glenn；Hashemi, Hadi；Klimczak-Plucińska, Hanna；Singh, Harman；Mehta, Harsh；Lehri, Harshal Tushar；Hazimeh, Hussein；Ballantyne, Ian；Szpektor, Idan；Nardini, Ivan；Pouget-Abadie, Jean；Chan, Jetha；Stanton, Joe；Wieting, John；Lai, Jonathan；Orbay, Jordi；Fernandez, Joseph；Newlan, Josh；Ji, Ju-yeong；Singh, Jyotinder；Black, Kat；Yu, Kathy；Hui, Kevin；Vodrahalli, Kiran；Greff, Klaus；Qiu, Linhai；Valentine, Marcella；Coelho, Marina；Ritter, Marvin；Hoffman, Matt；Watson, Matthew；Chaturvedi, Mayank；Moynihan, Michael；Ma, Min；Babar, Nabila；Noy, Natasha；Byrd, Nathan；Roy, Nick；Momchev, Nikola；Chauhan, Nilay；Sachdeva, Noveen；Bunyan, Oskar；Botarda, Pankil；Caron, Paul；Rubenstein, Paul Kishan；Culliton, Phil；Schmid, Philipp；Sessa, Pier Giuseppe；Xu, Pingmei；Stanczyk, Piotr；Tafti, Pouya；Shivanna, Rakesh；Wu, Renjie；Pan, Renke；Rokni, Reza；Willoughby, Rob；Vallu, Rohith；Mullins, Ryan；Jerome, Sammy；Smoot, Sara；Girgin, Sertan；Iqbal, Shariq；Reddy, Shashir；Sheth, Shruti；Põder, Siim；Bhatnagar, Sijal；Panyam, Sindhu Raghuram；Eiger, Sivan；Zhang, Susan；Liu, Tianqi；Yacovone, Trevor；Liechty, Tyler；Kalra, Uday；Evci, Utku；Misra, Vedant；Roseberry, Vincent；Feinberg, Vlad；Kolesnikov, Vlad；Han, Woohyun；Kwon, Woosuk；Chen, Xi；Chow, Yinlam；Zhu, Yuvein；Wei, Zichuan；Egyed, Zoltan；Cotruta, Victor；Giang, Minh；Kirk, Phoebe；Rao, Anand；Black, Kat；Babar, Nabila；Lo, Jessica；Moreira, Erica；Martins, Luiz Gustavo；Sanseviero, Omar；Gonzalez, Lucas；Gleicher, Zach；Warkentin, Tris；Mirrokni, Vahab；Senter, Evan；Collins, Eli；Barral, Joelle；Ghahramani, Zoubin；Hadsell, Raia；Matias, Yossi；Sculley, D.；Petrov, Slav；Fiedel, Noah；Shazeer, Noam；Vinyals, Oriol；Dean, Jeff；Hassabis, Demis；Kavukcuoglu, Koray；Farabet, Clement；Buchatskaya, Elena；Alayrac, Jean-Baptiste；Anil, Rohan；Dmitry；Lepikhin；Borgeaud, Sebastian；Bachem, Olivier；Joulin, Armand；Andreev, Alek；Hardin, Cassidy；Dadashi, Robert；Hussenot, Léonard
- arXiv 首次提交日期：2025/03/25

## 归档与阅读状态

已核对标题及摘要/导言、完成文件可读性检查；推荐章节待专题精读。

**状态：已取得本地原文，已整理入选导读；专题精读与实测尚未完成。**

| 本地原始文件 | 文件说明 |
| --- | --- |
| [AI021-gemma3.metadata.html](../../original_file/papers/AI021-gemma3.metadata.html) | 论文元数据页 |
| [AI021-gemma3.pdf](../../original_file/papers/AI021-gemma3.pdf) | 25 页 PDF |

## 入选理由与研究用途

研究不同规模模型、视觉语言支持与局部/全局注意力设计，作为稠密结构和缓存取舍的对照。

## 建议阅读定位

Model Architecture；attention design；training and evaluation。

建议阅读定位是后续精读的起点，不表示这些章节均已完成逐段研究。

## 适用边界与核对事项

不同尺寸的多模态和结构支持须分别核对；局部注意力不等于任意长上下文均无代价。

## 交叉阅读

- [AI013：GQA: Training Generalized Multi-Query Transformer Models from Multi-Head Checkpoints](../../ALGORITHMS/sources/AI013-gqa.md)
- [AI019：Qwen2.5-VL Technical Report](AI019-qwen25-vl.md)

[分类资料索引](README.md) · [全项目资料索引](../../sources.md)
