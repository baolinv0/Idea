# 最新证据摘要：2026-10-13精炼输入
源快照：72fec72348904bd5230202e78d55ab6459695d9a；读取对象仅为代码/协议及统计资料，不读取DNG像素。

## 已有结果（不是本轮运行）
1. 旧低分辨率共同后端的族均值最优动作翻转已撤回。
2. 完整H-aware双像素后验：3seed；N0/N1，8192源×16未来重复；128/256/512积分；关系规则在全部条件重新选择为固定4，相对其dev固定4收益0，区间[0,0]。这是选定规则退化同一个动作时的同一输出，不证明任意策略收益为零。
3. H-aware N0亮度规则绝对收益4.9623e-7、4.2234e-7、4.4986e-7（约1.3%–1.57%）；N1关系减亮度CI均跨0。
4. 旧H-blind策略迁入H-aware可优于继承的固定0.5，但不能证明重新选择的H-aware策略优于本域dev最佳固定4。
5. DNG4/8数值复核最大组级风险差1.077e-6；固定动作/24规则/288策略动作/收益符号稳定。相邻积分差不是严格误差界。
6. DNG历史控制：代码ae7c762bf18461fb1fb673b81b0ab0bc33c3e78e；3seed、4未来重复、2000组bootstrap；1152源交叉统计、96单元、768配对CI。后端只融合3个历史测量与单次future，不融合future重复。
7. iPhone两H融合后端四规则都固定8；S25纯H融合均值/噪声/梯度规则固定4，q99个别seed退化。
8. S25 H融合+Wiener梯度相对dev固定4收益17.465643%、17.211664%、17.280073%，绝对3.155361e-5、3.100738e-5、3.124488e-5。对均值直接差CI为[-8.463205e-5,0]、[-8.236767e-5,0]、[-8.342333e-5,0]；都包含0，绝对收益都低于旧示例delta1e-4。
9. 冻结Wiener梯度迁至纯融合有约13%收益，而纯融合重新选的梯度是固定4；完整保留两种比较，不互相替代。
10. DNG为34对、68个processed Linear RAW、同一会话11保守背景组，train/dev/diagnostic6/2/3组。诊断g04/g06/g10只有三个独立背景组，相机/crop/seed/噪声重复不增加场景数。源有噪，目标sqrt(x/(x+.5))，不是干净HDR/原生Bayer/真实重拍保真度。WLS和Wiener不能称充分Bayes后端。
11. 最新Claude response只记录自动审批拒绝，进程未创建、没有模型响应；跨家族审核未完成。不能当真review。
12. 2026-10-09追加查新5.5/10，PROCEED WITH CAUTION，仅针对收窄未证问题，不是上述最新实验证据已经得到完整外审的评分。

## 最近邻的已知覆盖
WYSIWYG2013已按最终外观/局部编辑优化曝光；EBSNet2020有preview语义+共同传统EF比较；AdaptiveAE2025有过去预览、预算/动态风险及后处理比较；DEBIR2026 §5明确后端能力偏置并使用广泛曝光pretrain/策略训练/微调。
Modeling Radiometric Uncertainty for Vision with Tone-mapped Color Images（1311.6887v2，TPAMI2014）§4/§5.1已有概率逆影调、多曝光后验重建，Fig6展示概率重建改变低误差曝光对范围。“补偿集合变化”不能单独算新颖性。
完整H+Y接口、冻结指定selector交叉、边际匹配+空间依赖留出的控制组合尚未在已读资料中发现；组合本身仍不是原创贡献。

## 原始资料路径
- capture_tm/2026-10-09/local-dng/CONCLUSIONS.md
- capture_tm/2026-10-09/local-dng/dng-history-control-3seed/results.json
- capture_tm/2026-10-09/local-dng/dng_history_control_independent_audit.md
- capture_tm/2026-10-09/local-dng/primary_overlap_audit.md
- capture_tm/2026-10-09/review-inputs/latest-complete-dossier/critical-dossier.md
本摘要由只读证据agent逐项核对。科研统计不等同于重新运行代码或重新生成数据。
