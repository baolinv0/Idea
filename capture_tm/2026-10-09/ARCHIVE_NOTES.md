# 归档与版本说明

## 最新结论

以 [CONCLUSIONS.md](CONCLUSIONS.md) 为当前入口。候选池、RAW_PROTOCOL与历史查新保留时间线，不能从它们单独提取早期阳性主张。
没有上传密码、API密钥值、SSH连接配置、训练数据、模型checkpoint或第三方论文全文。GEMINI_API_KEY只作为当时工具失败的环境变量名称出现，不含值。

## Review Status

实际调用：候选生成/独立jury/查新 gpt-6-astra xhigh；批判与精炼 gpt-6-astra ultra。查新 PROCEED WITH CAUTION 5/10；末轮精炼 REVISE/PROCEED、成熟度4/10、新颖度暂评2–3/10（不是完整查新重评分）。
执行者与审阅者都属OpenAI，按当时运行规则“Same-family review is provisional, not cross-family evidence.” 不能将其记录为跨family接受。
[实际run state](.aris/runs/capturetm-20261008-run01.json)、[查新response](.aris/traces/novelty-check/2026-10-08_run01/response.md)、[批判response](.aris/traces/research-review/2026-10-08_run01/response.md)、[精炼response](.aris/traces/research-review/2026-10-08_run01/response-round2.md)。
证据门BLOCKED针对科学工作流验收，不表示文件不存在或禁止归档。上传资料不更改该状态。

## 可移植整理

本归档保留原创报告、脚本、数值JSON、真实reviewer身份与回应。移除本机绝对路径；报告中本机技能链接改为本说明。审阅请求中的本地目录替换成 <local-workspace>；其科学任务文本保持。
旧本机交付清单、绝对路径delivery_check和时间戳重复副本不上传；重新生成仓库相对路径SHA256清单。原数值内容和四个实验脚本逻辑不变，统一为UTF-8/LF。
本机完整工作流助手不作为复现依赖；只需NumPy运行四个CPU脚本。未打包源ISP仓库或第三方模型。

## Scope

toy：单色静态、标量/双像素，固定目标sqrt(L/(L+.5))、Poisson、4e读出噪声、1000e满阱、12-bit ADC；动作倍率.125/.25/.5/1/2/4/8。
不是源库12/24动作预算、原生Bayer、运动、S24训练或真实相机。数值结果不能跨层级升级为采集信息保真或新算法结论。

## 2026-10-09 决定实验增补

H-aware与DNG4/8完整正负结果、合成双像素风险NPZ和独立数值审计已追加。H-aware执行本地提交f465e73与已发布c6a3fb4的完整源tree一致；原7e080d3仍为初始工程审查参照。未上传真实DNG、照片、像素缓存或模型权重。

初次归档的路径整理和校验清单属于当时版本。后续原始JSON及准备的外审dossier保留实际本机路径，作为本地复现/审阅定位，不能据初次说明称当前所有文件已去除绝对路径。跨家族Claude提交被自动审批拒绝，未启动；旧OpenAI审阅仍为provisional，科学工作流gate仍BLOCKED。

SHA256SUMS.txt现在覆盖当前归档的Git-normalized字节（UTF-8/LF文本、原始NPZ），不含其自身。初次清单保留在history/SHA256SUMS_INITIAL_20261009.txt。Windows自动换行转换后的工作副本不作为该Git内容校验输入；GitHub ZIP/原始blob可据此校验。MANIFEST为文件目录，不表示投稿贡献或审核接受。

## DNG历史信息控制归档 2026-10-09

代码执行和已发布提交均ae7c762bf18461fb1fb673b81b0ab0bc33c3e78e，源tree2364997b680efdfc57c951c09f9f22b6271a55c0。追加三seed正式原始JSON/1152行CSV/退出记录、完整独立数值审计脚本与报告，以及最新未提交的两份dossier；没有原图、真实像素缓存、权重或凭据。此前被拒绝Claude尝试trace未改。独立审计当时记录的output_files包含可选作者summary.json；该临时汇总已折入canonical报告后删除，正式results/CSV/run_meta三文件均未改。门禁重跑仍BLOCKED，两项实际跨家族接受欠缺，prepared材料和同家族数值审计均不算接受。SHA清单覆盖当前Git-normalized文件，不含清单本身；初次清单保留。
