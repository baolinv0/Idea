# Independent DNG 2/4 versus 4/8 refinement audit

Audited 2026-10-09T00:46:29.710688+00:00. This is a same-family, provisional numerical audit. It is not an independent-family review receipt. No capture simulation, posterior table calculation, policy search, test run, or experiment was restarted; this audit reads the completed JSON/CSV files, recomputes summaries from their recorded scalar rows, and reads Git object identities. Main reports and source code were not edited.

## Verdict

PASS for artifact identity, unchanged control backends, unchanged point-posterior decisions, and reconstruction of the six camera-by-seed refinement summaries. No blocking artifact inconsistency was found within this scope. Precision improved, and the evaluated policy decisions/signs are stable between the 4-node and 8-node runs. Complete quadrature convergence is not established.

## Raw artifacts and identity

- relative-experiment-retry02: [results.json](C:/Users/Lenovo/Documents/Codex/2026-10-08/capturetm-plan-chatgpt-conversation-6ac72ce4-202c/outputs/CaptureTM_Local_DNG_20261009/relative-experiment-retry02/results.json) (SHA256 `208b6a45f2145f8ed2ec7c08a563a2274aa71d2fd642a8fd64d79a2c5de7a3b6`), [source_metrics.csv](C:/Users/Lenovo/Documents/Codex/2026-10-08/capturetm-plan-chatgpt-conversation-6ac72ce4-202c/outputs/CaptureTM_Local_DNG_20261009/relative-experiment-retry02/source_metrics.csv) (SHA256 `14f7aadd0aa98ede6ad25345ddef6b60f3d513a7df13626a4a3333debf6ec0cc`); recorded code commit `09052a605b8251c539a6dda3268f2b1f183a95c8`, status `completed_real_content_relative_diagnostic`.
- relative-experiment-refinement04_08: [results.json](C:/Users/Lenovo/Documents/Codex/2026-10-08/capturetm-plan-chatgpt-conversation-6ac72ce4-202c/outputs/CaptureTM_Local_DNG_20261009/relative-experiment-refinement04_08/results.json) (SHA256 `5b14e9af0f0869f55e9c8bc956e79f2a4638149c56cd8c777baac7794e74d6a1`), [source_metrics.csv](C:/Users/Lenovo/Documents/Codex/2026-10-08/capturetm-plan-chatgpt-conversation-6ac72ce4-202c/outputs/CaptureTM_Local_DNG_20261009/relative-experiment-refinement04_08/source_metrics.csv) (SHA256 `4ffccad6885bd0eb6ef71a58d4a0474bb6f27761fb3d068aba06c29915914a11`); recorded code commit `f465e73c883a3abe3f46dc5d380fbf985f408b58`, status `completed_real_content_relative_diagnostic`.

The protocol is `local-dng-green-relative-20261009-v1`, protocol SHA256 `372bcc3f5bd9529f0f45c443983ebae2d4db8a17a15f38b77fcf030ad22bf8be`, source-manifest SHA256 `542d9f0bcbe08a9da889cc3f8677f5bd4a1d3fd59d844ff7e83f3b5b28c09177`. Both reports contain exactly the same 68-entry per-source cache SHA256 map; all source cache fingerprints match. Camera training groups, all 258 prior masses per camera (256 interior bins plus two endpoint atoms), and endpoint masses are exactly equal. Both use seeds 19/37/73, four future repeats, 256 prior bins, pseudomass 1e-6, the same exposure actions, sensor assumptions, target, spatial window candidates `[1,3,5,7]`, and reported Python/NumPy versions. Only `nodes_per_bin` and `low_nodes_per_bin` differ within the config: 4/2 versus 8/4.

Although the recorded commits differ, Git confirms identical implementation blobs for both runs: `dng_relative_experiment.py` blob `40d88552d481bab875a64e02054a67289efa539c` and `continuous_reference.py` blob `5d069e48c087615f9b7bb142f4da5bbc47c98d69`. The integration and ADC implementation are therefore unchanged between these commits.

Both CSV hashes were independently recomputed and match their JSON declarations. Each CSV has 216 distinct rows with exactly the same row order and `(seed, camera, backend, source_id, group_id, split)` identities. Each camera/seed/backend contains 12 diagnostic source IDs and three diagnostic groups. The cache and source-map comparisons cover all 68 sources; the scalar CSV records diagnostic sources only.

## Control backends and decisions

All 144 inverse/local-Wiener CSV rows are exactly identical as parsed strings across every risk and action column. Their full JSON backend summaries, frozen rule metadata, development risks, fixed choices, diagnostics and intervals are also exactly equal. All six camera/seed per-action development-selected Wiener windows are unchanged.

For point posterior, all six development-fixed choices remain exposure 2 (action index 4). All 24 selected rule tuples `(feature, threshold, left, right)` and train-only threshold candidate arrays match exactly. All 72 diagnostic source rows retain the same fixed index and four policy actions (zero changes among 288 policy-action entries). The numerical development risk values change, as expected from refined integration; the frozen decisions do not.

The largest point-posterior change in a single recorded source/action risk is `4.380184941765036e-06`. Reconstructing every diagnostic action mean, fixed risk, policy risk, source-action count and policy gain from the CSV succeeds: maximum risk reconstruction error `0.000000000000000e+00`, maximum policy-minus-fixed difference reconstruction error `0.000000000000000e+00`. Gain formula checked as `(fixed_risk − policy_risk) / fixed_risk`.

## Six refinement summaries

| Camera | Seed | max abs(2−4) | max abs(4−8) | Ratio |
|---|---:|---:|---:|---:|
| iphone | 19 | 6.620319025750e-06 | 1.074645406249e-06 | 6.1605 |
| s25 | 19 | 4.079152105115e-07 | 2.780227107266e-08 | 14.6720 |
| iphone | 37 | 6.635846751813e-06 | 1.077071455297e-06 | 6.1610 |
| s25 | 37 | 3.678253765351e-07 | 2.777954291598e-08 | 13.2409 |
| iphone | 73 | 6.633071903440e-06 | 1.076787188192e-06 | 6.1601 |
| s25 | 73 | 4.011308617047e-07 | 2.795346991021e-08 | 14.3499 |

The global maximum decreases from `6.635846751812825e-06` to `1.077071455297289e-06` (factor `6.161009`). Each reported maximum equals the largest absolute entry of its seven-action low-minus-high vector. More strongly, independently recomputed old 4-node CSV group-action means minus new 8-node CSV means reproduce the new reported 4-minus-8 vectors within `1.128944992203957e-18`. This validates the bridge between the old high calculation and the refinement low calculation without rerunning either.

Action order: exposure multipliers `[0.125, 0.25, 0.5, 1, 2, 4, 8]`. Each vector is the mean of the three diagnostic group means, with sources averaged inside each group.

- iphone, seed 19: `[1.074645406249e-06, 5.975283535744e-07, 1.997723149431e-07, 1.862346829127e-07, 2.649604300002e-07, 7.891252317785e-08, -1.647020499653e-07]`.
- s25, seed 19: `[1.471018384855e-09, 9.185752201817e-09, 2.780227107266e-08, 2.200526878019e-08, 9.181251958764e-09, 2.625886386890e-09, 2.566233688897e-09]`.
- iphone, seed 37: `[1.077071455297e-06, 5.949059656639e-07, 2.021240170856e-07, 1.847221913432e-07, 2.572049425985e-07, 7.870493232084e-08, -1.697512474543e-07]`.
- s25, seed 37: `[1.855587255327e-09, 9.178242881250e-09, 2.777954291598e-08, 2.190657023510e-08, 9.627762074824e-09, 2.770672383789e-09, -3.919218038661e-10]`.
- iphone, seed 73: `[1.076787188192e-06, 5.910976228364e-07, 2.001388966494e-07, 1.840081846070e-07, 2.619161174513e-07, 8.191331131640e-08, -1.702870778133e-07]`.
- s25, seed 73: `[1.785867108447e-09, 8.725488041313e-09, 2.795346991021e-08, 2.249899151399e-08, 9.045702097233e-09, 2.816434059851e-09, 2.264785050782e-09]`.

These are differences between two finite integration rules for group-balanced scalar risks, not certified absolute errors against an exact integral, posterior-uniform error bounds, pixelwise error bounds, or statistical confidence intervals.

## Point-posterior gain signs

Positive values below mean a reduction relative to that same run’s frozen dev-fixed action. All 24 gain signs are unchanged. The largest absolute change is `0.071285122` percentage points.

| Camera | Seed | Feature | 4-node gain (%) | 8-node gain (%) |
|---|---:|---|---:|---:|
| iphone | 19 | mean_brightness | 18.321504385 | 18.282247725 |
| iphone | 19 | q99_brightness | 13.153178557 | 13.167568088 |
| iphone | 19 | temporal_noise | 25.446894431 | 25.432393571 |
| iphone | 19 | local_gradient | -44.360957658 | -44.432242780 |
| s25 | 19 | mean_brightness | 8.279123760 | 8.279543863 |
| s25 | 19 | q99_brightness | -18.433098279 | -18.430636274 |
| s25 | 19 | temporal_noise | 8.279123760 | 8.279543863 |
| s25 | 19 | local_gradient | -45.642589898 | -45.642293940 |
| iphone | 37 | mean_brightness | 18.387048882 | 18.348260541 |
| iphone | 37 | q99_brightness | 13.027694074 | 13.041741790 |
| iphone | 37 | temporal_noise | 25.470989988 | 25.456663014 |
| iphone | 37 | local_gradient | -43.829574645 | -43.898383189 |
| s25 | 37 | mean_brightness | 8.006457086 | 8.006831378 |
| s25 | 37 | q99_brightness | -18.683643282 | -18.681314176 |
| s25 | 37 | temporal_noise | 8.006457086 | 8.006831378 |
| s25 | 37 | local_gradient | -45.976109937 | -45.976045188 |
| iphone | 73 | mean_brightness | 18.421524860 | 18.382971585 |
| iphone | 73 | q99_brightness | 13.095735240 | 13.110322060 |
| iphone | 73 | temporal_noise | 25.508316503 | 25.494260166 |
| iphone | 73 | local_gradient | -44.178207562 | -44.247955028 |
| s25 | 73 | mean_brightness | 7.999492910 | 7.999877102 |
| s25 | 73 | q99_brightness | 6.460776338 | 6.461681390 |
| s25 | 73 | temporal_noise | 7.999492910 | 7.999877102 |
| s25 | 73 | local_gradient | -45.806369996 | -45.805952728 |

iPhone: mean/q99/temporal gains remain positive and local-gradient gains remain negative for all seeds. S25: mean and temporal remain positive; gradient remains negative; q99 remains negative for seeds 19/37 and positive for seed 73. That q99 seed dependence predates refinement and should not be described as an integration-induced sign reversal.

## Qualifications and remaining steps

No additional rerun is required to support the narrow statement “4/8 improved aggregate numerical precision without changing the evaluated decisions or gain signs.” A claim of full convergence would require a defined tolerance or an independent error argument, with additional numerical evidence where needed. A small aggregate difference can hide larger source/action differences; the current maximum single-source drift is recorded above. Low-minus-high signs are mixed, so this refinement is not a certified one-sided risk bound.

The comparison changes only integration resolution under the same empirical 1D prior. It does not test prior-bin/model approximation, H-aware restoration, an unrestricted image backend, camera calibration, independent real recapture, clean HDR ground truth, motion, or Bayer data. The original one-session, three-diagnostic-group, descriptive-CI and frozen-development-selection qualifications still apply. Noise seeds, repeats and crops do not increase independent scene count.

No execution-process exit-code receipt was independently obtained in this task; the completed JSON/CSV consistency is the audited evidence. This audit cannot replace cross-family evidence-gate receipts.
