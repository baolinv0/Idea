# 用户原始 Motivation

来源：本会话用户提供内容，保留论述，Markdown空白及公式排版作规范化。属于最初问题定义，不是已验证科学结论。
后续对UltraLED/UltraFusion机制、最低预算、先验变量与风险保证的收窄见[当前结论](../CONCLUSIONS.md)。

motivation：**在有限观测信息下，单帧恢复、多帧采集和生成先验各自能把 HDR/低照图像恢复到什么程度，以及“真实信息”和“合理幻觉”的边界在哪里。**

## 给导师的1分钟版本

### Motivation：有限观测下HDR图像恢复的真实信息上限

手机HDR / 夜景成像正在出现一个明显的技术分叉：

**一条路线是增加真实观测**——通过多曝光、多帧burst获取更多光子和不同曝光的信息，再进行融合；

**另一条路线是减少真实采集、增加模型先验**——例如只利用一张短曝光RAW，通过去噪、提亮甚至生成式恢复，推断暗部和高动态范围细节。

问题在于，目前很多方法主要比较“最终图像看起来是否更好”，但没有充分回答一个更基础的问题：

> 当原始短曝光图像本身缺少足够的光子和动态范围信息时，算法恢复出来的细节究竟有多少是真实观测支持的，又有多少是模型先验生成的？

这会形成三个不同的能力上限：

1. **单帧非生成恢复**
   - 受单次曝光获得的光子数、读噪和传感器动态范围约束。
   - 可以通过去噪和图像先验改善观感，但无法真正增加已经丢失的物理观测信息。
   - 极暗区域容易出现“干净但缺少真实纹理”的结果。
2. **单帧生成式恢复**
   - 可以利用更强的自然图像先验，产生比传统去噪更丰富、更自然的纹理。
   - 但当观测证据不足时，模型可能生成“合理但错误”的结构，即hallucination。
   - 因此它可能提高perceptual quality，却不一定提高physical fidelity。
3. **多帧 / 多曝光融合**
   - 通过增加真实观测获得更多光子、不同曝光区间以及潜在的亚像素互补信息。
   - 理论上可以降低真实信息的不确定性，因此具有单帧模型无法替代的优势。
   - 但代价是运动、配准、鬼影、功耗、时延和系统复杂度。

因此，我真正想研究的不是“生成模型是否比传统HDR好”，而是：

> 观测信息量与恢复保真度之间究竟存在什么关系？增加多少真实观测信息后，生成先验带来的收益从“幻觉”逐渐变成“可信恢复”？

最终希望建立一条 **Observation Budget → Reconstruction Fidelity → Perceptual Quality** 的关系。

例如控制：
- 1 / 2 / 4 / 8 / 16帧；
- 不同曝光组合；
- 不同暗部SNR；
- 静态到运动场景；

然后同时评价：
- 传统重建误差；
- 感知质量；
- 局部真实纹理恢复率；
- hallucination rate；
- confidence / uncertainty calibration。

这样可以回答一个目前对手机HDR很实际的问题：

> 什么时候应该增加真实曝光/多帧采集，什么时候应该交给单帧恢复模型，什么时候才适合使用生成先验？

这可能比单纯提出一个新的HDR网络更具有系统意义。

## 如果导师继续追问“你的创新点在哪里？”

现在**不要急着回答“我要设计一个什么网络”**。先把科学问题压缩成：

> 现有HDR恢复缺少一个“观测证据—恢复保真度—生成幻觉”的统一分析框架。

最关键的未知量是：

**How much additional observation is needed for faithful reconstruction?**

也就是你刚才问的：

**“到底提高多少可参考信息，才能保证生成结果是保真的？”**

这里“保证”最好换成 **达到某个可测的错误概率/保真阈值**，否则很容易变成不可证伪的问题。

例如定义：

P(hallucination | N, SNR, ΔE, motion) < ε

研究：

N, SNR, ΔE → faithfulness / hallucination

这就从一个“想做生成HDR”的工程想法，变成了一个**可以做实验、可以证伪的研究问题**。

## 和前面讨论的V1 / UltraLED / UltraFusion怎么串起来

可以用这一条线讲：

**vivo V1类实时短曝光增强**

→ 证明**不增加真实曝光也可以显著改善视觉效果**

→ **UltraLED**

→ 进一步说明**单张短曝光RAW＋强先验可以恢复非常高动态范围的视觉结果**

→ 但问题是：

> 这些恢复出来的细节有多少来自观测，有多少来自先验？

→ **UltraFusion / 多曝光HDR**

→ 提供另一种答案：

> 与其让模型猜，不如增加真实观测。

→ 所以真正值得研究的是：

**Single-frame prior ↔ Additional physical observations**

而不是简单的：

**CNN vs Diffusion vs HDR**

这也是我认为这个motivation目前最值得和导师讨论的版本。

**当前阶段不要进入方法设计。** 按Research Playbook，这仍然属于 **SCOUT → CONVERGE 的问题定义阶段**；需要先证明这个“观测量—保真度—幻觉”的现象确实存在，而且现有工作没有已经回答它。

## PROJECT_RESEARCH_PLAYBOOK

Current stage: SCOUT → CONVERGE
Current bottleneck: 尚未证明“额外真实观测对生成恢复保真度存在可量化的临界收益”。
Current question: **How much additional observation is needed for faithful HDR reconstruction?**
Evidence gained: 已形成单帧非生成 / 单帧生成 / 多帧融合的机制区分。
Unresolved risk: 这个问题可能已有工作系统研究，需要做method-level novelty search。
Decision recommendation: **先和导师讨论问题，不承诺生成模型方案。**
Next single action: 检索并建立“observation budget / hallucination / faithful restoration / multi-frame RAW”最接近工作的lineage。
Exit condition: 找到明确frontier residual，并设计一个能区分H1/H0的最小probe。
Repository artifact to update: 01_RESEARCH_STATE.md的Problem Anchor / Current Question / Frontier Residual。
