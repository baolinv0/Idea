# Idea Discovery：有限观测HDR的候选问题
Date: 2026-10-08（Asia/Shanghai）
Stage: SCOUT → CONVERGE
Scope: 静态Bayer RAW HDR/低照；真实观测、先验与局部事实
Candidate discovery: 12项；暂定优先3项；新实验0项
Formal workflow status: **BLOCKED**（证据门控工具缺失，缺跨模型家族验收）；实质产出为候选池、文献证据和问题级提案。

## 当前判断

主线保留 **#12：生成恢复设置会不会改变等成本曝光配置的选择？** 科学备选是 **#1：输出稳定能否支持停止采集？** 便宜的证据入口是 **#4：任务省光子收益有多少来自识别器输入适配？**
其余候选完整保留；#5/#8不宜独立成题，#11暂不作为静态主线。这里的排序基于问题贴合度、可证伪性、近邻威胁和获取证据的成本，没有实验信号排名或新颖性确认。

你提出“这些现象可以从已有论文结论获得”是当前收敛的重要约束。更多观测减小歧义、曝光分配改变噪声、生成强度影响结果已有直接证据，不需要为了再次证明它们立即采集。剩余候选必须回答这些机制是否造成新的采集选择或停止失效。

## Ranked Ideas
<a id="ranked-ideas"></a>

| 文献核查优先级 | 候选 | 成题所需的发现 | 当前状态 |
|---|---|---|---|
| 1 | #12 先验操作与等成本曝光选择 | 在事实风险和可读性目标下，改变现成设置会稳定改变配置排序/达标集合 | 主线候选；尚无直接证据 |
| 2 | #1 稳定与正确的预算进程 | 低生成分歧导致错误停止，而增加特定真实观测仍能纠错 | 独立备选；一致≠真本身已知 |
| 3 | #4 任务预算与读出适配 | 公平非生成读出改变对所需预算的解释或选择 | 低成本入口；未必足以独立成论文 |
| 4–9，不作精细次序 | #6独立测量核验、#7采集与计算、#9阶段覆盖、#2语境预算、#3合成一致性、#10非单调系统风险 | 各自需要明确的决策后果，详见完整池与审查 | 保留但有较强先例/可行性风险 |
| 当前不作独立主线 | #5擦除权衡、#8多事实联合风险、#11时间拼接 | 现有表述偏经典统计/去鬼影；应先作协议或未来备选 | 降级，记录未删除 |

### 优先1：生成先验会不会改变“应该怎样拍”？

**问题：** 固定总曝光时间、读出次数和增益，物理SNR/饱和覆盖更好的曝光配置，是否仍最容易满足局部事实风险和可读性要求？改变现成生成恢复操作后，应该选的配置会不会改变？
**H1：** 同一冻结模型的合法操作改变配置排序或达标集合，差异可复现且足以改变采集选择。
**H0：** 排序由非生成基线和已知物理质量解释；先验只改变观感或一致平移质量，没有决策变化。
**创新负担：** 更换估计器改变最优实验设计并不新。必须有事实目标下的新规律和实际选择后果，不只interaction显著。最近邻是Noise-Optimal Capture、AdaptiveAE、BIGPrior和BurstGP，见下方谱系。
**当前动作：** 查同传感器、同预算、同模型的现有消融是否直接回答这一点。原四帧A/B留作备用；单T两配置不能确定最低预算。

### 优先2：什么时候“稳定了”仍不能停止采集？

**问题：** 随真实观测增加，跨seed分歧低到足以触发停止时，局部事实错误是否仍有一个未下降的区间？
**H1：** 在固定接受覆盖率下，生成一致性的风险校准或停止判断失效；补充真实证据仍可纠错。
**H0：** 在声明分布内，一致性与错误同步改善，没有足以改变停止选择的脱钩。
**创新负担：** 一致但错误已有先例。候选针对RAW真实预算进程和停止后果；SceneFaith的跨VLM共识不能当成生成器跨seed结论。[SceneFaith Appendix I](https://arxiv.org/html/2609.34781v1)
**当前动作：** 核对One Photon等是否同时有预算、分歧、事实错误与覆盖率的联合数据；只有缺这一证据且值得研究，才考虑现成输出重分析。

### 优先3：“少拍很多”是在恢复事实，还是改善识别器输入？

**问题：** 生成恢复相对“raw直接送现成reader”的任务预算优势，加入合适的非生成预处理后还剩多少？
**H1：** 公平适配后优势显著缩小，改变原有预算解释；**H0：** 主要优势仍保持。
**创新负担：** 输入适配已成熟，补baseline未必成题。One Photon §7.2使用同一个现成QR decoder，是有效端到端对照；当前未拆分的归因不能直接否定其结果。[One Photon 原文](https://arxiv.org/html/2610.02675v1)
**当前动作：** 只读检查raw缩放/映射/threshold/去噪和解码设置、错误解码与拒识。信息未公开只能写“不能判定”，不能预设生成优势会消失。


## Literature Landscape
<a id="literature-landscape"></a>

检索截至2026-10-08；用一手论文/官方会议页核对方法输入、消融和指标。关键词覆盖 observation/photon budget、faithful restoration、hallucination、RAW burst、exposure allocation、consistency、active acquisition、context bias。未找到本地论文库。下面是机制谱系，不是跨论文分数排名；不同传感器/任务/模型的数值不能拼成因果曲线。

| 谱系及一手来源 | 真实输入与现有证据 | 本次选题受到的约束 |
|---|---|---|
| [Noise-Optimal Capture，CVPR2010](https://people.csail.mit.edu/hasinoff/hdrnoise/)；[HDR+，2016](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/) | 前者在相同总时间和照片数下优化噪声；后者融合同曝光短RAW burst | 曝光优化、更多真实光子与降噪不是空白；HDR+不能误称多曝光bracketing |
| [RawHDR，ICCV2023](https://arxiv.org/html/2309.02020v1)；[UltraLED，NeurIPS2025](https://arxiv.org/html/2510.07741v1) | 单RAW监督恢复；UltraLED是两阶段U-Net，其多曝光参考是训练/评价目标 | UltraLED不应列作diffusion；非生成网络也有先验，不能由架构标签先判定事实错误 |
| [UltraFusion，CVPR2025](https://arxiv.org/html/2501.11515v1) | 两张真实不同曝光RGB+扩散引导修补，直接输出LDR融合结果；Sec4.3/Fig10–11对照guidance形式 | “真实采集”和“生成先验”不是互斥路线；现有消融不是等成本局部事实风险对照 |
| [BurstGP，2026预印本](https://arxiv.org/html/2604.23508v1) | RAW burst重建+视频生成先验；Table6改变生成分支条件，single-frame分支仍有全burst重建 | 不能把它当一张真实观测vs多张的公平证据；已研究强度/条件及保真—感知权衡 |
| [Single-Shot HDR，2026预印本](https://arxiv.org/html/2605.11628v1)；[Bracket Diffusion，Eurographics2025/v2](https://arxiv.org/html/2405.14304v2)；[WACV2026曝光一致扩散](https://arxiv.org/abs/2602.19706) | 单次观测可生成合成曝光，或显式约束曝光之间一致 | 合成曝光有视觉和推理用途；不能当独立物理证据，也不能声称作者保证全部事实正确 |
| [AdaptiveAE，ICCV2025](https://arxiv.org/html/2508.13503v1)；[LuckyHDR，2026预印本](https://arxiv.org/html/2604.19976v1) | 前者预算感知选择快门/ISO/栈长；后者用对齐后观测像素的凸组合完成RAW多曝光融合 | 泛泛学习曝光选择已很近；观测驱动设计仍不等于经校准的局部事实风险承诺 |
| [BIGPrior，TIP2022](https://arxiv.org/abs/2011.01406) | 显式解耦网络先验与数据保真，并提供像素级先验依赖量 | 不能声称首次区分“观测贡献”和“先验贡献” |
| [Hallucination Index，MICCAI2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11956116/) | 控制显微成像SNR，研究恢复与参考分布差异；更好MSE不一定更少幻觉 | “SNR—幻觉关系”已有；其指数不是本项目局部事实错误概率 |
| [One Photon, Many Worlds，2026-10-02预印本](https://arxiv.org/html/2610.02675v1) | SPAD观测预算、生成歧义与边缘/OCR/QR/人脸几何任务；Sec7.2/Fig13用同一个现成QR解码器比較raw与生成结果 | 宽泛“拍多少才能可信”高度重合；结论依赖训练分布/任务。raw直送reader的预算不是物理最优下界 |
| [HalluGen，CVPR2026](https://arxiv.org/html/2512.03345v1)；[LL-Bench，2026预印本](https://arxiv.org/html/2606.02535v1) | 前者区分测量一致但错误的幻觉、提供局部评价；后者包含HDR/低照人工幻觉评价 | 泛幻觉benchmark或“一致≠真”的主张不足 |
| [TeReDiff，ICLR2026](https://openreview.net/pdf?id=jt2c2H6auR)；[SceneFaith，2026-09-28预印本](https://arxiv.org/html/2609.34781v1) | 前者文本保真恢复；后者有fixed-target-patch、blur×context对照，Appendix I报告跨VLM共识中的共享错误和覆盖率 | 语境干预及共识错误本身已被研究；跨模型共识、生成跨seed分歧、轨迹方差是不同信号 |
| [ClearText-Video，2026预印本](https://arxiv.org/html/2608.28784v1) | HQ/DQ/RQ对照，区分恢复侧与读出侧错误；Sec6说明感知增强不保证文字和下游收益 | 不能把恢复→理解误差归因本身当首次；曝光/传感器噪声不在其当前退化范围 |
| [AdaSense，ECCV2024](https://arxiv.org/html/2407.08256v1)；[GPARA，2026-09预印本](https://arxiv.org/html/2609.34172v1) | 用后验/风险选择未来真实线性测量，后者含等成本点测量 | 泛泛“用不确定性决定补拍”已有；RAW互补曝光需有新的可测决策后果 |
| [K-RCPS，ICML2023](https://proceedings.mlr.press/v202/teneggi23a.html)；[图像质量conformal bounds，2025](https://arxiv.org/html/2505.09528v1) | 像素风险/区间或PSNR等质量界；[分布漂移UQ，2025](https://arxiv.org/html/2510.10947v1)还用测量变化估计不确定性 | 必须明确保证单位和适用分布；像素区间或整体质量不是每个局部事实正确的保证 |
| [ResFlow-Tuner，2026预印本](https://arxiv.org/abs/2603.22027)；[LEADer，2026](https://arxiv.org/abs/2608.06981) | 推理时计算扩展、主动计算采样 | “多算一点”已有；LEADer的active sampling不等于新增物理读出 |

文献身份和本文关键输入结构已人工核对；自动核验工具verify_papers.py未找到，保留 **[UNVERIFIED：自动核验]**。该标记不表示已查的一手论文不存在。本文也不将预印本的新颖性主张视作已通过同行验收。

## Novelty Verification
<a id="novelty-verification"></a>

### 本轮文献证据probe已经得到的结果

| 候选所需证据 | 已找到的直接证据 | 仍缺什么 |
|---|---|---|
| 等成本曝光分配会改变物理质量 | Noise-Optimal Capture项目对照，等时间/照片数，噪声目标 | 同模型现成先验设置下，曝光配置的局部事实风险/可读性排序 |
| 多观测减小生成歧义 | One Photon Sec5–9；不同属性在不同预算改善 | 常规Bayer RAW等成本曝光；独立采集噪声、可达风险与覆盖率 |
| 生成条件/强度改变恢复结果 | BurstGP Table4/6、Fig1；UltraFusion Fig10–11 | 直接把先验操作变化归因于曝光配置选择的受控对照 |
| 一致结果仍可错误 | HalluGen Sec3.1；SceneFaith Appendix I/Table18 | RAW恢复中跨seed一致性是否误导停止采集，及其后果大小 |
| 少量观测改善现成识别器任务 | One Photon Sec7.2/Fig13 | 适配原始观测的非生成预处理/读出后，相同错误与拒识要求的预算优势 |

这些论文可以承担原Minimal Probe A/B的**一般机制依据**。它们不能共同拼接出新因果结论，也没有直接验证用户那组四帧配方。尚未找到所需受控对照，只说明当前证据缺口；不证明现象存在，更不证明全球文献空白。

### 需要降级的宽泛创新表述

- “第一次建立观测量—幻觉关系”：One Photon与Hallucination Index已非常接近。
- “第一次区分真实信息和先验幻觉”：BIGPrior与成像幻觉谱系已有。
- “第一次发现一致却错/语境改写”：HalluGen和SceneFaith压缩这一空间。
- “第一次用不确定性指导真实测量”：AdaSense/GPARA已有。
- “第一次同时评价视觉质量和文字事实”：TeReDiff/CTVid已有。

可继续的是这些已知机制是否造成**尚未被直接解释的采集选择、停止时机或预算归因错误**。检索未发现精确覆盖，不写NOVELTY CONFIRMED。

## External Critical Review
<a id="external-critical-review"></a>

Review configuration: fresh-session gpt-6-astra / ultra；read-only；完整阅读12项候选。总体立场 **PROCEED WITH CAUTION，只继续文献核查**。独立会话避免沿用生成过程中的判断，但仍属同模型家族，未取得跨家族验收。
本次审查另查SceneFaith、ClearText-Video、One Photon，以及Noise-Optimal Capture/BIGPrior官方资料；其余近邻沿用已核对的候选池，并未虚称全部重新深核。
Durable trace: `work/.aris/traces/idea-discovery/2026-10-08_run01/review.md`。完整池记录也在同一trace目录。

| ID | 裁决 | 审查指出的主要问题和放弃条件 |
|---|---|---|
| 12 | 谨慎继续，暂定第一 | 估计器改变实验设计是经典现象；只有稳定改变事实目标下采集选择才有潜力。物理指标/非生成基线解释全部排序，或设置仅平移质量，则不支持H1 |
| 1 | 谨慎继续，暂定第二 | 低方差偏差已知；需预算进程中的停止失效。已有相同盲区或同覆盖率错误与分歧同步改善，则放弃当前主张 |
| 4 | 谨慎继续，暂定第三 | 同decoder不自动证明适配公平，也不自动证明不公平。若已存在公平适配基线且主要优势保留，应关闭“主要来自适配”的质疑 |
| 2 | 降级保留 | SceneFaith已fixed patch和blur×context；贝叶斯先验赔率也预期不同证据需求。只将blur换成photon budget不足 |
| 3 | 低优先保留 | 优化一致性本来会降低分歧。必须重新校准阈值/同覆盖率比较；若检测能力不变，H1失败。无开关是可行性问题而非H0 |
| 5 | 放弃当前独立表述 | 虚构—擦除属于成熟风险—覆盖率权衡；作为全项目三态评价协议。只有它改变预算选择才重启独立题 |
| 6 | 备选 | 留出核验/后验预测/主动测量已有；必须记入留出损失并与全部观测用于恢复比较。固定总预算无净收益或普通交叉验证即可解释，则不足 |
| 7 | 备选 | 多算不能增加信息不等于无任务收益。必须同平台计入流水并行；跨点来自硬件/接口不公平时不能用 |
| 8 | 放弃当前独立表述 | 多重比较与联合风险成熟。相关性显著、公式或patch换事实不足；需特殊依赖结构造成有意义预算错误 |
| 9 | 降级保留 | CTVid已有恢复侧/读出侧归因；必须非生成中间已正确、后生成覆盖且影响追加采集收益。几个案例不足 |
| 10 | 低优先保留 | 非最优流程非单调不意外；必须合法嵌套真实读出、场景平均可重复。旧数据被替换/接口不支持/归一化变化不算 |
| 11 | 放弃当前静态主线 | 去鬼影/时间混合已有；只有共同事实不属于任何真实时刻且现有方法未处理，才考虑未来重启 |

采纳的审查修订：
1. 所有“一致性”分别说明跨seed、轨迹、曝光、跨模型，不借用彼此结论。
2. 候选3必须在阈值重校准后比较；候选6必须计算留出观测使恢复证据减少的成本；候选7计入流水并行。
3. 候选2/9不再把语境干预/阶段归因当首次；5/8作为测量协议保留。
4. 无数据/接口标记暂不可验证；小样本未检出不宣称H0。未找到论文不等于新颖性证实。

## Refined Proposal
提案仅收敛问题和证据，不设计或训练新网络。
- [候选问题提案](../refine-logs/FINAL_PROPOSAL.md)
- [文献先行判别路线](../refine-logs/EXPERIMENT_PLAN.md)
- [未启动实验的状态记录](../refine-logs/EXPERIMENT_TRACKER.md)
当前唯一活动块是最近邻的直接证据检查。物理A/B和冻结推理均为条件式备用，不是已启动任务。

## Workflow Evidence and Limits
技能由用户明确调用。已完成实质文献梳理、12候选生成、定向近邻检查、独立会话批评和问题级提案；所有新实验结果为无。
- run_state.py与idea_discovery_gate.py在规范查找链中未找到，正式证据门控未执行；诊断状态记录保存在work/.aris/runs/，不冒称脚本生成的PASS。
- 可用Codex MCP跨家族复核路由缺失；fresh Astra仅作同模型家族审查，没有accept receipt。
- Gemini CLI源尝试失败：环境没有GEMINI_API_KEY（exit41）；未读取凭据或修改认证，没有把空结果当证据。
- verify_papers.py未找到；文献保留[UNVERIFIED：自动核验]，已查的一手身份和关键方法人工核对。
- render-html技能和研究合同模板未找到；未输出HTML，也未把候选当已验收方法合同。问题提案仍可供导师讨论。
- 正式状态 **BLOCKED** 依据技能原文：“If either helper is unavailable, the final report is BLOCKED; do not silently continue without a state record.”
- 用户要求停留SCOUT→CONVERGE，因此未遵循通用技能默认的训练/物理pilot路径；当前没有经验新颖性验收。

## Next Single Action
补齐#12最近邻的同预算/同模型/同设置曝光对照证据矩阵：先确定现有工作是否已经回答配置排序或达标集合。#4的decoder审计可以作为便宜的独立核查入口；暂不把三个问题合成一个方法。

## Appendix: Complete Candidate Pool
下列12项保留生成时的核心问题、H1/H0、最近邻、判别动作和风险。正式优先级/去留以本报告前面的审查结果为准，生成时的可行性计划估计不是已测成本。


# 完整候选池：SCOUT，非验收结论
Date: 2026-10-08
范围：手机Bayer RAW HDR/低照；真实观测、非生成/生成先验、局部事实与采集决策。
用户优先约束：文献证据先行；不进入新网络设计，不训练；物理Minimal Probe A/B仅备用。目标不是重新证明SNR增大一般改善恢复。候选全部未实验，排名不得冒称经验排名。
生成来源：fresh gpt-6-astra/xhigh子代理11项；root补充12；机械去重，无预淘汰。
外部审查配置只能提供同模型家族独立会话审查，不满足跨家族验收。Gate scripts missing。所有文献[UNVERIFIED：自动核验脚本未运行]，不等于论文身份未人工检查。

## 1 生成结果稳定是否先于事实正确？
Lens: contradiction / diagnostic. key stable_wrong_before_truth_convergence
问题：更多真实观测/采样收敛时，局部seed一致性会不会先达到平台而事实仍错？
H1：存在可重复预算区间，分歧下降而清晰稳定错误不降，相同接受覆盖率的一致性风险校准失效。H0：在声明适用分布中一致性与事实错误同步改善，未出现该失效。
近邻：[One Photon, Many Worlds](https://arxiv.org/html/2610.02675v1)；[iRAG ICCV2025](https://openaccess.thecvf.com/content/ICCV2025/html/Lee_Reference-based_Super-Resolution_via_Image-based_Retrieval-Augmented_Generation_Diffusion_ICCV_2025_paper.html) Fig6轨迹方差；[HalluGen](https://arxiv.org/html/2512.03345v1)已知一致但错误。
差异：特定预算区间/接受风险/停止采集盲区，不能只写一致性≠正确。轨迹方差与跨seed方差须分开。
首行动：查variance定义和conditional-error/coverage结果；已有输出足够才重标。后续冻结权重多seed、场景级统计。
价值：发现错误停止条件或限定可用条件。风险：一般先验偏差演示不新。成本：文献1–2人日（计划估计），推理/GPU未估。

## 2 相同局部证据，不同语境需要不同采集量？
Lens: untested assumption / causal diagnostic. key context_prior_changes_local_fact_at_fixed_evidence
问题：目标低照字符/符号观测不变时，外围语境是否改写局部事实并提高摆脱错误的预算？
H1：固定目标像素，外围干预系统改变局部事实；逆语境/罕见事实达到相同风险与可读性需更多证据。H0：效应由编辑伪影/常见难度解释，或增加证据后无有意义预算差。
近邻：[TeReDiff ICLR2026](https://openreview.net/pdf?id=jt2c2H6auR)已文本幻觉/场景语境；语言偏置、context/crop成熟。
差异：目标观测不变的语境干预与额外物理证据需求；不再做泛OCR幻觉benchmark。
首行动：查罕见/随机字符串、context/crop、局部固定反事实消融。后续如需要，用已有图和同一退化创建成对上下文；不训练。
价值：局部SNR不足以决定采集要求，或支持局部稳健性。风险：须匹配字形/对比度并排除拼接边界、分布外编辑。
成本：文献1–2人日，后续数日–一周准备估计，算力未知。

## 3 合成曝光一致是否降低错误可检测性？
Lens: contradiction. key synthetic_bracket_consistency_hides_shared_errors
问题：单次真实观测生成的多曝光共享错误时，强一致性会不会掩盖事实错误？
H1：固定输入，提高曝光一致性压低曝光间分歧，但事实错误不相应降低，以分歧检测的性能下降。H0：一致性同步改善事实/没有检测盲区。
近邻：[Single-Shot HDR](https://arxiv.org/html/2605.11628v1)；[Bracket Diffusion v2](https://arxiv.org/html/2405.14304v2)；[Exposure-Consistent Diffusion WACV2026](https://arxiv.org/abs/2602.19706)；HalluGen。
差异：一致性约束对诊断力的作用，而非数据处理不等式或指称作者保证事实。
首行动：查现成消融能否同时比较一致性与局部参考错误。后续仅用现成开关/权重，不改模型凑消融。
价值：区分合成bracket视觉作用与核验作用。风险：自然已知一致≠真、模型无可用独立开关。
成本：文献1人日，权重可用未确认。

## 4 任务“省光子”有多少来自decoder输入适配？
Lens: attribution diagnostic. key photon_savings_vs_decoder_input_adaptation
问题：生成恢复降低采集预算的任务收益，有多少简单非生成预处理/合适读出也能获得？
H1：对raw使用适配预处理或噪声任务读出后，生成相对raw直接喂现成decoder的预算优势显著缩小。H0：公平适配后生成仍保持主要优势。
近邻：[One Photon Sec7.2/Fig13](https://arxiv.org/html/2610.02675v1)同一off-the-shelf QR decoder；task-oriented restoration/domain adaptation成熟。
差异：拆开重建、输入适配、任务先验的预算贡献；端到端提升是真的，不称它虚假或物理极限。
首行动：原文/代码核对raw缩放、threshold、传统去噪/reader基线与错误decode/拒识。必要后续已有数据CPU基线、极简符号似然判别，不训练新网络。
价值：改变采集预算解释或找到廉价路径；若只补更强baseline则不足。
成本：文献1–2人日，数据未确认，CPU可行性待验证。

## 5 少生成是否只是把虚构转成擦除？
Lens: diagnostic. key fabrication_reduction_trades_into_fact_erasure
问题：降低先验强度让错误但清晰变成不可读，还是变成正确？
H1：减弱先验主要将清晰错误转为擦除，计入可读性后安全排序或达标采集选择改变。H0：事实正确率真正改善且覆盖率不受有意义损害。
近邻：HalluGen、[MRI visual/diagnostic study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11519109/)、感知失真/precision–recall。
差异：现成RAW/HDR路径三态转移与采集选择；错误分类本身非创新。
首行动：查strength/guidance消融是否同时正确、错误、擦除；可重标已公开输出。
价值：保守设置是否真达成目标。风险：只是经典权衡改名。
成本：文献1人日，人工标注可能高于推理。

## 6 少量独立真实观测能验证哪些稳定错误？
Lens: method transfer / detectability. key heldout_measurement_detectability_of_stable_fact_errors
问题：恢复以外的真实读出能否暴露生成器样本自己没有暴露的错误，所需互补性是什么？
H1：留出独立观测识别低seed方差错误，但同样饱和/不可见的验证不起作用；互补曝光改变检测力。H0：风险已被样本分歧解释或留出无净收益。
近邻：HalluGen、[On Hallucinations in Tomographic Image Reconstruction](https://arxiv.org/abs/2012.00646)、[AdaSense](https://arxiv.org/html/2407.08256v1)、[GPARA](https://arxiv.org/html/2609.34172v1)、posterior predictive checking。
差异：固定验证预算的可检测边界；不声称首次不确定性主动采集。
首行动：查measurement holdout/预测检查是否控制成本/互补性。后续拆已有独立burst，恢复损失与验证收益都计入。
价值：何种核验有用/无效。风险：简单移植交叉验证不够。
成本：文献2人日，独立读出可用性未查。

## 7 同样端到端时间，多拍还是多算？
Lens: scaling regime. key capture_compute_tradeoff_for_factual_risk
H1：二维采集时间×推理时间存在按退化分区的事实风险交叉；证据不足时多算主要提高观感/共识，补拍收益更大。H0：合法工作区间一个轴始终占优。
近邻：[ResFlow-Tuner](https://arxiv.org/abs/2603.22027)已有restoration test-time scaling；OnePhoton已有观测预算。
差异：同硬件冻结路径下二维事实边界，不提出TTS。
首行动：查步数/seed/reward消融是否含事实和同平台采集延迟。后续先profile再小网格，无新训练。
价值：系统资源选择。风险：只是多算不增加信息，或跨硬件曲线不公平；允许并行时成本不是简单相加。
成本：文献2人日；无可靠GPU小时数。

## 8 多个局部事实的联合风险怎样决定整图预算？
Lens: statistical transfer. key joint_fact_error_dependence_controls_image_budget
H1：生成错误跨区域相关性随先验变化，独立patch模型错估整图至少一错的预算。H0：简单独立或保守界足够指导实际成本。
近邻：HalluGen/SHAFE、[K-RCPS](https://proceedings.mlr.press/v202/teneggi23a.html)、[Conformal Bounds on Full-Reference Image Quality](https://arxiv.org/html/2505.09528v1)。
差异：事实错误联合分布及预算后果；写1-(1-p)^K或union bound非新。
首行动：核对保证单位pixel/patch/image/task；重标已有多事实图的共现。
价值：局部承诺能否组合为整图。风险：成熟多重比较、需要特殊依赖结构。
成本：文献1–2人日，标注/CPU为主。

## 9 事实已拍到，在哪个阶段被覆盖？
Lens: stage diagnostic. key already_observed_facts_overwritten_after_fusion
H1：最终错误中的一部分非生成中间结果已正确；后生成阶段成为预算收益瓶颈。H0：错误主要来自输入不足，无阶段覆盖现象或不足以影响选择。
近邻：[BurstGP](https://arxiv.org/html/2604.23508v1)single-frame diffusion分支已看到完整burst重建；UltraFusion；像素条件注入/生成破坏细节成熟。
差异：同局部逐阶段事实转移和追加采集边际收益，不把generator条件帧数当真实采集数。
首行动：查中间输出、强度消融；必要保存已有模型自然中间结果。
价值：把预算花在采集还是修证据利用。风险：挑个失败case不成题。
成本：文献1人日，部署资源未知。

## 10 增加嵌套真实观测，冻结系统风险会反增吗？
Lens: contradiction / scaling. key nested_real_observations_nonmonotone_pipeline_risk
H1：保留所有旧观测、总预算增加、合法输入接口内，平均事实风险可重复上升并定位到流程。H0：工作区间单调改善；个例反转只是噪声。
近邻：OnePhoton、多帧伪影/OOD；经典最优决策可忽略新增观测。
差异：实际系统违反理想信息单调性；不说物理信息有害。
首行动：预算消融横轴、误差条、逐场景；后续已有嵌套burst子集、冻结路径。
价值：实用预算规则。风险：变长不支持/人为失配，无一般科学发现。
成本：文献1人日，模型合法接口待核对。

## 11 动态HDR会融合出未曾同时存在的事实？
Lens: time-scale diagnostic. key temporally_incompatible_facts_in_hdr_fusion
H1：增加采集窗改善噪声，却提高跨时刻语义拼接；结果不属于任何真实时刻。H0：参考帧/去鬼影已处理，只有已知边缘伪影。
近邻：AdaptiveAE、动态HDR/deghosting、video reconstruction。
差异：同目标时刻的事实共存关系及采集窗选择。
首行动：查数据GT时刻、电子屏/交通灯等公开案例；后续已有时间标签序列。
价值：时间分辨率–证据量权衡。风险：退化去鬼影且超出当前静态优先。
成本：文献1–2人日，数据未知；保留候选。

## 12 生成先验会改变等成本曝光配置排序吗？
Lens: decision / untested assumption. key prior_changes_equal_cost_exposure_selection
问题：固定总曝光时间、读出数、增益时，传统SNR/饱和覆盖最优的配方是否仍最容易满足局部事实风险与可读性目标？
H1：现成先验强度改变等成本曝光配置的事实风险排序/目标可达性，且不只由传统融合的物理SNR、饱和或已知感知失真权衡解释。H0：排序始终由物理证据和基线解释，先验仅平移观感，不改变采集选择。
近邻：[Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/)、AdaptiveAE、BurstGP、OnePhoton、[LuckyHDR](https://arxiv.org/html/2604.19976v1)、BIGPrior。
差异：观测与先验交互必须改变采集选择；仅interaction显著/传感器换为Bayer不够。
首行动：提取同传感器、同预算、同模型的曝光消融是否同时含事实/覆盖率；缺这种直接证据不等于证明现象存在。
备选后续：用户A=N1/4/8固定每帧t仅现象检查；B=N4,T4t固定增益 [t,t,t,t] vs [t/4,t/4,t/2,3t]，等时间/读数但证据不同。两配置单T只能比较不能定最低成本；独立采集/高SNR非生成参考，seed不当场景。
价值：什么时候先验确实改变采集决策。风险：差异只是已知成像噪声，静态无效、模型不支持曝光配置、现成强度操作不可比较。
成本：先文献2人日，物理验证未授权启动/无设备或GPU成本测量。

## 证据底线
三状态正确可读/错误清晰/擦除；条件错误率同时覆盖率；无confidence signal不叫自信错误。多seed/patch非独立场景，场景级推断；同场景独立采集区分噪声vsseed。固定强度记录操作意义，不能跨模型以数字大小充当同一先验强度。未找直接证据不等于证实novelty/缺口。

## 新补充文献边界
[BigPrior TIP2022](https://arxiv.org/abs/2011.01406)已解耦先验幻觉与数据保真并给per-pixel reliance，不能声称首次统一二者。
[LuckyHDR April2026](https://arxiv.org/html/2604.19976v1)输出为曝光校正邻域观测凸组合，研究观测驱动RAW多曝光、任意长度，作者称避免合成幻觉；不是单独证明所有局部事实正确。
[AdaSense ECCV2024](https://arxiv.org/html/2407.08256v1)按posterior covariance选未来真实linear measurements，不能把采集不确定性优化当创新。
[GPARA Sept2026](https://arxiv.org/html/2609.34172v1)equal-cost线性点测量主动采集，泛化grounding/active acquisition很近。
[LEADer MM2026](https://arxiv.org/abs/2608.06981)active sampling针对计算采样，不是新增物理观测。
[Distribution-shift UQ CAMSAP2025](https://arxiv.org/html/2510.10947v1)用measurement variation稳定性估计OOD不确定性；不能偷换成低seed方差保证真。
