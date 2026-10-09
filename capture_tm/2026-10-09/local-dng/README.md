# CaptureTM：本地DNG与连续参考诊断
日期：2026-10-09。当前研究状态REVISE，idea-discovery gate仍BLOCKED；投稿贡献尚未确认。

先读[完整正负结论与可复用发现](CONCLUSIONS.md)。最新实验代码位于[工程分支](https://github.com/baolinv0/modular_neural_isp/tree/feature/capture-tm-c-20261005/research/ae_tm/diagnostics)；DNG最终实验提交09052a605b8251c539a6dda3268f2b1f183a95c8，报告复现工具提交58d64b1。

已实际完成：68份DNG审计；三seed N0连续参考和反向copula N1；三seed真实内容相对曝光实验；逐源成本、规则间配对区间、冻结DNG后端交叉矩阵；独立代码与照文档环境验证。没有神经训练、原生Bayer/干净HDR、真实相机重拍或正式S24test证据。

资料：
- [汇总原始统计](summary.json)
- [DNG完整审计](dng_audit.json)、[审计执行记录](audit_run_meta.json)
- [N0/N1原始结果](continuous-reference/results.json)、[执行元数据](continuous-reference/run_meta.json)、source-metrics/*.npz（仅合成源风险与动作，不含真实像素）
- [DNG最终原始结果](relative-experiment-retry02/results.json)、[逐源指标](relative-experiment-retry02/source_metrics.csv)、[失败/修复与范围记录](relative-experiment-retry02/run_meta.json)
- [冻结DNG后端交叉矩阵](dng_backend_cross.csv)
- [独立代码/环境审计](independent_audit.md)、[锁定环境](env-spec.json)、[实际见证](environment_witness.json)
- [新一手文献线索及未核验范围](REFERENCES_UPDATE.md)
- relative-experiment-retry01保留修复前数值资格版本；本轮结论以retry02为准。

全部DNG、照片、contact sheet、真实像素缓存均未上传。输入路径只由本地CLI提供。DNG源已处理/噪声/可能裁切；这里模拟额外曝光/噪声，以原bounded绿色源的固定解析变换为目标，不声称独立专家GT。

最新决定：H-aware与DNG4/8已完成并独立审计。H-aware关系规则恒4、收益0；DNG所有冻结动作和收益符号不变。当前缺口是明确的新颖贡献与实际跨家族外审，不能升级复杂方法主张。

当前验收缺口：查新和批判审阅的实际模型均属OpenAI系列，接受状态provisional；2026-10-09重新运行evidence gate退出1，仍缺有效跨系列凭据。没有修改gate策略或伪造接受。

最新资料：[H-aware原始结果](history-reference/results.json)、[全部交叉单元汇总](history-reference/summary.json)、[H-aware独立审计](history_independent_audit.md)、[DNG4/8原始结果](relative-experiment-refinement04_08/results.json)、[精度审计](dng_refinement_independent_audit.md)、[文献原文核读](primary_overlap_audit.md)。H-aware已发布等价代码提交c6a3fb4；其完整Git源tree与执行用本地f465e73一致。外部Claude审阅等待用户授权，未启动、无响应。

DNG历史信息控制已完成：[原始JSON](dng-history-control-3seed/results.json)、[完整1152行CSV](dng-history-control-3seed/source_metrics.csv)、[执行记录](dng-history-control-3seed/run_meta.json)、[独立审计](dng_history_control_independent_audit.md)。iPhone固定、S25简单梯度局部收益/CI包含0均保留，详见canonical报告，仍无跨家族接受。代码实际执行与已发布均ae7c762。
