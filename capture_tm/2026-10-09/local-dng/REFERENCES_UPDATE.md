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
