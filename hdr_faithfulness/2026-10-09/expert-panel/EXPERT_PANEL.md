# HDR idea：六个独立研究视角与交叉讨论

日期：2026-10-08—09（Asia/Shanghai）。阶段：SCOUT → CONVERGE。

本报告由六个独立 AI agent 按指定研究者的公开研究方向进行评议。角色分配和下述结论均由 AI 产生，不代表研究者本人观点、参与或背书。没有联系任何研究者。首轮使用相同共同材料、独立新上下文，并隐藏此前排序和其他评议；算力限制使任务依次运行。它们属于同一模型家族，不能当作跨模型验证或新颖性证明。

A/B 暂保留为两个有条件的科学候选，C 暂作共同解释基线。首轮存在分歧，后文保留个人裁决。这些候选尚无本项目 pilot 支持；本轮只查原文、主页和现成代码，没有启动采集、推理或训练。

## 讨论对象

- **A：同一冻结恢复流程的合法现成设置，会不会改变等成本曝光配置的事实风险—可读性排序或达标集合？** 原候选 #12。要求实际采集选择后果；一般“融合器影响曝光选择”已不是残差。
- **B：跨 seed 一致性用于停拍时，是否会在事实风险仍过高时停止，而独立追加观测还能纠错？** 原候选 #1。要求有使用依据的停止规则、相同覆盖率与全策略评价。
- **C：生成恢复所报告的下游少拍收益，在公平的非生成预处理/适当读出后还剩多少？** 原候选 #4。是有效端到端收益的归因问题，不预设已有比较不公平。

等曝光时间、读出数和增益不等于等局部有效证据。生成 seed 与独立采集噪声分开，多 patch / seed 不是独立场景；单成本点只能比较配置。没有置信信号，称“错误且一致”，不称“自信错误”。

## 角色与身份依据

角色是按公开研究方向分配的评议关注点，不是对本人立场的推断。

| 研究者视角 | 身份依据 | 分配的关注点 |
|---|---|---|
| 张磊 / Lei Zhang | [香港理工主页](https://www4.comp.polyu.edu.hk/~cslzhang/)列有 OPPO Research Institute 关联 | 真实恢复、生成先验、保真与感知、独立方法贡献 |
| Michael S. Brown | [York 主页](https://www.eecs.yorku.ca/~mbrown/)、[ICCV 2023 材料](https://www.eecs.yorku.ca/~mbrown/ICCV2023_Brown.html)列 Samsung AI Center Toronto 关联；不据此声称当前职务 | RAW、ISP、辐射/颜色标定、读出公平性 |
| 薛天帆 / Tianfan Xue | [CUHK 研究主页](https://tianfan.info/)列 AdaptiveAE、UltraFusion 等 | 曝光、多帧、合法模型接口、真实观测互补 |
| 李重仪 / Chongyi Li | [研究主页](https://li-chongyi.github.io/)、[南开教师页](https://cc.nankai.edu.cn/2021/0323/c37281a575893/page.htm) | 真实退化、可靠恢复、事实风险与任务评价 |
| Jiawen Chen | [个人研究主页](https://people.csail.mit.edu/jiawen/)确认 Google / Adobe 成像经历及 Waabi Principal Researcher 身份 | 经典 burst、噪声与处理链、部署成本、强非生成基线 |
| Felix Heide | [Princeton 主页](https://www.cs.princeton.edu/~fheide/)、[计算成像实验室](https://light.princeton.edu/) | 物理可辨识性、信息与采样、传感器和算法联合决策 |

用户确认了此前身份对应问题。首位 agent 返回曾误写李重仪的中文名；英文身份和主页对应正确，本报告已更正。未把同名 arXiv 检索页当作唯一身份依据。

## 独立首轮裁决

这是研究潜力排序，不是实测性能排序。多数意见只用于识别争点。

| 视角 | 暂定排序 | A | B | C |
|---|---|---|---|---|
| Lei Zhang（张磊） | A > B > C | 谨慎继续 | 谨慎继续 | 合并为诊断 |
| Michael S. Brown | A > B > C | 谨慎继续 | 合并为诊断 | 合并为诊断 |
| Tianfan Xue（薛天帆） | B > A > C | 谨慎继续 | 谨慎继续 | 合并为诊断 |
| Chongyi Li（李重仪） | B > A > C | 谨慎继续 | 谨慎继续 | 合并为诊断 |
| Jiawen Chen | A > B > C | 谨慎继续 | 谨慎继续 | 合并为诊断 |
| Felix Heide | A > B > C | 谨慎继续 | 合并为诊断 | 放弃当前独立框架；保留基线 |

四位暂排 A 第一，两位暂排 B 第一。六位均未支持 C 以当前表述独立立题，其中 Felix 明确建议放弃当前独立框架，但保留其控制价值。Brown 和 Felix 将 B 暂放诊断位；其余四位允许继续核查。这些分歧没有被综合意见抹去。

## 六位首轮意见（编辑摘要）

以下是主 agent 对实际返回意见的压缩整理，不是逐字记录，更不是研究者发言。每位的“补核来源”指该 agent 本轮读取的来源；其他最近邻沿用共同材料，未由每位重复全文核查。

### Lei Zhang（张磊）

Agent：/root/panel_lei_zhang。暂定排序：A > B > C。

公开PiSA-SR有像素保真/语义细节两类调节；OSEDiff用低质输入取代随机噪声起点。操作语义须核实，降低随机性不等于真。
A谨慎继续，可独立。同成本事实目标下选择有意义，但物理SNR、饱和、融合、输入失配可解释反转；估计器影响最优选择本身已知。查NoiseOptimal目标函数；合法设置下重复选择变化且物理解释不足才加强判断。
B谨慎继续，条件独立。停止后的风险/新增数据纠错可核算，但低方差偏差旧，确定性恢复器没有同类seed信号。查OnePhoton的联合停止分析；武断阈值/挑图或已有直接覆盖则降级。
C合并诊断。生成适配现成reader也有效；未描述不能说不公平。查raw预处理/decoder/调参预算，跨reader、任务、噪声稳定分解且改变预算选择才独立。
排序A>B>C。质疑：信息严格占优时的反选究竟是任务偏好还是输入失配？

最值得交叉回答：局部观测信息严格占优的配置却被冻结恢复器反选，如何区分有意义任务偏好和输入失配？

补核来源：[来源1](https://www4.comp.polyu.edu.hk/~cslzhang/papers.htm)、[来源2](https://arxiv.org/abs/2412.03017)、[来源3](https://arxiv.org/pdf/2406.08177v2)。

### Michael S. Brown

Agent：/root/panel_michael_brown。暂定排序：A > B > C。

A谨慎继续。关注黑电平、曝光归一化、裁剪、去马赛克和tone-map混杂；等时间读出不等局部有效证据。NoiseOptimal已等成本物理SNR。统一标定/输出链后配置达标仍变且选择损失可解释才加强，常规融合解释则降诊断。
B合并诊断。固定测量seed算法变化与独立重新采集噪声不同；采集外层、seed内层、独立单位场景。先核OnePhoton独立采集还是固定观测多生成。同覆盖率、固定ISP、追加独立证据纠错才可升格。
C合并诊断。RAW→RGB必要链路混合信号恢复与接口适配。缺描述不能说不公平；BridgingGap早已分视觉/识别。核输入范围、归一化、threshold、拒识。跨reader/任务系统性改预算才主线。
潜力排序A>B>C；执行先C的公平控制。质疑：B追加数据纠错是否仅亮度/读出适配改变，因而与C同一现象？

最值得交叉回答：额外真实证据纠错是否只是改变亮度/对比度/读出输入分布？若不排除，B与C可能是同一机制。

补核来源：[来源1](https://www.eecs.yorku.ca/~mbrown/)、[来源2](https://www.eecs.yorku.ca/~mbrown/ICCV2023_Brown.html)、[来源3](https://people.csail.mit.edu/hasinoff/hdrnoise/)、[来源4](https://arxiv.org/abs/1901.09482)。

### Tianfan Xue（薛天帆）

Agent：/root/panel_tianfan_xue。暂定排序：B > A > C。

A谨慎继续。AdaptiveAE Fig5/Table3已明确融合器影响EV选择，不能拿一般交互/排序翻转当新意。残差是同冻结模型合法操作与事实目标的选择损失；可重复达标集合且物理解释不足才强化。
B谨慎继续，第一。停止后果可测，有观测软引导并不事实认证。查OnePhoton跨seed/coverage/追加观测的联合停止结果，不能只稳定错误图。
C合并诊断。reader预处理/量化接口先核查；未知≠不公平。跨reader归因规律才独立。
接口：UltraFusion加载器读取ue/oe两张RGB且可能缩放，不直接支持任意RAW栈。原生API strength=13层控制注入强度，steps采样路径；uncond=None时cfg_scale不走CFG分支，不能做有效CFG扫描。接口缺口不可算H0，不临时加方法补接口。
排序B>A>C。质疑：新增数据改变物理SNR/饱和，怎样分离生成机制决策影响？

最值得交叉回答：新增曝光同时改局部SNR与饱和覆盖，怎样将A反转/B纠错归因于生成机制的决策影响而不是已知物理HDR收益？

补核来源：[来源1](https://tianfan.info/)、[来源2](https://arxiv.org/html/2508.13503v1)、[来源3](https://arxiv.org/html/2501.11515v1)、[来源4](https://github.com/OpenImagingLab/UltraFusion/blob/main/dataset/test_dataset.py)、[来源5](https://github.com/OpenImagingLab/UltraFusion/blob/main/pipeline/V4_CA/pipeline.py)、[来源6](https://github.com/OpenImagingLab/UltraFusion/blob/main/utils/V4_CA/sampler.py)。

### Chongyi Li（李重仪）

Agent：/root/panel_chongyi_li。暂定排序：B > A > C。

此评议仅模拟其公开研究方向，不代表本人意见或背书。其主页强调真实条件下的可靠视觉、恢复、生成与应用。优先看真实退化下事实是否保留，以及质量指标能否支持采集决策。
A：PROCEED WITH CAUTION。恢复器放回采集链路可能产生实际曝光选择损失，但等时间/读出不等于等有效证据；饱和、读噪、归一化、融合均可解释排序。先验操作并不纯。需控制已知物理解释后跨独立场景的可预测选择损失。单场景反转/interaction显著不够。最近邻沿用Noise-Optimal Capture、AdaptiveAE、BIGPrior。
B：PROCEED WITH CAUTION，第一。已一致却应继续拍有明确决策后果。OnePhoton已预算/样本/任务，HalluGen已有测量一致错误，但不能等同跨seed。seed离散反映采样器覆盖，不等事实不确定性。先查每输入样本一致性与正确率配对；同覆盖率停止超标、额外独立观测纠错才增强判断。
C：MERGE-AS-DIAGNOSTIC。同reader对raw/恢复图有效但未分解归因；便宜非生成适配可缩差也不否定生成。核缩放/二值化/decoder，未详述不等于没做。跨任务/reader稳定分解规律才重考虑独立立题。
排序B>A>C。质疑：多个固定预算节点反复检查首次达标停拍后，风险保证是否仍成立？需区分生成信号失效与重复检查失效。

最值得交叉回答：固定预算风险校准在反复检查、首次达标即停止后是否仍有效？B需区分采样一致性盲区与重复检查失效。

补核来源：[来源1](https://li-chongyi.github.io/)、[来源2](https://arxiv.org/html/2610.02675v1)、[来源3](https://arxiv.org/html/2512.03345v1)。

### Jiawen Chen

Agent：/root/panel_jiawen_chen。暂定排序：A > B > C。

A谨慎继续，第一。曝光分配系统价值强；饱和、异方差、融合、归一化可解释翻转。Unprocessing显示处理链重要，设置不统称纯先验。先比较NoiseOptimal/AdaptiveAE目标约束；跨场景排除解释后选择损失可升格。
B谨慎继续，次。跨seed固定条件下共享错误可能不表现分歧；无合理停拍规则易成旧缺陷演示。核OnePhoton联合分析；同coverage校准后仍提前停止且独立追加证据纠错可升格，校准后消失降诊断。计入多seed部署成本。
C合并诊断。处理适配不是不公平证据。核raw定义、normalization、threshold、decoder；跨任务改变最低达标预算且分解贡献才提高。Classic Video Denoising含学习参数预测，非生成不等无学习。
排序A>B>C，未证新颖性。质询现实停拍规则及新增可辨识证据。

最值得交叉回答：现实有用的跨seed停拍规则是什么？共享偏差何以超出已知不确定性缺陷，新增测量带来什么可辨识证据？

补核来源：[来源1](https://people.csail.mit.edu/jiawen/)、[来源2](https://arxiv.org/html/1811.11127v1)、[来源3](https://arxiv.org/html/2504.03136v1)。

### Felix Heide

Agent：/root/panel_felix_heide。暂定排序：A > B > C。

A谨慎继续，第一。LuckyHDR物理因素联合处理支持链路决策；局部SNR不完整描述可辨识性。处理器没充分利用证据可翻转排序，不表示物理上限变了。核曝光/基准帧消融与NoiseOptimal。可复现事实风险变化、选择损失及物理解释余量才能推进。
B合并诊断。OnePhoton真逆向核与学到的近似条件分布有区别，seed只测算法变化，未证真实后验。采样塌缩/先验失配的稳定错误已知。核7.2/9联合事实/coverage/停止后果；同覆盖率多场景超额错误且新增观测纠错可升格。
C放弃当前独立题框架，保留baseline。OnePhoton同QR decoder端到端收益有效但未分解贡献。适配成熟，强baseline不自动论文。跨预算/reader归因稳定改变采集选择可重开。
排序A>B>C。质询物理有效信息与利用能力的区分。

最值得交叉回答：SNR/裁剪相近而事实风险不同，如何分离测量的事实有效信息与恢复器利用信息的能力？

补核来源：[来源1](https://www.cs.princeton.edu/~fheide/)、[来源2](https://light.princeton.edu/)、[来源3](https://arxiv.org/html/2604.19976v1)、[来源4](https://arxiv.org/html/2610.02675v1)。

## 三个实际交叉回合

三位在首轮完成后才收到其他 agent 的具体质询。其余三位首轮质询用于发起讨论，没有虚构它们的二轮回复。以下仍为编辑摘要。

### Lei Zhang（张磊）、Felix Heide → Felix Heide

质询：局部信息占优的配置被反选时，怎样区别任务偏好、模型失配和物理信息上限？

实际回复摘要：维持A谨慎、B诊断、C放弃当前独立框架。局部SNR高不是通道信息支配；同任务/损失/先验且已证明支配时，最优决策可忽略新增信息而不变差。冻结器反选先说明利用受限；若另换损失/先验/成本则比较条件改变。先核官方输入契约、训练退化、曝光归一化、元数据和操作数据保真语义；合法适配消除反选支持失配，未有对照不等排除失配。A只称明确冻结流程/分布内可达事实风险及采集决策损失，不称物理上限、单预算最低成本或Bayes最优界。

### Chongyi Li（李重仪）、Jiawen Chen → Michael S. Brown

质询：固定预算校准是否能保证首次一致即停的风险？怎样分开信号盲区、停止选择、处理链变化？

实际回复摘要：维持A谨慎、B/C诊断。固定节点边际校准不直接保证路径选择后的停止风险；正确模型且含完整停止历史的后验是另一对象，不笼统称optional stopping破坏后验。现实规则需检查节点、seed数、阈值/接受区，多seed推理读出等待成本与曝光分别报告。最便宜回放已有完整预算序列，每场景首次停点/错误/覆盖率；固定点同coverage的一致错误体现信号盲区，停止子集进一步风险升高体现选择效应。场景作单位。已有亮度/对比度/饱和分层、曝光归一化ISP固定；reader输入范围改善路径纠错不够新增事实证据归因。缺完整序列不能回溯停止风险。

### Michael S. Brown、Tianfan Xue（薛天帆）、Felix Heide → Jiawen Chen

质询：新增观测纠错是否只是输入适配或已知物理HDR收益？何时B独立、何时归入C？

实际回复摘要：保持A>B>C。核补材/代码/已有逐预算输出：新增观测是否伴随曝光归一化、tone-map、threshold、reader改变，seed是否仅作用同一观测。配置只识别混杂不证明机制；若有独立真值，查事实纠正而非拒识→解码成功。若亮度/对比度/噪声适配及公平非生成处理获得相同纠错，且校准后无额外停止损失，B降C诊断。若同coverage一致性规则反复提前停拍，新增真实观测纠正独立真值确认错误，适配解释不足，B才可独立。A先用SNR/饱和/传统融合解释，再看操作有无额外配置/达标变化，不求纯先验但记录语义；接受Felix流程损失而非物理上限限定。

## 本轮新增的、可查证的约束

**A 的宽泛表述已被直接最近邻覆盖。** AdaptiveAE §4.1 / Fig.5 明确讨论深度曝光融合模型对 EV 选择的不同影响，Table 3 还测试不同融合后端。因此，不能把“恢复器影响采集配置”本身作为新发现；当前残差只能收窄到同一冻结模型的合法设置、局部事实风险—覆盖率目标及实际选择损失。原文没有因此自动证明本候选要求的事实风险反转。[AdaptiveAE 原文](https://arxiv.org/html/2508.13503v1)

**UltraFusion 不能直接承担原定 RAW burst probe 的全部接口要求。** 本轮读到的官方测试加载器取 ue / oe 两张图并转 RGB；pipeline 的 strength 改 13 层 control scales，steps 改采样过程。该路径明确令 uncond=None，sampler 在此条件下直接调用 conditional model，故该路径的 cfg_scale 不构成有效 CFG 扫描。这是接口语义检查，不能把 strength 统称纯先验强度，也不能因接口不足判 H0。检查的是 2026-10-08 的 main 路径，未运行、未锁定 commit，其他版本需另核。[加载器](https://github.com/OpenImagingLab/UltraFusion/blob/main/dataset/test_dataset.py)、[pipeline](https://github.com/OpenImagingLab/UltraFusion/blob/main/pipeline/V4_CA/pipeline.py)、[sampler](https://github.com/OpenImagingLab/UltraFusion/blob/main/utils/V4_CA/sampler.py)

**跨 seed 的议题必须限定恢复器。** 张磊视角补核了带可调保真/语义路径的 PiSA-SR 与以低质输入为起点的 OSEDiff。B 不覆盖所有生成恢复器，也不能把确定性路径的稳定当作校准。[PiSA-SR](https://arxiv.org/abs/2412.03017)、[OSEDiff](https://arxiv.org/pdf/2406.08177v2)

**处理链应先进入解释基线。** Jiawen 视角核查 Unprocessing，强调 RAW 噪声经过增益、颜色与后续处理会影响恢复；它也指出 Classic Video Denoising 含学习式参数预测，非生成不等于无学习。[Unprocessing](https://arxiv.org/html/1811.11127v1)、[Classic Video Denoising](https://arxiv.org/html/2504.03136v1)

**“重复查看风险”不是新的统计概念。** 时间一致置信序列和在线选择后的校准已有专门理论；它们不是本任务的现成事实风险保证，但进一步压缩了 B 的新意。B 若要立题，必须证明具体采集/恢复/停拍策略的残差，而不能只重现选择偏差。[Confidence sequences](https://arxiv.org/abs/1810.08240)、[CAP](https://arxiv.org/abs/2403.07728)

## 综合判断与收敛后的问题

这轮不凭票数定题。A 的支持较多，但 AdaptiveAE 已覆盖其宽泛关系，且原先考虑的 UltraFusion 输入与开关并不能直接承担 RAW burst 对照；B 的停止后果有科学吸引力，但共享偏差、近似采样与序贯选择都是成熟风险。两者都需要比现象展示更具体的残差。

**暂维持 A 为优先文献核查对象，B 为有条件的科学备选，C 为两者必需的解释控制。** 这与“证明了 A/B 新颖”不同。Brown/Felix 将 B 置于诊断位的反对理由仍保留。

A 收窄为：在声明的相机、场景和同一冻结恢复流程内，合法操作是否使沿用物理指标或另一个操作设定选出的等成本曝光配置产生可重复的事实决策损失？测的是候选配置集合内、给定流程的损失；局部 SNR 较高不是信息支配证明。若合法适配或传统物理基线解释后消失，应降级。若只有排序翻转而无实际达标/选择后果，也不独立立题。

B 收窄为：一个有实际使用依据、计入推理成本的跨 seed 一致性停拍规则，在完整停止策略校准后，是否仍有事实风险盲区，而追加独立观测有可靠纠错收益？不能自行编一个很差的阈值再证明它失败。先区分固定预算信号不准、停止选择效应、接口适配、真实新证据；如果正确校准后失效消失，则诊断结论已经足够。

C 的地位是控制和归因：统一合法处理链、合适输入范围、公平调参预算，以及非生成处理/读出路径。非生成可包含已有学习式恢复；本阶段不训练新 reader。控制缩小收益不否认原系统收益；控制后仍有收益也不自动证明输出每个事实正确。

## 下一项单一行动

建立一张**直接证据与现成接口矩阵**，优先核对 AdaptiveAE 的融合器消融、Noise-Optimal 的目标/成本、UltraFusion 的合法输入/设置，以及 One Photon 的预算—样本—任务—停止联合结果和可用数据/代码。

每行必须从同一工作提取：真实输入、曝光/读出/增益成本、冻结后端、设置实际含义、局部物理解释、事实真值、错误/拒识、覆盖率、独立重复单位、是否已有采集选择或停止后果。未报告记“未报告”，不跨论文拼接因果，也不把缺数据当 H0。

出口只有两类：已有工作直接回答，候选降级；或保留明确残差并确认合法现成接口/已有数据足以检查。此后才决定是否启用原 Minimal Probe。现在不承诺生成网络、训练或新采集。

## 执行与证据边界

- 已完成六个独立首轮及三个定向交叉回复；只有后者的三个目标实际回复了交叉质询，没有声称六位全部参加二轮辩论。
- 没有真实教授参加；全部是按公开方向分配的 AI 视角。同家族 agent 的独立上下文有助于减少从众，不等于统计独立证据或跨家族审查。
- 没有采集、模型推理、训练或新实验。原 Minimal Probe 是备用，不被本报告启动。
- 前一轮 idea-discovery 的正式门控仍为 BLOCKED：helper / 跨家族审查路由缺失；本次讨论不冒称补齐该门控。
- 压缩记录和共同材料保存在工作目录；本报告提供用户可读结论。所有“未找到直接证据”均不是证明文献不存在。
