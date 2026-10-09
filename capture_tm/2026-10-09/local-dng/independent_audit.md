# CaptureTM local diagnostic independent audit

Date: 2026-10-09, Asia/Shanghai. Reviewer: independent Codex subagent in the same model family as the executor. This is a provisional code, numerical, and environment audit, not cross-family approval. No code was edited, no experiment was restarted, and no push was performed. No photographs are included.

## Verdict and blocking status

No unresolved blocking implementation defect was identified in the frozen N0/N1 calculation within its stated information set. The two numerical defects found in the relative-DNG posterior table were repaired by the root executor, and the latest seven regressions passed independently. The current code is usable for the narrow, explicitly qualified diagnostics. It does not support a fully optimized backend, unrestricted image Bayes bound, real-camera acquisition gain, expert-GT quality, clean HDR, Bayer reconstruction, neural training, or pristine formal-test claim.

The important remaining scientific claim blocker is the renderer information set. continuous_reference.py:181 accepts only the future ADC pair and known exposure. evaluate_costs at line 271 calls that interface; preview codes are discarded after extracting policy features at lines 402 and 412. The computed mean is E_train[T(L)|Y_e,do(e)] under the fixed training prior. With adaptive A=pi(H), a renderer observing only (Y,A) generally needs P_train(A=e|L) as a prior-selection factor. A renderer observing actual history needs E_train[T(L)|H,Y,A]; when A is determined by H, A adds no information once H is given. The current renderer uses neither conditioning route.

This is a valid common fixed-renderer comparison of specified systems, but it cannot establish that a sufficient backend using available previews still needs the policy. An H-aware posterior is required to test that stronger statement, under a separate explicit protocol; the effect on policy gain is unknown.

A constructed information-set probe confirmed the difference without using photographs or conducting a new policy-risk experiment. For the same future codes [4095,4095] at permitted exposure 8, the current renderer returns [0.5407667854,0.8527372271]. Multiplying the original physical likelihood by three .25-exposure preview likelihoods gives [0.4563889988,0.8298366935] with history [[130,1100]] repeated three times and [0.5598605186,0.8691737120] with [[220,1600]] repeated three times.

## Physical likelihood and integration

capture_codes at lines 234–237 draws actual Poisson electrons, adds independent Gaussian read noise, clips to [0,1000] electrons, and rounds 4095 times the normalized result. Shot noise is not approximated as Gaussian. Analog and digital gains are one.

ADCLikelihood at lines 83–140 uses the correct ADC half-cell boundaries: zero includes negative-read clipping and all signal below 1000*.5/4095; the top code includes signal at or above 1000*(4095-.5)/4095. Continuous read noise makes round-to-even ties probability zero. Interior cells use stable CDF/survival differences. Integer counts through 1032 are explicit; the complete Poisson survival function above 1032 is assigned to the top code. The retained read kernels and upper-tail approximation have the stated conservative absolute per-cell error 3*Phi(-8)=1.8662881723e-15, excluding floating-point error. This is not a relative likelihood or posterior error guarantee when evidence is extremely small.

Uniform-marginal Gauss–Legendre integration is correct. Product-prior evidence and target moments factor into two one-dimensional integrals; copula evidence and moments use a single paired integral. The mixture weights and posterior component probability at lines 205–217 are correct. Rotation quadrature splits at its discontinuity. Linear, reverse, and rotation maps preserve uniform marginals.

Actual result-file likelihood normalization error is 2.9287683390e-13. The 256-versus-512 comparisons have maximum absolute action-mean risk difference below 9.14e-19 and maximum source/action cost difference below 5.12e-17 across all three seeds and both populations. This supports convergence on the realized draws and selected rules, not all possible observations. The code correctly calls the highest node count a numerical reference rather than a proof of exact convergence.

## Independence, frozen selection, and confidence intervals

sample_sources creates IID two-pixel latent pairs and does not return component IDs. Thirteen spawned streams separate source generation, previews, future captures, and bootstrap draws for train/development/N0/N1. Repeated future draws remain nested within an independent source. Future draws are independent of policy previews; evaluation policies use observed preview features plus frozen rules only.

Train quantiles .1 through .9 define threshold candidates. Development expected costs select the threshold, two actions, and one fixed action. Brightness and temporal-noise controls have equal threshold/two-action capacity. Empty development partitions are excluded. Diagnostic costs do not enter selectors. Rules freeze once at selection nodes and are reused for all node comparisons and both populations. N1 switches actual dependence to reverse at unchanged mixture weight and preserves marginals; the renderer keeps its training prior. This is a known toy dependence shift, not unknown image-prior or real-camera generalization.

paired_bootstrap resamples paired independent-source differences after averaging future repetitions. Intervals are conditional on the frozen rule and finite realized future captures. They omit train/development selection uncertainty, are not cross-seed intervals, and are not simultaneous multiplicity-adjusted intervals. future_mc_se_by_action correctly estimates the conditional noise contribution to action means. There is no directly paired residual-versus-brightness interval or interval for percentage reduction. Separate policy-versus-fixed intervals do not prove policy-versus-policy significance.

The hindsight minimum is properly named hindsight_min_realized_future_cost and identified as using unavailable future noise. Ground truth is the fixed analytic transform of sampled latents; it is not generated from predictions and no prediction-dependent score normalization is present.

## Direct result-file check

Read directly: outputs/CaptureTM_Local_DNG_20261009/continuous-reference/results.json. Configuration: seeds 19/37/73; 2048 train sources; 4096 development sources; 8192 sources per diagnostic per seed; 16 future repetitions; nodes 64/128/256/512; selection nodes 512; 2000 bootstrap replicates; chunk 256; likelihood chunk 64.

Residual-rule reductions versus development-selected fixed exposure .5 are 7.3806%, 7.6193%, 8.4310% for N0 and 14.8816%, 15.5976%, 16.5146% for N1. All six paired absolute-difference intervals versus fixed are negative. These numbers support the restricted-renderer simulation comparison only.

The N0/N1 JSON does not itself contain a Git commit. The initial audited checkout was 5c72145f4d11daf4779a0620babe1818921c895d. Retain external command/commit/exit linkage, or include it and the protocol hash in future JSON. This audit did not independently witness the larger CLI process start or restart it.

## DNG source and crop integrity

The frozen protocol groups source pairs before cropping, with both cameras of a pair sharing one group and split. validate_groups at dng_audit.py:82–100 rejects duplicate groups/pairs and incomplete coverage. Source hashes are checked across splits at lines 191–195. Only processed stacked linear RGB is accepted; this diagnostic rejects Bayer/CFA input. Files named GT are only existence-checked and remain unused with unverified provenance.

I inspected the existing aggregate dng_audit.json, local cache manifest, and numeric cache properties without exporting pixels. All 68 arrays are finite, bounded in [0,1], and shaped (8,64,64). All crop coordinates fit recorded source dimensions. The actual protocol SHA256 matches audit and cache metadata; source IDs, cameras, groups, splits, and source hashes agree between audit and cache manifest.

Counts: 34 pairs, 68 DNGs, 68 distinct DNG file hashes, 11 declared background groups. Source counts train/development/diagnostic are 28/16/24; group counts are 6/2/3. All decoded buffers are RawType.Stack. Thirty-four reported white levels are 65535, thirty-four are 4095, and all black levels are zero. Metadata contains 68 processed-linear-RGB IFDs plus non-raw previews. No source hash or declared group crosses a split.

These verify current file identity, declared splits, and crop validity. They do not establish independent locations/capture sessions or independently re-decode original pixels to prove cache derivation. Manual scene grouping is conservative but unproven. Crops, frames, both cameras, and noise repetitions do not increase independent scene count.

The input remains processed, already noisy and potentially clipped green DNG content. Synthetic relative re-exposure does not recover original scene radiance or calibrate cameras. There is no Bayer RAW, clean-HDR, expert-GT, physical recapture, original CaptureTM catalog, or formal S24 evidence. The single-session, three-diagnostic-group bootstrap is descriptive.

## Relative-DNG defects, repair evidence, and scope

Original table code required positive double-precision evidence for every ADC code. At exposure .125, source support [0,1] implies maximum Poisson mean 125; P(ADC=4095|mean=125) underflows to zero. A prior-density floor cannot solve numerical underflow. Root independently observed a CLI failure and committed 34b98c43b66ea576de455fb9a0e5630c9c002d5e while this audit was running.

Repair 34b98c4 rescales the same sparse Poisson/read/ADC kernel using logpmf/logsumexp and preserves the complete upper Poisson tail. Its positive-series remainder bound is valid because subsequent Poisson ratios decrease. Independent 65-digit Decimal full-tail checks gave log-tail absolute errors 4.55e-13 at mean 50, zero at 125, and 1.14e-13 at 500. The synthetic two-bin prior generated a finite 7x4096 table. No Gaussian replacement was introduced.

A second edge remained: positive subnormal evidence could retain ordinary arithmetic while its numerator underflowed. With prior [0,.5,.5,0], four nodes per bin, and exposure .125, 178 cells had positive evidence below 1e-290. The maximum ordinary-versus-log-scaled prediction difference was .8116460064 at ADC 3121. Such codes are astronomically improbable under this bounded simulation, so this did not demonstrate incorrect measured risks, but it invalidated all-code numerical correctness.

Root then committed 5bc80cf9cbf03c6a1a5dfaaa61709bde87082434. Current posterior_tables:123 uses ordinary arithmetic only for evidence >=1e-250 and original-kernel log scaling below it. The new code3121 regression compares with the log-scaled result and requires a prediction above .8. Seven updated relative-DNG tests passed independently in 3.60s, exit 0. No unresolved blocker remains from these two findings.

The empirical prior uses training sources only, balances groups, retains endpoint atoms, and discloses the small density floor. Composite quadrature weights are correct. The full-code lookup does not merge ADC observations, but is still a numerical posterior within an estimated one-dimensional prior. Wiener filters use dimensions (1,1,window,window), so repeats and patches are not mixed. Preview features use observed noisy previews. Camera-specific windows, fixed actions, and thresholds use development costs only. The unclipped noiseless inversion check is explicitly outside the clipped ADC model. Noise parameters are engineering assumptions, not camera calibration.

Static selection dataflow has no diagnostic-risk input. Nevertheless source_risks precomputes all splits before selectors run. Literal protocol wording “freeze before diagnostic risk” differs from that order. Describe this honestly as precomputed counterfactual risks followed by train/development-only selection and frozen diagnostic summaries; do not claim diagnostic costs were never computed before freezing. This is no identified selection leakage.

The relative-DNG process was active during this audit. I did not wait for missing output or label it failed, and do not certify its eventual risk numbers here.

## Fresh agent follows documented environment

Read .aris/compute/local.md and executed its entire PowerShell invocation verbatim from the primary repository. Ordinary execution failed before process creation with helper_unknown_error: setup refresh had errors. Authorized escalated execution succeeded. No install or rebuild occurred. Resolved-spec SHA256 independently matched e8b4ddc1227e9ddb1f16cca49db5586abb3a8c4696825e7738076ebb6408e9b8.

The documented invocation exited 0 and wrote work/capturetm-local-dng/fresh_doc_witness.json. Actual outputs:

- Python 3.12.14; NumPy 2.3.5; SciPy 1.18.1; rawpy 0.27.1; tifffile 2026.9.20.
- Seed19 Poisson(100), 32 draws, sum3146; Normal CDF(0)=.5.
- Integral x² on [0,1]=.33333333333333337; estimated quadrature error3.700743415417189e-15; witness PASS.
- test_continuous_reference.py plus test_dng_audit.py: 20 passed in3.09s.

The package/kernel claims match the ledger. Its stored status was AGENT_FOLLOWS_DOC_PENDING when read; this actual fresh-agent witness now exists, without silently rewriting the ledger. CPU utilization/count, CUDA/GPU capability, neural validation, and camera calibration are not established by these kernels. The witness does not independently assert imagecodecs/pytest pins or actual thread counts.

Other observed tests: the original four relative-DNG tests passed in1.90s; six after34b98c4 passed in2.76s; seven after5bc80cf passed in3.60s. All these commands exited0. A deliberately strict probe expecting the old table failure instead raised its own assertion after the concurrent root repair had already replaced that code; subsequent explicit inspection and numerical checks superseded that probe. It is not attributed as a failure of the repaired implementation.

## Optional improvements and limitations

1. Add explicit H/selection-conditioning exclusions to N0/N1 protocol/report limitations and preserve current results as restricted-renderer evidence. Treat H-aware work as a new protocol.
2. Add direct paired policy-versus-policy comparisons before asserting that a residual feature is significantly better than brightness. Selection and finite-noise uncertainty need their own scope.
3. Preserve exact run/commit/protocol linkage. Current source tests and kernel witness are not a substitute for larger-run execution records.
4. Relative-DNG load-time validation checks only protocol hash. Validate cache source rows/content provenance too; current metadata/shape checks passed, but future stale-cache substitution could otherwise be silent.
5. DNG audit/cache writers permit overwrite. Fresh directories or exclusive writes would better preserve evidence; no improper current overwrite was established.
6. Highest-node convergence and absolute cell-tail bounds do not imply uniformly accurate rare-event posterior inference.
7. This same-family provisional audit cannot satisfy an external cross-family integrity gate.

Acceptance: documented invocation and physical/numerical tests passed; repaired relative-DNG regressions passed. Use N0/N1 only with the common restricted-renderer, finite-simulation, and conditional-interval qualifiers. Strong-backend and real-camera manuscript claims remain unsupported.

