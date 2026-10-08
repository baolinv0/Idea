# FINAL_PROPOSAL — 候选问题提案
Date: 2026-10-08
Stage: SCOUT → CONVERGE
Status: PROVISIONAL；无pilot；问题级提案，尚未进入方法设计。
Canonical discussion: idea-stage/IDEA_REPORT.md

## Problem Anchor
在静态Bayer RAW HDR/低照成像中，检查冻结恢复流程及其现成操作设置是否改变等采集成本曝光配置的局部事实风险和可读性排序。研究对象是采集决策，不是另一个HDR网络或跨方法榜单。

## Current Question
Does changing an existing generative-restoration setting change which equal-cost exposure schedule meets a local factual-risk and readability target?

“How much additional observation”保留为长期问题。当前单成本点不能给最低预算，也不预设临界点存在。

## Scientific Claim（待检验）
在部分明确工作区间内，物理质量更优的配置未必最容易满足局部事实目标；某个可操作的现成生成设置会改变配置排序/目标可达性，并产生有实际意义的采集决策差异。
正结果必须超出统计交互显著：呈现不同采集选择及其事实风险/可读性后果。
负结果同样有用：在声明范围内，采集选择可继续由非生成路径和已知物理指标指导。

## H1 / H0
H1：同一传感器、同成本、同模型的现成设置改变时，测试配置集合中的风险—覆盖率排序或达标集合可复现改变。
H0：排序/达标集合保持稳定，或所谓改变只是噪声、读出/显示变化、非法输入、已知SNR/饱和/配准劣化及评价偏差；先验设置只改变观感而不改变所需采集选择。
未检出≠证实H0；需后续预设可检测效应和误差范围。

## Operational Definition
将局部目标分为正确可读、错误但清晰、擦除/不可判定。令A为可读输出，报告
R(e,s)=P(错误事实 | A,e,s)，Coverage(e,s)=P(A | e,s)，
同时给出无条件错误但清晰率、正确可读率、擦除率。
e是曝光配置，s是现成恢复操作；s可能同时改变数据保真和先验依赖，不称纯先验强度。
达标集合限于所测试配置：R≤预定ε，Coverage≥预定c。阈值由任务定义，不凭当前文献数值替代。
没有模型置信信号时，只称稳定错误，不称自信错误。
清晰度和事实真值分别判定；OCR只作读出，不能把OCR输出作为ground truth。

## Nearest Prior and Frontier Residual
[Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/)已做等成本曝光物理优化；[AdaptiveAE](https://arxiv.org/html/2508.13503v1)已做预算感知曝光与下游重建；[BurstGP](https://arxiv.org/html/2604.23508v1)已改变生成条件/强度；[One Photon](https://arxiv.org/html/2610.02675v1)已研究SPAD观测预算与任务。
本轮尚未找到将等成本Bayer曝光、同冻结模型现成操作、局部事实风险和覆盖率放在同一受控对照中并证明采集选择改变的证据。
这不是“已经证明不存在”；必须沿最近邻补充材料与引用继续检查。

## Minimum Convincing Evidence
1. 论文或后续数据的真实输入、成本、模型接口与操作可比较；光子数/局部SNR/饱和率有解释基线。
2. 相同场景及任务上的局部三态结果与不确定范围；条件错误率和覆盖率完整，不靠擦除取得低风险。
3. 观察到不同配置选择/达标集合，以及错误选择带来的可读性或风险损失；不只一张失败图或一个p值。
4. 排除读出适配不足、展示处理、强度语义混淆及多seed伪独立。保留合法失败和负结果。
5. 若确认物理试验有必要，独立高SNR非生成参考、独立采集重复、场景级验证。

## Feasibility Gate Before Any Experiment
先确认现成冻结模型可以合法处理所比较的输入，且有操作含义明确的设置。若模型不支持变长/曝光组合，不能临时训练组件或违反接口制造效应。
先确认已有公开数据含足够曝光和传感器噪声信息；否则不能称物理预算研究。
代码/权重/数据可用性尚未全面确认；没有GPU小时或样本量估计。

## Current Decision
优先文献核查这条主线；稳定性停止采集候选为独立备选，decoder预算归因候选为低成本诊断入口。三个问题暂不合成复杂方案。
Next single action: 对最近邻的同预算、同模型曝光/强度消融填写一张直接证据矩阵，判定是否已有配置排序/达标证据。不是运行网络。
