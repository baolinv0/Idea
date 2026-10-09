"""Independent same-family audit; direct CSV statistics, no formal rerun."""
from pathlib import Path
import csv, hashlib, inspect, json, subprocess, sys, time, traceback
from datetime import datetime, timezone
from collections import Counter
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
ROOT=Path(__file__).resolve().parents[2]
REPO=ROOT/"work/repositories/modular_neural_isp"
D=REPO/"research/ae_tm/diagnostics"
OUT=ROOT/"outputs/CaptureTM_Local_DNG_20261009"
NEW=OUT/"dng-history-control-3seed"
CACHE=ROOT/"work/capturetm-local-dng/private-pixel-cache"
RAW=Path(r"C:\Users\Lenovo\Desktop\DNG\s25_iphone16_dng")
JP,MP=Path(__file__).with_suffix(".json"),Path(__file__).with_suffix(".md")
B=("H_blind_inverse","H_blind_Wiener","H_aware_classical_fusion","H_aware_fusion_Wiener")
F=("mean_brightness","q99_brightness","temporal_noise","local_gradient")
E=np.array([.125,.25,.5,1.,2.,4.,8.])
RF=[f"risk_e{e:g}" for e in E]
COMMIT="ae7c762bf18461fb1fb673b81b0ab0bc33c3e78e"
TREE="2364997b680efdfc57c951c09f9f22b6271a55c0"
sys.path.insert(0,str(D))
import dng_history_control as ctl
def req(x,m):
    if not x: raise AssertionError(m)
def sha(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()
def rj(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def rows(p):
    with Path(p).open(newline="",encoding="utf-8") as f: return list(csv.DictReader(f))
def err(a,b):
    x,y=np.asarray(a,dtype=float),np.asarray(b,dtype=float)
    req(x.shape==y.shape,"numeric shape")
    return float(np.max(np.abs(x-y))) if x.size else 0.
def tone(x):
    x=np.asarray(x,dtype=float); return np.sqrt(x/(x+.5))
def capture(x,e,rng):
    v=rng.poisson(1000*e*x)+rng.normal(0,4,x.shape)
    return np.rint(np.clip(v,0,1000)*4095/1000).astype(np.int16)
def feat(h):
    v=h.astype(float)/4095/.25; m=v.mean(axis=0)
    g=np.concatenate((np.diff(m,axis=1).ravel(),np.diff(m,axis=2).ravel()))
    return np.array([m.mean(),np.quantile(m,.99),np.sqrt(v.var(axis=0,ddof=1).mean()),np.mean(np.abs(g))])
def fusion(h,y,e):
    xhat=np.clip((h.astype(float)/4095/.25).mean(axis=0),0,1)
    estimates,noises,masks=[],[],[]
    for yy in y:
        obs=np.concatenate((h,yy[None]),axis=0)
        es=np.array([.25,.25,.25,e])[:,None,None,None]
        var=(1000*es*xhat[None]+16)/(1000000*es**2)+1/(12*4095**2*es**2)
        w=np.where(obs==4095,0.,1/var); total=w.sum(axis=0); missing=total==0
        estimate=np.ones_like(total); noise=np.ones_like(total)
        np.divide((w*obs.astype(float)/4095/es).sum(axis=0),total,out=estimate,where=~missing)
        np.divide(1.,total,out=noise,where=~missing)
        estimates.append(np.clip(estimate,0,1)); noises.append(noise); masks.append(missing)
    return np.stack(estimates),np.stack(noises),np.stack(masks)
def box(x,w):
    padded=np.pad(x,((0,0),(0,0),(w//2,w//2),(w//2,w//2)),mode="symmetric")
    return sliding_window_view(padded,(w,w),axis=(-2,-1)).mean(axis=(-2,-1))
def spatial(signal,noise,w,mask):
    value=signal
    if w!=1:
        mean=box(signal,w); var=np.maximum(0,box(signal*signal,w)-mean*mean)
        gain=np.clip(1-box(noise,w)/np.maximum(var,1e-20),0,1)
        value=mean+gain*(signal-mean)
    return tone(np.clip(np.where(mask,1.,value),0,1))
def gm(v,rr):
    gg=sorted({r["group_id"] for r in rr})
    return gg,np.array([np.mean(v[[i for i,r in enumerate(rr) if r["group_id"]==g]],axis=0) for g in gg])
def ci(v,rr,stream):
    gg,mm=gm(v,rr); rng=np.random.default_rng(stream)
    q=np.quantile(mm[rng.integers(0,3,(2000,3))].mean(axis=1),[.025,.975])
    return {"mean_difference":float(mm.mean()),"ci95":q.tolist(),"group_mean_differences":dict(zip(gg,mm.tolist()))}
def ccheck(a,b,errors):
    errors["CI_mean"]=max(errors["CI_mean"],abs(a["mean_difference"]-b["mean_difference"]))
    errors["CI_endpoints"]=max(errors["CI_endpoints"],err(a["ci95"],b["descriptive_paired_cluster_percentile_ci95"]))
    errors["CI_group_values"]=max(errors["CI_group_values"],err(list(a["group_mean_differences"].values()),[b["group_mean_differences"][g] for g in a["group_mean_differences"]]))
    req(b["diagnostic_group_count"]==3 and b["bootstrap_replicates"]==2000,"CI unit/count")
    req(max(errors.values())<=1e-16,"statistical disagreement")
def main():
    start=time.perf_counter()
    a,m=rj(NEW/"results.json"),rj(NEW/"run_meta.json")
    old,refined=rj(OUT/"relative-experiment-retry02/results.json"),rj(OUT/"relative-experiment-refinement04_08/results.json")
    audit,cache,protocol=rj(OUT/"dng_audit.json"),rj(CACHE/"cache_manifest.json"),rj(D/"DNG_PROTOCOL.json")
    report={"status":"RUNNING","audited_at_utc":datetime.now(timezone.utc).isoformat(),"source_commit":COMMIT,"source_tree":TREE,
      "audit_scope":"independent same-family code/numerical audit; not cross-family review or novelty verdict",
      "stats_implementation":"CSV group means and documented SeedSequence, no call to cross_evaluate/paired_cluster_ci"}
    req(m["status"]=="COMPLETED" and m["exit_code"]==0,"formal completion")
    req(a["git_commit"]==m["git_commit"]==COMMIT and not a["git_worktree_dirty"],"clean frozen commit")
    req(subprocess.check_output(["git","show","-s","--format=%T",COMMIT],cwd=REPO,text=True).strip()==TREE==m["source_tree"],"tree")
    req(a["source_metrics_sha256"]==sha(NEW/"source_metrics.csv"),"CSV hash")
    req(a["new_protocol_sha256"]==sha(D/"DNG_HISTORY_CONTROL.md"),"new protocol")
    req(a["original_protocol_sha256"]==audit["protocol_sha256"]==cache["protocol_sha256"]==old["protocol_sha256"]==refined["protocol_sha256"]==sha(D/"DNG_PROTOCOL.json"),"original protocol")
    req(a["source_manifest_sha256"]==audit["manifest_sha256"]==old["source_manifest_sha256"]==refined["source_manifest_sha256"]==sha(RAW/"dataset.json"),"original manifest")
    req(a["config"]["seeds"]==[19,37,73] and a["config"]["future_repeats"]==4 and a["config"]["past_preview_frames"]==3 and a["config"]["past_preview_exposure"]==.25 and a["config"]["bootstrap_replicates"]==2000 and a["config"]["bayesian_nodes"] is None,"config")
    req(a["actions"]==protocol["actions"]==E.tolist(),"actions")
    req(a["sensor_assumptions"]=={"full_well":1000.,"read_sd":4.,"adc_max":4095,"camera_calibrated":False},"sensor")
    req({p.name for p in NEW.iterdir()} <= {"results.json","source_metrics.csv","run_meta.json","summary.json"},"no pixel outputs")
    sources=audit["sources"]; sm={s["source_id"]:s for s in sources}; cm={s["source_id"]:s for s in cache["sources"]}
    req(len(sm)==68==a["source_count"] and set(sm)==set(cm) and len({s["sha256"] for s in sources})==68,"unique sources")
    grouping={pid:(g["group_id"],g["split"]) for g in protocol["source_groups"] for pid in g["pair_ids"]}
    for s in sources:
        sid=s["source_id"]
        req((s["group_id"],s["split"])==grouping[s["pair_id"]],"frozen split")
        req({k:s[k] for k in cm[sid]}==cm[sid],"cache identity")
        req(sha(RAW/s["path"])==s["sha256"],"original DNG bytes "+sid)
        req(sha(CACHE/f"{sid}.npz")==a["cache_sha256"][sid]==old["cache_sha256"][sid]==refined["cache_sha256"][sid],"cache bytes")
        with np.load(CACHE/f"{sid}.npz",allow_pickle=False) as z:
            x=z["green"]
            req(set(z.files)=={"green"} and x.shape==(8,64,64) and np.isfinite(x).all() and x.min()>=0 and x.max()<=1,"cache schema")
    req(dict(Counter(s["split"] for s in sources))=={"train":28,"development":16,"diagnostic":24},"source counts")
    report["provenance"]={"raw_DNG_hashes_verified":68,"cache_hashes_verified":68,"source_split_counts":{"train":28,"development":16,"diagnostic":24},
      "original_protocol_sha256":audit["protocol_sha256"],"source_manifest_sha256":audit["manifest_sha256"],
      "diagnostic_groups":["g04","g06","g10"],"output_files":sorted(p.name for p in NEW.iterdir()),"raw_pixels_exported":False,
      "formal_exit_code":0,"formal_internal_seconds":a["elapsed_seconds"],"launcher_seconds":m["wall_seconds"]}
    print("all 68 raw/cache byte hashes and frozen protocol verified",flush=True)
    test=subprocess.run([sys.executable,"-m","pytest","-q","research/ae_tm/tests/test_ae_tm_dng_history_control.py"],cwd=REPO,text=True,capture_output=True)
    report["committed_tests"]={"exit_code":test.returncode,"stdout":test.stdout,"stderr":test.stderr}
    req(test.returncode==0 and "13 passed" in test.stdout,"13 committed tests")
    rng=np.random.default_rng(10103); fe=ve=se=0.; probes=0
    for trial in range(5):
        h=rng.integers(0,4096,(3,2,9,10),dtype=np.int16); y=rng.integers(0,4096,(4,2,9,10),dtype=np.int16)
        h[:,0,0,0]=4095; y[:,0,0,0]=4095; h[:,1,0,0]=0; y[:,1,0,0]=0
        for e in E:
            expected=fusion(h,y,float(e)); actual=ctl.classical_fusion_estimate(h,y,float(e))
            fe=max(fe,err(expected[0],actual[0])); ve=max(ve,err(expected[1],actual[1]))
            req(np.array_equal(expected[2],actual[2]),"fallback mask"); probes+=1
            for w in (1,3,5,7):
                pred=ctl.fusion_wiener_target(*actual[:2],w,actual[2])
                se=max(se,err(spatial(*expected[:2],w,expected[2]),pred))
                yy=y.copy(); yy[3]=4095; alt=ctl.classical_fusion_estimate(h,yy,float(e))
                req(np.array_equal(pred[:3],ctl.fusion_wiener_target(*alt[:2],w,alt[2])[:3]),"repeat isolation")
                changed=actual[0].copy(); changed[:,1]=0
                req(np.array_equal(pred[:,0],ctl.fusion_wiener_target(changed,actual[1],w,actual[2])[:,0]),"patch isolation")
    req(fe<=2e-15 and ve<=2e-15 and se<=1e-12,"independent WLS/spatial")
    h=np.zeros((3,1,3,3),dtype=np.int16); y=np.full((1,1,3,3),500,dtype=np.int16)
    s,_,_=ctl.classical_fusion_estimate(h,y,1.)
    req(np.all(s>0) and np.all(s<500/4095),"zero code kept")
    dropped=ctl.classical_fusion_estimate(h,np.full_like(y,4095),1.)
    req(np.all(dropped[0]==0) and not dropped[2].any(),"top dropped")
    fallback=ctl.classical_fusion_estimate(np.full_like(h,4095),np.full_like(y,4095),1.)
    req(np.all(fallback[0]==1) and np.all(fallback[1]==1) and fallback[2].all(),"finite fallback")
    req(set(inspect.signature(ctl.classical_fusion_estimate).parameters)=={"history_codes","future_codes","exposure"},"no latent input")
    report["functional_probes"]={"explicit_WLS_probes":probes,"manual_2D_spatial_probes":probes*4,"max_estimate_error":fe,"max_variance_error":ve,
      "max_spatial_target_error":se,"repeat_isolation":True,"patch_isolation":True,"zero_keep_top_drop":True,"finite_fallback":True}
    print("independent explicit WLS and manual 2D filter probes passed",flush=True)


    features={}
    for seed in (19,37,73):
        for s in sources:
            with np.load(CACHE/f"{s['source_id']}.npz",allow_pickle=False) as z: x=z["green"].astype(float)
            camid=0 if s["camera"]=="iphone" else 1
            stream=np.random.SeedSequence([seed,s["pair_id"],camid]).spawn(2)[0]
            h=capture(np.broadcast_to(x,(3,)+x.shape),.25,np.random.default_rng(stream)); f=feat(h)
            hh,ff=ctl.preview_history_and_features(x,np.random.default_rng(stream))
            lf=ctl.legacy.preview_features(x,np.random.default_rng(stream))
            req(np.array_equal(h,hh) and np.array_equal(f,ff) and np.array_equal(f,lf),"exact original H/features")
            features[(seed,s["source_id"])]=f
    report["history_features"]={"source_seed_combinations":204,"H_codes_max_error":0.,"new_and_legacy_features_max_error":0.,"future_frames_recaptured":0}
    print("204 rebuilt H/code/features match exactly; no formal future recapture",flush=True)
    rr=rows(NEW/"source_metrics.csv")
    key=lambda r:(int(r["seed"]),r["camera"],r["source_selector"],r["renderer"],r["source_id"])
    lk={key(r):r for r in rr}; req(len(rr)==len(lk)==1152,"1152 unique crossover source rows")
    okey=lambda r:(int(r["seed"]),r["camera"],r["backend"],r["source_id"])
    ol={okey(r):r for r in rows(OUT/"relative-experiment-retry02/source_metrics.csv")}
    rl={okey(r):r for r in rows(OUT/"relative-experiment-refinement04_08/source_metrics.csv")}
    lm={"H_blind_inverse":"inverse","H_blind_Wiener":"local_wiener"}; matched=0
    for r in rr:
        s=sm[r["source_id"]]
        req(r["camera"]==s["camera"] and r["group_id"]==s["group_id"] and r["split"]==s["split"]=="diagnostic","CSV source identity")
        if r["source_selector"]==r["renderer"] and r["renderer"] in lm:
            prev=ol[(int(r["seed"]),r["camera"],lm[r["renderer"]],r["source_id"])]
            for field in RF+["dev_fixed_action"]+[f"policy_action_{f}" for f in F]:
                req(float(r[field])==float(prev[field])==float(rl[okey(prev)][field]),"legacy exact "+field)
            matched+=1
    req(matched==144,"144 blind legacy source rows")
    report["legacy_parity"]={"rows_verified":144,"actions_per_row":7,"max_risk_absolute_difference":0.,
      "dev_fixed_mismatches":0,"frozen_rule_action_mismatches":0,"baseline_outputs":["retry02","refinement04_08"]}
    errors={k:0. for k in ("action_risk","fixed_risk","policy_risk","CI_mean","CI_endpoints","CI_group_values")}
    cells,diagonal,degen,changes=[],[],[],[]; nc=nquant=nactions=0
    for rep in a["replicates"]:
        seed=rep["seed"]
        req(rep["all_weight_zero_counts_by_action"]==[0]*7,"actual all-weight-zero count")
        req(rep["pixel_observations_per_action"]==68*4*8*64*64,"pixel count")
        for camid,camera in enumerate(("iphone","s25")):
            cr=rep["cameras"][camera]
            ss=[s for s in sources if s["camera"]==camera]
            ds=[s for s in ss if s["split"]=="diagnostic"]; ts=[s for s in ss if s["split"]=="train"]
            req(cr["source_counts_by_split"]=={"train":14,"development":8,"diagnostic":12},"camera split counts")
            req(cr["diagnostic_group_ids"]==["g04","g06","g10"],"group units")
            selectors=cr["frozen_selectors"]
            for si,sname in enumerate(B):
                sel=selectors[sname]; fixed=sel["dev_fixed_action_index"]
                req(fixed==int(np.argmin(sel["dev_group_balanced_risk_by_action"])) and sel["dev_fixed_exposure"]==float(E[fixed]),"fixed argmin/exposure")
                opts=a["config"]["windows"][sname]
                req([opts[i] for i in sel["window_indices"]]==sel["dev_selected_windows_by_action"],"dev window indices")
                for fi,f in enumerate(F):
                    rule=sel["frozen_rules"][f]
                    q=np.unique(np.quantile([features[(seed,s["source_id"])][fi] for s in ts],np.arange(.1,1,.1)))
                    req(np.array_equal(q,rule["candidate_thresholds_train_only"]) and rule["threshold"] in q,"train-only quantile grid")
                    req(0<=rule["left"]<7 and 0<=rule["right"]<7,"legal rule actions")
                    nquant+=1
                    aa=[rule["left"] if features[(seed,s["source_id"])][fi]<=rule["threshold"] else rule["right"] for s in ds]
                    degen.append({"seed":seed,"camera":camera,"selector":sname,"rule":f,"left":rule["left"],"right":rule["right"],
                      "globally_constant":rule["left"]==rule["right"],"equals_dev_fixed":rule["left"]==rule["right"]==fixed,"diagnostic_used_actions":sorted(set(aa))})
                if sname in lm:
                    oc=next(r for r in old["replicates"] if r["seed"]==seed)["cameras"][camera]
                    os=oc["backends"][lm[sname]]
                    req(sel["frozen_rules"]==os["frozen_rules"] and sel["dev_group_balanced_risk_by_action"]==os["dev_risk_by_action"]
                      and sel["dev_fixed_exposure"]==os["diagnostic"]["dev_fixed_exposure"],"legacy full frozen selectors")
                    if sname=="H_blind_Wiener": req(sel["dev_selected_windows_by_action"]==oc["dev_selected_spatial_windows"],"legacy windows")
                for ri,rname in enumerate(B):
                    sr=[lk[(seed,camera,sname,rname,s["source_id"])] for s in ds]
                    c=np.array([[float(r[f]) for f in RF] for r in sr])
                    req(np.isfinite(c).all() and np.all(c>=0),"finite costs")
                    cell=cr["backend_cross_matrix"][sname][rname]
                    req(cell["source_selector_dev_fixed_action_index"]==fixed and cell["source_selector_dev_fixed_exposure"]==float(E[fixed]),"cross source fixed")
                    req(cell["renderer_windows"]==selectors[rname]["dev_selected_windows_by_action"],"renderer own frozen windows")
                    req(all(int(r["source_selector_dev_fixed_action"])==int(r["dev_fixed_action"])==fixed for r in sr),"CSV source fixed")
                    _,ga=gm(c,sr); ar=ga.mean(axis=0); fc=c[:,fixed]; _,fg=gm(fc,sr); fr=float(fg.mean())
                    errors["action_risk"]=max(errors["action_risk"],err(ar,cell["group_balanced_risk_by_action"]))
                    errors["fixed_risk"]=max(errors["fixed_risk"],abs(fr-cell["fixed_group_balanced_risk"]))
                    acts={}
                    for fi,f in enumerate(F):
                        rule=sel["frozen_rules"][f]
                        aa=np.array([rule["left"] if features[(seed,s["source_id"])][fi]<=rule["threshold"] else rule["right"] for s in ds])
                        req(np.array_equal(aa,[int(r[f"policy_action_{f}"]) for r in sr]),"CSV actions from independent H")
                        req(all(int(lk[(seed,camera,sname,B[0],s["source_id"])][f"policy_action_{f}"])==int(lk[(seed,camera,sname,rname,s["source_id"])][f"policy_action_{f}"]) for s in ds),"frozen actions across columns")
                        acts[f]=aa; nactions+=len(aa)
                    brightness=c[np.arange(len(c)),acts["mean_brightness"]]
                    children=np.random.SeedSequence([seed,camid,si,ri,9081]).spawn(8)
                    entry={"seed":seed,"camera":camera,"selector":sname,"renderer":rname,"selector_fixed_index":fixed,
                      "selector_fixed_exposure":float(E[fixed]),"action_risks":ar.tolist(),"fixed_risk":fr,"policies":{}}
                    for fi,f in enumerate(F):
                        v=c[np.arange(len(c)),acts[f]]; _,gv=gm(v,sr); risk=float(gv.mean())
                        p=cell["policies"][f]
                        errors["policy_risk"]=max(errors["policy_risk"],abs(risk-p["group_balanced_risk"]))
                        req(np.array_equal(np.bincount(acts[f],minlength=7),p["source_action_counts"]),"action counts")
                        cf=ci(v-fc,sr,children[2*fi]); cb=ci(v-brightness,sr,children[2*fi+1])
                        ccheck(cf,p["paired_rule_minus_selector_fixed"],errors); ccheck(cb,p["paired_rule_minus_mean_brightness"],errors); nc+=2
                        entry["policies"][f]={"risk":risk,"gain_percent_vs_source_fixed":100*(1-risk/fr),"rule_minus_fixed":cf,
                          "direct_rule_minus_brightness":cb,"action_counts":np.bincount(acts[f],minlength=7).tolist()}
                        if sname==rname:
                            diagonal.append({"seed":seed,"camera":camera,"backend":rname,"rule":f,"fixed_exposure":float(E[fixed]),"fixed_risk":fr,"policy_risk":risk,
                              "gain_percent":100*(1-risk/fr),"fixed_difference":cf["mean_difference"],"fixed_ci95":cf["ci95"],
                              "direct_brightness_difference":cb["mean_difference"],"direct_brightness_ci95":cb["ci95"],
                              "left_exposure":float(E[sel["frozen_rules"][f]["left"]]),"right_exposure":float(E[sel["frozen_rules"][f]["right"]])})
                    cells.append(entry)
    req(len(cells)==96 and nc==768 and max(errors.values())<=1e-16,"96 cells and 768 CIs")
    for seed in (19,37,73):
        for camera in ("iphone","s25"):
            for sname in B:
                cc=[c for c in cells if c["seed"]==seed and c["camera"]==camera and c["selector"]==sname]
                for f in F:
                    dd=[c["policies"][f]["rule_minus_fixed"]["mean_difference"] for c in cc]
                    if min(dd)<0<max(dd):
                        changes.append({"seed":seed,"camera":camera,"selector":sname,"rule":f,
                          "renderer_differences":{c["renderer"]:c["policies"][f]["rule_minus_fixed"]["mean_difference"] for c in cc}})
    report["recalculation"]={"csv_rows":1152,"matrix_cells":96,"paired_CIs":768,"train_only_threshold_sets":nquant,
      "diagnostic_rule_actions_verified":nactions,"all_source_selector_fixed_actions_retained":True,"max_absolute_errors":errors,
      "cells":cells,"diagonal_policies":diagonal,"frozen_rule_degeneracy":degen,"renderer_fixed_difference_sign_changes":changes}
    report["actual_all_weight_zero_counts"]={str(r["seed"]):r["all_weight_zero_counts_by_action"] for r in a["replicates"]}
    report["limitations"]=[
      "Approximate data-dependent WLS with uncalibrated unclipped independent-noise variance; estimated/censored weights and clipping bias remain.",
      "Local Wiener is a classical simplicity control, not a strong unrestricted image Bayes bound.",
      "Same processed noisy/clipped surrogate, not clean radiance, expert GT, physical recapture or S24.",
      "Only three diagnostic groups from one session; camera/crop/noise copies add no independent scenes.",
      "768 CIs are descriptive, conditional on frozen development selections, not independent discoveries.",
      "Same-family audit does not replace the pending cross-family novelty and critical reviews."]
    report["status"]="PASS_WITH_SCOPE_LIMITS"; report["audit_elapsed_seconds"]=time.perf_counter()-start
    JP.write_text(json.dumps(report,indent=2,allow_nan=False)+"\n",encoding="utf-8")
    lines=["# DNG history-control independent code and numerical audit","",
      "**PASS_WITH_SCOPE_LIMITS**. Same-family independent code/numerical audit; not cross-family review or novelty verdict.",
      f"Frozen source commit {COMMIT}, tree {TREE}. Formal exit 0; internal {a['elapsed_seconds']:.6f}s; launcher {m['wall_seconds']:.6f}s.","",
      "## Provenance and functional checks","",
      "- Verified all 68 actual original DNG byte hashes, cache byte hashes, frozen source identities/splits, protocol/manifest hashes and legal actions. Original source counts: train 28, development 16, diagnostic 24.",
      "- Runner outputs results.json/source_metrics.csv/run_meta.json. A post-run root summary.json also exists and was excluded from this audit; no real H/future/source pixel array was exported.",
      "- Renderer receives H plus only one future repeat, known e and no target/latent/source identity. Changing another repeat or patch cannot change this prediction.",
      "- Same 2D window is used for fusion signal moments and local nominal noise mean. No repeat/patch filtering.",
      "- Observed top code 4095 loses its weight; zero code retains weight. All-weight-zero case gives finite estimate 1/variance 1 and spatial processing preserves estimate 1.",
      f"- Independent explicit WLS: {probes} probes, maximum estimate error {fe:.3e}, variance error {ve:.3e}; manual sliding-window spatial: {probes*4} probes, maximum tone-target error {se:.3e}.",
      "- Independently rebuilt all 204 seed/source H captures/features; codes and new/legacy feature vectors exactly agree. No seven-action formal future simulation was rerun.",
      "- Committed necessary tests: 13 passed, exit 0.","",
      "## Legacy and paired statistics","",
      "- All 144 H-blind diagonal source rows match both retry02 and refinement04_08 exactly for seven action costs, fixed actions and four policy actions.",
      "- Blind full frozen rule dictionaries, development action risks and Wiener windows match original output.",
      f"- Directly recomputed 96 matrix cells and 768 paired CIs from 1152 source CSV rows; verified {nquant} train-only threshold sets and {nactions} diagnostic rule actions from independently rebuilt H.",
      "- Every cross cell retains its SOURCE selector fixed action and threshold actions; the renderer retains its own frozen development windows. No cell-specific fixed action reselection.",
      "- Average sources within each of g04/g06/g10 first, then give the three groups equal weight. Bootstrap samples groups, not crop/noise/source copies.","",
      "| Quantity | Maximum absolute error versus raw results.json |","|---|---:|"]
    lines += [f"| {k} | {v:.3e} |" for k,v in errors.items()]
    lines += ["","Actual all-weight-zero counts at all seven actions: seed 19 [0,0,0,0,0,0,0], seed 37 [0,0,0,0,0,0,0], seed 73 [0,0,0,0,0,0,0].","",
      "## H-aware own-backend outcomes","",
      "Gains compare each selector with its own dev fixed e. Negative means worse. Direct paired difference is rule minus mean-brightness; negative favors the named rule. Intervals are descriptive.","",
      "| Camera | Seed | Backend | Fixed e | Rule | Gain vs fixed % | Direct difference vs mean | Direct paired 95% CI | Frozen e left/right |",
      "|---|---:|---|---:|---|---:|---:|---|---|"]
    for r in diagonal:
        if r["backend"].startswith("H_aware"):
            lo,hi=r["direct_brightness_ci95"]
            lines.append(f"| {r['camera']} | {r['seed']} | {r['backend']} | {r['fixed_exposure']:g} | {r['rule']} | {r['gain_percent']:.6f} | {r['direct_brightness_difference']:.8e} | [{lo:.8e}, {hi:.8e}] | {r['left_exposure']:g}/{r['right_exposure']:g} |")
    lines += ["","## Frozen-rule degeneracy and renderer-dependent signs",""]
    for camera in ("iphone","s25"):
        for backend in B[2:]:
            dd=[r for r in degen if r["camera"]==camera and r["selector"]==backend]
            lines.append(f"- {camera}, {backend}: {sum(r['globally_constant'] for r in dd)}/12 globally constant rules; {sum(r['equals_dev_fixed'] for r in dd)}/12 exactly equal their source dev fixed.")
    lines += [f"- {len(changes)} seed/camera/selector/rule combinations change sign of rule-minus-source-fixed when replayed through different renderers. Complete cases and all 96 cells are in the JSON audit.","","## Limits",""]
    lines += ["- "+v for v in report["limitations"]]
    lines += ["","No implementation or paired-summary mismatch found in this frozen diagnostic. Constant or worse residual rules do not establish complex AE necessity; surviving gains are conditional on these classical backends, uncalibrated sensor assumptions and three backgrounds.",
      "","Audit command: task venv Python work/capturetm-local-dng/dng_history_control_independent_audit.py. No calls to cross_evaluate/paired_cluster_ci, selector refit, formal future rerun or experiment/dataset writes.",
      f"Audit elapsed {report['audit_elapsed_seconds']:.6f}s. Exit 0 after assertions. JSON SHA256 {sha(JP)}.",""]
    MP.write_text("\n".join(lines),encoding="utf-8")
    print(json.dumps({"status":report["status"],"matrix_cells":96,"paired_CIs":768,"legacy_exact_rows":144,
      "max_errors":errors,"elapsed_seconds":report["audit_elapsed_seconds"]}),flush=True)
    return 0
if __name__=="__main__":
    try: raise SystemExit(main())
    except Exception as e:
        failure={"status":"FAILED","error":repr(e),"traceback":traceback.format_exc(),"scope":"same-family independent audit"}
        JP.write_text(json.dumps(failure,indent=2)+"\n",encoding="utf-8")
        MP.write_text("# DNG history-control independent audit\n\n**FAILED**\n\n"+repr(e)+"\n\n"+failure["traceback"],encoding="utf-8")
        raise
