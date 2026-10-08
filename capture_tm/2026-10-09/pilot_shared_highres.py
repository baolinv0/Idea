"""Follow-up within spatial pilot: shared, bidirectional local backend; causal simple rule.
No test family ID or clean latent enters renderer/policy inference.
"""
import json,time,argparse
from pathlib import Path
import numpy as np
import pilot_mechanisms as base
E=base.EXPOSURES; BA=256;BB=256
def pair(n,rng):
    a=rng.uniform(.05,.30,n);b=4*a+.6;p=rng.permutation(n)
    return a,b,p
def joint_fit(za,zb,y,axis):
    ia=base.binned(za,BA);ib=base.binned(zb,BB);idx=ia*BB+ib
    cnt=np.bincount(idx,minlength=BA*BB);sm=np.bincount(idx,weights=y,minlength=BA*BB)
    z=za if axis==0 else zb; lut=base.fit_lut(z,y)
    if axis==0:
        v=np.interp(np.linspace(0,base.BINS-1,BA),np.arange(base.BINS),lut)
        out=np.repeat(v,BB)
    else:
        v=np.interp(np.linspace(0,base.BINS-1,BB),np.arange(base.BINS),lut)
        out=np.tile(v,BA)
    ok=cnt>0;out[ok]=sm[ok]/cnt[ok]
    return out.reshape(BA,BB)
def evaluate_backend(tables,a,b,p,rng):
    costs=[]
    for e,(ta,tb) in zip(E,tables):
        za=base.capture(a,e,rng);zb=base.capture(b,e,rng)
        both=[]
        for pp in [np.arange(len(a)),p]:
            ia=base.binned(za,BA);ib=base.binned(zb[pp],BB)
            both.append(.5*((ta[ia,ib]-base.tone(a))**2+(tb[ia,ib]-base.tone(b[pp]))**2))
        costs.append(np.concatenate(both))
    return np.array(costs).T
def preview_residual(a,b,p,rng):
    # Three common past previews at known exposure .25, independent sensor draws.
    ah=0.;bh=0.
    for _ in range(3):
        ah=ah+base.capture(a,.25,rng)/.25
        bh=bh+base.capture(b,.25,rng)/.25
    ah/=3;bh/=3
    return np.concatenate([np.abs(bh-(4*ah+.6)),np.abs(bh[p]-(4*ah+.6))])
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--outdir",required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True);start=time.perf_counter();rows=[]
    for seed in base.SEEDS:
        rng=np.random.default_rng(seed+9000)
        a,b,p=pair(250000,rng)
        tables=[]
        for e in E:
            za=base.capture(a,e,rng);zb=base.capture(b,e,rng)
            # One mixed training population, one shared backend per action, no family flag.
            az=np.concatenate([za,za]);bz=np.concatenate([zb,zb[p]])
            ay=np.concatenate([base.tone(a),base.tone(a)])
            by=np.concatenate([base.tone(b),base.tone(b[p])])
            tables.append((joint_fit(az,bz,ay,0),joint_fit(az,bz,by,1)))
        ad,bd,pd=pair(50000,rng);at,bt,pt=pair(100000,rng)
        dc=evaluate_backend(tables,ad,bd,pd,rng);tc=evaluate_backend(tables,at,bt,pt,rng)
        dr=preview_residual(ad,bd,pd,rng);tr=preview_residual(at,bt,pt,rng)
        fixed=int(np.argmin(dc.mean(0)))
        # Simple correlation-residual rule, dev-selected threshold and two actions.
        selected=None
        for threshold in np.linspace(.02,.4,20):
            flag=dr<=threshold
            if flag.sum()<100 or (~flag).sum()<100:continue
            il=int(np.argmin(dc[flag].mean(0)));ir=int(np.argmin(dc[~flag].mean(0)))
            score=np.where(flag,dc[:,il],dc[:,ir]).mean()
            if selected is None or score<selected[0]:selected=(float(score),float(threshold),il,ir)
        _,thr,il,ir=selected
        ruleaction=np.where(tr<=thr,il,ir)
        rulemse=float(tc[np.arange(len(tc)),ruleaction].mean())
        fmse=float(tc[:,fixed].mean())
        n=len(at);means=np.array([tc[:n].mean(0),tc[n:].mean(0)])
        familybest=means.argmin(1)
        rows.append({"seed":seed,"mean_mse_by_family_and_exposure":means.tolist(),
                     "test_best_exposures_diagnostic":[float(E[i]) for i in familybest],
                     "best_fixed_dev_exposure":float(E[fixed]),"fixed_test_mse":fmse,
                     "rule_threshold_from_dev":thr,"rule_actions_from_dev":[float(E[il]),float(E[ir])],
                     "rule_test_mse":rulemse,"rule_relative_mse_reduction_vs_fixed":1-rulemse/fmse,
                     "test_family_conditioned_diagnostic_mse":float(means.min(1).mean()),
                     "test_hindsight_min_realized_loss_mse":float(tc.min(1).mean())})
    result={"status":"completed_cpu_followup","elapsed_seconds":time.perf_counter()-start,"exposures":E.tolist(),
            "replicates":rows,"scope":"Shared equal-bin bidirectional local estimators fit on mixed populations; one per action. Test rule uses only three .25-exposure noisy previews and a known linear prior, no family ID. Targets/latents used only for fitting and evaluation. No real-camera/neural validation.",
            "hindsight_note":"Minimum over realized test losses uses unavailable future measurements/noise; it is not a latent or causal oracle and is excluded from claims.",
            "not_tested":"Generalization to unknown nonlinear priors/full images/strong neural backends; scene-wise confidence intervals; adaptive risk predictor."}
    (out/"shared_backend_results.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps({"seconds":result["elapsed_seconds"],"family_best":[r["test_best_exposures_diagnostic"] for r in rows],
                      "rule_reductions":[r["rule_relative_mse_reduction_vs_fixed"] for r in rows]}))
if __name__=="__main__":main()
