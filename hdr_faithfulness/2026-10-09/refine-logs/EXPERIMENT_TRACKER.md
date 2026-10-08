# 实验任务表

日期：2026-10-09。范围：规划；0个实证任务已运行，无GPU任务、无训练。
状态说明：PLANNED=已规划；PARTIAL_READONLY=只读核查部分完成；CONDITIONAL=满足前置条件后才可执行；OPTIONAL=非核心。不是排队/部署状态。

| Run ID | Milestone | 目的 | 数据/系统 | 指标与交付 | 优先级 | 状态 | 前置条件/停止点 |
|---|---|---|---|---|---|---|---|
| R001 | M0 | 直接证据/新意残差 | AdaptiveAE等最近邻原文 | 同工作证据矩阵 | MUST | PARTIAL_READONLY | 已有直接覆盖则缩题 |
| R002 | M0 | 冻结输入与操作契约 | SUPIR-Q、RAW数据清单 | 合法输入、操作语义、权重/数据实际状态 | MUST | PARTIAL_READONLY | 已核官方代码，未下载/本地验证 |
| R003 | M1 | 最小官方接口sanity | 4 RGB×2设置×1seed | 开关生效、输出形状、时延/显存 | MUST | CONDITIONAL | 权重与CUDA环境就绪；拟8次推理 |
| R004 | M1 | 传感器/参考检查 | dark/flat、高SNR两参考 | 曝光、噪声、饱和、几何、参考独立 | MUST | CONDITIONAL | 设备/现成metadata可用；无数据不伪造 |
| R005 | M1 | baseline与三态标签sanity | F0/F1/F2、实体真值 | Q/W/Z守恒、ground truth来源、固定显示/读出 | MUST | CONDITIONAL | R003/R004通过；不运行训练sanity |
| R006 | M2 | 开发pilot | 24scene×24生成输出 | R/C/U、D方向、物理解释、盲评成本 | MUST | CONDITIONAL | 仿真仅筛查，no pilot yet |
| R007 | M2 | 冻结样本量/预算/规则 | 开发scene-level差异 | N、3pp阈值、统计方法和测试锁定记录 | MUST | PLANNED | 160起点/320建议上限不保证power |
| R008 | M3 | 校准选曝光/阈值 | 80独立scene | e_hat0/e_hat1、可比coverage | MUST | CONDITIONAL | 选择相同/coverage不足则不启动完整确认 |
| R009 | M4 | C1确认 | N独立test scene，F2四cell | Gamma、同时D0/D1、支持性达标集合 | MUST | CONDITIONAL | 不test-oracle，不追加到显著 |
| R010 | M4 | C2/C归因控制 | 相同输出F0/F1/F2、固定读出 | 输入适配、SNR/饱和与错误来源 | MUST | CONDITIONAL | 用全部有效primary scene，不挑有利图 |
| R011 | M5 | B停止回放 | 已有完整N=1/4/8序列 | 全策略risk/coverage/stop/cost | NICE | OPTIONAL | 缺完整序列/现实规则则仅诊断 |
| R012 | M5 | 额外验证范围 | 第二设备/多T/运动 | 边界与复现 | NICE | OPTIONAL | 核心成立后另立预算，不计本轮must |

核心五块E0–E4，对应10个must任务＋2个optional任务。实际必须推理次数由E0数据路线及E2锁定结果决定，不把一个任务行当一次推理。
首三项：R001→R002→（条件就绪后）R003。当前唯一已发生的是网页/文件只读核查和统计设计审查。
关联：[完整计划](EXPERIMENT_PLAN.md)
