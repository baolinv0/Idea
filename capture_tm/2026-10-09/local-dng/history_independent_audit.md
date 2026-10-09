# History-aware CaptureTM independent audit

Date: 2026-10-09, Asia/Shanghai. Audited commit: f465e73c883a3abe3f46dc5d380fbf985f408b58. Reviewer: independent Codex subagent in the executor's model family. This is same-family provisional code/numerical review, not an external or cross-family receipt.

No code was edited, no job was restarted, and no Git push was performed. Only this audit report is saved. The formal three-seed process remained in progress; its completed JSON was absent at the final check. Completed seed19 source arrays were inspected directly as partial evidence, not labelled a completed three-seed result.

## Verdict

No unresolved blocking correctness defect was found in the new implementation or controlled selector/renderer comparison. The previously missing history conditioning is now present: within the known training prior and numerical physical chain, H_aware evaluates the target mean conditioned on all three preview ADC pairs and each individual future ADC pair at its known intervention exposure. This fixes the information-set limitation of the earlier renderer for this particular known two-pixel toy.

It still does not establish unknown-prior or N1-shift Bayes optimality, an unrestricted full-image backend, a trained neural TM, real-camera gain, clean HDR, Bayer reconstruction, expert GT, or a pristine formal S24 test. The numerical posterior retains the shared likelihood's absolute read-tail approximation and rare-observation underflow limitations. No positive scientific conclusion is an acceptance requirement.

## Posterior formula and scaling

history_reference.py:64–93 prepares observed history by known exposure and pixel. Every matching history frame contributes its likelihood; only identical exposure values are grouped for lookup efficiency. Grouping is not averaging the observations or discarding frames.

At lines 96–103, each future-row likelihood receives the sum of all corresponding source-history log likelihoods. The independent component therefore uses products for a and b separately, and the copula component uses the products on its paired a/b grids. At lines 156–163, the same per-pixel offset is shared between independent and copula grids. Consequently both component evidences are scaled by the same exp(-offset_a-offset_b), which cancels from the posterior ratios without changing posterior component weights. Separate component normalization would have been wrong; it is not performed here.

Lines 164–174 correctly compute independent evidence as za*zb, copula evidence as the weighted paired product, and the mixture target moments and posterior copula probability. The finite Gauss–Legendre weights are preserved in both components. Reverse and rotated grids are supported, with rotation discontinuities inherited from the original quadrature.

Each Monte Carlo future repeat is rendered separately against the same three available previews. The implementation does not pool the sixteen hypothetical future captures as extra observations. Targets/latents enter only evaluate_backends, outside the inference interface.

Given H and a deterministic action A=pi(H), action selection supplies no additional information about L. Treating e as do(e) is therefore correct for the H-aware conditional mean. The H-blind renderer intentionally remains the prior-conditioned fixed-intervention reference and is explicitly not claimed optimal for observationally selected exposure. Both backends retain the training prior during N1, so Bayes-optimality under that shifted true prior is not claimed.

Log accumulation prevents underflow of otherwise representable products; it does not recover an individual physical-kernel likelihood already rounded to zero. The code raises on zero/nonfinite node evidence rather than silently changing the sensor model. The old per-cell absolute tail bound is not a uniform relative-likelihood or posterior-error bound.

## Source, repeat, and observation indexing

The API accepts future shape (sources,2) or (sources,repeats,2). Flattening uses source first, repeat second. At line 153 the mapping row_sources[flat_index//repeats] is correct even when a chunk crosses a source boundary. Explicit source_indices refer to the first future axis and correctly handle reordering and repeated source IDs. No-history and zero-frame-history paths call the original posterior directly and preserve shapes.

History metadata must be a positive scalar or one exposure per frame. Codes must be finite integer ADC values in range. Prepared histories are tied to the reference object/node grid. The controlled runner requires exactly three frames at .25; the general posterior API can accept other explicitly known history exposure vectors. Source/repeat dimension checks are correct for the runner's usage.

## Frozen 2x2 cross-evaluation and intervals

freeze_selectors at lines 210–217 independently selects each backend's fixed action and each feature's threshold/two-action rule using the same train-feature candidates and its own development costs. Selection occurs once at selection_nodes. No diagnostic cost enters the selection function and no node-specific diagnostic refit occurs.

cross_evaluate at lines 232–273 replays both frozen selectors against both renderer cost arrays. In every cell it keeps the source selector's original development-selected fixed action; it does not quietly reselect a better fixed comparator for the destination renderer. Frozen feature actions are also unchanged. Rule-minus-fixed and residual-minus-brightness arithmetic uses the same ordered sources and realized capture cube.

CIs resample paired independent-source cost differences after future repetitions have been averaged. Reinitializing each comparison from the same source-bootstrap SeedSequence intentionally reuses bootstrap indices across cells and contrasts. This is legitimate paired reuse, not extra independent evidence. The CIs condition on fixed policies and finite captured Monte Carlo draws. They do not include development-selection uncertainty, provide a cross-seed interval, or make simultaneous multiplicity-adjusted coverage claims.

The new direct residual-minus-brightness CI repairs the earlier evidence gap where two separate policy-versus-fixed CIs could not prove policy-versus-policy differences. No directly paired H-aware-minus-H-blind CI is currently reported. For a statistical claim about empirical backend differences, calculate that explicit contrast from the source arrays; per-action point comparisons alone are not an uncertainty interval.

## Shared model, streams, and evidence arrays

The runner imports the original Prior, ADCLikelihood, quadrature, tone, exposures, source sampler, previews, and future generator without replacing the sensor model. Thirteen child streams use the original mapping: train 0/1, development 2/3/4, N0 5/6/7, N1 8/9/10, bootstrap 11/12.

Source NPZ creation at lines 298–315 has deterministic ordered IDs, sequential source_index, exact history and future ADC arrays, node/backend/source/action cost axes, feature labels, both selectors' frozen actions and fixed indices, and exposure labels. Cost stacking order follows recorded nodes and renderer_names. Both reports and source arrays use exclusive writes. Existing source files are checked before expensive execution; partial files after interruption remain evidence rather than being overwritten.

Like the original JSON, this JSON does not contain a Git commit or protocol content hash. The inspected commit and frozen protocol are identified here; root execution records should preserve exact command/commit/exit linkage. No CPU RSS measurement is emitted, so the memory analysis below is a structural bound rather than observed peak usage.

## Memory structure

History storage consists of unique ADC-code-by-node lookup tables and source-by-frame inverse indices. The renderer never tiles a source-by-node history tensor across future repeats. Temporary products are limited by observation chunk times nodes.

For the stated 8192 sources, sixteen repeats, and 512 nodes, one saved future cube is 3.5 MiB; three-node/two-backend/source/action costs are 2.625 MiB per population; history codes are .09375 MiB. One worst-case unique-ADC table is at most 4096*512*8 bytes =16 MiB. The default linear prior reuses equal independent/copula history axes and future tables; rotated priors can require separate grids. Four chunk log arrays at chunk256/nodes512 occupy4 MiB, with additional similarly bounded scaled arrays.

Storage and work therefore grow with unique_codes*nodes, chunk*nodes, source*frame indices, source*actions*repeats observation cubes, and saved source/action cost arrays. There is no source*repeat*nodes history tile. Keeping all requested node costs and stacking them for NPZ causes bounded extra copies; increasing arbitrary source/node/uniquely exposed-history counts can still increase memory. This is no claim of measured constant memory or a hardware guarantee.

## Independent verification

The thirteen new tests ran independently in the documented local Python environment: 13 passed in10.21s, exit0. These cover no-history equivalence, explicit likelihood products, component updates, clipping and low boundaries, history permutation, source/repeat indexing, node/chunk agreement, observation-only API, shape rejection, frozen cross arithmetic, original streams, and source-array output.

Additional read-only probes covered gaps in the default-linear manual integration test. A full independent two-dimensional product-prior grid plus one-dimensional copula integration was compared with the implementation for:
- weight0 and weight1 linear priors;
- reverse and rotation copulas at weight.37;
- known history exposures [.125,.25,.5];
- four sources, two future repeats, and chunk3.

Across32 source/repeat cases, maximum target-mean difference was3.33e-16 and maximum component-posterior difference4.44e-16. These probes wrote no files and used no photographs.

## Actual partial-run regressions

The completed seed19 N0 and N1 NPZs were already present, each with cost shape (3,2,8192,7), nodes128/256/512, and16 future repeats. I read them without waiting for the full result JSON.

For both populations:
- H_blind512 source/action costs are bit-identical to the preserved continuous-reference NPZ.
- H_blind256 action means exactly equal the preserved old JSON means.
- Preview features, H-blind frozen actions, and its fixed action index are identical.
- Replaying the documented source/history/future streams reproduced all saved history codes, future codes, and features exactly.
- source_index is sequential and all8192 ordered source IDs are unique.

This confirms actual physical-chain and stream parity for completed seed19, not merely matching function names.

N0 H-aware mean risk is lower at all seven actions. At exposure4, H-aware risk is3.1611264836e-5 versus H-blind3.3411733465e-4. The seven H-aware-minus-H-blind mean differences are:
[-8.1605824593e-4, -3.1370170526e-4, -1.0852702743e-4, -1.5661711068e-4, -3.0905071233e-4, -3.0250606982e-4, -1.0125542745e-3].

This is consistent with the additional-information property under the true N0 training prior: an exact posterior using H and Y cannot have larger expected squared-error risk than a renderer using a subset of those observations. The property concerns expectation, not every source/noise realization. The observed differences have the expected sign and are substantial; no independent backend-difference interval was computed here.

N1 H-aware point risks were also lower at all seven actions in completed seed19, but there is no corresponding Bayes theorem under its mismatched training prior. The selected fixed exposures are .5 for H_blind and4 for H_aware.

Completed seed19 H-aware256-versus512 maximum absolute action-mean differences were3.02e-20 for N0 and3.12e-19 for N1. Maximum source/action differences were5.07e-17 and7.22e-17. H-aware128-versus512 source/action differences were below3.54e-17 in both populations. This supports convergence for these actual draws; it is no all-observation guarantee.

The formal three-seed JSON remained absent at the last check. Seed37/73 results, whole-run exit, phase runtimes, and final matrix significance are not certified by this partial audit. An active process was not called failed.

## Optional improvements and remaining limits

1. Include direct paired backend contrasts before using an empirical confidence statement about H-aware versus H-blind.
2. Preserve code commit, protocol hash, exact command, and execution exit linkage in the final evidence record.
3. Add reverse/rotation/weight-endpoint hand-integration regressions if broader copula configurations are intended as maintained interfaces; current independent probes passed.
4. Keep source, training-selection, finite-noise, node-integration, and seed uncertainty scopes distinct.
5. Preserve both the earlier H-blind diagnostic and this new H-aware protocol; do not reinterpret earlier restricted-renderer gains as having used H.
6. Retain known-prior/two-pixel and N1-mismatch qualifiers. This code fixes history conditioning, not the absent real-camera/full-image evidence.
7. Same-family provisional review cannot satisfy an external cross-family acceptance gate.

No blocking bug was found. The active run may continue within the authorized frozen simulation protocol. Scientific claims must await its actual complete results and remain limited to this numerical known-prior diagnostic.



## Workflow-gap audit addendum (2026-10-09)

Read-only follow-up requested to explain why the workflow is not complete. This section preserves the earlier independent code audit and partial-run checks. It does not change the main IDEA_REPORT, run state, or experiment execution.

### Canonical documents and raw state

The current published working report is work/repositories/Idea/capture_tm/2026-10-09/idea-stage/IDEA_REPORT.md. It is newer than work/idea-discovery/idea-stage/IDEA_REPORT.md and includes the completed restricted N0/N1 and local DNG diagnostics. However, its text still describes H-aware as being implemented; implementation and formal execution have since advanced. The tracker retains old PLANNED N0/N1 table rows plus a later execution update. These are documentation synchronization issues, not evidence that the completed restricted runs did not occur.

Both actual run-state files were read. The canonical repository copy is .aris/runs/capturetm-20261008-run01.json, updated2026-10-09T00:07:30Z. It records:
- executor_model=codex-gpt-6, executor_family=openai;
- policy.provisional_advances=false;
- research-lit, idea-creator, research-refine-pipeline: done;
- novelty-check and research-review: provisional, reviewer=gpt-6-astra, reviewer_family=openai, review_independence=same-family, acceptance_status=provisional;
- idea-discovery-evidence gate: BLOCKED, with exactly the two reviewer-provenance reasons printed in the canonical report.

Proposal, experiment plan, tracker, and research contract exist and were read. The novelty20261009 provenance file records another fresh-context review with PROCEED WITH CAUTION, but reported_exact_model is null and model_family_independence_verified is false. It cannot repair the required cross-family receipt by itself.

### Exact idea-discovery Evidence Gate gaps

The mandatory gate gaps are two acceptance receipts, not missing GPU runs or an unfinished proposal:

1. Novelty verification needs an actual permitted reviewer from a different verified model family, reviewing the updated direction and evidence, with a positive explicit identity-bearing verdict and durable trace/thread ID. PROCEED WITH CAUTION is an eligible positive verdict, but same-family provenance is not eligible under this run's policy.
2. External critical review needs an actual different-family, identity-bearing positive verdict on the updated hypothesis, raw positive/negative results, risks, and next decision. A fresh OpenAI agent is still same-family and cannot satisfy this receipt.
3. Fold the substantive returned findings into the anchored canonical report sections. Update proposal/plan/tracker/contract if the findings or completed H-aware decision change them. Then record truthful stage completion/acceptance through the run-state contract using actual model identities and actual durable verdict IDs.
4. Re-run the deterministic idea_discovery_gate on this same canonical report/run. Only a real PASS can replace the BLOCKED final workflow status. The audit did not run this mutating gate or manufacture receipts.

These requirements come from C:/Users/Lenovo/.agents/skills/idea-discovery/SKILL.md, “Per-stage evidence gate”, which says “do not present the workflow as complete”, and the installed runtime rule “Same-family review is provisional, not cross-family evidence.” The requirement is explicit, not this auditor's inferred demand for another confirmation. Existing survey, idea generation, proposal, plan, tracker, and contract do not need to be recreated solely to remove these two receipt gaps.

Finishing additional CPU diagnostics alone cannot change the gate to PASS. Conversely, passing this discovery gate does not mean a manuscript is submission-ready.

### Latest H-aware artifacts and direct partial data

Raw outputs/CaptureTM_Local_DNG_20261009/history-reference/run_meta.json records RUNNING, local commitf465e73, seeds19/37/73, train2048, development4096,8192 sources per diagnostic,16 future repeats, nodes128/256/512, selection512,2000bootstraps. This metadata was read as an execution record, not treated as measured outcome evidence.

Four complete source NPZs were present: seed19 and37, each N0 and N1. The final results.json remained absent at the last actual check. No experiment was re-run, waited for, stopped, or restarted. The three-seed JSON, seed73 outcomes, final process exit, and final direct-CI matrix are therefore pending and not certified by this addendum.

Direct source-array checks on all four available seed/population files:
- H_blind512 source/action costs are bit-identical to the preserved old continuous-reference arrays.
- H-aware means are lower at every one of the seven actions in these files.
- Frozen2x2 matrix points were recalculated from the saved source/action costs, saved selector actions, and each selector's own saved fixed action. There was no reselection or use of executor summaries.

Important provisional negative evidence: the H-aware-trained known-linear-residual rule selects only exposure4 in both available seeds and both populations. Its risk exactly equals its own fixed-exposure risk. For its own H-aware backend, N0 residual-minus-brightness point differences are +4.9623091710e-7 (seed19) and +4.2233632829e-7 (seed37), so brightness has the slightly lower point risk. N1 corresponding point differences are +3.7992189157e-8 and +7.2525635705e-9. The H-aware-trained residual rule currently provides zero improvement over its own fixed comparator.

Replaying the H-blind-trained residual rule on H-aware produces a large gain against that selector's inherited fixed exposure.5, but this is a crossover cell with a deliberately retained historical comparator. It is not evidence that residual adaptation remains necessary after training the selector for the H-aware backend. For example, seed19N0:
- H_blind selector/H_blind backend: fixed.5 risk1.9796909084e-4, residual1.8335772511e-4.
- H_blind selector/H-aware backend: fixed.5 risk8.9442063408e-5, residual5.2926170702e-5.
- H-aware selector/H_blind backend: fixed4 risk3.3411733465e-4, residual identical.
- H-aware selector/H-aware backend: fixed4 risk3.1611264836e-5, residual identical; brightness3.1115033919e-5.

No three-seed significance conclusion or direct residual-minus-brightness CI is asserted while the final JSON is absent. The final audit should verify the actual recorded CIs and all12 matrix cells across seeds/populations (four cells per population per seed), using raw source costs and selectors. This partial evidence argues against interpreting a transferred old selector's gain as proof that an adaptive relation rule is needed by the fully history-conditioned toy backend.

### Separate submission-evidence gaps

The current proposal's C1–C3 remain candidates. Submission readiness requires deciding what claim survives, not automatically launching all planned training:

1. Complete and audit the current H-aware outcome, including all three seeds, raw direct residual-minus-brightness intervals, full frozen crossover, and numerical convergence. Update canonical conclusions with negative results. If fixed/simple rules suffice after full-history rendering, stop a complex-AE necessity claim and retain the honest diagnostic/negative result.
2. Demonstrate a defensible difference from existing optimal-exposure/Bayes-design/noise-clipping work. The current discovery scores and same-family proceed verdicts are not novel-contribution evidence.
3. If retaining full-image claims, freeze the actual common actions/target/budget/interface/source splits and test independent source scenes, controlled matched spatial dependencies, global/local simple rules, sufficiently converged backends, and independent trained-backend crossover. The current known two-pixel prior and point/local-Wiener DNG families do not provide this evidence.
4. If claiming real camera/HDR acquisition benefit, obtain calibrated physical multi-exposure or appropriate original sensor data and valid target/fidelity provenance. The processed bounded green DNGs with relative synthetic noise are not real recapture, Bayer or clean HDR. This is conditional on that claim; it is not an automatic prerequisite for a narrowly scoped simulation paper.
5. Keep prespecified delta, paired-source uncertainty, selection uncertainty, and true held-out conditions explicit. More crops/noise repetitions from one DNG session cannot supply new independent scenes.

None of these submission-evidence items is currently listed by the deterministic idea-discovery gate as an absent artifact. They are scientific follow-on requirements according to the retained claim and the proposal's decision gates, separate from the two hard cross-family receipt gaps.



## Completed three-seed H-aware outcome audit (supersedes earlier pending snapshots)

The final outputs/CaptureTM_Local_DNG_20261009/history-reference/results.json and all six seed/population NPZ files appeared after the preceding snapshot. The JSON records completed_history_simulated_diagnostic, seeds19/37/73, nodes128/256/512, selection512, train2048, development4096,8192 sources per diagnostic,16 future repeats,2000 bootstrap replicates, and elapsed_seconds1102.1631016000174. The root executor separately witnessed exit0 from its original process session. This auditor read the raw finished artifacts and did not re-run captures, renderers, training, selectors, or the experiment.

At the first completed-JSON read, run_meta.json still said RUNNING. That was a documentation state mismatch; the finished JSON and six complete arrays were independently checked. Synchronize the execution record if not already done. The earlier “JSON absent” passages are accurate historical snapshots and are superseded by this section. Also, there are24 matrix cells overall (three seeds times two populations times four cells), correcting the earlier follow-up's mistaken reference to12.

### Complete arithmetic and CI verification

Independently recomputed from saved source costs and actions:
- all24 selector-by-renderer matrix cells;
- all96 paired percentile CIs: three feature rules versus the source selector's fixed action, plus residual versus brightness, in each cell;
- per-action means at every node and backend;
- node-report action differences and maximum source/action differences;
- selected-action counts, JSON rule replay against saved preview features, fixed action indices, ordered/unique source IDs, and shape/finite/nonnegative cost validity.

Bootstrap verification reused the documented child11/12 source indices for the16 contrasts in each seed/population,2000 replicates and chunk64. This recomputes statistics on the existing arrays; it is not another experiment. Maximum differences between independently reconstructed and recorded means, percentile CI endpoints, and node report values were all exactly0. The verification process exited0.

For all three seeds and both populations, H_blind512 source/action costs, preview features, actions, fixed index, and frozen rule dictionaries exactly reproduce the preserved old continuous-reference artifacts. H_blind128/256/512 action means match the old JSON. No regression due to altered sources or rendering was found.

H-aware risk is lower at all seven actions in every N0 and N1 seed. Under N0 this is consistent with the known-prior additional-information property; under N1 it remains an observed result, not a mismatched-prior Bayes guarantee. H-aware256-versus512 maximum source/action difference across all six populations is8.7169854668e-17. Recorded convergence values exactly reproduce the arrays.

### Final scientific decision within the toy protocol

After selecting for H-aware on development data, the known-linear-residual rule degenerates to the same fixed exposure4 in all three seeds. All8192 sources in both N0 and N1 receive4. Its risk is exactly its own fixed risk; rule-minus-fixed mean is0 and paired CI is[0,0] in every case. This is an exact equality of selected actions, not an ambiguous underpowered negative result.

For the H-aware selector evaluated on its H-aware renderer, the direct residual-minus-brightness results are:

| Population | Seed | Difference | Paired95%CI |
|---|---:|---:|---|
| N0 | 19 | +4.9623091710e-7 | [3.3328846472e-7,6.7516082041e-7] |
| N0 | 37 | +4.2233632829e-7 | [2.4320555721e-7,6.0094475716e-7] |
| N0 | 73 | +4.4985636752e-7 | [2.7839715634e-7,6.2518283004e-7] |
| N1 | 19 | +3.7992189157e-8 | [-8.7250977707e-8,1.7580484147e-7] |
| N1 | 37 | +7.2525635705e-9 | [-1.2168168589e-7,1.5299530346e-7] |
| N1 | 73 | -2.7669986827e-8 | [-1.8447652147e-7,1.3440242880e-7] |

Positive differences favor brightness. Brightness is slightly better in N0 in all three conditional source-bootstrap comparisons, approximately1.30%–1.57% relative to the selected fixed4 risk. Its absolute gain is only4.2e-7–5.0e-7 and below the earlier1e-4 practical tolerance. N1 direct intervals all include0. No special necessity of the known relation rule is established after full-history conditioning and selector reselection.

The controlled crossover must be interpreted with its intended comparator:
- H_blind-trained selector / H_blind renderer keeps fixed.5. Its residual-minus-brightness N0 interval crosses0 in every seed; N1 intervals favor residual.
- H_blind-trained selector / H-aware renderer also keeps its inherited fixed.5. Residual beats that comparator and that old brightness selector in every seed/population.
- H-aware-trained selector / H_blind renderer keeps fixed4; residual is exactly that fixed policy. On N0 brightness is slightly better; on N1 residual-minus-brightness intervals cross0.
- H-aware-trained selector / H-aware renderer keeps fixed4; residual has zero adaptive benefit. N0 brightness is slightly better; N1 differences are uncertain.

Thus transferring an old selector to the new renderer can retain a large gain against an old suboptimal fixed comparator while the reselected H-aware rule needs no adaptation. Reporting only the positive transfer cell would misstate the decision. This is why all four frozen cells, each with the source selector's own fixed baseline, are necessary.

The outcome weakens the proposed claim that an adaptive relationship rule is required after sufficiently using the available observations in this known-prior two-pixel model. It supports a qualified diagnostic/negative result: backend information and selector retraining materially alter apparent AE value. It does not prove that fixed exposure suffices on unknown full-image priors or real cameras, nor identify a novel general theorem beyond familiar conditional-mean principles.

### Effect on workflow status

The H-aware experiment and its complete three-seed arithmetic audit are now finished. The corresponding canonical report/proposal/tracker next-step wording should be updated from “being implemented/pending” and should preserve the negative result. Do not schedule the same experiment again to seek a positive outcome.

The deterministic idea-discovery Evidence Gate still has the two documented cross-family reviewer-receipt gaps. These completed numerical results should be supplied to the actual novelty and critical reviewers; they do not themselves create those receipts or make the workflow PASS. A reviewer may recommend proceeding with a narrower diagnostic/negative contribution, or abandoning/pivoting. Record the actual verdict rather than treating completion of the experiment as acceptance.

No unresolved implementation defect was found. This completed result audit is same-family provisional review, not cross-family acceptance.
