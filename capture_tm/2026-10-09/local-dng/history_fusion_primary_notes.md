# DNG历史融合控制：公开资料与范围

读取日期：2026-10-09。以下是primary页面的实际阅读记录，不能当跨家族新颖性裁决。

- [Learnable Exposure Fusion for Dynamic Scenes](https://arxiv.org/abs/1804.01611)，2018-04-04提交。官方标题、作者、提交日期和摘要已直接核读；摘要讨论2/3张LDR图像融合及运动导致的配准问题。仅摘要，尚未全文对比，不声称已覆盖或未覆盖当前完整实验。
- [Lights, Camera, Attack: Exploiting Temporal HDR Fusion with Pulsed Light](https://arxiv.org/abs/2609.37742)，2026-09-29提交。官方摘要讨论照明时序变化造成跨曝光不一致。本地控制没有运动或照明变化，因此不能泛化到动态融合；不扩展本项目为安全攻击研究。仅摘要，未做全文同主张裁决。
- [Live HDR+ and Dual Exposure Controls on Pixel 4 and 4a](https://research.google/blog/live-hdr-and-dual-exposure-controls-on-pixel-4-and-4a/)，Google Research 2020-08-03。作者资料介绍已有欠曝光burst的对齐、合并和tone mapping，支持多帧复用作为既有简单控制。它不是当前WLS具体公式的验证来源。

身份核验helper另行返回WARN、pending_rate=1.0，两篇均verify_pending，reason=arxiv_verify_pending。这是helper的临时API状态；保留原始输出papers-history-control-verified.json，不把它改写为helper PASS。上面的直接官方页面读取记录与helper状态分列。

该控制只检查静态处理过Linear RAW内容的相对模拟，使用同一既有3张历史H及单张未来捕获；没有新采集预算。逆方差融合为近似经典后端，不称Bayes下界、无偏恢复或原创方法。它若消除策略收益，只能在本协议范围否定该收益的必要性；若仍有收益，也不能绕过三个诊断背景组、单会话和弱后端的限制。
