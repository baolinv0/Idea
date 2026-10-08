# 01_RESEARCH_STATE
Updated: 2026-10-08（Asia/Shanghai）
Stage: SCOUT → CONVERGE
Decision: PROCEED WITH CAUTION；先做文献证据收敛，必要时再做现象验证，不承诺模型方案。
Status: novelty assessment provisional；fresh-session同模型家族复核已完成并支持谨慎继续；尚无实验结果。
Origin: 当前工作区没有既有研究状态文件；本文件根据用户提供的Playbook快照与本轮检索新建。

## Problem Anchor
在常规Bayer RAW HDR/低照成像中，研究固定采集成本下“曝光分配×先验强度”与局部事实错误、可读性、感知质量的关系。希望得到指定传感器、场景分布与冻结模型下的经验采集需求；不将网络比较当作物理信息上限。

## Current Question
Under a fixed capture-time budget, how do exposure allocation and prior strength change local factual-error risk in Bayer RAW HDR reconstruction, and which acquisition schedules meet a prespecified risk and readability target?

## Evidence Gained
- [Hallucination Index（MICCAI2024）](https://pmc.ncbi.nlm.nih.gov/articles/PMC11956116/) 已量化SNR与生成幻觉指数关系。
- [One Photon, Many Worlds（2026-10-02）](https://arxiv.org/html/2610.02675v1) 已刻画SPAD观测预算与生成歧义/任务错误，宽泛预算问题不再可声称首次。
- [UltraFusion](https://arxiv.org/html/2501.11515v1) 是两次真实曝光结合生成先验；[UltraLED](https://arxiv.org/html/2510.07741v1) 是单RAW两阶段U-Net恢复。采集方式与先验应作为两个轴。
- [Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/) 与 [AdaptiveAE](https://arxiv.org/html/2508.13503v1) 已研究曝光选择；前者有严格等时间/照片数对照，后者含预算感知策略与栈长惩罚，不将其惩罚视作严格固定时间证明。
- [HalluGen](https://arxiv.org/html/2512.03345v1)、[LL-Bench](https://arxiv.org/html/2606.02535v1) 和 [K-RCPS](https://proceedings.mlr.press/v202/teneggi23a.html) 限制“尚无幻觉评价/风险校准框架”的表述。
- 上述论文人工检查了一手资料，未运行可选verify_papers.py（安装路径未找到）；自动核验状态为[UNVERIFIED]。

## Frontier Residual（候选，未证实）
本轮未找到完整覆盖常规Bayer RAW、固定总采集时间/读出次数、曝光分配与先验强度交互、预定义局部事实错误及校准风险采集要求的研究。
贡献必须来自可复现交互或由此改变的采集决策。仅换传感器、增加帧数曲线、重复“SNR↑幻觉↓”、提出新评价网格或优化曝光本身，均不足以建立新颖性。

## Current Bottleneck
尚未为配置排序变化和局部风险阈值找到可直接引用的对照证据。先区分论文已回答的一般机制、仅能推断的关系和需要新验证的结果；不预设必须采集，也不预设拐点存在。

## Minimal Probe（当前改为文献证据检查）
当前先从论文提取直接证据，不启动新采集、复现实验或网络设计。原A/B方案移为备用，具体N=1/4/8与四帧曝光配方不是已有论文已验证的结论。

### 已有证据可以支持的部分
1. A的一般趋势：SPAD中观测预算增加，生成歧义及任务误差减少。[One Photon, Many Worlds：Sec.5–9](https://arxiv.org/html/2610.02675v1)。模拟显微成像中较高输入SNR降低幻觉指数。[Hallucination Index：Sec.3–4、Fig.4](https://pmc.ncbi.nlm.nih.gov/articles/PMC11956116/)。
2. B的物理基础：相同总采集时间及照片数下，曝光分配可改变最坏区域SNR。[Noise-Optimal Capture：Fig.4–7/作者项目对照](https://people.csail.mit.edu/hasinoff/hdrnoise/)。
3. 真实参考可用于引导生成修补：[UltraFusion：Sec.3.2、Sec.4.3/Fig.10–11](https://arxiv.org/html/2501.11515v1)；该工作没有给出独立局部事实风险保证。
4. 生成条件和强度会影响保真—感知权衡：[BurstGP：Fig.1、Table6、Fig.12](https://arxiv.org/html/2604.23508v1)。其single-frame扩散分支已经收到全burst重建，不能拿来证明一张真实采集与多张真实采集的公平差异。
以上继续采用原文人工核对；可选自动核验脚本未运行，[UNVERIFIED]状态不变。

### 证据提取规则
对每项核心主张记录：原文图/表/章节、真实输入观测、是否固定总时间/增益/读出数、比较模型是否相同、评价的是SNR/失真/观感/事实错误中的哪一项、结论适用范围。已有消融可直接作为证据，无需为了确认一般现象重做实验。
传感器标定、独立采集重复、seed与采集噪声分开、场景级统计、错误率与覆盖率等是评价协议要求；它们约束未来实验，不是当前必须先完成的科学发现。
不同论文的benchmark数值只有在预算、输入、数据和评价协议可比时，才可比较；不能拼接成新的因果或风险阈值结论。

### 仍需找到直接证据的两项
- 常规Bayer RAW在相同采集成本下，生成先验是否改变满足局部事实风险/可读性目标的曝光配置排序或目标可达性。
- 在明确定义的传感器、模型、场景分布与局部错误事件下，最低预算和校准风险阈值是多少。
先检索能直接回答它们的实验对照；只有确认文献未回答且问题值得推进，才决定是否启用备用采集probe。尚未找到不等于证明没有。


## H1 / H0
H1：等预算下先验强度与曝光分配存在可复现的局部风险交互，并改变达到指定风险与可读性要求的采集选择。
H0：收益仅是已知SNR/饱和覆盖改善，没有可复现的额外交互。
小pilot未检出不能证明H0；需预设可检测效应与确认阶段样本设计。

## Unresolved Risks
SPAD预算工作高度接近；数据与模型限制可能使交互不能外推；事实错误指标可能混淆噪声/擦除；全抹平导致低错误假象；同模型家族审查非跨模型独立；论文自动核验与引用图覆盖不完整。

## Next Single Action
围绕剩余两项问题定向检查关键论文的消融、补充材料与引用谱系，记录是否有同传感器、同预算、同模型的局部事实风险对照。

## Exit Condition
完成主张—原文对照—适用条件—证据缺口的映射，确认问题已被回答或明确未覆盖的可测问题。只有仍存在值得推进的缺口时，才讨论备用实验；不直接进入新网络设计。
