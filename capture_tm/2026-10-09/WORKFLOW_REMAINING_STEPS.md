## 2026-10-13 更新：本次精炼完成，科学路线需重提机制

research-refine实际完成5/5轮，最终6.85/10、RETHINK（当前toy与算法贡献路线）；方法诊断闭合、停止当前toy阳性实验、复杂AE升级暂停。原问题保留。
新toy已由解析置换不变性判为零值对照，无待补MC。H-aware、DNG4/8和完整历史信息控制早已完成，继续作为正负证据，不重复执行。新机制卡和原创delta缺失，不进入网络训练或run-experiment。
本次同属OpenAI的native方法审核不替代下述跨家族验收，旧BLOCKED状态不变；未新提交外部Claude。技能循环completed不代表投稿READY或gate PASS。
[最终提案](refine-logs/FINAL_PROPOSAL.md) · [真实五轮意见](research-refine/2026-10-13/refine-logs/REFINEMENT_REPORT.md)。

以下为此前跨家族流程的历史剩余步骤，最新科学方向以上述停止决定为准。

# CaptureTM：剩余步骤与完成标准

更新：2026-10-09。研究状态REVISE；Evidence Gate仍BLOCKED；投稿贡献尚未确认。

## workflow is not complete 的直接原因

run_state其他三个阶段为done，novelty-check与research-review为provisional：实际旧审核者与执行者同属OpenAI，尚无有效不同模型家族接受凭据。HTML不是渲染故障；不能修改provisional_advances来消除提示。

技能[idea-discovery/SKILL.md](C:/Users/Lenovo/.agents/skills/idea-discovery/SKILL.md)要求“Before presenting this report as complete, run the per-stage evidence gate”；[codex-runtime.md](C:/Users/Lenovo/.agents/skills/shared-references/codex-runtime.md)写明“Same-family review is provisional, not cross-family evidence.”

## 已完成，毋须重复

| 步骤 | 完成证据 | 当前解释 |
|---|---|---|
| H-aware双像素后验及2×2交叉 | 3seed，退出0、1102.163秒；24单元/96CI独立重算 | H-aware关系规则恒4、收益0；只限已知prior双像素 |
| DNG积分4/8数值复核 | 3seed，退出0、200.798秒；固定/24规则/288动作/符号稳定 | 当前定性结果稳定；不是严格绝对误差界 |
| DNG历史信息4×4经典控制 | 3seed，退出0、203.385秒；53测试，1152行/96单元/768CI | iPhone固定；S25简单梯度局部正结果、CI包含0；近似WLS/三个诊断组 |
| 正负证据及代码整理 | 新代码已发布ae7c762；完整原始JSON/CSV、协议、审计均在本归档 | 归档完整不代表科学主张已验证 |

## 必补步骤，按依赖顺序

| 顺序 | 需要做什么 | 完成标准 | 当前状态 |
|---|---|---|---|
| 1 | 实际跨家族novelty-check | 审阅最新方法、全部正负原始证据和近邻全文；形成PROCEED/PROCEED WITH CAUTION裁决及一条可核验delta，保留实际模型身份、完整响应、durable trace；ABANDON须指出具体已包含结果的已发表论文 | 最新dossier已备齐；Claude外部提交待用户明确授权，未启动 |
| 2 | 实际跨家族research-review | 独立读取协议/代码/全部结果，判断是否推进和最小决定实验；保留真实身份/响应/裁决。明确proceed才可接受；风险清单本身不是负裁决 | 同上；本地代码/数值审计不替代它 |
| 3 | 据两次真实裁决收敛主张 | 更新canonical IDEA_REPORT、proposal、plan、tracker、contract；区分已证、条件主张和未证。若只解释为已知原理，停止该主张；若没有幸存idea，保留BLOCKED并重新选/审核，不伪造正裁决 | C1–C3未确认；复杂关系网络暂无升级证据 |
| 4 | 录入真实接受并重跑门禁 | 仅在实际正裁决、identity和trace齐备时run_state accept；idea_discovery_gate实际退出0/PASS，再同步MD/HTML源校验、最新审核记录、manifest/checksums与GitHub | 当前两审核provisional，gate BLOCKED |

## 流程完成之后，怎样才算投稿证据足够

Gate PASS表示idea-discovery证据记录完整，不等于投稿就绪。若审核保留了一个明确、可核验的原创贡献，再补它真正需要的实验：充分后端/必要强基线、独立场景或采集会话、预先冻结的留出与直接配对检验、与claim相应的消融。若claim涉及真实相机/HDR，则需真实重拍、标定及适合GT；现有processed Linear RAW相对模拟不能代替这些证据。

当前S25梯度是简单规则/有限近似后端的局部结果，三个组区间包含0；不能据相对百分比宣称复杂AE必需。现有双像素H-aware阴性和iPhone规则固定也不能推成所有图像自适应无效。没有审核支持的剩余机制时，不强行增加网络寻找阳性。

## 当前唯一待用户输入的事项

自动审批已拒绝把非公开协议、代码和完整实验统计提交给外部Claude服务，理由是此前授权没有明确覆盖此资料类别向该具体服务的发送。两份latest-complete-dossier已本地准备，不含DNG原图、照片或真实像素缓存；此前尝试未启动、未产生响应。等待对这个具体提交的明确授权；没有用其他外部服务绕过拒绝。

最短后续链：授权后的两次实际外审 → 据裁决收敛主张/下一最小实验 → 真实接受、门禁与归档同步。H-aware、DNG4/8和历史融合已经完成，不重复实验寻求阳性。
