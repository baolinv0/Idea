# CaptureTM 讨论归档

最新更新：2026-10-13（Asia/Shanghai）。本次research-refine已完成5轮实际GPT-6-Astra/xhigh原生agent评审，最终**6.85/10，RETHINK（当前配对toy与算法贡献路线）**；方法诊断闭合，未到投稿READY。

[最终提案](refine-logs/FINAL_PROPOSAL.md) · [五轮完整评审与精炼报告](research-refine/2026-10-13/refine-logs/REFINEMENT_REPORT.md) · [解析零值证明](research-refine/2026-10-13/refine-logs/SYMMETRY_AUDIT.md) · [本轮全部资料](research-refine/2026-10-13/README.md)

## 当前决定
新配对toy的共同先验、测量与目标对列内交换保持不变，G等变后端下每个动作条件风险也不变，因此正确配对删减的V_pair=0。全24排列对照混入位置角色标签，归因已撤回。关闭当前toy阳性实验计划，复杂AE升级暂停；原空间曝光问题保留。
本次没有新CPU/GPU/实拍实验。现有H-aware与DNG4/8及完整历史融合控制已完成，不能再列为待办。下一机制尚缺失，不新增网络或把控制组合当创新。

## 已完成的实验与边界
[完整正负结论](local-dng/CONCLUSIONS.md) · [DNG历史信息控制](local-dng/history_fusion_primary_notes.md) · [确定性结论及限制](CONCLUSIONS.md) · [文献与工程资料](REFERENCES.md)。
H-aware关系规则重选后恒4，仅限该规则；S25 H融合+Wiener梯度相对dev固定4约3.1e-5收益，梯度/均值直接差各seed区间含0，统计基础仍是单会话三个背景组。新toy解析零值不将这些结果推广成普遍阴性。

## 审核及后续
此次同一原生agent持续审核，执行/评审同属OpenAI；原跨家族证据门仍未完成。本次技能循环completed仅表示达到MAX_ROUNDS，不能改旧gate为PASS。
[剩余流程与完成标准](WORKFLOW_REMAINING_STEPS.md) · [本轮研究状态](research-refine/2026-10-13/01_RESEARCH_STATE.md) · [实际审核身份](research-refine/2026-10-13/refine-logs/REVIEW_PROVENANCE.json)。
后续需要具体关系机制、公平反事实与H可用风险预测，并找到最近邻未覆盖的精确差异；当前未确认frontier residual。

## 历史资料与复现
[2026-10-09查新](novelty-check/README.md) · [idea报告](idea-stage/IDEA_REPORT.md) · [历史实验计划](refine-logs/EXPERIMENT_PLAN.md) · [原README](history/README_before_refine_20261013_72fec723.md) · [旧提案](refine-logs/FINAL_PROPOSAL_before_20261013_72fec723.md)。
原实验源码与数值原件保留，复现指令和当时解释见原README及各实验目录；历史计划须结合当前停止决定，不直接执行。
[全部文件目录](MANIFEST.md) · [归档文本校验](SHA256SUMS.txt)。私有本轮.aris调用trace留本地，全部可读原始评审与bundle已归档。
