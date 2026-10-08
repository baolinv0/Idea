# 主要参考来源与用途

这些是讨论中访问/引用的一手来源；完整逐篇判断见文献与评议报告。部分近邻由共同材料供给，并非每位agent独立阅读全文。资料截至本次2026-10-08—09讨论，未声称穷尽覆盖。

| 主题 | 来源 | 在讨论中的作用 |
|---|---|---|
| 等成本HDR采集 | [Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/) | 曝光/照片数与噪声优化已知 |
| 手机RAW burst | [HDR+论文](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/)、[数据说明](https://storage.googleapis.com/hdrplusdata/README.html) | 真实burst与输入metadata，不自动满足本次配方 |
| 曝光依赖恢复器 | [AdaptiveAE](https://arxiv.org/html/2508.13503v1) | A宽泛关系的直接最近邻 |
| RAW HDR | [RawHDR](https://arxiv.org/html/2309.02020v1)、[官方数据/代码](https://github.com/yunhao-zou/RawHDR) | RAW与HDR目标/数据范围 |
| 单RAW增强 | [UltraLED](https://arxiv.org/html/2510.07741v1) | 单RAW两阶段U-Net，不能误称diffusion |
| 双曝光生成融合 | [UltraFusion](https://arxiv.org/html/2501.11515v1)、[官方库](https://github.com/OpenImagingLab/UltraFusion) | 真实曝光与先验混合；合法接口约束 |
| burst生成恢复 | [BurstGP](https://arxiv.org/html/2604.23508v1) | 分支输入不能误作真实采集数对照 |
| RAW多曝光 | [LuckyHDR](https://arxiv.org/html/2604.19976v1) | 物理采集、模糊与融合解释 |
| 先验/数据保真 | [BIGPrior](https://arxiv.org/abs/2011.01406) | 宽泛先验保真区分已知 |
| 低光子预算 | [One Photon](https://arxiv.org/html/2610.02675v1) | 预算、样本、任务与reader收益威胁 |
| 一致但错误 | [HalluGen](https://arxiv.org/html/2512.03345v1) | measurement consistency不等真值 |
| 共识与共享错 | [SceneFaith](https://arxiv.org/html/2609.34781v1) | 跨模型共识不等跨seed信号 |
| 读出与恢复 | [ClearText-Video](https://arxiv.org/html/2608.28784v1)、[TeReDiff](https://openreview.net/pdf?id=jt2c2H6auR) | 恢复/任务评价与错误归因 |
| 计算摄影/识别 | [Bridging the Gap](https://arxiv.org/abs/1901.09482) | 输入适配/视觉与识别差异 |
| 风险控制恢复 | [K-RCPS](https://proceedings.mlr.press/v202/teneggi23a.html) | 风险控制不自动等事实保证 |
| 主动测量 | [AdaSense](https://arxiv.org/html/2407.08256v1)、[GPARA](https://arxiv.org/html/2609.34172v1) | 泛泛不确定性补测已近 |
| 保真/语义操作 | [PiSA-SR](https://arxiv.org/abs/2412.03017) | 设置实际含义与A可比性 |
| 确定性路径 | [OSEDiff](https://arxiv.org/pdf/2406.08177v2) | B不能覆盖所有生成器 |
| RAW处理链 | [Unprocessing](https://arxiv.org/html/1811.11127v1) | 增益/颜色/噪声与处理链控制 |
| 非生成可学习 | [Classic Video Denoising](https://arxiv.org/html/2504.03136v1) | 非生成不等于无学习 |
| 当前拟用恢复器 | [SUPIR论文](https://arxiv.org/html/2401.13627v2)、[官方库](https://github.com/Fanghua-Yu/SUPIR) | 冻结RGB恢复的合法control操作 |
| 序贯统计 | [Confidence sequences](https://arxiv.org/abs/1810.08240)、[CAP](https://arxiv.org/abs/2403.07728) | 重复检查/选择后校准是成熟问题 |
| 精确错误率界 | [R官方binom.test说明](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/binom.test.html) | 二项式区间前提与保守认证 |

研究者身份与角色依据见[六视角报告](expert-panel/EXPERT_PANEL.md)。V1等产品叙述保留在用户原始动机中，本归档未将它们升级为已验证的科学证据。
