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
| N0 连续/数值后验参考后端 | PLANNED_FIRST | 先排除残余分箱/稀疏估计；未执行 |
| N1 留出实际空间依赖强度 | PLANNED_SECOND | 固定规则与目标；不能只改变混合比例 |
| E0 原库动作/目标/split冻结 | PLANNED | 原库协议未实际复现 |
| E2/E3 独立强后端/GPU | CONDITIONAL | 上述决定检验通过后 |
| E4 S24/实拍/标定 | DEFERRED | 没有真实HDR重捕获证据 |

原始结果全部保留。hindsight_min统计利用未来已实现噪声，禁止当latent/causal oracle或可实现regret。
恢复从N0开始，不为追求阳性重跑已完成的机制probe。
