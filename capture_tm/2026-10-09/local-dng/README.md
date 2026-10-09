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

当前科学缺口：参考后端遗漏三张历史预览及动作选择先验。因此当前结果只适用于共同H-blind后端。H-aware后验及严格2selectors×2renderers交叉矩阵正在独立worktree实现；DNG4/8积分refinement待做。只有这些决定检验及必要强基线支持后，才安排投稿贡献确认和后续训练。

当前验收缺口：查新和批判审阅的实际模型均属OpenAI系列，接受状态provisional；2026-10-09重新运行evidence gate退出1，仍缺有效跨系列凭据。没有修改gate策略或伪造接受。
