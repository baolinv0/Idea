# vivo 影调色彩研究：已验证结论与证据边界

本页为 vivo 照片 **SDR** 研究的结论归档，不构成本目录既有 HDR 恢复研究的实验结果。来源为独立的 [vivo-aesthetic-tone-color 项目](https://github.com/baolinv0/vivo-aesthetic-tone-color)，保留原研究范围与未验证项。

归档来源：[原结论文件](https://github.com/baolinv0/vivo-aesthetic-tone-color/blob/a3ff28668eb136508b31f56606a5f20c71a3dbe1/docs/aesthetic_v2/VERIFIED_CONCLUSIONS.md)，冻结源提交 `a3ff28668eb136508b31f56606a5f20c71a3dbe1`，源文件 Git blob `9d00ae80f5a2e00cc5ebf7d6ba9a0f735777c562`。只调整本页标题、来源说明和三个链接，未修改科学结论或表内数值。完整原始实验数据仍保留在来源仓库，本目录仅上传结论与证据链接。代码修改见[原项目草稿PR #1](https://github.com/baolinv0/vivo-aesthetic-tone-color/pull/1)。

登记日期：2026-10-09（Asia/Shanghai）。本页整理截至算法与结果基线 `04b901aaf4e2301009d1c24e486d7c6c3c6d8082` 的已验证结论。研究顺序为先比较效果，再考虑效率。这里的“确定性”指结论有明确代码或实际执行证据，不表示所有设备、运行与场景均逐位一致。

完整原值和失败记录见[机器可读结果](https://github.com/baolinv0/vivo-aesthetic-tone-color/blob/a3ff28668eb136508b31f56606a5f20c71a3dbe1/docs/aesthetic_v2/quality_pilot_results_20261009.json)，图像、运行与研究判断见[效果结果报告](https://github.com/baolinv0/vivo-aesthetic-tone-color/blob/a3ff28668eb136508b31f56606a5f20c71a3dbe1/docs/aesthetic_v2/QUALITY_PILOT_RESULTS.md)，执行前设计见[研究合同](https://github.com/baolinv0/vivo-aesthetic-tone-color/blob/a3ff28668eb136508b31f56606a5f20c71a3dbe1/docs/aesthetic_v2/QUALITY_FIRST_RESEARCH.md)。

## 1. 三组候选比较已实际完成

| 比较 | 完整12MP输出 | 完成150步的逐图拟合 | 实际执行 |
|---|---:|---:|---|
| style0/1/2、B＋全局CbCr、C＋全局CbCr、C＋空间CbCr | 18/18 | 9/9 | [首轮](https://github.com/baolinv0/vivo-aesthetic-tone-color/actions/runs/37857970636)＋[核验后续算](https://github.com/baolinv0/vivo-aesthetic-tone-color/actions/runs/37863221218) |
| C-spatial的guide4/guide1 | 9/9 | 6/6 | [引导对照](https://github.com/baolinv0/vivo-aesthetic-tone-color/actions/runs/37862183610) |
| C-spatial/guide4的保护λ0/λ10 | 9/9 | 6/6 | [裁剪保护对照](https://github.com/baolinv0/vivo-aesthetic-tone-color/actions/runs/37865352178) |

六路线首轮只有12/18输出及6/9拟合，第三源因累计计算窗口耗尽而未完成。续算校验输入、参考、模型、controls、输出及完整有限历史，复用旧两源六次拟合，只新算第三源三次；不将复用成果称作新计算。后两组在自己的run内各重新拟合两路，未拼接旧run作为配对baseline。三个实验仍使用同三个已见户外VAL源，不是新增独立场景或36张独立照片。

style0/1/2为上游已有训练权重；投影是逐图优化控制，不是新训练的控制预测模型。B/C均有空间影调网格，global只指色彩映射；各表示容量不同，不能把此矩阵当作等容量贡献证明。

## 2. 原亮度引导确实没有覆盖全部深度

限定当前线性RGB输入域[0,1]、Rec.709亮度、guide4、深度D=8、align_corners=True：

`u = log(1+L)/log(5) ≤ log(2)/log(5) = 0.4306765581`；
连续深度索引 `k = 7u ≤ 3.0147359065`。

按0起始编号，planes5–7没有直接图像插值采样，plane4只在极高亮度处有少量权重。三个实际源的750,000像素插值统计也记录planes5–7的正直接权重像素数为0。未采样层仍受平滑正则，controls非零不能反推直接图像监督或有效自由度。

guide1的三源实测在全部八个planes都有正采样，但两个源最终拟合total更高；三个源在两个裁剪前节点的新增越界比例，以及影调修改的log-luma TV，均高于同run guide4。**增加覆盖是已验证的结构变化；稳定质量收益没有被本轮支持。** 默认guide4保留，guide1仅为研究选项。公式推导适用上述输入域和插值设置，不外推到未裁剪HDR输入。

## 3. 裁剪保护确实减少本组三源的新增越界

固定同源输入/参考、style0权重、C-spatial/guide4、seed42、150步、lr=.03与reference_strength=.5，λ0/10在同run内每源初始distribution完全相同。

定义逐RGB通道的 `E(z)=relu(-z)+relu(z-1)`。在 `ltm_preclip` 和 `pre_gamma` 分别计算 `mean(relu(E(candidate)-E(baseline.detach())))`，两节点之和乘λ加入原目标。保护权重10是未校准的固定探索值。

| 源 | pre_gamma新增越界像素：λ0→10 | ltm_preclip新增越界像素：λ0→10 |
|---|---:|---:|
| img_0000 | 0.3776% → 0.1801% | 0.2276% → 0.0987% |
| img_0001 | 0.8411% → 0.0716% | 0.1924% → 0.0315% |
| img_0002 | 0.1473% → 0.0240% | 0.1367% → 0.0331% |

这些比例都在750×1000的quarter可微渲染测量：任一候选RGB通道越界，且同节点baseline像素此前无通道越界，计为新增像素。六个保护后比例均下降并低于0.5%，**不是12MP裁剪前节点测量，也不是全图资格或美学通过**。已有baseline越界可能保留；软损失测量越界幅度增加，不保证新增越界像素计数阈值。

distribution在源0/2降低、源1升高；源0的修改log-luma TV与laplacian P95增加。各项原值已保留，结构指标尚未校准；不能由这些指标选定整体画质赢家，也不能跨λ用包含不同保护项的total排名。因此保护λ10保留为下一轮教师目标候选，默认权重仍为0。

## 4. 全图分位数目标不能单独约束语义位置

当前全图亮度及各RGB通道的分位数数据项，对RGB像素向量的共同位置置换保持不变。它们能描述明暗和颜色分布，但单独不能判别人脸、天空或物体的颜色应出现在哪些位置。亮度数据项提供部分跨通道约束，仍不能唯一恢复完整RGB联合分布。增加空间网格参数不会自动消除这个目标的不可辨识性。

这项性质只针对上述分位数数据项，不能外推到包含空间正则的完整优化目标；本轮未新增真实区域语义效果。后续仍需比较真实来源的区域目标、细节与保持约束，并在未见场景检查肤色、物体色、光照结构与偏好。已有keep-mask路径与区域目标入口不能代替真实mask来源或对应关系。

## 5. 默认兼容与失败证据保存已通过检查

[上述基线提交CI](https://github.com/baolinv0/vivo-aesthetic-tone-color/actions/runs/37869554639)为653 passed、2 CUDA skipped、5 warnings，原六路线、引导、保护、续算四条functional self-tests均实际通过。

- 在真实小尺寸renderer＋Adam的受控fixture中，独立旧目标oracle、默认及显式λ0各执行150步，history与三类controls逐值/bitwise一致。该证据不等于真实照片跨run逐位复现。
- 正权重的越界梯度、已有越界、非法权重、节点形状/有限性契约、保存与重放检查通过；λ0跳过新增损失路径。
- 三条拟合脚本在native调用前保存完整拟合证据和controls。强制native异常fixture均验证150步拟合计数为1、ready输出为0、native只调用一次，且保存内容checksum可回读。
- 已完成且有限的150步拟合计数独立于输出ready状态，原失败仍进入记录；不以requested步骤或缺失输出伪造完成状态。

相同配置存在跨run浮点和post-fit差异，原值未覆盖。只读检查未发现固定BGU的float64 retry修改默认dtype、线程、精度或RNG等全局状态；这仅排除所查代码的状态泄漏假设，没有解释差异或证明跨设备可复现。独立review的实现、计数与报告意见已修复。

## 当前可以据此作出的研究决定

保留原默认与全部已验证对照，把C-spatial/guide4＋λ10继续作为质量目标候选；先验证细节/保持及真实区域目标，再形成可靠教师并比较少数控制预测模型。效率和手机部署在效果阶段之后研究。

目前没有新控制预测训练、真人美学胜率、未见TEST或全场景效果结论。当前接入在WB/CCM后已裁剪为线性[0,1]，无法由本轮算法恢复此前丢失的高光；照片SDR证据不能扩展为HDR、视频或Live效果。

完整PNG、固定512×512 crops、controls与诊断保存在结果报告链接的GitHub Actions artifacts，保留期至2026-10-22/23左右；仓库中的文字结论、原始数值JSON与执行身份可随Git提交长期追溯。artifact过期后不能仅凭文字声称重新核验了完整照片。
