# 文献与工程资料

资料记录截至2026-10-09；链接到一手原文/作者项目。这里不上传第三方论文全文。会议信息与arXiv首发时间分开理解；这不是穷尽检索或引用影响力排名。

| 工作 | 一手资料 | 与本题关系 |
|---|---|---|
| Learning a Reinforced Agent for Flexible Exposure Bracketing Selection（EBSNet/MEFNet），CVPR2020 | [arXiv2005.12536](https://arxiv.org/html/2005.12536v1) | 预览→有限曝光组合，后端质量反馈与联合训练 |
| Neural Auto-Exposure for High-Dynamic Range Object Detection，CVPR2021 | [CVF原文](https://openaccess.thecvf.com/content/CVPR2021/papers/Onzon_Neural_Auto-Exposure_for_High-Dynamic_Range_Object_Detection_CVPR_2021_paper.pdf) | 物理AE与下游目标协同 |
| AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes，ICCV2025 | [arXiv2508.13503](https://arxiv.org/html/2508.13503v1) | 三预览、预算、快门/ISO、运动与跨后处理 |
| Dynamic Exposure Burst Image Restoration（DEBIR），2026 | [arXiv2603.21784](https://arxiv.org/html/2603.21784v1)、[官方实现](https://github.com/woo525/DEBIR) | 预览驱动burst；后端偏置和staged/joint比较 |
| Modular Neural Image Signal Processing | [arXiv2512.08564](https://arxiv.org/html/2512.08564v3) | 数字增益与可编辑photofinishing基础 |
| Edit-aware RAW Reconstruction，CVPR2026 | [arXiv2512.05859](https://arxiv.org/html/2512.05859v2)、[官方代码](https://github.com/SamsungLabs/edit-aware-raw/) | 随机编辑ISP渲染域损失；编辑鲁棒性已有先例 |
| Benchmarking RAW and RGB Restoration in Image Signal Processors，2026 | [arXiv2609.02831](https://arxiv.org/html/2609.02831v1) | 恢复器与目标ISP分布/目标域匹配混杂 |
| DRIFT: Deep Restoration, ISP Fusion, and Tone-mapping，2026 | [arXiv2604.03402](https://arxiv.org/html/2604.03402v1) | 恢复、融合与可调影调管线 |
| Burst photography for high dynamic range and low-light imaging on mobile cameras（HDR+），2016 | [作者官方资料](https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/) | 低曝光保护高光，融合降噪，再TM |
| Noise-Optimal Capture for High Dynamic Range Photography，CVPR2010 | [作者项目](https://people.csail.mit.edu/hasinoff/hdrnoise/) | 详细噪声模型、固定采集时间下最优序列 |
| Optimal exposure time for satellite imaging? A trade-off between residual tip-tilt and registration accuracy，2026 | [arXiv2609.17023](https://arxiv.org/abs/2609.17023) | 后处理后质量最优曝光；本轮只核摘要，不宣布同构 |
| Exposure Bracketing Is All You Need For A High-Quality Image，ICLR2025 | [官方论文页](https://proceedings.iclr.cc/paper_files/paper/2025/hash/ede6851dbcde82ed40d794b5b9958e9b-Abstract-Conference.html) | 包围输入恢复，未来多帧扩展近邻 |

## 工程与数据来源

- [源研究分支](https://github.com/baolinv0/modular_neural_isp/tree/feature/capture-tm-c-20261005)，归档分析固定[7e080d3](https://github.com/baolinv0/modular_neural_isp/tree/7e080d373accd28150034b68718c27a21f932a09)。
- [研究问题](https://github.com/baolinv0/modular_neural_isp/blob/7e080d373accd28150034b68718c27a21f932a09/research/ae_tm/RESEARCH.md)。
- [S24官方说明](https://github.com/SamsungLabs/time-aware-awb/blob/main/s24-raw-srgb-dataset/README.md)：处理过的三通道源与样式GT，不单独提供本研究需要的无裁切HDR真值或时序重捕获证据。
- 本仓库的四个CPU脚本和JSON是本次原创探测产物，协议与源工程不同，不冒充官方实现。

## 身份核验与历史状态

[原核验输入](papers-input.json)和[实际结果](papers-verified.json)确认七个指定arXiv ID存在，返回PASS/pending=0；该助手不等于主张审计。
原输入把AdaptiveAE标题写成非官方简写，历史文件保留原样；本表使用一手正式标题。20261008历史报告的UNVERIFIED表示当时尚未找到助手，不是论文不存在；后续核验只覆盖上述七ID，不追溯声明全部文献已核验。
