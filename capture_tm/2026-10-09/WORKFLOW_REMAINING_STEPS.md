# CaptureTM：剩余步骤与完成标准

更新：2026-10-09。研究状态 REVISE；idea-discovery Evidence Gate 为 BLOCKED；投稿贡献尚未确认。

## 一、报告中 workflow is not complete 的直接原因

实际 run_state 的其他三个阶段已 done，只有以下两个审核阶段是 provisional：

| 必补阶段 | 当前证据 | 完成标准 |
|---|---|---|
| novelty-check | 审阅者与执行者同属 OpenAI | 对最新主张及原始证据完成实际不同模型家族审阅，取得 PROCEED / PROCEED WITH CAUTION 明确裁决；记录真实模型身份、完整响应和可追溯 receipt |
| research-review | 审阅者与执行者同属 OpenAI | 独立检查最新协议、完整正负结果及技术提案，形成是否值得推进及最小决定实验的明确裁决；记录真实身份、响应和 receipt |

随后把审阅结论合入 canonical IDEA_REPORT.md，使用真实凭据更新 run_state 的 acceptance，再运行 idea_discovery_gate.py，只有实际 PASS 才能称 idea-discovery 流程完成。不能修改 provisional_advances 绕过。

技能依据：[idea-discovery/SKILL.md](C:/Users/Lenovo/.agents/skills/idea-discovery/SKILL.md) 要求 “Before presenting this report as complete, run the per-stage evidence gate”。[codex-runtime.md](C:/Users/Lenovo/.agents/skills/shared-references/codex-runtime.md) 明确写明 “Same-family review is provisional, not cross-family evidence.”

## 二、按证据依赖顺序推进的步骤

| 顺序 | 工作 | 当前实际状态 | 验收标准 |
|---|---|---|---|
| 1 | 完成 H-aware 后验与交叉检验 | 已完成，40项相关测试通过；3seed原始JSON/6份NPZ已生成，24个交叉单元和96条CI独立重算一致 | DONE：退出0、1102.163秒；全H关系规则恒4、收益0；N0亮度微小优、N1直接CI跨0。仅此已知双像素prior范围 |
| 2 | DNG 数值精度复核 | 已完成4/8复核，退出0、200.798秒；最大组级风险差1.077e-6，固定动作、24规则、288动作和收益符号不变 | DONE：保持输入/先验/种子一致；支持当前定性结果稳定，不宣称严格完全收敛或任意图像Bayes界 |
| 3 | 决定哪些投稿主张保留 | H-aware阴性结果已确认；当前停止复杂关系策略必要性主张，候选条件规律/评测发现仍未确认创新 | 用完整H-aware与DNG结果区分“后端遗漏信息”“已知先验规则”“可泛化剩余选择价值”；比较直接配对差、预先约定绝对收益标准，不因各自优于固定曝光就声称复杂特征必要 |
| 4 | 更新查新并补齐两次外审 | 旧审阅真实但同家族；新文献已核读；两份Claude只读外审材料准备完毕，自动审批拒绝外部资料提交，待用户明确授权 | 核对最近工作及经典最近邻；仅凭摘要的论文明确标记，逐条写可核验delta；评审独立读取原始代码、协议和全部正负结果，按第一节保留真实裁决凭据 |
| 5 | 更新研究契约、proposal、plan、tracker | 已补齐最新完整阴性结论、停止条件与状态，保留旧协议和历史结果；外审后再收敛最终投稿主张 | 用当前证据重写主张、限制、停止条件和最小下一实验；清楚区分已执行、运行中、待执行及条件触发实验 |
| 6 | 重跑门禁、归档与GitHub同步 | 既有代码已上传；最新H-aware与DNG4/8完整结果正在同步，gate仍有两项审核凭据缺口 | 实际gate PASS后同步MD/HTML和源校验、审核状态及可复现结果；代码上传指定工程分支，所有正负结论上传Idea；如裁决未通过，保留真实BLOCKED/REVISE原因 |

## 三、流程完成之后，怎样才算投稿证据足够

Gate PASS 表示 idea-discovery 证据记录完整，不等于投稿就绪。

若残余机制仍有稳定、超出简单解释的收益，再按最终claim补足充分后端/必要神经基线、独立场景或采集会话、空间依赖与先验变化留出以及相应消融。当前DNG来自同一采集会话，只有三个诊断背景组；处理过的Linear RAW内容相对模拟不能替代原生Bayer、真实多曝光重拍、标定或独立专家GT。只在投稿主张确实需要时要求相应数据。

若H-aware后端消除策略差距，或简单规则足够，就保留负结果，将贡献限定为条件规律、失效边界或评测发现；不为获得阳性改动原目标、动作和统计单位，也不强行增加网络。

目前优先级：授权后的两次实际跨家族外审 → 根据真实裁决确定投稿贡献/停止条件 → gate与最终同步。H-aware和DNG4/8已完成，不重复实验寻求阳性。
