# CaptureTM 查新检索记录
日期：2026-10-09（Asia/Shanghai）；源快照：4ba0d34df29de9a46d2f81cfbc9e43f16d2e64af。
本记录保存实际检索，不将关键词命中等同于原论文包含研究结论。

## 覆盖
C1：补偿后近最优动作集合/剩余收益。C2：边际匹配后空间可恢复性。C3：独立后端收益/搭档适配。
覆盖2024–2026、早期基础工作，最近六个月窗口2026-04-09至2026-10-09（before:2026-10-10）。
渠道：web 检索原始 arXiv/CVF/作者页/出版页；alphaXiv广泛发现；arXiv/CrossRef/Semantic Scholar helper仅用于文献存在性检查。没有把alphaXiv的中间AI报告当作原论文。

## 母任务实际查询
1. [C1] `"exposure selection" "restoration" "backend" dynamic exposure burst`
2. [C1] `"near-optimal" exposure tone mapping compensation`
3. [C3] `"auto exposure" "post-processing" AdaptiveAE`
4. [C3] `"exposure" "restoration" "joint" 2026 2025 2024`
5. [C1] `"Dynamic Exposure Burst Image Restoration"`
6. [C3] `"Learning to Control Camera Exposure" "2024"`
7. [C3] `"exposure" "cross" "restoration" "backend" camera`
8. [C1] `"exposure bracketing" "tone mapping" optimal neural 2024 2025 2026`
9. [C1] `camera exposure near optimal set reconstruction risk tone mapping`
10. [C3] `"exposure" "post-processing" "methods" "AdaptiveAE"`
11. [C3] `"Learning to Control Camera Exposure" "post-processing"`
12. [C3] `"auto exposure" "generalization" "ISP" 2026 after:2026-04-09 before:2026-10-10`
13. [C1] `site:arxiv.org exposure optimal reconstruction compensation 2026`
14. [C1] `site:openreview.net exposure acquisition restoration 2026`
15. [C3] `site:proceedings.mlr.press/v267 exposure camera restoration`
16. [C3] `site:papers.nips.cc "exposure" "2025"`
17. [coverage] `ICML 2026 proceedings exposure camera acquisition restoration`
18. [coverage] `site:proceedings.iclr.cc/paper_files/paper/2026 "exposure"`
19. [coverage] `site:proceedings.neurips.cc/paper_files/paper/2025 "exposure" camera`
20. [coverage] `camera exposure restoration after:2026-04-09 before:2026-10-10 site:arxiv.org`
21. [source] `"Digital Gimbal" arxiv`
22. [source] `"Neural Auto-Exposure" arxiv`
23. [source] `"Active short-long exposure deblurring"`
24. [coverage] `site:proceedings.mlr.press "2026" "image" "acquisition"`
25. [C1] `"near optimal exposure" image reconstruction`
26. [C1] `"exposure" "compensation" "Bayes risk"`
27. [C3] `"exposure selection" "different" "fusion methods"`
28. [coverage] `site:arxiv.org "exposure" "restoration" after:2026-04-09 before:2026-10-10`
29. [coverage] `"DeAltHDR" arxiv`
30. [coverage] `site:openreview.net "ICML 2026" "exposure" image camera`
31. [coverage] `"exposure bracketing" "restoration" after:2026-04-09 before:2026-10-10`
32. [venue] `site:proceedings.mlr.press/v306/ exposure camera`
33. [venue] `site:proceedings.mlr.press/v306/ "acquisition" "reconstruction"`
34. [venue] `site:proceedings.mlr.press/v306/ "optimal" "sensing"`

## C2独立文献agent实际查询
以下35条来自agent最终返回的实际查询日志。
1. `"Noise-Optimal Capture for High Dynamic Range Photography"`
2. `"task driven" "exposure" camera optimization`
3. `"optimal exposure" "spatial" noise saturation Bayes`
4. `automatic exposure control image restoration task aware exposure 2024 2025 2026`
5. `"exposure" "histogram" "spatial correlation" reconstruction`
6. `"Bayesian" "exposure" "acquisition" imaging optimal`
7. `"optimal exposure" "restoration" camera paper`
8. `"task-driven exposure" camera`
9. `"automatic exposure" "Bayesian" camera image paper`
10. `"exposure" "Bayes risk" image camera`
11. `"exposure control" "spatial" "saturation" image restoration`
12. `"optimal exposure" "correlation" image noise camera`
13. `"exposure" "spatial" "noise" after:2026-04-09 before:2026-10-10 site:arxiv.org`
14. `"automatic exposure" after:2024-01-01 before:2026-10-10 site:openaccess.thecvf.com`
15. `"exposure" "histogram" "restoration" after:2026-04-09 before:2026-10-10`
16. `"One-Shot Optimal Exposure Control" paper`
17. `"HDR Metering" Gallo 2012 paper`
18. `"Optimal HDR Reconstruction with Linear Digital Cameras" pdf`
19. `"exposure" "Bayes" "Blackwell" image acquisition`
20. `"WYSIWYG Computational Photography via Viewfinder Editing"`
21. `"exposure" "tone mapping" "capture" "optimal" 2024 2025 2026`
22. `"exposure selection" "spatial" "HDR" reconstruction histogram`
23. `site:graphics.stanford.edu/papers/wysiwyg "metering" "5.1"`
24. `site:graphics.stanford.edu/papers/wysiwyg "noise" "derivative"`
25. `site:graphics.stanford.edu/papers/wysiwyg "histogram" "global"`
26. `"WYSIWYG Computational Photography" "noise" "histogram"`
27. `"WYSIWYG Computational Photography" "V(x" "5"`
28. `"WYSIWYG Computational Photography" "5.1" "derivative"`
29. `"WYSIWYG Computational Photography via Viewfinder Editing" pdf nvidia`
30. `"WYSIWYG Computational Photography" "J(x, y"`
31. `"WYSIWYG Computational Photography" "independent" "noise"`
32. `"Metering for Exposure Stacks" pdf Gallo`
33. `"WYSIWYG Computational Photography" "Prior Work" "capture"`
34. `"Automatic Exposure" "Bayesian" "NeurIPS" after:2024-01-01 before:2026-10-10`
35. `"exposure control" "ICLR" "ICML" after:2024-01-01 before:2026-10-10`

## alphaXiv发现查询
keywords=[AdaptiveAE, Dynamic Exposure Burst Image Restoration, exposure bracketing, tone mapping]；difficulty=7；prioritize=recency。
question: Which papers already study exposure selection benefit after restoration and tone mapping compensation, with independent post-processing backends and matched spatial scene statistics?
返回AdaptiveAE、DOME-HDR、DRIFT、Scene-Segmentation-Based Exposure Compensation、Real-Time Scene-Adaptive Tone Mapping、Rethinking Exposure Correction、ECMamba。其中数字曝光校正与物理曝光采集分开判断；ECMamba只作为发现项，未用于裁决。

## 会议与近期筛查
- [ICLR2026目录](https://proceedings.iclr.cc/paper_files/paper/2026)：Exposure/Camera标题筛查找到DeAltHDR，作者页关联[OpenReview](https://openreview.net/forum?id=buzIPnGxA8)。OpenReview浏览器挑战阻止正文读取，未用于精确重合裁决。
- [ICML2026，PMLR306](https://proceedings.mlr.press/v306/)：先从官方PMLR索引识别正确卷号（非2025的267卷），做exposure/camera、acquisition/reconstruction、optimal/sensing查询。返回关键词异义（例如社会/多模态 exposure）及通用active-sensing来源，未找到直接包含CaptureTM受控结果的条目。索引find没有相关标题命中；这是有限标题检索，不能证明全集没有相关论文。
- [NeurIPS2025](https://proceedings.neurips.cc/paper_files/paper/2025)：查到UltraLED、BurstDeflicker、Neural Exposure Fields等。分别属于固定单短曝光恢复、闪烁消除、视图合成；未据此否定CaptureTM。没有将尚未读取的NeurIPS2026 proceedings称为已检索。
- 六个月内重点读：Benchmarking RAW and RGB Restoration（9月2日）、Satellite exposure（9月15日）、DOME-HDR（8月6日）；另检查4月12日DRIFT修订、4月23日Edit-aware RAW修订。DEBIR首次3月23日虽在六个月窗口前，仍是方法级最近邻。

## 读取深度与限制
EBSNet、AdaptiveAE、DEBIR的摘要/相关工作及关键对比段落直接读原始全文。WYSIWYG、Metering for Exposure Stacks的完整PDF抓取失败，使用原作者页和原PDF索引中的具体段落，限制已写进矩阵。其他辅助来源按矩阵标注实际深度。
本检查没有证明全领域不存在先例；无精确包含的检索结论只适用于这些查询、截止日期和已读段落。