# EXPERIMENT_TRACKER
开始2026-10-08，最终整理2026-10-09（Asia/Shanghai）。GPU实际0。
CPU墙钟：主运行10.54秒、点式2048复核10.99秒、共同32×128复核7.49秒、共同256×256复核14.63秒；合计约43.65秒，不含工具启动等待。
| ID | 实际状态 | 证据/范围 |
|---|---|---|
| P1 标量集合 | DONE_CPU_MECHANISM_ONLY | pilots、pilots-resolution；细δ对分箱敏感 |
| P2 分族空间先验 | DONE_CPU_LIMITED | 已知先验、原32×128局部可翻转；不是物理边界 |
| P2 共同双向32×128 | DONE_CPU_PRELIMINARY | pilots-shared；两族4/1，规则14.45%–14.90% |
| P2 共同双向256×256 | DONE_CPU_NEGATIVE_FOR_FAMILY_FLIP | pilots-shared-highres；两族均.5；规则9.07%–9.45%，平均绝对1.94e-5，不达δ1e-4必要替换标准 |
| P3 交叉点式后端 | DONE_CPU_NO_PARTNER_SIGNAL | 全部选择曝光1，不能证明神经迁移 |
| N0 连续/数值后验参考后端 | DONE_H_BLIND | 3seed/8192源×16重复/64–512节点；H-blind范围受限 |
| N1 留出实际空间依赖强度 | DONE_REVERSE_COPULA | 保边际反向依赖，固定prior与规则；不称未知图像泛化 |
| H0 完整H后验与2×2交叉 | DONE_NEGATIVE_FOR_RESIDUAL_NECESSITY | 3seed；H-aware关系规则恒4、收益0；1102.163秒 |
| D0 DNG每bin4/8积分复核 | DONE_STABLE_DECISIONS | 固定动作/24规则/288动作/收益符号不变；200.798秒 |
| E0 原库动作/目标/split冻结 | PLANNED | 原库协议未实际复现 |
| E2/E3 独立强后端/GPU | CONDITIONAL | 上述决定检验通过后 |
| E4 S24/实拍/标定 | DEFERRED | 没有真实HDR重捕获证据 |

原始结果全部保留。hindsight_min统计利用未来已实现噪声，禁止当latent/causal oracle或可实现regret。
恢复从N0开始，不为追求阳性重跑已完成的机制probe。

## Local diagnostic execution update 2026-10-09

N0/N1受限版本与本地DNG相对诊断已执行，详见[完整结论](../local-dng/CONCLUSIONS.md)。N0的连续风险稳定但参考后端未融合H；N0关系规则相对亮度规则的直接CI跨零。N1反向依赖留出已完成，仍为已知训练prior模型。下一决定实验改为H-aware后验及严格冻结后端交叉矩阵；DNG4/8积分 refinement待做。正式神经强后端、有效跨系列评审与最终gate尚未完成。原计划和历史结果保留，当前状态以新执行结论为准。

## Latest completed decision and next action 2026-10-09

本节覆盖前面的历史PLANNED/待执行描述，保留原Problem Anchor和旧对照。H-aware三种子及DNG4/8复核均已完成、退出0并独立数值审计。H-aware专属关系规则全部退化为固定4、收益0；亮度仅有微小N0收益且N1差异不确定。DNG精度改善，固定动作、全部规则、动作和收益符号保持稳定。

当前不升级复杂risk网络或GPU。最小下一行动是：对已完成完整正负证据进行最新查新和实际不同家族外审，决定是否有原创的条件规律/评测发现；若只是已有Bayes/恢复知识的演示，保留负结果并停止该算法主张。不能把普通后端交叉或“恢复影响曝光集合”当单独创新。

C1–C3仍未在未知完整图像和充分神经后端中验证。若外审提出一个明确、可核验的原创剩余问题，再冻结下一最小对照；若涉及原库动作/target或新任务，写独立protocol后推进。已有DNG只有一个采集会话和三个诊断组，不能当真实重拍证据。

两份具体外审dossier已准备。自动审批拒绝将非公开协议/代码/实验结果提交给Claude服务，当前等待用户明确授权；尚无Claude响应。跨家族接受凭据和Evidence Gate未完成。旧六小时AutoDL预算已结束，本轮无新增远程/GPU授权。

完整结论与逐源证据：[local-dng](../local-dng/CONCLUSIONS.md)；剩余步骤：[WORKFLOW_REMAINING_STEPS](../WORKFLOW_REMAINING_STEPS.md)。
