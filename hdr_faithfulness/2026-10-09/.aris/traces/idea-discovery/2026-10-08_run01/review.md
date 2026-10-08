# Fresh-session review folded notes
Configured reviewer: gpt-6-astra/ultra
Agent: /root/idea_pool_review
Status: same-family, provisional, no acceptance receipt

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
- [候选问题提案](../../../../refine-logs/FINAL_PROPOSAL.md)
- [文献先行判别路线](../../../../refine-logs/EXPERIMENT_PLAN.md)
- [未启动实验的状态记录](../../../../refine-logs/EXPERIMENT_TRACKER.md)
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

