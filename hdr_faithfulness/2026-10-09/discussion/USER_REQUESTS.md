# 用户请求与阶段转折

来源：本会话用户请求摘录和阶段整理；不是完整聊天/工具原始日志。日期：2026-10-08—09。

1. 提出有限观测下HDR/低照恢复的真实信息与合理幻觉边界，要求SCOUT→CONVERGE，先查已有工作，不进入网络方法设计。完整内容见[原始motivation](USER_MOTIVATION.md)。
2. 提供静态RAW、独立高SNR参考、等成本曝光配方及事实风险/coverage规则；提醒一般机制可从已有论文得到。见[原始Minimal Probe](USER_MINIMAL_PROBE.md)。
3. 明确调用idea-discovery，基于讨论发掘idea。结果是12候选，并收敛为A/#12、B/#1、C/#4。
4. 要求将最终候选分配给“OPPO张磊、加拿大Samsung Brown、xuetainfan、lichongyi、Jiawen Chen、Felix Heide”等独立agent讨论，并确认身份对应。六个角色以公开研究方向模拟，不冒称真实教授参与。结果见[独立评议](../expert-panel/EXPERT_PANEL.md)。
5. 调用experiment-bridge，对确定idea进行实验规划。选择A用于规划，B条件诊断、C共同控制；只规划，没有实现、推理、采集、训练或部署。见[计划](../refine-logs/EXPERIMENT_PLAN.md)。
6. 明确要求使用GitHub插件，将上述讨论资料与结论上传至baolinv0/Idea。本目录归档已有文本、历史、来源和当前结论；仓库已有CaptureTM资料作为独立记录保留。

## 本次收敛路径

宽泛观测量—保真—幻觉问题 → 文献优先 → method-level novelty search → 12候选 → A/B/C六视角讨论 → A冻结流程采集决策损失的规划。
长期“How much additional observation?”仍保留，但当前单成本点不提供最低预算，未证明临界收益。

## 被后续收紧的表达

- “保证保真”改为可测风险/coverage及有效置信边界。
- “自信错误”在无confidence信号时改为错误且一致/错误但清晰。
- “先验强度”改为现成操作实际语义，不默认纯先验变量。
- “恢复器影响曝光”已知；A要求具体实际选择损失。
- “严格同coverage”与5pp容差内可比区分。
- AI模拟意见、同家族独立上下文与真实教授/跨家族验收分开。
