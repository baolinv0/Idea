# 有限观测下 RAW HDR 恢复：查新与问题收敛
日期：2026-10-08（Asia/Shanghai）｜阶段：SCOUT → CONVERGE

## 当前行动更新：文献证据优先（2026-10-08）
用户指出Minimal Probe中的若干结论可以从已有论文获得。本轮核对后采用此调整：当前先提取原文对照并建立“主张—证据—适用条件—未回答部分”的证据链，不把已知一般趋势的复现实验作为SCOUT阶段必经门槛。原A/B采集方案仅保留为备用。后续复核为同模型家族，provisional，不构成新的独立跨模型验收。

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



## 查新结论
**PROCEED WITH CAUTION，5/10：先完成文献证据收敛，必要时再进入最小现象验证，但目前不能把宽泛 motivation 当作已确认创新。** 分数是早期研究判断，不是接收概率。具体薄弱点是：SPAD 中已有“光子预算→生成后验与任务错误”的直接研究，固定预算曝光优化也已有成熟谱系。Bayer RAW 替换传感器、扩大帧数消融，单独不足以支撑贡献。

候选贡献应是一个可验证的发现：在固定采集成本下，曝光分配与先验强度是否存在影响局部事实错误的交互，以及它是否改变达到指定风险与可读性要求所需的采集决策。本轮尚未找到完整覆盖该设定的工作；这是检索后推断的候选缺口，不能证明文献空白。

没有运行实验，没有证实临界收益，也没有进入网络设计。

## 必须修正的机制表述
- **UltraLED** 是单张短曝光 RAW 的 ratio-map 曝光校正与 brightness-aware RAW 去噪，使用两个 U-Net。它可以代表学习先验恢复，不能直接当作扩散生成 HDR 的例子。参考曝光栈不等于推理输入。[原文](https://arxiv.org/html/2510.07741v1)
- **UltraFusion** 用两张真实不同曝光 RGB 与 Stable Diffusion 做引导修补，并直接输出融合后的 LDR 图像。它已经结合额外观测与生成先验，因此不能放在“纯物理融合”一侧，也不能把其观感指标直接当作线性 HDR 辐射保真度。[原文](https://arxiv.org/html/2501.11515v1)
- **HDR+** 使用同曝光短 RAW burst；多帧与多曝光应分别标注。[作者论文页](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/)
- 分类宜改为两个轴：**真实采集方式 × 恢复先验强度**。非生成模型也可能改错结构；生成采样很稳定也可能持续生成同一错误。确定性、采样一致性、观测一致性和事实正确性须分别测量。[确定性恢复的相关理论](https://proceedings.mlr.press/v235/ohayon24a.html)
- vivo V1 的具体采集路径未在本轮核验，不宜据此断言“不增加真实曝光”。生成的多张曝光图同样不能计为多次真实采集。

## 核心主张与最近工作
| 候选主张 | 最近工作 | 尚需建立的差异 |
|---|---|---|
| 观测信息影响保真、感知与幻觉 | Hallucination Index；One Photon, Many Worlds | 一般现象已有。需要常规 RAW 的曝光/饱和/读噪交互及局部风险决策 |
| 多个真实观测约束生成先验 | UltraFusion；BurstGP | 组合已有。需要真正改变采集输入并控制总成本 |
| 局部错误与不确定性可以评价 | Hallucination maps；HalluGen；LL-Bench；K-RCPS | 评价/校准已有。需要明确错误事件，不能将指标分数、区间覆盖率等同错误概率 |
| 固定预算曝光分配影响可信恢复 | Noise-Optimal Capture；预算感知的AdaptiveAE | 曝光优化已有。需要超越传统 SNR/PSNR 的先验相关风险发现 |

## 最近谱系
文献状态说明：**[UNVERIFIED] 表示未通过技能要求的 verify_papers.py 自动核验**，该可选脚本在已搜索的安装技能路径中未找到；下面论文身份与关键机制已通过一手页面/原文核对。部分 CVF 页面返回 403，以 arXiv/作者页面替代。该标记不能解释成已经运行自动核验。

| 一手论文 | 年份/出处 | 已回答的部分 | 当前设定的差异 |
|---|---|---|---|
| [UNVERIFIED] [Noise-Optimal Capture for High Dynamic Range Photography](https://people.csail.mit.edu/hasinoff/hdrnoise/) | CVPR 2010 | 固定时间与照片数的快门/ISO优化、最坏区域SNR | 未研究生成式局部事实风险 |
| [UNVERIFIED] [Burst photography for high dynamic range and low-light imaging on mobile cameras](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/) | SIGGRAPH Asia 2016 | 同曝光 RAW burst 配准融合、暗部降噪 | 未标定生成先验的事实错误边界 |
| [UNVERIFIED] [The Perception-Distortion Tradeoff](https://arxiv.org/abs/1711.06077) | CVPR 2018 | 感知分布与平均失真存在权衡 | 不是采集预算—局部幻觉阈值 |
| [UNVERIFIED] [On hallucinations in tomographic image reconstruction](https://arxiv.org/abs/2012.00646) | TMI 2021；2020预印本 | 测量/广义零空间分解与幻觉图 | 有噪、裁剪 RAW 不可直接套精确线性零空间 |
| [UNVERIFIED] [How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control](https://proceedings.mlr.press/v202/teneggi23a.html) | ICML 2023 | 生成恢复的校准区间与风险控制 | 不保证每张点估计正确；未给 RAW 采集阈值 |
| [UNVERIFIED] [RawHDR: High Dynamic Range Image Reconstruction from a Single Raw Image](https://arxiv.org/html/2309.02020v1) | ICCV 2023 | 单 RAW HDR 监督重建 | 未扫真实采集预算与局部错误率 |
| [UNVERIFIED] [Hallucination Index: An Image Quality Metric for Generative Reconstruction Models](https://pmc.ncbi.nlm.nih.gov/articles/PMC11956116/) | MICCAI 2024 | 模拟显微噪声实验中，输入SNR增加使幻觉指数降低 | 指数是参考分布距离，非事件错误率；未研究Bayer曝光分配 |
| [UNVERIFIED] [UltraFusion: Ultra High Dynamic Imaging using Exposure Fusion](https://arxiv.org/html/2501.11515v1) | CVPR 2025 | 两真实曝光与生成先验的融合 | 无受控成本扫掠与独立局部事实风险阈值 |
| [UNVERIFIED] [UltraLED: Learning to See Everything in Ultra-High Dynamic Range Scenes](https://arxiv.org/html/2510.07741v1) | NeurIPS 2025 | 单短 RAW 的曝光校正与去噪 | 非扩散生成；无事实风险校准 |
| [UNVERIFIED] [AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes](https://arxiv.org/html/2508.13503v1) | ICCV 2025 | 预算感知的ISO/快门、栈长惩罚与运动权衡 | 栈长惩罚非严格等时间对照；非生成式事实错误风险 |
| [UNVERIFIED] [BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors](https://arxiv.org/html/2604.23508v1) | 2026-04-26预印本 | burst重建加视频生成先验，单/多帧扩散条件消融 | 单帧条件分支已使用整段burst重建，不能当作1 vs14次真实观测实验 |
| [UNVERIFIED] [HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration](https://arxiv.org/html/2512.03345v1) | CVPR 2026；2025预印本 | 可控幻觉数据、局部检测与SHAFE | 以MRI为主，非受控RAW采集预算 |
| [UNVERIFIED] [LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models](https://arxiv.org/html/2606.02535v1) | 2026-06-01预印本 | 包括HDR/低照的偏好和幻觉标注 | 未控制传感器真实采集预算 |
| [UNVERIFIED] [One Photon, Many Worlds: Posteriors and Predictions with Single-Photon Cameras](https://arxiv.org/html/2610.02675v1) | 2026-10-02预印本 | 二值SPAD预算增加时，生成歧义及边缘/OCR/QR/脸几何错误收敛 | 常规Bayer、读噪、曝光分配与校准局部事实风险仍不同 |

**最强近邻是 One Photon, Many Worlds。** Sec.9 报告其任务通常在20–50帧接近性能平台，并明确承认经验结果依赖数据与协议。该数值不能转成手机HDR的帧数要求。它已实做宽泛预算问题，必须放在Related Work的中心，而非当作遥远背景。[原文Sec.9](https://arxiv.org/html/2610.02675v1#S9)

补充检查的一手前沿： [Single-Shot HDR Recovery via a Video Diffusion Prior](https://arxiv.org/html/2605.11628v1)、[ExpoCM](https://arxiv.org/html/2605.02464v1)、[DiffHDR](https://arxiv.org/html/2604.06161v1)、[High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences](https://arxiv.org/html/2609.27274v1)。分别涉及单次真实采集的生成曝光、单图生成HDR、视频生成重曝光及三帧同曝光RAW；没有据此发现完整的候选风险预算实验。这些条目同属 [UNVERIFIED] 自动核验状态。

另检查 [RODS（NeurIPS 2025）](https://papers.nips.cc/paper_files/paper/2025/hash/24c79c21eb699e9efdebaafa40ed0e4d-Abstract-Conference.html)、[确定性恢复的感知—鲁棒性权衡（ICML 2024）](https://proceedings.mlr.press/v235/ohayon24a.html)及[卫星burst自监督不确定性（UAI 2026）](https://proceedings.mlr.press/v337/zheng26a.html)。它们提醒我们区分生成采样缺陷、场景事实错误和校准不确定性。自动核验状态同上。

## 问题锚点与可测目标
建议将“真实信息上限”改为**给定成像系统和场景分布下的经验保真边界**。比较几个网络的效果不能建立所有算法的物理信息上限。

预算不能只写N，应至少记录 b=(独立读出数N、各快门t_i、增益/ISO、采集时延)，并记录局部SNR、饱和/有效曝光覆盖、后续运动参数。相同帧数不等于相同信息；相同时间不等于相同保留信息。固定每帧曝光增加N和固定总曝光拆分N是两个问题。

对冻结模型m与指定场景分布D，预定义局部错误事件H，再研究：
R_m(b;D)=P(H=1 | b,m,D)。
最小可行预算是在预先给定候选预算集合里，满足风险上置信界≤ε，且可读性/有效覆盖与感知质量达到预设要求的最小成本方案。要求未达到时报告“未达到”，不强行寻找阈值或拐点。这里没有单图、分布外或所有模型通用的保证。

H不能定义成任意像素误差。至少区分：错误但清晰的事实、正确可读事实、模糊/不可判定或擦除。报告全部样本的错误率，以及有明确输出样本上的条件错误率和接受覆盖率。这样“全部抹平”不能伪装成安全。自然纹理、随机文字和高光辐射误差应分别报告。LPIPS/观感不能单独证明事实正确。

## 备用采集probe：文献证据不足时再启用
1. **静态、标定、已知事实。** 少量独立场景，包含亮区与暗区、测试前新随机生成的文字/符号/纹理及自然物体。采独立高SNR非生成参考，固定光照、光圈；标定黑电平、增益、读噪、饱和。同一场景需要独立采集重复，以区分传感器噪声与生成seed随机性。随机内容用于压低训练记忆混杂，不能外推成全部自然图像分布。
2. **增长预算，仅作已知现象检查。** N=1/4/8，每帧t，承认总时间随N增长。复制同一帧是负对照，其独立读出数仍为1，噪声相关性不能伪造为独立。
3. **等预算，是候选发现的关键对照。** 固定N=4、总曝光T=4t，比较[t,t,t,t]与[t/4,t/4,t/2,3t]。固定增益与读出数，记录开销。这里只比较一个T下的配置，最低成本需求须后续增加预算候选并独立校准。相同入射曝光预算，故意改变暗部与高光的有效证据；不能声称两组SNR相等。
4. **固定恢复路径。** 物理融合/保真重建基线，再对同一融合输入应用现成生成恢复模型的可用先验强度设置；不训练新网。记录强度参数到底改变去噪、条件约束还是细节生成；现成preset若混合这些变化，结论只对该设置成立。生成器若仅接收融合图，结论必须限定“融合后生成”这一路径，不能推广为直接多帧条件生成。
5. **分开评价正确性与外观。** 固定显示映射，盲评可读事实与观感；记录假细节、擦除和参考误差。多seed只检查模型变化，不能充当独立场景、校准数据或真实观测。可读错误不自动等于“自信错误”；没有独立置信信号时先不宣称置信度已校准。

**H0：** 观察到的收益可由常规去噪、SNR或饱和覆盖改善解释；等成本下没有可复现的“先验强度×曝光分配”额外风险交互。
**H1：** 在上述控制下，局部事实错误—可读性—感知质量边界存在可复现交互，足以改变满足预设风险要求的采集选择。

H1不是“多拍更好”。两组bracket/同曝的简单主效应仍可能只是经典HDR结论。预先指定局部SNR、饱和率和传统融合结果的解释基线；需要先用交互/配对分析检验，再考察先验是否改变配置排序或目标可达性。补充局部噪声/饱和近似匹配对照可帮助排除“只是去噪更强”。交互显著本身不证明新机制。小pilot仅估效应量；未检出不等于证明H0。风险阈值须在独立场景级校准/留出数据上确认，并处理多预算选择；不要把多个相关patch或seed当作样本数。

## 给导师的修订版一分钟
我想研究常规RAW HDR成像的可信恢复边界。已有工作表明，增加光子观测会降低生成恢复的不确定性，也已有方法融合真实多曝光与生成先验。因此我不把这个一般现象作为创新，而是问：在固定采集时间内，帧数与曝光分配怎样影响局部事实错误，生成先验的强度又怎样改变这种关系？我希望用可审计的真实RAW观测和独立参考，分别记录错误但清晰的细节、正确细节和不可恢复区域，找到满足指定风险及可读性要求的采集条件。当前先从已有论文提取机制与公平对照证据，明确尚未回答的局部风险问题；必要时再做静态等预算验证。

## 检索与审查边界
检索使用观测预算、光子预算、幻觉度量、可信恢复、conformal风险、RAW burst与曝光分配等多种措辞，检查2024–2026方法及2026-04-08以来的近期预印本；定向搜索ICLR2026/ICML2026/NeurIPS2025官方域。没有逐篇遍历全部会议索引、引用图及所有补充材料。Google Scholar/Semantic Scholar并未作为可用独立API运行，不能声称数据库检索穷尽。

本机没有暴露Codex reviewer MCP，按技能降级使用fresh-session同模型家族subagent复核。review_status: completed_same_family；acceptance_status: provisional。复核支持PROCEED WITH CAUTION/5分，要求证据落到配置选择变化、独立采集重复及明确物理解释基线；这些修正已并入probe。实际完整回复保存于NOVELTY_REVIEW.md；不能声称独立跨模型通过。当前目录没有原始研究状态或Playbook文件，随报告保存新的状态快照，没有改动未提供的研究仓库。


## 下一单步
围绕配置排序与局部风险阈值定向检查原文消融、补充材料和引用谱系；先提取直接证据，暂不承诺采集实验或生成网络。
