# CaptureTM 讨论归档

归档日期：2026-10-09（Asia/Shanghai）。
研究题目候选：**固定目标下曝光选择收益：后端补偿与空间可预测性**。

[确定性结论](CONCLUSIONS.md) · [文献与工程资料](REFERENCES.md) · [完整挖掘报告](idea-stage/IDEA_REPORT.md) · [提案](refine-logs/FINAL_PROPOSAL.md) · [实验计划](refine-logs/EXPERIMENT_PLAN.md)


## 2026-10-09 追加查新结果

本轮裁决：**PROCEED WITH CAUTION，收窄问题新颖性 5.5/10**。允许推进最小决定实验，核心条件规律尚未验证。

[完整查新报告](novelty-check/NOVELTY_REPORT_20261009.md) · [方法级最近邻矩阵](novelty-check/PRIOR_ART_MATRIX_20261009.md) · [实际检索日志](novelty-check/SEARCH_LOG_20261009.md) · [全部查新材料](novelty-check/README.md)

## 已能确认的结果

1. 本次实际运行的是独立的标量/静态双像素 CPU 玩具模型，没有复现原仓库动作预算，没有 GPU、S24 真实训练或实拍。
2. 共同后端的局部分箱从 32×128 改为 256×256 后，两族最佳固定倍率由 4/1 变成 0.5/0.5；“稳定的族间物理最优曝光翻转”已撤回。
3. 256×256 有限后端下，利用已知线性先验、只看三张有噪预览的简单规则，在独立测试集比开发集选出的最佳固定曝光降低约 9.07%–9.45% MSE；范围限于该玩具分布。平均绝对改善约 1.94×10⁻⁵，小于示例 δ=10⁻⁴ 的等效容差。
4. 点式后端交叉实验没有搭档专属动作优势信号；不能称神经联合策略迁移已证。

每项结论的数据、代码、限制与撤回记录见 [CONCLUSIONS.md](CONCLUSIONS.md)。

## 复现

Python 3.12 环境，实际使用 NumPy 2.3.5。四个脚本保持原实现；后面两个共享实验导入同目录 pilot_mechanisms.py。它们不是完整 CaptureTM 训练程序。

~~~sh
python -m pip install -r requirements.txt
python pilot_mechanisms.py --outdir reproduced/pilots
python pilot_resolution_check.py --outdir reproduced/pilots-resolution
python pilot_shared_backend.py --outdir reproduced/pilots-shared
python pilot_shared_highres.py --outdir reproduced/pilots-shared-highres
~~~

固定种子为 19、37、73；原始输出保留在各 pilots 目录。不要覆盖原始文件，把复现结果写到 reproduced/。事后跨未来噪声取最小误差的 hindsight 统计，不是可实现 latent/causal oracle，不能用来声称策略 regret。

## 文件入口

- [10 个原始候选](candidate_pool.md)：编号不是最终新颖性裁决。
- [原始协议](RAW_PROTOCOL.md)：查新审阅输入；其中早期结果需结合最终结论阅读。
- [最新报告](idea-stage/IDEA_REPORT.md)、[HTML 阅读版](idea-stage/IDEA_REPORT.html)。
- [提案](refine-logs/FINAL_PROPOSAL.md)、[计划](refine-logs/EXPERIMENT_PLAN.md)、[执行状态表](refine-logs/EXPERIMENT_TRACKER.md)、[研究契约](idea-stage/docs/research_contract.md)。
- [历史查新](history/NOVELTY_CHECK_20261008.md)：保留当时判断，不覆盖最终数值复核。
- [实际论文身份核验](papers-verified.json)：只确认 7 个 arXiv ID 存在，不等于确认每项科学主张。
- [审阅记录与归档说明](ARCHIVE_NOTES.md)、[文件校验](SHA256SUMS.txt)。

## 下一步与状态

先做同输入连续/数值后验参考后端，再留出真实空间依赖强度，判断简单规则收益能否脱离分箱误差及已知先验。尚无必要新增 risk 网络或扩大 GPU。
科学精炼为 REVISE；查新与批判审阅都实际发生，但同属 OpenAI 系列，跨系列证据门 BLOCKED。归档已完成不等于科学假说已验证。
