# DNG history-control independent code and numerical audit

**PASS_WITH_SCOPE_LIMITS**. Same-family independent code/numerical audit; not cross-family review or novelty verdict.
Frozen source commit ae7c762bf18461fb1fb673b81b0ab0bc33c3e78e, tree 2364997b680efdfc57c951c09f9f22b6271a55c0. Formal exit 0; internal 203.385142s; launcher 205.674104s.

## Provenance and functional checks

- Verified all 68 actual original DNG byte hashes, cache byte hashes, frozen source identities/splits, protocol/manifest hashes and legal actions. Original source counts: train 28, development 16, diagnostic 24.
- Runner outputs results.json/source_metrics.csv/run_meta.json. A post-run root summary.json also exists and was excluded from this audit; no real H/future/source pixel array was exported.
- Renderer receives H plus only one future repeat, known e and no target/latent/source identity. Changing another repeat or patch cannot change this prediction.
- Same 2D window is used for fusion signal moments and local nominal noise mean. No repeat/patch filtering.
- Observed top code 4095 loses its weight; zero code retains weight. All-weight-zero case gives finite estimate 1/variance 1 and spatial processing preserves estimate 1.
- Independent explicit WLS: 35 probes, maximum estimate error 4.441e-16, variance error 0.000e+00; manual sliding-window spatial: 140 probes, maximum tone-target error 8.660e-15.
- Independently rebuilt all 204 seed/source H captures/features; codes and new/legacy feature vectors exactly agree. No seven-action formal future simulation was rerun.
- Committed necessary tests: 13 passed, exit 0.

## Legacy and paired statistics

- All 144 H-blind diagonal source rows match both retry02 and refinement04_08 exactly for seven action costs, fixed actions and four policy actions.
- Blind full frozen rule dictionaries, development action risks and Wiener windows match original output.
- Directly recomputed 96 matrix cells and 768 paired CIs from 1152 source CSV rows; verified 96 train-only threshold sets and 4608 diagnostic rule actions from independently rebuilt H.
- Every cross cell retains its SOURCE selector fixed action and threshold actions; the renderer retains its own frozen development windows. No cell-specific fixed action reselection.
- Average sources within each of g04/g06/g10 first, then give the three groups equal weight. Bootstrap samples groups, not crop/noise/source copies.

| Quantity | Maximum absolute error versus raw results.json |
|---|---:|
| action_risk | 0.000e+00 |
| fixed_risk | 0.000e+00 |
| policy_risk | 0.000e+00 |
| CI_mean | 0.000e+00 |
| CI_endpoints | 0.000e+00 |
| CI_group_values | 0.000e+00 |

Actual all-weight-zero counts at all seven actions: seed 19 [0,0,0,0,0,0,0], seed 37 [0,0,0,0,0,0,0], seed 73 [0,0,0,0,0,0,0].

## H-aware own-backend outcomes

Gains compare each selector with its own dev fixed e. Negative means worse. Direct paired difference is rule minus mean-brightness; negative favors the named rule. Intervals are descriptive.

| Camera | Seed | Backend | Fixed e | Rule | Gain vs fixed % | Direct difference vs mean | Direct paired 95% CI | Frozen e left/right |
|---|---:|---|---:|---|---:|---:|---|---|
| iphone | 19 | H_aware_classical_fusion | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_classical_fusion | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_classical_fusion | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_classical_fusion | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_fusion_Wiener | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_fusion_Wiener | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_fusion_Wiener | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 19 | H_aware_fusion_Wiener | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| s25 | 19 | H_aware_classical_fusion | 4 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 19 | H_aware_classical_fusion | 4 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 19 | H_aware_classical_fusion | 4 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 19 | H_aware_classical_fusion | 4 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 19 | H_aware_fusion_Wiener | 4 | mean_brightness | 0.257375 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/8 |
| s25 | 19 | H_aware_fusion_Wiener | 4 | q99_brightness | -0.368834 | 1.13131519e-06 | [-8.63385506e-06, 8.08243514e-06] | 8/4 |
| s25 | 19 | H_aware_fusion_Wiener | 4 | temporal_noise | 0.000000 | 4.64976040e-07 | [0.00000000e+00, 1.39492812e-06] | 4/4 |
| s25 | 19 | H_aware_fusion_Wiener | 4 | local_gradient | 17.465643 | -3.10886335e-05 | [-8.46320455e-05, 0.00000000e+00] | 8/4 |
| iphone | 37 | H_aware_classical_fusion | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_classical_fusion | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_classical_fusion | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_classical_fusion | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_fusion_Wiener | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_fusion_Wiener | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_fusion_Wiener | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 37 | H_aware_fusion_Wiener | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| s25 | 37 | H_aware_classical_fusion | 4 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 37 | H_aware_classical_fusion | 4 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 37 | H_aware_classical_fusion | 4 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 37 | H_aware_classical_fusion | 4 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 37 | H_aware_fusion_Wiener | 4 | mean_brightness | 0.246683 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/8 |
| s25 | 37 | H_aware_fusion_Wiener | 4 | q99_brightness | -0.163553 | 7.39052597e-07 | [-9.32126251e-06, 8.16104289e-06] | 8/4 |
| s25 | 37 | H_aware_fusion_Wiener | 4 | temporal_noise | 0.246683 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/8 |
| s25 | 37 | H_aware_fusion_Wiener | 4 | local_gradient | 17.211664 | -3.05629767e-05 | [-8.23676677e-05, 0.00000000e+00] | 8/4 |
| iphone | 73 | H_aware_classical_fusion | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_classical_fusion | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_classical_fusion | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_classical_fusion | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_fusion_Wiener | 8 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_fusion_Wiener | 8 | q99_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_fusion_Wiener | 8 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| iphone | 73 | H_aware_fusion_Wiener | 8 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 8/8 |
| s25 | 73 | H_aware_classical_fusion | 4 | mean_brightness | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 73 | H_aware_classical_fusion | 4 | q99_brightness | -29.033013 | 4.38870201e-05 | [3.04401527e-05, 6.19170832e-05] | 4/2 |
| s25 | 73 | H_aware_classical_fusion | 4 | temporal_noise | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 73 | H_aware_classical_fusion | 4 | local_gradient | 0.000000 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/4 |
| s25 | 73 | H_aware_fusion_Wiener | 4 | mean_brightness | 0.252431 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/8 |
| s25 | 73 | H_aware_fusion_Wiener | 4 | q99_brightness | -0.236130 | 8.83389127e-07 | [-8.94201692e-06, 7.94186573e-06] | 8/4 |
| s25 | 73 | H_aware_fusion_Wiener | 4 | temporal_noise | 0.252431 | 0.00000000e+00 | [0.00000000e+00, 0.00000000e+00] | 4/8 |
| s25 | 73 | H_aware_fusion_Wiener | 4 | local_gradient | 17.280073 | -3.07884503e-05 | [-8.34233338e-05, 0.00000000e+00] | 8/4 |

## Frozen-rule degeneracy and renderer-dependent signs

- iphone, H_aware_classical_fusion: 12/12 globally constant rules; 12/12 exactly equal their source dev fixed.
- iphone, H_aware_fusion_Wiener: 12/12 globally constant rules; 12/12 exactly equal their source dev fixed.
- s25, H_aware_classical_fusion: 11/12 globally constant rules; 11/12 exactly equal their source dev fixed.
- s25, H_aware_fusion_Wiener: 1/12 globally constant rules; 1/12 exactly equal their source dev fixed.
- 48 seed/camera/selector/rule combinations change sign of rule-minus-source-fixed when replayed through different renderers. Complete cases and all 96 cells are in the JSON audit.

## Limits

- Approximate data-dependent WLS with uncalibrated unclipped independent-noise variance; estimated/censored weights and clipping bias remain.
- Local Wiener is a classical simplicity control, not a strong unrestricted image Bayes bound.
- Same processed noisy/clipped surrogate, not clean radiance, expert GT, physical recapture or S24.
- Only three diagnostic groups from one session; camera/crop/noise copies add no independent scenes.
- 768 CIs are descriptive, conditional on frozen development selections, not independent discoveries.
- Same-family audit does not replace the pending cross-family novelty and critical reviews.

No implementation or paired-summary mismatch found in this frozen diagnostic. Constant or worse residual rules do not establish complex AE necessity; surviving gains are conditional on these classical backends, uncalibrated sensor assumptions and three backgrounds.

Audit command: task venv Python work/capturetm-local-dng/dng_history_control_independent_audit.py. No calls to cross_evaluate/paired_cluster_ci, selector refit, formal future rerun or experiment/dataset writes.
Audit elapsed 21.700266s. Exit 0 after assertions. JSON SHA256 767c85777dc1b98b2b60941ca65039e01f324d252ce55ff93fec9fbe36dd8859.
