# HDR 恢复：观测证据、事实保真与采集选择

归档日期：2026-10-09。讨论跨度：2026-10-08—09。
本目录保存本次讨论的原始问题、查新、12个候选、独立AI视角评议、实验规划与时间戳历史。

**当前状态：A已选用于实验规划；没有pilot或模型实验，未确认新颖性。** B是条件式诊断，C是共同解释控制。此前idea-discovery正式门控未重新验收，不把规划完成或同模型家族评议写成验收PASS。六位研究者视角均由AI模拟，不代表本人意见、参与或背书。

## 建议阅读顺序

1. [当前结论与边界](CONCLUSIONS.md)
2. [最新研究状态](01_RESEARCH_STATE.md)
3. [六个独立研究视角与实际交叉回复](expert-panel/EXPERT_PANEL.md)
4. [实验计划](refine-logs/EXPERIMENT_PLAN.md)、[任务表](refine-logs/EXPERIMENT_TRACKER.md)、[研究合同](idea-stage/docs/research_contract.md)
5. [12候选与文献lineage](idea-stage/IDEA_REPORT.md)
6. [查新报告](NOVELTY_CHECK_REPORT.md)、[查新审查](NOVELTY_REVIEW.md)

## 原始讨论与证据

- [用户原始motivation](discussion/USER_MOTIVATION.md)
- [用户原始Minimal Probe](discussion/USER_MINIMAL_PROBE.md)
- [研究请求及阶段转折](discussion/USER_REQUESTS.md)
- [早期新颖性dossier](evidence/NOVELTY_DOSSIER.md)、[检索日志](evidence/SEARCH_LOG.md)
- [专家讨论共同材料](expert-panel/COMMON_PACKET.md)、[实际评议编辑记录](expert-panel/REVIEW_NOTES.json)
- [主要参考来源](REFERENCES.md)
- [完整文件清单](MANIFEST.md)、[归档说明](ARCHIVE_NOTES.md)

早期dossier、查新稿与时间戳版本保存研究过程；它们不替代最新结论。历史“wrong-but-confident”“纯prior-strength”“最低成本”等表述已被后续边界收窄。

## 本次实验规划

主对照：N=4、T=4t、固定增益；[t,t,t,t]与[t/4,t/4,t/2,3t]。
拟冻结RAW非生成融合/显示→SUPIR-Q RGB恢复，仅改变原生s_stage2=1.00/0.93。研究整条声明流程的选择损失，不称原生RAW生成HDR或物理信息上限。

主终点是校准选择后在锁定测试上的交叉选型损失，预注册s0→s1方向。开发24场景、校准80场景、测试暂160–320；样本数须在看测试前由pilot锁定，范围不是power保证。coverage差≤5pp只称预设容差内可比。

当前第一步：直接证据矩阵与实际模型/数据就绪检查。未下载权重、未租GPU、未采集或运行模型。

本目录与仓库已有CaptureTM归档属于不同讨论记录；不自动合并它们的实验或结论。

## 补充归档：vivo 影调色彩研究结论

按用户指定目录，新增[已验证结论与证据边界](VIVO_AESTHETIC_VERIFIED_CONCLUSIONS.md)。来源为独立的 vivo-aesthetic-tone-color 项目：照片SDR候选比较、quarter裁剪诊断与工程检查。完整数据以冻结来源链接引用；本次仅归档结论，不改变上文HDR恢复研究“尚未运行pilot/模型实验”的状态，也不构成HDR或全场景效果证据。
