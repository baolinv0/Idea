> 历史档案：2026-10-08首次查新报告。其UNVERIFIED/未找到助手及5.5分均为当时状态；后续七ID核验、空间probe与撤回，以[当前结论](../CONCLUSIONS.md)和[最新报告](../idea-stage/IDEA_REPORT.md)为准。不追溯修改历史正文。

# CaptureTM 新颖性核查报告
日期：2026-10-08（Asia/Shanghai）  
核查对象：`feature/capture-tm-c-20261005`  
固定提交：[7e080d3](https://github.com/baolinv0/modular_neural_isp/commit/7e080d373accd28150034b68718c27a21f932a09)  
核查类型：论文选题与方法查新；本次未修改远端仓库、启动训练或访问正式测试图像。

## 结论
**PROCEED WITH CAUTION，暂评 5.5/10。可以继续做有明确停止条件的小实验；目前不能把现有实现包装为已成立的新算法。**

“曝光选择由最终图像质量驱动”“曝光与后处理联合训练”“噪声、饱和、可靠性需要显式考虑”均已有直接先例。尚值得验证的差异，是在共同外观目标下，用公平且足够强的对照，量化物理采集改善与影调拟合的关系，并定位联合优化真正有额外价值的条件。本轮未找到已经给出这一**完整具体结果**的论文，也没有足够依据判定应放弃。检索未命中不等于证明首次。

谨慎的具体原因：强 TM、顺序优化和简单保护尚未对比；新的边界或机制尚未实测；泛泛的“联合有时不如顺序”“后处理不能恢复丢失信息”已有人讨论。

## 方法与证据状态
[研究骨架](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/research/ae_tm/RESEARCH.md)提出：策略根据可用历史观测，从合法物理曝光动作中选取采集方案；TM 将采集结果映射到所有候选共享的固定外观目标。研究允许发现联合没有必要，并要求强 TM、顺序优化和简单曝光保护作为挑战基线。

现有实现是三帧历史预览与实际曝光参数输入的轻量策略、独立模拟/渲染的有限候选期望优化，以及冻结上游系数网络上的小 TM 适配器。**精确枚举分类期望不是对真实传感器反传，也不是 AdaptiveAE 的 RL 复现。**该组合是可执行研究基础，尚未显示算法级独特性。[策略代码](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/capture_tm/learned_policy.py#L160)

历史目标为解析固定外观；当前训练目标已包含权重 0.02 的 `missing` 可靠性代理。因此不能把“新增一个missing损失”说成尚未实现的首次贡献，也不能凭旧结果直接断言纯外观损失已造成失败。[现有目标](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/capture_tm/joint_objective.py#L10)

三项直接影响论文主张的限制：

- TM 的 207,224 个上游系数网络参数冻结，仅训练 **2,663 参数适配器**，尚不能代表充分训练的强 TM。[适配器](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/capture_tm/learned_tone.py#L29)
- 历史 HDR 规则策略只访问固定包围子集，学习策略访问完整 24 计划；训练步数相同也不等于候选渲染量相同。新计划承诺公平协议，不能回溯赋予旧结果。[历史结果审查](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/docs/capture_tm/JOINT_RESULTS_REVIEW.md#L48)
- 历史审查未建立联合优于只训练 TM；最新 R1 是软件与合成 smoke，真实 S24 配对、颜色、目标、mask验收及训练仍未完成。[R1报告](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/research/ae_tm/reports/R1/autodl-smoke-20261007/reply.md#L24)

代码已有可选 Bayer/rolling-shutter 模拟路径，但它仍是工程模拟，不能称实测手机标定或真实 Bayer 画质证据。[采集代码](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/capture_tm/acquisition.py#L251)

## 四个核心主张
| 主张 | 最接近的工作 | 已知部分 | 仍值得验证的具体差异 |
|---|---|---|---|
| C1：合法物理曝光与渲染面向共同终端目标联合优化 | EBSNet/MEFNet；Neural AE；AdaptiveAE；DEBIR | 曝光决策由后端反馈训练、与后端协同已有先例 | 单帧/静态场景、共同外观目标下的具体机制；仅改变后端名字或期望梯度估计器不够 |
| C2：采集曝光与渲染意图解耦，并保护不可靠信息 | Modular ISP；DRIFT；ExpoCM；RawHDRV | 数字增益、影调、曝光掩码与可靠性损失均有邻近工作 | 新条件或约束必须解决已定位的失败，并优于简单饱和保护；当前尚无明确新机制 |
| C3：终端外观损失可能掩盖有害采集损失 | Personalized AE；Neural AE；DEBIR | 不可逆损失与后处理局限已知；分阶段可优于端到端已有实验 | 稳健的量化边界、可观测判据，排除容量/目标域/训练失败；不能只展示一个饱和例子 |
| C4：公平对照揭示联合何时必要、何时可被替代 | DEBIR；RAW/RGB Restoration benchmark | 阶段训练与目标管线适配会影响结论已有证据 | 针对**物理 AE与外观 TM**的因果比较、跨噪声/动态范围规律及真实采集复核 |

C1、C2当前主要是已有机制的研究组合；C3、C4的潜力属于**尚待发现的实验结论**。四组消融、增加损失、换数据集和联合优于冻结基线，都不能独自承担这一差异。

## 最近邻论文
核验说明：已打开以下一手页面，核心论文进一步读取摘要、相关工作和方法/实验。安装环境未找到技能要求的 `verify_papers.py`，故按 D1 给每条保留 **[UNVERIFIED]**，表示辅助脚本核验未完成；不表示这些已打开的作者原文不存在。预印本与正式会议信息分别注明。

| 论文 | 年份/来源 | 与本方案的重合 | 尚未被该文直接给出的部分 |
|---|---|---|---|
| [UNVERIFIED] [Personalized Exposure Control Using Adaptive Metering and Reinforcement Learning](https://arxiv.org/html/1803.02269v3) | 2018，作者预印本 | 实时物理曝光、语义与偏好；相关工作明确讨论采集信息丢失后无法靠后处理恢复 | 不提供强 TM/顺序/联合公平比较中的定量失配边界 |
| [UNVERIFIED] [Learning a Reinforced Agent for Flexible Exposure Bracketing Selection](https://arxiv.org/html/2005.12536v1) | CVPR 2020 | 从预览选有限包围动作；EBSNet和MEFNet由最终质量反馈迭代联合训练；先预训练后交替 | 后端是融合而非本方案单帧 TM；没有因此自动覆盖本方案待验证诊断 |
| [UNVERIFIED] [Neural Auto-Exposure for High-Dynamic Range Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.pdf) | CVPR 2021 | 模拟采集、AE、可微 ISP和下游网络端到端协同 | 优化检测目标，非固定专家外观；不构成本方案完整结果的复现 |
| [UNVERIFIED] [AdaptiveAE](https://arxiv.org/html/2508.13503v1) | ICCV 2025 | 快门/ISO策略、运动/噪声模拟、用户时间预算、HDR质量反馈 | 本方案要辨认采集收益与可学习影调的关系；需实验证明这一差异 |
| [UNVERIFIED] [Dynamic Exposure Burst Image Restoration（DEBIR）](https://arxiv.org/html/2603.21784v1) | 2026；CVPR2026程序列出该题 | 可微 burst 模拟、曝光预测、后端训练；§6.3/Table5已比较并发现分阶段优于E2E | 目标是低照度 clean RAW restoration；未等同于固定外观与采集保真的完整诊断 |
| [UNVERIFIED] [Modular Neural Image Signal Processing](https://arxiv.org/html/2512.08564v3) | 2025预印本，2026-03修订 | photofinishing 内 digital gain/GTM/LTM/chroma/gamma联合学习、样式渲染 | 是上游复用骨干；数字曝光调整不同于决定下一次快门/ISO |
| [UNVERIFIED] [DRIFT: Deep Restoration, ISP Fusion, and Tone-mapping](https://arxiv.org/html/2604.03402v1) | 2026-04-03预印本 | 恢复与可调影调形成统一管线、参考影调一致性 | 统一系统不等于物理曝光策略联合训练；不能按标题推断其已有本方案 |
| [UNVERIFIED] [Exposure Bracketing Is All You Need For A High-Quality Image](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ede6851dbcde82ed40d794b5b9958e9b-Abstract-Conference.html) | ICLR 2025 | 包围图像的恢复/HDR/增强、合成预训练和真实适配 | 不直接学习本方案的因果物理曝光策略；多帧外推时需考虑的强邻居 |
| [UNVERIFIED] [Benchmarking RAW and RGB Restoration in Image Signal Processors](https://arxiv.org/html/2609.02831v1) | 2026-09-02预印本 | 控制固定ISP，分离恢复位置与目标ISP训练适配，揭示对照混杂 | 不学习物理AE或联合更新ISP；它覆盖方法论相邻问题，不是本研究的否决依据 |
| [UNVERIFIED] [ExpoCM](https://arxiv.org/html/2605.02464v1) | 2026-05-04预印本，作者注CVPR2026 | 曝光掩码、亮度/色度加权损失、饱和/暗部差异 | 采集后的生成式HDR恢复；生成细节不同于新增实测信息 |
| [UNVERIFIED] [RawHDRV](https://arxiv.org/html/2609.27274v1) | 2026-09-23预印本 | Bayer通道与饱和/噪声特性、可靠区域掩码、加权融合与颜色损失 | 单曝光RAW视频恢复；所读内容没有本方案的物理曝光策略 |

最重要的反例是 **EBSNet 的联合机制**和 **DEBIR 已有分阶段优于端到端的发现**。它们要求收紧叙事，而非自动否定新实验结论。建议投稿前优先核对/适配这两类基线，不把 AdaptiveAE作为唯一邻居。

其他已筛查线索：

- [POS-ISP](https://arxiv.org/html/2604.06938v1)：ISP模块顺序/参数与终端奖励；其“exposure control”需按实际后处理机制比较，不能与物理重采集混称。
- [JOCA](https://arxiv.org/html/2512.06763v1)：硬件、自适应控制和下游任务协同。支持“共同设计”概念早已有先例，不证明本方案的具体发现已被做过。
- [HDRAgent](https://arxiv.org/abs/2606.09110)、[DOME-HDR](https://arxiv.org/abs/2608.05626)：对已获得的多曝光输入做重建调度/SDR–HDR生成；本轮摘要筛查没有显示直接复现目标物理 AE–TM研究。
- [Mono4DGS-HDR，ICLR2026](https://proceedings.iclr.cc/paper_files/paper/2026/hash/f539e9461f89a12caea30645605eef51-Abstract-Conference.html)与 [NExF，NeurIPS2025](https://papers.nips.cc/paper_files/paper/2025/hash/c55e6792923cc16fd6ed5c3f672420a5-Abstract-Conference.html)：动态/多视角表示和曝光补偿，区别于选择下一次真实采集动作。
- Digital Gimbal、RealCamNet、Bricker to BRACE、Pixel-wise Exposure、Lights Camera Attack为发现层线索，未用其不完整信息判定重合或否决。

## 数据集本身能否支撑创新
[S24 官方说明](https://github.com/SamsungLabs/time-aware-awb/blob/main/s24-raw-srgb-dataset/README.md)把 raw_images 定义为去马赛克、黑电平归一化的三通道 PNG16；去噪版来自 Lightroom AI，style-0是人工渲染。它能支持静态外观代理实验，不能单独提供无裁切HDR辐射真值、时间序列或相机实际换曝光后的信息增益。

使用S24、样式GT或其采集元数据本身不是新贡献。应先完成输入/目标/几何/颜色/mask验收，保留原作者split并按 source family划分衍生样本。用于部署AE的噪声统计不能依赖去噪参考。真实曝光与高光论断还需要干净辐射源/实际RAW曝光包支持。

## 建议定位
**待验证的一句话差异：在相同物理动作、拍摄预算、外观目标与公开计算成本下，量化终端外观拟合与采集保真的失配，并验证哪些动态范围与噪声条件使强 TM或顺序优化无法替代 AE–TM协同。**

避免声称“首次端到端曝光与影调”“联合必然更好”或“新增missing/saturation loss就是创新”。如果最终只有“分阶段更稳定”或“保护饱和更好”，差异仍不足；应明确它相对 DEBIR/已有曝光保护多解释了什么。若强TM或简单保护已足够，这可以指导缩题，但不会自动成为代表作。

## 最小决定性证据

1. **可信采集与共同目标**：解析机制实验与S24外观实验分开；真实曝光验证另立证据层。所有候选使用同一目标/区域，初期可按新协议固定增益只变快门，保留旧协议。
2. **挑战可替代方案**：充分训练的强TM、先优化采集再优化TM、朴素联合加简单保护，使用共同候选动作/捕获时序与相同TM容量。分别报告更新数、候选渲染量、实际耗时，不把等步数叫等算力。
3. **失配需有独立价值判据**：提前定义相机/原始域有效信息或实际细节保真，区别于当前策略奖励和missing代理；独立共同后端/样式迁移可帮助判断收益来自采集还是渲染。若目标外观本来就允许压掉某些信息，信息保留惩罚改变的是任务效用，不能循环证明原目标“错误”。
4. **给出条件与消融**：按动态范围、噪声、新增裁切、TM容量、训练资源分层；再检验最小约束能否优于简单保护。控制原始域、补偿和对齐错误，防止把工程故障叫新现象。
5. **场景级稳健性**：多seed和按独立源场景配对统计；如果出现规律，再用实际相机曝光验证。大量crop不视为大量独立证据。

这是查新后的研究建议，尚未执行新实验；不替代仓库R2/G3阶段门槛。

## 检索与审查状态

- 检索跨 web 与 alphaXiv 两次发现查询；四个主张分别使用至少三种关键词表述，覆盖基础工作、2024–2026及最近六个月（2026-04-08至2026-10-08）。
- 查看/定向搜索最新可用 ICLR2026、ICML2026（PMLR306）与NeurIPS2025官方来源。ICML整册抓取因页面过大失败，采用定向检索；部分CVF页面403，使用作者arXiv全文。未逐篇穷尽整届会议，未声称直接读取完整Scholar/Semantic Scholar数据库。
- 引用辅助脚本：`verify_papers.py`未找到，D1降级；已读一手来源不等于该脚本已运行。
- 外部审查：Codex MCP精确工具缺失；已完成新鲜上下文同模型系列子代理复核，审查者读取完整dossier并打开四项核心一手来源。**同系列复核只能暂定，不能称跨模型独立验证。**
- `review_status: completed_same_family`；`acceptance_status: provisional`。本轮完成查新早期评估，不等同于论文贡献验收。

## 新鲜上下文审查与最终决定
复核评分 **5.5/10，PROCEED WITH CAUTION**，同意整体研究问题值得pilot，并认为C4的收益边界最有希望。复核重点挑战了：

- EBSNet已经涵盖预训练、最佳候选监督、有限动作和后端联合；只换训练梯度估计器不够。
- DEBIR已提供分阶段优于端到端的具体实验；必须揭示更有解释力的条件规律。
- 独立采集保真需要提前定义，不能用训练missing项循环定义成功。

最终定位仍是待验证实验贡献。建议明确选择：

1. 固定外观任务：约束改善同一留出目标或预先规定的扰动鲁棒性；
2. 外观–采集保真双目标：外观保持在预定容差内，提高独立保真并报告Pareto权衡。

需要提前规定实际收益阈值与“可替代”的等效容差；普通差异检验不显著，不能直接证明等效。离线全候选oracle仅作诊断上界，部署成绩必须来自因果观测。

**决定：继续做最小机制pilot，不冻结“联合更好”的论文叙事。** 不存在已指认论文包含完整拟研究结果，故不建议ABANDON；也未获得已成立的新方法或新规律，故保持暂定结论。

