# 独立研究视角评议：共同材料
Date: 2026-10-08
身份说明：按指定研究者的公开论文/研究方向模拟技术视角。所有结论都是AI代理分析，不是本人意见、参与或背书。
阶段：SCOUT→CONVERGE；文献证据优先；不设计新网络，不训练，不启动采集/推理。全部候选没有pilot结果，尚未确认新颖性。
此前已提出12个候选，本次只讨论最后三个。为避免从众，材料不提供既有排名和其他agent判断。

## Idea A（原候选12）：先验操作是否改变等成本曝光选择？
问题：固定总曝光时间、读出次数和增益时，物理SNR/饱和覆盖更好的曝光配置，是否仍最容易达到局部事实风险与可读性目标？现成冻结恢复器的操作设置变化是否会改变应该选的配置？
H1：同一模型合法现成操作改变测试配置的风险—覆盖率排序/达标集合，差异可重复且影响采集选择。
H0：排序稳定；或变化由已知物理质量、处理/评价/非法接口解释；先验只改变观感，无决策变化。
创新负担：估计器影响最优实验设计、曝光优化、先验/数据保真权衡都是已知；必须找到具体新规律或解释决策损失，interaction显著不够。
最近邻：
[Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/)已等时间/照片数优化噪声；
[AdaptiveAE](https://arxiv.org/html/2508.13503v1)预算感知快门/ISO/栈长；
[BIGPrior](https://arxiv.org/abs/2011.01406)先验和数据保真解耦；
[BurstGP](https://arxiv.org/html/2604.23508v1)生成条件和强度；
[One Photon](https://arxiv.org/html/2610.02675v1)SPAD预算和任务；
[LuckyHDR](https://arxiv.org/html/2604.19976v1)RAW多曝光观测像素融合。
当前缺口：本轮尚未找到上述要素同处一个受控事实对照的直接证据。未找到≠不存在，也不证明H1。

## Idea B（原候选1）：一致性是否误导停止采集？
问题：增加真实观测时，跨seed局部结果已经一致，事实风险是否仍未降到目标，而简单一致性停止规则提前停拍？
H1：相同接受覆盖率下，一致性风险校准/停止决定存在可重复盲区；额外真实证据仍能纠错。
H0：在声明分布中分歧与错误同步改善，不存在有意义的停止失效；或已有工作已回答。
创新负担：低方差也可能带偏、稳定≠真实本身已知，不能只挑失败图。需具体预算进程、风险校准和停止后果。
近邻：
[One Photon](https://arxiv.org/html/2610.02675v1)已随SPAD预算考察生成样本和任务；
[HalluGen](https://arxiv.org/html/2512.03345v1)Sec3.1区分测量一致但错误；
[SceneFaith](https://arxiv.org/html/2609.34781v1)Appendix I跨VLM共识保留共享错误并降低覆盖率；
[iRAG](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_Reference-based_Super-Resolution_via_Image-based_Retrieval-Augmented_Generation_Diffusion_ICCV_2025_paper.html)使用轨迹方差相关过滤；
[K-RCPS](https://proceedings.mlr.press/v202/teneggi23a.html)风险控制；
[measurement variation / distribution-shift UQ](https://arxiv.org/html/2510.10947v1)。
跨seed、轨迹方差、跨曝光、跨模型共识都是不同信号，不能互借结论。没有置信输出不得叫“自信错误”。
当前缺口：未取得常规RAW真实采集预算×跨seed一致性×事实风险×覆盖率的直接停止对照。

## Idea C（原候选4）：少拍的任务收益有多少来自读出适配？
问题：生成恢复相对raw输入的下游预算优势，加入公平的非生成预处理/噪声适配读出后还剩多少？
H1：公平适配后主要优势缩小，改变预算解释/选择；H0：优势主要保持，或公平基线已有。
原文触发点：[One Photon](https://arxiv.org/html/2610.02675v1)Sec7.2/Fig13用同一现成QR decoder比较raw与生成恢复；原文报告不同稳定解码预算。这是有效端到端收益，不预设论文比较不公平，不预设生成没有真实任务价值。
创新负担：domain adaptation/任务导向恢复成熟，补强baseline不自动成独立论文。缺预处理描述仅支持不能判定。
需拆解恢复、输入适配、任务先验的贡献；错误decode和拒识分开，不用reader输出当事实真值。
最近邻还有[Bridging the Gap Between Computational Photography and Visual Recognition](https://arxiv.org/abs/1901.09482)、[TeReDiff](https://openreview.net/pdf?id=jt2c2H6auR)、[ClearText-Video](https://arxiv.org/html/2608.28784v1)等恢复/任务评价工作。

## 用户Minimal Probe（只备用，不是当前活动）
静态标定RAW，亮暗随机已知事实加自然物体，独立高SNR非生成参考。
A: N=1/4/8，固定每帧t，总预算增长，现象检查。
B: N=4,T=4t，固定增益，[t,t,t,t] vs [t/4,t/4,t/2,3t]；等总时间/读出数但实际有效证据不同。
冻结非生成基线和现成生成恢复操作；不训练。设置未必是纯先验强度，记录数据保真/采样路径等实际意义。
同一场景独立采集重复；生成seed与采集噪声分开；多patch/seed不是独立场景。
预设局部SNR、饱和和传统融合解释基线；评价配置排序/目标可达性，非只p值。
正确可读、错误但清晰、擦除/不可判定；条件错误率须同时覆盖率。
单T两配置只比较配置，不能得最低采集成本。无模型合法输入/开关是可行性问题，不是H0证据。

## 共同评议任务
对A/B/C分别：
1. 最强支持与最致命反对；相近工作和是否只是成熟概念改名；
2. PROCEED WITH CAUTION / MERGE-AS-DIAGNOSTIC / ABANDON-CURRENT-FRAMING，给明确理由；
3. 一项最便宜的文献证据检查或已有数据分析；什么观察足以改变判断，什么证据不够；
4. 如何成为独立研究贡献；保持问题，不加网络组件。
然后给你自己的暂定排序（无实验排名），提一个其他视角agent最值得回答的技术质疑。
请用中文，约900–1500汉字；资料引用只用确实访问的一手来源或明确标注沿用共同材料；不能编造本人观点或引用。
