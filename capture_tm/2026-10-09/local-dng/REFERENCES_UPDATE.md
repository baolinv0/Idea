# 本地诊断后的文献增补
日期：2026-10-09。用途：下一轮查新 dossier 的线索，尚未替代正式查新或外部接受凭据。未据以下邻近工作宣布 ABANDON。

- [Noise-Optimal Capture for High Dynamic Range Photography，CVPR2010](https://people.csail.mit.edu/hasinoff/hdrnoise/)：已读作者项目摘要。已存在噪声模型下、同时间预算的采集优化；本轮不能把光子/噪声权衡或曝光最优化本身当新理论。
- [Modeling Radiometric Uncertainty for Vision with Tone-mapped Color Images，TPAMI2014](https://arxiv.org/abs/1311.6887)：已读arXiv元数据与摘要，DOI10.1109/TPAMI.2014.2318713。它为tone-mapped像素拟合潜在线性色彩分布，说明影调后的不确定性建模已有先例；当前没有核读全文，不宣称完整覆盖本轮采集协议。
- [AdaptiveAE，ICCV2025](https://arxiv.org/abs/2508.13503)：已有身份核验，本轮重新打开一手页面。作者已有基于过去帧的曝光风险预测；历史预览和普通曝光风险预测不能单独立项。

近六个月检索候选：
- [Optimize-at-Capture，arXiv2605.04397](https://arxiv.org/abs/2605.04397)：一手arXiv检索摘要称使用历史皮肤反射预测进行rPPG专用曝光控制。尚未helper核验/全文核读，标为[UNVERIFIED]线索；不能用作者应用收益支持本研究。
- [ExpoCM，CVPR2026](https://openaccess.thecvf.com/content/CVPR2026/html/Liu_ExpoCM_Exposure-Aware_One-Step_Generative_Single-Image_HDR_Reconstruction_CVPR_2026_paper.html)：CVF检索元数据可见，直接页面读取403。作者曝光相关恢复priors是相关后端线索，不是已确认的物理AE同构。[UNVERIFIED by helper]。
- [JOCA，WACV2026](https://openaccess.thecvf.com/content/WACV2026/html/Yan_JOCA_Task-Driven_Joint_Optimisation_of_Camera_Hardware_and_Adaptive_Camera_WACV_2026_paper.html)：CVF检索元数据可见，直接页面读取403。联合相机硬件、运行时控制和下游任务已有研究线索。[UNVERIFIED by helper]。

实际检索表述：
1. camera exposure selection Bayesian posterior spatial prior noise clipping tone mapping adaptive exposure
2. "auto exposure" "Bayesian" image prior saturation noise
3. "exposure" "posterior" "tone mapping" adaptive acquisition
4. site:arxiv.org "exposure" "Bayesian experimental design" camera
5. site:openaccess.thecvf.com exposure control noise saturation Bayesian2026
6. site:arxiv.org "adaptive exposure" "2026"

下一轮必须按实际H-aware及留出结果更新核心claim，核对候选全文/身份并进行有效独立审阅。本文件不赋予review receipt，不是穷尽检索。

## 本轮完成的原文与身份复核

官方arXiv11项标题已独立核对；旧输入仅AdaptiveAE标题错误，正式题名为AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes。原始核验输入保留，见[标题审计](paper_title_audit.json)。

新增helper已核实1311.6887、2605.04397、2609.17023、1807.10596的ID存在。Hasinoff Noise-Optimal Capture、ExpoCM、JOCA、Digital Gimbal和Learning to Control Camera Exposure via Reinforcement Learning的题名核验遇到Semantic Scholar暂时失败，标为[UNVERIFIED by helper]；主页面/作者PDF资料仍保留，不补造DOI或ID。首次additional输入因不支持url字段失败，已保存真实错误并修正后重新执行，最终WARN；这是资料核验失败记录，不是文献被判不存在。

已独立核读AdaptiveAE方法/§4.1 Table3，Noise-Optimal Capture§4–5，以及Radiometric Uncertainty§4/§5.1。泛泛曝光优化、后端交叉测试和不同恢复方法改变低误差曝光组合集合都已有直接先例；严格控制协议的组合未见于这三篇不等于创新已确认。完整原文范围和页码见[primary_overlap_audit.md](primary_overlap_audit.md)。
