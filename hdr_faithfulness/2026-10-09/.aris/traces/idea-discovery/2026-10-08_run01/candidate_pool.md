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
