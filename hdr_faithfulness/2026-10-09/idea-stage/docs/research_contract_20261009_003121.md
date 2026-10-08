# Research Contract

Date: 2026-10-09
Status: PROVISIONAL_PLANNING
Selected idea: A / 原候选#12
Canonical plan: refine-logs/EXPERIMENT_PLAN.md

本合同是实验问题、主张与否证规则的来源；不表示新颖性、样本量或执行验收已通过。所调用技能安装目录未找到RESEARCH_CONTRACT_TEMPLATE.md，本文件根据已选问题及完整计划建立可读合同，未冒称使用不存在的模板。

## Problem Anchor
同一冻结RAW→非生成融合/显示→RGB生成恢复流程的合法设置，是否改变等采集成本曝光选择，产生局部事实决策损失？

## System and Scope
主流程：F0固定非生成融合/显示，F1内部非生成stage1，F2同SUPIR-v0Q，s_stage2=1.00/0.93。其他参数/权重冻结。
静态单传感器、声明场景分布；eU=[t,t,t,t]、eB=[t/4,t/4,t/2,3t]，N=4,T=4t，固定增益。RGB生成端不输出经过验证的HDR辐射真值。
Non-goals：新网络、训练、传感器物理上限、最低采集预算、普遍停拍安全、广泛SOTA榜单。

## Claims
C1：独立测试支持配置风险排序反转，并支持s0→s1交叉选型损失Gamma下界>0.03，coverage可比。
C2：合法输入、固定显示/读出和强非生成解释控制下后果仍有直接证据。操作不称纯先验变量，SNR不称通道信息支配。
B：只有完整预算序列才作停止诊断，不是当前主张。
C：公平输入/读出适配为共同控制，不能预设已有工作不公平。

## Estimands
R=P(accepted wrong | accepted)，C=P(accepted)，U=P(accepted wrong)。
e_hat0/e_hat1由校准集冻结策略选择；Gamma=R_test(e_hat0,s1)−R_test(e_hat1,s1)。
D0/D1为两个配置各设置的风险差。测试不得重新选配置或方向。
Q/W/Z三态互斥完备；correct-readable和erase同时报告，不称无置信信号的错误为“自信错误”。

## Data and Truth
实体事实manifest为主真值；独立高SNR非生成参考验证真实性。
公开数据优先，仿真仅筛查，现实结论须真实确认。
scene为独立单位；同底图/布置的patch、采集重复、seed嵌套。主流每scene预选一个事实和(r,k)，其余辅助。
按scene_family分开发/校准/测试。不得以另一恢复器/OCR/VLM预测充当ground truth。

## Frozen Design
开发24scene，校准80scene；测试N暂以160起点/320建议上限。N及协议在查看测试前锁定。
2曝光×2设置×2采集重复×3seed；无训练。
建议ε=.05、coverage=.80、可比coverage差容差=.05、实际损失门槛=.03；开发结束前允许基于任务代价修改一次并记录，之后冻结。
四风险同时区间推导D/Gamma；稀有错不用零宽bootstrap冒充证书。达标risk上界和coverage下界另作明确家族认证。

## Acceptance and Falsification
确认：合法链路、不同校准选择、预设容差内coverage可比、两个D同时相反符号、Gamma下界>3pp，且控制未发现使对照无效的问题。
停止/降级：已有直接覆盖；非法接口；cal选择相同；coverage不可比；所需N超预算；信号仅个例/interaction/known adapter。
未检出或宽区间称不确定/范围内未支持，不证普遍H0。
不追加锁定测试到显著；任何事后协议改变建立新轮次。

## Evidence and Execution Status
Independent planning-design audit: completed by fresh agent /root/plan_design_audit.
Code implementation/review: not applicable this planning-only request.
Empirical results: none.
Next action: E0/R001 evidence matrix and R002 actual interface/data readiness.
Prior idea-discovery formal gate: old BLOCKED status not re-evaluated; planning does not clear it.
