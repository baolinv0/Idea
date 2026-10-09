# CaptureTM 研究方向挖掘
日期：2026-10-08。范围：物理曝光 AE、采集信息与影调 TM。参照分支 feature/capture-tm-c-20261005，固定 HEAD 7e080d373accd28150034b68718c27a21f932a09。
流程：research-lit → idea-creator → novelty-check → research-review → research-refine-pipeline。
状态：REVISE / 研究准备稿。初轮查新 PROCEED WITH CAUTION（5/10）；批判审阅 PROCEED（只推进最小实验，成熟度4/10）；同系列审阅，最终证据门未接受。CPU 实验已完成；没有正式神经训练或真实相机证据。

经过决定性检验后，仍待查新的研究问题是：**当曝光差异已获得充分、公平的后端补偿时，哪些可观测的空间关系仍会改变最优物理曝光？** 主线由“可补偿范围”定义，空间关系反例提供机制证据，独立后端交叉评测排除搭档适配。三者构成一个问题，不能算三项独立创新。

最新决定检验（2026-10-09）：H-aware三种子与DNG4/8积分复核均已完成并独立审计。H-aware残差规则退化为固定4，未保留特殊关系自适应收益。现有证据不足以确认投稿贡献；两次跨家族外审等待明确外部提交授权，gate仍BLOCKED。见下文History-aware Decision Update与[完整正负结论](../local-dng/CONCLUSIONS.md)。

## Literature Landscape

本轮在既有查新基础上扩展了后期编辑、空间可恢复性与后端分布匹配检索。来源包括一手 arXiv/CVF、作者官方项目、alphaXiv 发现与网页检索。Gemini CLI 实际调用失败：缺 GEMINI_API_KEY；没有把它的输出当审阅证据。不是所有会议/年份的穷尽检索。

| 一手工作 | 已存在的内容与本研究约束 |
|---|---|
| [EBSNet/MEFNet，CVPR 2020](https://arxiv.org/html/2005.12536v1) | 预览与有限包围曝光选择，以融合质量反馈并联合训练。泛泛联合 AE＋后端已被覆盖。 |
| [Neural Auto-Exposure，CVPR 2021](https://openaccess.thecvf.com/content/CVPR2021/papers/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.pdf) | 针对检测任务联合优化曝光与下游处理；“下游目标驱动物理 AE”并非空白。 |
| [AdaptiveAE，ICCV 2025](https://arxiv.org/html/2508.13503v1) | 三预览、快门/ISO、动态场景和时间预算；附录跨后处理测试。追加帧与换后端测试本身不足以构成新意。 |
| [DEBIR，2026](https://arxiv.org/html/2603.21784v1) | 预览、增益、运动驱动 burst；讨论后端偏置与 staged/joint。训练顺序或搭档偏置不能单独立项。 |
| [Modular Neural ISP](https://arxiv.org/html/2512.08564v3) | 模块化 photofinishing、增益、可编辑 TM；现仓库上游基础。 |
| [Edit-aware RAW Reconstruction，CVPR 2026](https://arxiv.org/html/2512.05859v2) | 随机采样 ISP 编辑，在渲染域监督 RAW 重建并评估编辑。多风格鲁棒损失已有直接先例。 |
| [Benchmarking RAW and RGB Restoration in ISPs，2026](https://arxiv.org/html/2609.02831v1) | 目标 ISP 匹配能影响排名，明确 RAW/RGB 目标域不完全对齐的限制；公平后端训练是必要控制。 |
| [DRIFT，2026](https://arxiv.org/html/2604.03402v1) | 恢复、融合、影调的一体化及推理调节；整个管线或适配器本身不足以区分。 |
| [HDR+，SIGGRAPH Asia 2016](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/) | 低曝光保护高光，融合改善阴影后再影调；经典高光保护与光子/噪声权衡必须作为基线。 |

verify_papers.py 本轮确认了 EBSNet、AdaptiveAE、DEBIR、Modular ISP、Edit-aware RAW、Benchmarking RAW/RGB、DRIFT 七个 arXiv ID 的存在，返回 PASS、pending=0。身份核验不等于核对论文每项主张；检索输入中 AdaptiveAE 简写标题有误，正式标题为 **AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes**，报告按一手来源修正。

已有代码与实验事实决定了切入点。旧 learned 与规则动作库未完全对齐；207224 参数上游被冻结，只训练 2663 参数适配器，不能代表强 TM；旧数据规模约 40 个小合成场景，R1 为 8-scene GPU smoke。未见 S24 真实数据训练、原生 Bayer 标定或 joint 胜过 TM-only 的证据。既有 loss 已包括亮度、梯度与 missing proxy，因此也不能预设“纯外观目标必然失败”。

## Ranked Ideas

全部十个可行候选均交给独立 jury，未按生成者偏好淘汰。生成与 jury 都是实际 gpt-6-astra/xhigh 子代理。评分 V=研究价值、F=当前机制鉴别可行性、R=新颖风险；综合 0.45V+0.30F+0.25(10−R)，是优先级，不是发表概率。此评分为高局部分辨率复核之前的jury优先级；右栏按最终证据降级，不能据分数忽略阴性复核。

| 排名/候选ID | 问题 | V/F/R；综合 | 当前证据与去向 |
|---|---|---|---|
| 1 / 1 | 强 TM 后还剩多少曝光选择价值：可补偿集合 | 8/8/5；7.25 | CPU 出现噪声下近最优集合收缩；熟知物理权衡风险仍高。选为主线。 |
| 2 / 2 | 同直方图、不同空间关系是否改变最优曝光 | 8.5/7.5/5.5；7.15 | 分族有限后端可翻转，但共同256×256后端两族都选0.5；作为未确认机制备选，停止稳定物理翻转主张。 |
| 3 / 3 | 收益能否迁移到独立同目标后端 | 7/8.5/7；6.45 | 本轮所有选择器选同一动作，没有搭档特有优势信号。保留为控制，不独立立项。 |
| 4 / 8 | 三预览下最优曝光是否可识别 | 7/8/7.5；6.18 | 理论可行；一般 POMDP 已知。作为 causal oracle 差距的辅助分析。 |
| 5 / 7 | 模拟器标定误差会怎样推翻动作排序 | 6.5/7.5/7；5.93 | 待验证；缺真实标定范围。支持主线的敏感性检查。 |
| 6 / 4 | 后揭示编辑意图的采集代价 | 7.5/6/8；5.68 | 新协议；Edit-aware RAW 强近邻。暂存，不更换当前固定目标。 |
| 7 / 6 | 均值匹配下减少尾部曝光失败 | 6.5/7.5/8；5.68 | 新效用；CVaR、高光保护常规。暂存。 |
| 8 / 9 | 等数量曝光目录按渲染可区分性分档 | 6/8/8.5；5.48 | 新动作集合协议；须挑战 log-EV 与 greedy cover。暂存工程方向。 |
| 9 / 10 | 只测量、不融合的预览是否值得扣预算 | 7/5/7.5；5.28 | 新时序协议；AdaptiveAE 与融合基线压力高。暂存。 |
| 10 / 5 | 曝光/数字增益对称性是否导致训练病态 | 5/8/8.5；5.03 | 一般 gauge/归一化解释很强。优先作为工程消融。 |

方法迁移视角产生候选 4/6；训练结果矛盾产生 1/3/5；未检验假设产生 2/8/10；资源/标定尺度产生 7/9。没有为追求数量增加新网络。

每个候选的机制、最近邻、廉价验证、复杂度与停止条件见附录候选池；GPU 时间只是未来筛选估算，各项 ≤2 小时，未启动 GPU 或扩大原服务器预算。

### 已执行的三个 CPU pilot

统一配置：250000 个拟合样本、100000 个独立评测样本，种子 19/37/73；Poisson＋4 电子读出噪声、1000 电子满阱、12-bit ADC；固定目标 sqrt(L/(L+0.5))。曝光倍率 0.125、0.25、0.5、1、2、4、8。约 11 秒/次；512 bins 主运行，2048 bins 复核。此倍率网格是单独玩具协议，**不是原仓库 12/24 个合法动作的复现**。

**P1：可补偿集合。** 关闭噪声和裁切、连续反演时，所有曝光的目标误差约为机器精度。仅启用裁切/ADC（还有 LUT 估计误差）时，δMSE=10⁻⁴ 的近最优集合为 {0.125,0.25,0.5,1}；加入噪声后变为 {1}。这是机制存在性信号，不能证明新理论。收紧容差至 10⁻⁵ 时，无噪声集合随 LUT 分辨率改变，故不把数值宽度当稳定结论。

**P2：边际匹配、邻域改变。** 两像素 a∼U(0.05,0.30)、b=4a+0.6；对照仅打乱 b 的配对，并同时置换对应标签和捕获观测。边际多重集与饱和比例严格相同。点式估计器的两族误差曲线一致；等大小局部估计器下：

| 独立评测对象 | 最优倍率（诊断） | 平均 MSE |
|---|---:|---:|
| 相关族，点式 | 0.5 | 2.489×10⁻⁴ |
| 打乱族，点式 | 0.5 | 2.489×10⁻⁴ |
| 相关族，局部 | 4 | 4.039×10⁻⁵ |
| 打乱族，局部 | 0.5 | 2.490×10⁻⁴ |

3/3 种子保持上述原32×128局部估计器排序。2048 bins复核只提高点式LUT，不提高局部轴，因此不能据此称局部机制已通过分辨率复核。相关族局部后端在 4 倍的 MSE 比其 0.5 倍约低 84%，这个百分比**仅属于该玩具先验**。估计器分别在两族拟合，尚未证明共同后端或因果 AE 能识别族；不属于完整图像同直方图实验，也未排除局部相关/梯度等简单统计。空间先验的推断不等于新增实测信息。

**P3：同目标后端交叉。** 两个独立拟合同类 LUT 和固定曝光归一化后端，使用独立 development 集选曝光。3/3 种子、全部选择器都选 1 倍，交叉矩阵每行相同。因此没有后端专属选择优势，也没有神经策略迁移证据。它是有效的阴性对照，不能改写成“跨后端鲁棒性已证明”。

### P2 追检：共同后端与实际局部分辨率

根据批判审阅，把暗/亮两方向都联合恢复，并用同一个混合训练后端（每动作一个，不给族ID）。策略只看三张已知0.25倍、独立噪声的过去预览；相关残差规则的阈值和两动作在独立development上选，test不选动作。

| 共同双向后端 | 相关/打乱两族最佳固定倍率（3种子） | 简单causal规则相对dev最佳固定的test MSE下降 |
|---|---|---|
| 32×128局部分箱 | 4 / 1 | 14.45%–14.90%，平均绝对4.09×10⁻⁵ |
| **256×256局部分箱** | **0.5 / 0.5** | **9.07%–9.45%，平均绝对1.94×10⁻⁵** |

所以先前共同后端的**族均值动作翻转不稳**，不再保留为物理边界证据。规则仍可以利用族内连续内容获益，两族平均最优相同不等于所有场景同动作；但它直接利用已知b=4a+0.6先验，尚非未知先验泛化。δ=10⁻⁴时收益低于所设绝对容差，不能声称必须改变固定曝光。

提高分箱也可能产生稀疏估计误差，本轮不将256×256当“充分强后端”。下一决定实验是连续/数值后验参考后端、局部分箱占用与回退检查，再做依赖强度和先验留出。**不新增risk网络，不以更多训练挽救不稳的翻转。**
[共同后端原始结果](../pilots-shared/shared_backend_results.json)；[256×256结果](../pilots-shared-highres/shared_backend_results.json)；脚本与原结果均保留。


共同限制：无正式神经模型、无 motion/Bayer、无 S24 真数据、无实拍。单点/两像素条件均值估计不能当真实强后端的严格下界。结果保留原始 JSON、完整脚本与更高分辨率复核，不重复 GPU 实验。

## Novelty Verification

实际独立 reviewer gpt-6-astra/xhigh，/root/discovery_novelty，在未读其他评审下审阅原始协议、脚本和 JSON。裁决 **PROCEED WITH CAUTION，novelty 5/10**；没有找到完整覆盖所设控制条件的对等论文，但现有 pilot 主要演示已有知识，尚不能称新发现。

最接近 AdaptiveAE（含去模糊补偿和跨后处理），训练公平性最近邻 DEBIR；EBSNet 早已用语义推断饱和区域。剩余空间应严格缩为：**共同恢复系统和相同因果观测下，控制每动作边际统计，空间依赖导致可预测的动作风险变化，并给出简单规则充分/不足的边界。**

新增必须对照的经典 [Noise-Optimal Capture，CVPR 2010](https://people.csail.mit.edu/hasinoff/hdrnoise/) 已研究噪声模型下固定时间的最优采集；[Optimal exposure time for satellite imaging?，2026](https://arxiv.org/abs/2609.17023) 已讨论后处理后质量最优曝光（目前核读摘要，不据此宣布同构）。一般 Bayes 实验设计、裁切与先验恢复不当新理论。

reviewer 指出：细容差集合受 LUT 分箱影响；分族后端相当于获知先验；原局部估计仅恢复亮像素；P3不是迁移阳性。后续共同混合/双向后端复核补了部分缺口，但不追溯改写此轮裁决。
完整原始响应及实际身份：[trace](../.aris/traces/novelty-check/2026-10-08_run01/response.md)，meta同目录。executor与reviewer同属OpenAI，状态provisional；没有跨family接受凭据。

## External Critical Review

实际 gpt-6-astra/ultra 独立审阅原始代码、结果与提案，未获得其他jury/novelty结论。首轮裁决 **PROCEED（只做最小决定实验）**，成熟度4/10，潜在新颖度3/10（此轮不是完整查新评分）。

最强部分是严格边际匹配、训练/dev/test分离与仅看预览的规则；最致命问题是**有限后端的离散化可能制造曝光偏好**。32箱暗轴在低曝光仅覆盖少数箱，2048点式复核没有解决此问题。据此实际跑256×256追检，族均值翻转消失，报告下调主张。

已修正：有限已训练f的经验风险与函数类最优分开；事后跨未来噪声取min改名hindsight统计并排除主张；CI跨零意味着排序不确定，翻转须两条件风险差区间位于零的两侧且超过锁定δ；已知先验、原库适用性和真实信息增益的范围分别限定。

当前允许的结论仅是：**在指定静态双像素混合分布和有限共享后端中，已知空间关系的简单因果规则能改善固定目标误差**。没有强后端普遍增益或复杂策略必要性证据。
末轮精炼核验256×256原始数据后给出 **REVISE / PROCEED**，成熟度仍4/10、新颖度暂评2–3/10（非查新重评分）。保留题目“固定目标下曝光选择收益：后端补偿与空间可预测性”；下一步只做连续参考后端与空间依赖留出，暂不新增网络/GPU。完整首轮响应及真实身份位于[trace](../.aris/traces/research-review/2026-10-08_run01/response.md)。

## Local Diagnostic Update 2026-10-09

- 完整审计：34对、68个唯一处理过的Linear RAW，11个保守背景组，6/2/3组用于train/development/diagnostic；同一会话，不称独立真实场景大样本。
- 连续参考：3seed、8192源×16次未来重复、64–512积分节点；已知关系规则相对固定曝光下降7.38%–8.43%，反向依赖留出下降14.88%–16.51%。256/512节点动作平均风险差<1e-18。
- 直接关系规则减亮度规则的配对CI在N0三个seed均跨零；不能据各自对固定曝光显著，就宣布关系特征独立必要。N1直接CI不跨零，但仍属于训练prior失配的双像素模型。
- 独立代码审计确认后端信息缺口：当前后验只用未来捕获与已知曝光，没有使用三张H或动作选择事件。这是共同受限后端比较，不是充分后端/Bayes下界。
- DNG真实内容相对诊断已跑通3seed、三个有限后端、四个预设规则；规则收益随后端改变，有明显阴性/反转；三个诊断组的区间只作描述。没有神经训练、原生Bayer、专家GT或真实多曝光重拍证据。
- 当前代码已上传工程分支；原始JSON、逐源成本、冻结后端交叉矩阵、失败修复与复现环境见[local-dng](../local-dng/README.md)。原实验target/actions/formalS24test保持原状。
- 本条是前次运行状态；H-aware及DNG4/8现已完成，详见下一节决定结论。DNG积分2/4节点每prior bin最大风险差6.636e-6，后续4/8 refinement用于确认更严格数值口径。

## History-aware Decision Update 2026-10-09

本节是已完成决定实验的新结论；前面的H-blind、有限分箱与旧审阅保留为历史证据。当前尚未确认可投稿贡献。

H-aware正式三种子、每诊断8192个双像素源×16次未来重复、128/256/512积分已完成，退出0，内部耗时1102.163秒。两个后端共享同一源、H与未来ADC捕获；各自development选择器冻结，再完整交叉。独立审计重算6份NPZ、24个交叉单元、96条配对区间，JSON重算误差0。256/512最大逐源成本差8.717e-17、最大动作平均风险差9.136e-19。

关键阴性结论：三个种子、N0/N1中，H-aware训练的已知关系残差规则全部选固定4，相对自己的dev固定4收益为0、CI[0,0]。N0亮度规则仅有1.30%–1.57%微小改善，绝对约4.2e-7–5.0e-7；N1直接残差减亮度区间全部跨0。旧H-blind选择器转到H-aware仍胜其继承的固定.5，但不能据这个正的交叉单元证明重新选择后的H-aware系统需要残差自适应。

| 条件 | seed | H-aware固定4／残差规则MSE | 亮度规则下降 | 残差减亮度MSE及配对95%CI |
|---|---:|---:|---:|---|
| N0_diagnostic | 19 | 3.16112648e-05 | 1.5698% | +4.9623e-07 [+3.3329e-07, +6.7516e-07] |
| N1_dependence_diagnostic | 19 | 3.93647970e-05 | 0.0965% | +3.7992e-08 [-8.7251e-08, +1.7580e-07] |
| N0_diagnostic | 37 | 3.24936279e-05 | 1.2998% | +4.2234e-07 [+2.4321e-07, +6.0094e-07] |
| N1_dependence_diagnostic | 37 | 3.87476610e-05 | 0.0187% | +7.2526e-09 [-1.2168e-07, +1.5300e-07] |
| N0_diagnostic | 73 | 3.23532889e-05 | 1.3905% | +4.4986e-07 [+2.7840e-07, +6.2518e-07] |
| N1_dependence_diagnostic | 73 | 3.88220666e-05 | -0.0713% | -2.7670e-08 [-1.8448e-07, +1.3440e-07] |

DNG每prior bin4/8节点复核完成，退出0、耗时200.798秒；全部216行源标识、prior和输入一致。最大组级动作风险差由2/4的6.636e-6降至4/8的1.077e-6。六个point-posterior固定动作仍为2，24条规则和288个策略动作不变，所有收益符号不变；inverse/Wiener的144行成本与动作完全一致。支持当前定性诊断稳定，不把相邻积分规则之差当严格误差界或完全收敛证明。

投稿判断：**现有证据不支持把复杂联合AE–TM或关系风险网络的必要性当主贡献。** 可以复用的是输入信息一致、后端专属选择器重新冻结、直接简单规则比较的诊断原则；其是否有足够原创发现支撑投稿，仍需真实外审判断。不能推到任意图像、未知prior或真实相机。

主文献进一步核读：AdaptiveAE §4.1/Table3已有一般后端交叉测试；Modeling Radiometric Uncertainty §5.1/Fig6已有不同恢复方式改变低误差曝光组合集合。不能把这两点独立算新意。身份核验的API暂时失败条目标UNVERIFIED，完整核读与范围见[文献增补](../local-dng/REFERENCES_UPDATE.md)。

最新原始结果：[H-aware JSON](../local-dng/history-reference/results.json)、[完整冻结交叉](../local-dng/history-reference/summary.json)、[独立数值审计](../local-dng/history_independent_audit.md)、[DNG4/8结果](../local-dng/relative-experiment-refinement04_08/results.json)、[DNG独立复核](../local-dng/dng_refinement_independent_audit.md)。源NPZ仅含模拟双像素数据，不含真实图片。

两份只读跨家族外审材料已准备；自动审批拒绝向外部Claude提交非公开研究资料，目前等待用户对该目的地和材料的明确授权。此次Claude审阅未启动，无模型响应、无接受凭据。既有同家族审阅仍provisional，gate继续BLOCKED。没有以新增CPU结果替代这两个审核凭据。

## Refined Proposal

选定的 Problem Anchor：固定目标、因果三预览、相同合法动作与预算，研究充分后端补偿后仍然可识别的曝光选择价值。主张与正式验证条件将落入 FINAL_PROPOSAL 和研究契约。

产物：
- [候选原始说明](../candidate_pool.md)
- [proposal](../refine-logs/FINAL_PROPOSAL.md)
- [experiment plan](../refine-logs/EXPERIMENT_PLAN.md)
- [tracker](../refine-logs/EXPERIMENT_TRACKER.md)
- [research contract](docs/research_contract.md)
- [原始结果](../pilots/pilot_results.json)
- [点式分辨率复核](../pilots-resolution/pilot_results.json)
- [共同后端局部分辨率复核](../pilots-shared-highres/shared_backend_results.json)
- [复现脚本](../pilot_mechanisms.py)

## Deferred and Stopped Claims

暂存候选 4/6/9/10，因为它们改变效用、动作集合或时序；不是宣布问题无价值。候选 5 不作主贡献。候选 3 不作“已有阳性”的独立 idea。停止现阶段的“joint 一定更优”“随机编辑 loss 是首次”“裁切面积即可定义真实信息损失”论断。

若强后端消除大部分策略差距，或局部规则在留出条件下等效，报告机制/负结果，停止复杂算法主张；若共同因果策略不能识别有用结构，不把 oracle 翻转当部署价值。

## Final Recommendation and Acceptance

研究题目建议：**固定目标下曝光选择收益：后端补偿与空间可预测性**。这是下一轮假设，不是已验证论文贡献。10候选已筛选，3个CPU机制probe及必要数值追检已运行，proposal/plan/tracker已形成。N0/N1受限版本已执行；H-aware及冻结后端交叉已完成；当前下一步是据阴性结果更新查新和外审，正式神经训练缺乏升级证据。

技能[idea-discovery](C:/Users/Lenovo/.agents/skills/idea-discovery/SKILL.md)要求最终确定性证据门，并明确“do not present the workflow as complete”；[运行时规则](C:/Users/Lenovo/.agents/skills/shared-references/codex-runtime.md)写明“Same-family review is provisional, not cross-family evidence.” 本轮配置的两次审阅实际均为OpenAI gpt-6-astra，与执行者同family；没有虚构其他模型接受。实际证据门结果见下方及.aris/runs状态。当前可审阅的研究产物已经备齐，验收仍为暂定。


步骤、当前状态与完成标准见[剩余步骤清单](../WORKFLOW_REMAINING_STEPS.md)。

<!-- ARIS_IDEA_DISCOVERY_EVIDENCE_GATE:START -->
## Evidence Gate
**Status:** BLOCKED

The workflow is not complete. Required stage evidence is missing:
- BLOCKED: novelty-check review provenance invalid (provisional review cannot advance this run)
- BLOCKED: research-review review provenance invalid (provisional review cannot advance this run)
<!-- ARIS_IDEA_DISCOVERY_EVIDENCE_GATE:END -->
