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
