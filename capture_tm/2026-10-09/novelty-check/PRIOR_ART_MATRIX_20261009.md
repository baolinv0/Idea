# CaptureTM 方法级最近邻矩阵
日期：2026-10-09；精确研究问题见查新报告。列“未包含”是对本次已读内容的判断，不是证明整篇/整个领域不存在相关结果。
标记：✓ canonical helper确认存在；VERIFY_PENDING为暂时API失败。存在性与科学主张相容性分开。

| 原始工作 | 已经包含，不能再作首创 | 已读位置 | 与候选C1–C3的剩余差异 |
|---|---|---|---|
| ✓ [WYSIWYG Computational Photography via Viewfinder Editing](https://graphics.stanford.edu/papers/wysiwyg/)，TOG/SIGGRAPH Asia2013 | 最终外观、局部编辑指导曝光采集；相同后处理比较appearance/histogram metering | 作者页；原PDF索引§2.2、§5，Eq4/7–10、Fig1；全PDF抓取失败 | 逐像素目标依赖L与编辑E，未报告固定目标、边际/各动作饱和匹配后只变空间恢复关系的规律；需排除局部目标权重变化造成的差异 |
| ✓ [EBSNet/MEFNet](https://arxiv.org/html/2005.12536v1)，CVPR2020 | 预览语义＋照明选择括号；AE与融合联合训练；所有selector用同一传统EF比较 | 摘要、§2–3、§4.3/Table2、§4.4 | “超越直方图”“共同后端比较”已做；未见充分补偿审计、精确匹配与未知空间关系留出 |
| ✓ [AdaptiveAE](https://arxiv.org/html/2508.13503v1)，ICCV2025 | 三帧过去预览、shutter/ISO、时间和运动约束；最终HDR reward；比较前/中/后deblur | 摘要、§2–4、A.2 | A.2是deblur放置比较，不能称完整selector×独立backend矩阵；未见C2受控关系规律 |
| ✓ [DEBIR](https://arxiv.org/html/2603.21784v1)，2026 | 从preview/gain/motion预测burst曝光；恢复损失训练；明确后端早期能力偏置和分阶段缓解 | 摘要、§2/4/5、§6 Table5、S7 | “后端能力影响最优曝光”已有直接讨论；新场景/新相机泛化不是未知恢复关系留出；未给C2边际匹配规律 |
| ✓ [Noise-Optimal Capture](https://people.csail.mit.edu/hasinoff/hdrnoise/)，CVPR2010 | 曝光/ISO及时间/帧数预算，噪声模型，最坏SNR优化 | 摘要、§5–6及讨论，独立agent | 原始irradiance SNR目标与充分空间恢复后的条件风险不同；噪声/饱和的基本折中不能作新理论 |
| VERIFY_PENDING [Optimal HDR Reconstruction with Linear Digital Cameras](https://vcai.mpi-inf.mpg.de/projects/opthdr/)，CVPR2010 | 标定、irradiance不确定性、像素SNR曝光目标；不确定性控制bilateral filter | 原PDF摘要、引言、§8–9，独立agent | 空间传感器噪声不等于场景空间先验；未给补偿后的匹配场景排序规律 |
| ✓ [Metering for Exposure Stacks](https://oraziogallo.github.io/publication/gallo2012metering/)，CGF2012 | 完整irradiance histogram及噪声/量化感知metering | 摘要、原PDF索引引言/相关工作；全PDF抓取失败 | 是必须承认的histogram基线；未隔离相同直方图下的空间恢复性 |
| ✓ [Blur/Noise Trade-Off](https://boracchi.faculty.polimi.it/docs/2011_UniformMotionBlur_Boracchi_Foi.pdf)，TIP2011 | 恢复误差决定最优曝光；已知PSF/oracle regularization仍有有限最优点；其测试类别的内容变化影响较小 | 摘要、误差分析、IV.C，独立agent | 对效应大小提供反证压力；不是C2已被证明或直接被否定，没有饱和匹配/因果关系留出 |
| ✓ [Digital Gimbal](https://arxiv.org/html/2012.04515v1)，CVPR2021 | 可微曝光积分模型与burst恢复一起优化 | 摘要、§2–3 | 训练后曝光参数固定；未做充分共同后端后的条件规律 |
| ✓ [Active Short-Long Exposure Deblurring](https://webpages.tuni.fi/vision/public_data/publications/icpr2022_active_burst_deblurring.pdf)，ICPR2022 | 拍摄前viewfinder选择S-L曝光用于恢复 | 摘要、§II | 因果预览选择恢复动作已有；未见C2匹配与充分补偿审计 |
| ✓ [JOCA](https://arxiv.org/html/2512.06763v1)，WACV2026 | 硬件、adaptive exposure/gain、下游任务联合设计，噪声/裁切/运动模型 | 摘要、§2–4及设置，独立agent | 硬件/任务共同变化，与CaptureTM固定协议不同；未分离C2 |
| ✓ [BracketIRE](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ede6851dbcde82ed40d794b5b9958e9b-Abstract-Conference.html)，ICLR2025 | 曝光括号支撑去噪、去模糊、HDR、SR的统一恢复 | 官方摘要 | 提供后端及任务背景；非自适应AE补偿边界分析 |
| ✓ [RAW/RGB Restoration Benchmark](https://arxiv.org/html/2609.02831v1)，2026-09 | 固定ISP、匹配训练条件，目标ISP训练改变恢复域比较 | 摘要、§1–2 | 公平后端与训练分布对齐本身已是分析范式；曝光不是这里的受控动作 |
| ✓ [Satellite Exposure](https://arxiv.org/pdf/2609.17023)，2026-09预印本 | 后处理质量、固定总观测时间、空间导数影响配准信息，优化曝光 | 摘要、§3.1–3.4/§4/结论，独立agent | 最优曝光依赖空间结构的宽泛命题已有；没有CaptureTM的饱和匹配、预览识别及关系留出；未确认正式SPIE出版 |

## 扩展筛查
[Modular Neural ISP](https://arxiv.org/abs/2512.08564)、[Edit-aware RAW](https://arxiv.org/abs/2512.05859)、[DRIFT](https://arxiv.org/abs/2604.03402)为后端/目标背景。
[DOME-HDR](https://arxiv.org/html/2608.05626v1)读取摘要/相关工作与其“given三张LDR”的协议，未将生成融合推广为物理AE选择结论。
[实时HDR检测TM](https://arxiv.org/abs/2608.30400)、[空间非均匀曝光校正](https://arxiv.org/abs/2604.04136)、[分割曝光补偿](https://arxiv.org/abs/2410.19839)是数字处理背景，不能混同曝光时长。
[Neural Auto-Exposure for HDR Object Detection](https://openaccess.thecvf.com/content/CVPR2021/papers/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.pdf)存在性helper已确认；网页全文读取失败，本次仅作为task-driven capture背景，非精确包含裁决依据。
[Camera Exposure RL](https://arxiv.org/abs/2404.01636)读取原摘要，是实时AE背景。
VERIFY_PENDING [HDR+](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/)原文存在性helper暂时失败；不参与残余新颖性否决。
[DeAltHDR](https://openreview.net/forum?id=buzIPnGxA8)身份来自官方ICLR2026目录及作者页，OpenReview挑战阻止正文。本次未送入已读24项的helper清单，未将其标为不存在，也未用于裁决。

## 理论定位
条件均值/后验方差的MSE最优性、near-optimal set、empirical regret、空间先验利用、跨后端评测都是基础工具或评测控制，不各自承载创新。可发表差异必须是这些工具支持的新且可证伪的曝光—补偿条件规律。