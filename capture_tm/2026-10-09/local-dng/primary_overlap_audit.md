# Primary-source protocol overlap audit

Date: 2026-10-09. Scope: read-only examination of three specified primary papers; no experiment re-review, code change, main-report edit, or external acceptance receipt. Same-family provisional literature check.

## Criteria used

A: the selector and renderer both receive the same fixed three already-available preview observations H, with rendering conditioned on H plus the new capture Y. Sharing an evolving exposure stack is related but not automatically this exact interface.

B: exposure selectors are fixed before testing and their predicted captures are replayed across fixed recovery backends under one target. Distinguish this basic cross-test from the stricter two-backend-specific-selector crossover, with each selector retaining its own development-selected fixed comparator.

C: match marginal brightness/measurement statistics while changing spatial dependence, and test its usable exposure-risk boundary with a common backend, causal observations, held-out dependence and simple-rule controls.

“Not found” below means not established in the inspected method/experiments; it is not proof of absence from all papers/code or proof that CaptureTM is novel.

## Findings

| Primary paper | A: exact fixed H+Y interface | B: frozen cross-backend evaluation | C: controlled marginal/spatial boundary |
|---|---|---|---|
| AdaptiveAE | Stage-wise shared/reused LDR information; exact fixed three-H-plus-new-Y not documented | Basic test present; stricter backend-specific selector/fixed-baseline crossover not documented | Not found |
| Noise-Optimal Capture | Not documented | Not found; one analytical merging estimator | Not found |
| Radiometric Uncertainty | No AE selector; observations fused | Reconstruction methods compared, no selector crossover | Not found |

### AdaptiveAE

Read the official arXiv full HTML, §§3.2–3.4, §4 including Table3, AppendixA.2/A.4. This was not abstract-only. ArXiv/CVF PDF fetches failed, so PDF pagination is not asserted. [Full text](https://arxiv.org/html/2508.13503); [official accepted-paper record](https://openaccess.thecvf.com/content/ICCV2025/html/Xu_AdaptiveAE_An_Adaptive_Exposure_Strategy_for_HDR_Capturing_in_Dynamic_ICCV_2025_paper.html).

The policy starts with three preview LDRs, then updates an exposure stack. Current-state LDRs inform the policy and DeepHDR-based reward, with some frames inherited between stages. Final fusion is described for the predicted LDR stack; I found no explicit requirement to retain all original previews alongside a separate new capture. [§§3.2–3.4, Figs3–4](https://arxiv.org/html/2508.13503).

Table3 is an actual four-AE-method-by-three-fusion-backend comparison; AdaptiveAE trains with DeepHDR then tests other pretrained fusers. Generic cross-backend testing is already implemented. It does not report the stricter backend-specific selector reselection/fixed-comparator protocol. Motion-stratified tests and deblur comparisons do not control brightness marginals while varying spatial dependence. [§4.1 Table3; §4.2; AppendixA.2](https://arxiv.org/html/2508.13503).

### Noise-Optimal Capture

Read the author-hosted main PDF's model/optimization and results, especially §4.1–4.2, PDFpp4–5; §5, pp5–8. Supplementary dark-current extension was not read. [Author project](https://people.csail.mit.edu/hasinoff/hdrnoise/); [main paper](https://people.csail.mit.edu/hasinoff/pubs/hasinoff-hdrnoise-2010.pdf).

It optimizes exposure-time/ISO multiplicities for worst-case SNR over a brightness range and derives a minimum-variance unbiased pixel merger. No common causal-preview selector/renderer interface or independent backend-selector crossover is described. [§4, Eqs4–7, PDFp4](https://people.csail.mit.edu/hasinoff/pubs/hasinoff-hdrnoise-2010.pdf#page=4).

Synthetic and real examples compare schedules under equal time/count constraints. Tone mapping displays the merged outputs; the objective is SNR, not fixed tone-target risk. Its scene-histogram discussion is not a controlled spatial-dependence experiment. Noise/clipping/budget-optimal acquisition are established overlap. [§5, PDFpp5–8](https://people.csail.mit.edu/hasinoff/pubs/hasinoff-hdrnoise-2010.pdf#page=5).

### Modeling Radiometric Uncertainty

Read arXivv2 PDF §§3–4 and §5.1, with §5.3 checked;14pages. Numeric PDF section numbering differs from Roman-numbered HTML. This was not abstract-only. [Official PDF](https://arxiv.org/pdf/1311.6887v2); [HTML](https://arxiv.org/html/1311.6887).

§4 derives a probabilistic inverse of the calibrated global tone map, numerical conditional means/covariances, and approximate Gaussian distributions. This is existing posterior/inverse-uncertainty methodology. [§4, PDFpp6–7](https://arxiv.org/pdf/1311.6887v2#page=6).

§5.1 fuses two known-exposure JPEG observations and compares probabilistic versus deterministic reconstruction across exposure pairs. Figure6 explicitly shows a larger set of pairs with low reconstruction error under probabilistic fusion. Thus generic “the backend changes acceptable exposure sets” is already demonstrated. There is no causal AE selector or frozen selector crossover. [§5.1, Fig6, PDFpp8–9](https://arxiv.org/pdf/1311.6887v2#page=8).

The implemented inverse uses a uniform chromaticity prior; higher-order scene priors are discussed. Deblurring adds a gradient prior, but neither experiment controls matched marginals while varying spatial dependence to establish AE benefit boundaries. [§4, PDFp6; §5.3, pp10–12](https://arxiv.org/pdf/1311.6887v2#page=6).

## Claim implications

The full A+B+C combination was not established by these three method/experiment sections. Several components already are: preview-driven exposure optimization, generic backend cross-tests, optimal noisy capture/merging, probabilistic inversion, and reconstruction-dependent acceptable exposure pairs. A different combination of controls is not automatically a novel scientific contribution.

CaptureTM's stricter frozen crossover can improve diagnostic attribution. Its controlled dependence test needs a substantive surviving finding, not merely an unreported protocol combination. The completed H-aware experiment's negative result about the residual rule should remain visible when requesting novelty and critical review. This primary-source check cannot create the missing cross-family acceptance receipts.

