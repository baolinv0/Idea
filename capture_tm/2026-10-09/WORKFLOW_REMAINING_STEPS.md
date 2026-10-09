# CaptureTM：剩余步骤与当前进度
更新：2026-10-09。代码和本轮全部正负结论已回传；研究仍REVISE，验收BLOCKED，未确认投稿贡献。

| Step | 当前实际状态 | 尚需完成 |
|---|---|---|
| N0连续参考 | 3seed、8192源×16重复、64–512积分已跑；数值稳定 | H-aware参考后端：把三张历史预览纳入后验，排除遗漏已知信息造成的收益 |
| N1依赖留出 | 保边际的反向copula留出已跑，规则冻结 | 在H-aware及更充分先验变化下确认；不称任意图像泛化 |
| DNG诊断 | 68个唯一DNG完整审计，6/2/3背景组；3seed相对实验已跑 | 每prior bin4/8积分refinement；更多独立场景/相机标定按贡献需要决定 |
| 后端与简单规则 | 反演、点后验、局部Wiener与全部4规则已比 | 当前家族受限；H-aware及必要充分神经后端仍未验；简单方法能解释就停止复杂主张 |
| 交叉评测 | 已保存3有限DNG后端冻结动作交叉矩阵 | H-aware/H-blind的2selectors×2renderers严格交叉矩阵 |
| 查新/批判审阅 | 既有同系列审阅与新代码审计均有真实记录 | 按最新claim重新核对文献，取得实际跨系列明确正判及可追溯身份 |
| 最终验收/同步 | 本轮代码、结果、负例、失败修复已同步 | 更新最终proposal/plan/tracker，记录有效接受后重跑gate，回传后续决定实验 |

下一步：H-aware后验 → DNG积分4/8 → 评估复杂方法必要性 → 更新查新与批判审阅 → 最终gate及GitHub同步。
不为得到阳性而改变目标、动作或统计单位。若简单方法充分或机制消失，保留负结果并调整贡献定位。

报告的“workflow is not complete”直接来自两项无效评审凭据。用户指定idea-discovery/SKILL.md要求实际review receipts和确定性gate；shared-references/codex-runtime.md明确写明“Same-family review is provisional, not cross-family evidence.”目前执行者与两位审阅者都属OpenAI，只能暂定。必须是真实不同系列模型的明确接受，不能修改provisional_advances绕过。

Gate PASS只表示idea-discovery证据完整，不等于投稿就绪。当前本地数据来自一个采集会话、三个诊断组，真实内容相对模拟不能替代真实多曝光重拍、Bayer或独立专家GT。
