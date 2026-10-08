> 历史草案（2026-10-08）。置信、先验设置、最低成本与创新点的当前边界见[最新结论](../CONCLUSIONS.md)。以下保留当时dossier，不视为已验证结论。

# Novelty dossier
Date: 2026-10-08 (Asia/Shanghai). SCOUT → CONVERGE only. No experiments run or method designed.

Question: How much additional real observation is needed for faithful HDR/low-light reconstruction? User distinguishes single-frame non-generative, single-frame generative, multiframe fusion. Revise to two axes: physical acquisition × prior strength, because UltraFusion is already a hybrid.

Four candidate claims:
1. Information/SNR governs hallucination/fidelity/perception. Already studied in Hallucination Index and One Photon, Many Worlds.
2. Additional real exposure constrains generation. UltraFusion and BurstGP already combine these.
3. Local factual risk can be quantified/calibrated. Hallucination maps, HalluGen, LL-Bench, K-RCPS already address related versions.
4. Fixed-budget conventional Bayer RAW exposure allocation produces a distinctive prior-dependent local factual-risk frontier. Allocation itself is old; candidate delta requires a nontrivial interaction or acquisition decision, not merely a new sensor/benchmark grid.

Source dossier, all papers found:
- The Perception-Distortion Tradeoff, CVPR2018, https://arxiv.org/abs/1711.06077 : distributional perceptual vs distortion tradeoff.
- On hallucinations in tomographic image reconstruction, TMI2021/preprint2020, https://arxiv.org/abs/2012.00646 : measurement/null-component hallucination maps; not an exact RAW noisy/clipped nullspace.
- The Perception-Robustness Tradeoff in Deterministic Image Restoration, ICML2024, https://proceedings.mlr.press/v235/ohayon24a.html : deterministic priors can be unstable.
- Hallucination Index: An Image Quality Metric for Generative Reconstruction Models, MICCAI2024, https://pmc.ncbi.nlm.nih.gov/articles/PMC11956116/ : microscopy, simulated correlated Gaussian noise, 5 SNR levels, repeated reconstructions. Higher SNR reduces index. Hellinger/reference-distribution score is NOT a factual-error probability. Gaussian/shift-invariance and noiseless-output degeneracy limit direct adoption.
- How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control, ICML2023, https://proceedings.mlr.press/v202/teneggi23a.html : K-RCPS pixel intervals/risk on face and CT denoising; interval coverage is not point-estimate correctness.
- RODS: Robust Optimization Inspired Diffusion Sampling for Detecting and Reducing Hallucination in Generative Models, NeurIPS2025, https://papers.nips.cc/paper_files/paper/2025/hash/24c79c21eb699e9efdebaafa40ed0e4d-Abstract-Conference.html : sampling artifacts, unconditional datasets; not scene-conditioned factual error.
- HalluGen: Synthesizing Realistic and Controllable Hallucinations for Evaluating Image Restoration, CVPR2026/preprint2025, https://arxiv.org/html/2512.03345v1 and https://github.com/edshkim98/HalluGen : controllable hallucination synthesis, annotated MRI dataset, SHAFE metric; CVF PDF 403, arXiv/official code checked.
- LL-Bench: Rethinking Low-Level Vision Evaluation in the Era of Large-Scale Generative Models, June2026 preprint, https://arxiv.org/html/2606.02535v1 : human hallucination/preference labels including HDR/low light; no controlled RAW budget sweep.
- Noise-Optimal Capture for High Dynamic Range Photography, 2010, https://people.csail.mit.edu/hasinoff/hdrnoise/ : equal total time/number, shutter/ISO optimization, worst-region SNR curves. Fixed-budget exposure allocation is old.
- Burst photography for high dynamic range and low-light imaging on mobile cameras, SIGGRAPH Asia2016, https://research.google/pubs/burst-photography-for-high-dynamic-range-and-low-light-imaging-on-mobile-cameras/ : HDR+, same-exposure short Bayer RAW bursts, Wiener fusion, not exposure bracket.
- RawHDR: High Dynamic Range Image Reconstruction from a Single Raw Image, ICCV2023, https://arxiv.org/html/2309.02020v1 : supervised single RAW reconstruction, no acquisition-risk sweep.
- UltraFusion: Ultra High Dynamic Imaging using Exposure Fusion, CVPR2025, https://arxiv.org/html/2501.11515v1 : TWO real differently exposed RGB + Stable Diffusion guidance/inpainting, up to 9 stops; not pure physical fusion.
- UltraLED: Learning to See Everything in Ultra-High Dynamic Range Scenes, NeurIPS2025, https://arxiv.org/html/2510.07741v1 : ONE short RAW, U-Net ratio-map correction + brightness-aware RAW denoising, not diffusion; 9-EV reference stack is not inference input.
- AdaptiveAE: An Adaptive Exposure Strategy for HDR Capturing in Dynamic Scenes, ICCV2025, https://arxiv.org/html/2508.13503v1 : RL shutter/ISO/frame count under time budget, noise/motion, existing fusion; not calibrated factual risk.
- BurstGP: Enhancing Raw Burst Image Super Resolution with Generative Priors, April2026 preprint, https://arxiv.org/html/2604.23508v1 : 14-frame BISR then video diffusion; Table6 compares diffusion conditioners. Single-frame diffusion already receives full-burst reconstruction: NOT 1 vs14 real observations. No capture budget risk sweep.
- Single-Shot HDR Recovery via a Video Diffusion Prior, May2026 preprint, https://arxiv.org/html/2605.11628v1 : ONE real LDR, 5 generated exposures; not5 independent observations.
- ExpoCM: Exposure-Aware One-Step Generative Single-Image HDR Reconstruction, CVPR2026, https://arxiv.org/html/2605.02464v1 : single LDR, regional exposure treatment, no true budget sweep.
- DiffHDR: Re-Exposing LDR Videos with Video Diffusion Models, April2026 preprint, https://arxiv.org/html/2604.06161v1 : LDR video/radiance inpainting, ambiguous saturated content, no fixed budget factual risk calibration.
- High Dynamic Range Video Reconstruction from Single-Exposure Raw Sequences, Sept2026 preprint, https://arxiv.org/html/2609.27274v1 : THREE real same-exposure RAW frames, channel/temporal complementarity, no factual risk threshold.
- One Photon, Many Worlds: Posteriors and Predictions with Single-Photon Cameras, 2026-10-02 preprint, https://arxiv.org/html/2610.02675v1 : STRONGEST overlap. Binary SPAD frame/photon budget, generative conditional ambiguity, edge/OCR/QR/facial errors. Sec9 typical20–50 frame task knee is empirical/dataset-specific. High-flux HDR extension future. Does not cover conventional Bayer readnoise/exposure allocation/calibrated local factual risk. Never transfer frame number to phones.
- Self-Supervised Uncertainty Estimation For Super-Resolution of Satellite Images, UAI2026, https://proceedings.mlr.press/v337/zheng26a.html : burst-based posterior mean/variance calibration, no generative HDR acquisition-risk policy.

Candidate residual: conventional Bayer RAW, fixed capture time/readouts, distinguish photon gain from exposure complementarity and prior bias, measure localized wrong-but-confident scene facts versus erasure/readability; estimate least-cost schedule satisfying a specified factual-risk AND perceptual/readability target. This is search-based inferred residual, not proven absence or physical upper bound. No universal threshold or mandatory knee.

Probe proposal (design only):
Static scenes with bright and dark newly randomized text/symbols/textures and natural objects; independent high-SNR non-generative reference. Calibrate gain/readnoise/black level/saturation; fixed flux/aperture.
(a) N=1/4/8, each t, total time increases: generic sanity check only.
(b) same N=4,T=4t: [t,t,t,t] vs [t/4,t/4,t/2,3t]. Same incident light/time/readout count; retained information/SNR differs intentionally. Account for duty cycle/gain/clipping.
Fixed physical fusion and pixel-fidelity baselines, then frozen existing generative enhancer on same fused image with available prior-strength presets. No architecture/training. A duplicate-frame control has N_unique=1 and correctly correlated noise, never new photons.
Predefine readable incorrect symbol/edge as factual hallucination, unreadable/erased separately, report both unconditional error and selective error WITH coverage. Separate natural-texture/radiometric metrics. Use same display mapping for perceptual ratings. Seeds quantify model variation, not independent scenes; stable outputs can still be wrong.
H0: observed changes are generic denoising or classical noise/saturation gains; no reproducible prior-strength × schedule interaction in factual error/readability/perceptual frontier at equal cost.
H1: this interaction exists and changes which capture schedule satisfies a prespecified factual risk plus nontrivial quality/readability target. Simple SNR↓hallucination or bracket↑PSNR is insufficient novelty.
Pilot maps effect sizes only. Later separate scene-level calibration/heldout confirmation and uncertainty bounds, address budget selection/multiple tests. Nonmonotone risk allowed, unreachable target reported. Sensor/model/scene distribution specificity.

Audit limits: optional verify_papers.py not found under .agents/.codex skill roots (rg); formal entries must be marked [UNVERIFIED], explicitly helper-unverified but primary sources inspected. No Codex reviewer MCP exposed, so fresh subagent fallback. Same-family review provisional, not cross-model independent. Targeted latest ICLR2026/ICML2026/NeurIPS2025 and last6 months searched; not exhaustive indexes/citation graph or all supplements. No original research state or playbook file in cwd, use user's supplied state. No vivoV1 mechanism verified.

Reviewer questions: Is the question novel? Closest prior and exact delta? Is 5/10 and PROCEED WITH CAUTION justified (thin delta=SPAD result already similar and acquisition optimization already done)? Is probe sufficient to discriminate novel interaction rather than known photon/SNR/HDR effects? Identify confounds and minimal corrections, not new network design. Read-only review.

=== NOVELTY VERDICT LIMITS (these bound how you judge, never how widely you search) ===
Search exhaustively; judge calibrated. Two failures waste months equally:
passing an idea a published paper already contains, and killing a viable idea
because the territory has neighbors.
1. Proximity is information, not a verdict. Someone working nearby goes in the
   report; it is not by itself a reason to reject.
2. ABANDON has exactly one qualification: a specific published paper already
   contains this result — name that paper. No named paper, no ABANDON.
3. Crowded-but-deltaed is PROCEED: state the delta in one sentence a reviewer
   could verify. Thin or contested delta is PROCEED WITH CAUTION — say what
   would make it carry, not why it should die. CAUTION is not a safe middle:
   if you cannot name the specific thing that makes the delta thin, the
   verdict is PROCEED.
4. Concurrent or competing work is not a veto. That is a race — report it and
   let the user decide whether to run it.
5. A direct attack on a central problem is legitimate novelty when nobody has
   executed it well. "This area is hot" does not mean "this area is taken."
6. This check is an early gate, never the last one — more triage, pilots, or
   external review still stand between any idea and a paper, whatever order
   this run uses. A wrongly passed idea dies cheaply at one of them; a wrongly
   killed idea is never seen again. When torn between two verdicts, choose the
   more permissive one.
Say plainly when an idea clears the check. Do not manufacture overlap.
