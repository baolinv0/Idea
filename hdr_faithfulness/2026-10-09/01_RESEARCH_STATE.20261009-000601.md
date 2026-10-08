# 01_RESEARCH_STATE
Updated: 2026-10-09（Asia/Shanghai）
Stage: SCOUT → CONVERGE
Decision: PROCEED WITH CAUTION；A/#12收窄为冻结流程采集决策损失，B/#1有条件备选，C/#4共同控制。
Status: 12候选、六视角独立首轮及三条交叉回复已整理；无pilot，未确认新颖性；idea-discovery正式门控BLOCKED。
Canonical report: [IDEA_REPORT.md](idea-stage/IDEA_REPORT.md)

## Problem Anchor
在常规Bayer RAW HDR/低照中，研究冻结恢复流程的现成操作是否改变等采集成本曝光配置的局部事实风险与可读性排序。长期研究“真实观测需要多少”；当前先确认是否有尚未被回答的采集决策问题。

## Current Question
Does changing an existing generative-restoration setting change which equal-cost exposure schedule meets a local factual-risk and readability target?
仅指测试配置集合、声明的传感器/场景/模型；单成本点不产生最低预算或普遍物理上限。

## Evidence Gained
- [Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/)已等时间/照片数优化物理SNR；[AdaptiveAE](https://arxiv.org/html/2508.13503v1)已预算感知选择曝光，不能把曝光优化本身当新意。
- [BIGPrior](https://arxiv.org/abs/2011.01406)已解耦先验与数据保真；宽泛“首次区分真实信息/先验”不可用。
- [One Photon](https://arxiv.org/html/2610.02675v1)已研究SPAD预算、生成歧义与任务；宽泛预算问题很近，reader路径的收益不等于物理信息下界。
- [BurstGP](https://arxiv.org/html/2604.23508v1)的single-frame生成分支仍看到全burst重建；不能当1张vs多张真实采集的对照。
- [UltraFusion](https://arxiv.org/html/2501.11515v1)同时有两次真实曝光和生成先验；[UltraLED](https://arxiv.org/html/2510.07741v1)是单RAW两阶段U-Net，不是diffusion。
- [HalluGen](https://arxiv.org/html/2512.03345v1)已区分一致但错误；[SceneFaith](https://arxiv.org/html/2609.34781v1)已fixed-target-patch/blur×context及跨模型共识错误。[CTVid](https://arxiv.org/html/2608.28784v1)已区分恢复/读出错误。
- [AdaSense](https://arxiv.org/html/2407.08256v1)/[GPARA](https://arxiv.org/html/2609.34172v1)已主动选择真实测量；泛泛不确定性补拍不可直接成题。
- 12候选经fresh-session gpt-6-astra/ultra只读审查，暂定12→1→4；同模型家族，不是跨家族验收。

## Frontier Residual（候选，未证实）
尚未找到同时覆盖等时间/读出数/增益、合法Bayer曝光配置、同冻结模型现成操作、局部事实错误与覆盖率，并直接证明采集选择改变的对照。
新意需来自可复现配置排序/达标集合变化及实际后果；仅新评价网格、交互显著、换传感器、一般先验偏差不足。
尚未找到不等于没有，也不证明现象存在。

## Current Bottleneck
缺同条件直接证据；模型/权重/数据接口适用性尚未全面核对。需要区分证据不足与流程没有利用已观测信息，不预设临界收益。

## Candidate Backups
#1：真实预算变化下，低跨seed分歧是否误导停止采集？必须同覆盖率校准，不能借用跨模型共识结论。
#4：raw适配预处理后，生成恢复的任务预算优势还剩多少？先审计原文reader路径，不预设不公平或优势消失。
其余候选与去留理由在完整报告；#5/#8是协议，#11暂离开静态主线。

## Current Minimal Probe
文献证据probe为当前活动；原A/B保留备用，未启动采集或推理。
已查主文：曝光分配改变物理质量、更多观测减少歧义、生成条件改变质量已有；尚缺主线配置选择证据。
提取每个消融的真实输入、时间/增益/读数、同模型条件、设置含义、SNR/饱和/配准、事实指标、覆盖率与重复单位。
不跨论文拼接因果结论，不拿少数展示图估总体风险。

## H1 / H0
H1：合法现成操作改变等成本测试配置的事实风险—覆盖率排序或达标集合，且可复现并影响采集选择。
H0：排序保持稳定，或变化由物理质量/评价/接口失配解释；先验未改变采集选择。
小样本未检出不证明H0。设置可能同时改变数据保真和先验，不称纯先验变量。

## Measurement Rules
正确可读/错误但清晰/擦除三态；条件错误率同时覆盖率及无条件错误率；无置信信号不叫自信错误。
seed与采集噪声分开；patch/seed非独立场景。高SNR参考须独立，不让生成结果定义真值。
单T两配置只比较配置，不定最低成本；未来若有必要才多T并校准。
现成模型非法输入/无设置开关属于可行性问题，不算科学否证。

## Next Single Action
补齐最近邻补充材料和引用中的直接证据矩阵，判断是否已存在同成本/同模型的局部事实配置选择结论。当前不设计新网络。

## Exit Condition
明确主张已被回答，或保留一个值得验证的可测残差，并确认合法现成路径/已有数据可行。之后才决定是否启用备用probe。

## Workflow Limits
无新实验；自动论文核验[UNVERIFIED]但关键一手来源人工核对。
run_state.py、idea_discovery_gate.py未找到；跨家族审查路由不可用，正式gate未执行且标BLOCKED。另存诊断状态，不冒称PASS。


## 2026-10-09：六个独立研究视角后的收敛更新

已按张磊、Michael S. Brown、薛天帆、李重仪、Jiawen Chen、Felix Heide的公开研究方向完成六个AI agent独立首轮；另有Felix/Brown/Jiawen三条实际交叉回复。不是研究者本人意见或参与；独立上下文均同模型家族，不能清除原正式gate。
[完整讨论报告](expert-panel/EXPERT_PANEL.md)

### Problem Anchor（最新收窄）
研究明确冻结恢复流程对采集选择的事实决策损失和适用边界。不能将给定流程可达性解释为传感器物理信息上限。

### Current Question（最新）
Within a declared camera and scene distribution, do legal operational settings of the same frozen restoration pipeline change which equal-cost exposure schedule meets a factual-risk and readability target, with reproducible decision loss?
A仍是优先文献核查对象；B停止可靠性是有条件备选；C处理/读出适配是共同解释基线。四位首选A、两位首选B只是潜力意见，不是新颖性证据。Brown/Felix将B暂置诊断位的异议保留。

### Evidence Gained（本轮新增）
- AdaptiveAE §4.1/Fig.5已明确融合模型影响EV选择，Table3测试不同融合后端；一般“恢复器改变曝光选择”不再是候选残差。原文不因此证明本题的局部事实风险反转。
- UltraFusion所查main路径输入ue/oe两张RGB；strength改控制注入，steps改采样；uncond=None时cfg_scale不走CFG分支。不能直接承担原RAW burst probe，不能将接口缺口当H0。
- 局部SNR高≠测量通道信息支配；同任务/损失/先验且已证明通道支配时，最优决策可忽略额外信息。冻结恢复器反选首先说明利用受限。
- 固定预算点的边际风险校准不自动保证首次一致即停的策略风险。正确模型且条件含完整停止历史的后验是不同对象，不笼统声称optional stopping破坏所有后验。
- B需真实使用依据的规则、完整预算序列、场景级重复、同覆盖率，以及曝光与多seed推理/等待成本分别报告。缺序列不能回溯停止风险。
- C不预设已有论文不公平；非生成不等于无学习。新增数据纠错需区别新增可辨识证据和reader输入适配。

### Frontier Residual（仍未证实）
一般曝光优化、恢复器依赖、稳定但错误、序贯选择、reader适配已成熟。A仅保留同冻结模型合法设置×等成本×局部事实/覆盖率×实际决策损失的直接证据缺口；B只有完整策略校准后仍有盲区并能由独立观测纠错时才可能升格。

### Next Single Action（最新）
建立“直接证据与现成接口矩阵”：AdaptiveAE/Noise-Optimal的目标与配置消融、UltraFusion输入/设置语义、One Photon预算—样本—事实—覆盖率—停止联合结果及数据/代码可用性。先确认有直接残差和合法现成路径，再决定是否启动备用Minimal Probe。

### Exit Condition / Limits（不变）
已有直接工作则降级；否则保留明确可测残差并证明现成路径/已有数据可检查。当前SCOUT→CONVERGE，不设计网络、不训练、不启动新采集。单预算两配置不定最低成本，无置信信号不称自信错误。无本项目pilot，未确认新颖性；idea-discovery正式gate仍BLOCKED。
