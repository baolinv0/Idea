"""CPU mechanism probes. No neural training, real-camera evidence, or repository execution.
Run: python pilot_mechanisms.py --outdir <directory>
Uses independent fitting/evaluation samples and known exposure metadata.
"""
import argparse, json, time
from pathlib import Path
import numpy as np

EXPOSURES=np.array([.125,.25,.5,1.,2.,4.,8.])
FW=1000.; READ=4.; ADC=4095.; BINS=512
TRAIN=250000; TEST=100000; SEEDS=[19,37,73]
def tone(x):
    return np.sqrt(np.maximum(x,0)/(np.maximum(x,0)+.5))
def capture(l, e, rng, noisy=True, clip=True):
    q=l*e*FW
    if noisy:
        q=rng.poisson(q)+rng.normal(0,READ,l.shape)
    q=np.maximum(q,0)
    if clip: q=np.minimum(q,FW)
    z=q/FW
    return np.rint(z*ADC)/ADC if clip else z
def binned(z, bins=BINS):
    return np.clip((z*(bins-1)).astype(int),0,bins-1)
def fit_lut(z,y):
    idx=binned(z)
    cnt=np.bincount(idx,minlength=BINS)
    total=np.bincount(idx,weights=y,minlength=BINS)
    ok=cnt>0
    return np.interp(np.arange(BINS),np.flatnonzero(ok),total[ok]/cnt[ok])
def fit_joint(za,zb,y,fallback):
    ba=binned(za,32); bb=binned(zb,128)
    idx=ba*128+bb
    cnt=np.bincount(idx,minlength=4096)
    sm=np.bincount(idx,weights=y,minlength=4096)
    # No test target is used. Empty joint bins back off to fitted pointwise estimator.
    table=np.tile(np.interp(np.linspace(0,BINS-1,128),np.arange(BINS),fallback),32)
    ok=cnt>0
    table[ok]=sm[ok]/cnt[ok]
    return table.reshape(32,128)
def mean_std(x):
    a=np.asarray(x,float)
    return {"mean":float(a.mean()),"sd_across_3_seeds":float(a.std(ddof=1))}
def pilot_one():
    regimes={}
    transfer=[]
    for noisy,clip,name in [(False,True,"clipping_only"),(True,True,"noise_and_clipping")]:
        rows=[]
        for seed in SEEDS:
            rng=np.random.default_rng(seed)
            tr=np.exp(rng.uniform(np.log(.01),np.log(2.0),TRAIN))
            tr2=np.exp(rng.uniform(np.log(.01),np.log(2.0),TRAIN))
            te=np.exp(rng.uniform(np.log(.01),np.log(2.0),TEST))
            y= tone(te)
            loss_a=[]; loss_b=[]; loss_fixed=[]; sat=[]
            for e in EXPOSURES:
                ztr=capture(tr,e,rng,noisy,clip)
                ztr2=capture(tr2,e,rng,noisy,clip)
                zte=capture(te,e,rng,noisy,clip)
                la=fit_lut(ztr,tone(tr)); lb=fit_lut(ztr2,tone(tr2))
                loss_a.append(float(np.mean((la[binned(zte)]-y)**2)))
                loss_b.append(float(np.mean((lb[binned(zte)]-y)**2)))
                loss_fixed.append(float(np.mean((tone(zte/e)-y)**2)))
                sat.append(float(np.mean(te*e>=1)))
            rows.append({"seed":seed,"lut_a_mse":loss_a,"lut_b_mse":loss_b,
                         "normalized_fixed_mse":loss_fixed,"latent_saturation_fraction":sat})
            if noisy:
                # Development samples select actions; test losses do not select actions here.
                dev=np.exp(rng.uniform(np.log(.01),np.log(2.0),TEST))
                devy=tone(dev)
                dl=[[],[],[]]
                # New, independent fits: equal exposure coverage for A and B.
                for e in EXPOSURES:
                    za=capture(tr,e,rng);zb=capture(tr2,e,rng);zd=capture(dev,e,rng)
                    aa=fit_lut(za,tone(tr));bb=fit_lut(zb,tone(tr2))
                    dl[0].append(float(np.mean((aa[binned(zd)]-devy)**2)))
                    dl[1].append(float(np.mean((bb[binned(zd)]-devy)**2)))
                    dl[2].append(float(np.mean((tone(zd/e)-devy)**2)))
                selected=[int(np.argmin(v)) for v in dl]
                costs=np.array([loss_a,loss_b,loss_fixed]).T
                transfer.append({"seed":seed,"selectors":["LUT_A","LUT_B","normalized_fixed"],
                                 "selected_exposures":[float(EXPOSURES[i]) for i in selected],
                                 "test_mse_matrix":[costs[i].tolist() for i in selected],
                                 "backend_order":["LUT_A","LUT_B","normalized_fixed"],
                                 "diagnostic_test_best_exposures":[float(EXPOSURES[np.argmin(v)]) for v in [loss_a,loss_b,loss_fixed]]})
        means=np.mean([r["lut_a_mse"] for r in rows],axis=0)
        eps=1e-4
        regimes[name]={"replicates":rows,
                       "lut_a_mse_mean":means.tolist(),
                       "best_exposure_by_test_diagnostic":float(EXPOSURES[np.argmin(means)]),
                       "near_optimal_sets_delta_mse":{str(d):EXPOSURES[means<=means.min()+d].tolist() for d in [1e-5,1e-4,5e-4]},
                       "tolerance_note":"Exploratory fixed absolute MSE grid, not tuned to success."}
    # Exact continuous invertible control, distinct from finite-binned noisy estimator.
    l=np.exp(np.random.default_rng(919).uniform(np.log(.01),np.log(2),TEST))
    ideal=[float(np.mean((tone((l*e)/e)-tone(l))**2)) for e in EXPOSURES]
    return {"ideal_no_noise_no_clipping_mse":ideal,"regimes":regimes,
            "limitation":"Marginal pointwise Bayes regression approximation, not an unrestricted spatial/neural lower bound."},transfer

def pilot_spatial():
    rows=[]
    for seed in SEEDS:
        rng=np.random.default_rng(seed+500)
        atr=rng.uniform(.05,.30,TRAIN); btr=4*atr+.6
        ate=rng.uniform(.05,.30,TEST); bte=4*ate+.6
        permtr=rng.permutation(TRAIN);permte=rng.permutation(TEST)
        losses={"predictable_point":[],"predictable_local":[],"shuffled_point":[],"shuffled_local":[]}
        clips=[]
        for e in EXPOSURES:
            za=capture(atr,e,rng);zb=capture(btr,e,rng)
            zta=capture(ate,e,rng);ztb=capture(bte,e,rng)
            for family,pt,pe in [("predictable",np.arange(TRAIN),np.arange(TEST)),("shuffled",permtr,permte)]:
                # Permute bright latent, target and captured observation together: exact matched marginal histogram.
                yatr=tone(atr);ybtr=tone(btr[pt]);ya=tone(ate);yb=tone(bte[pe])
                lat=fit_lut(za,yatr);lbt=fit_lut(zb[pt],ybtr)
                pred_a=lat[binned(zta)];pred_b=lbt[binned(ztb[pe])]
                point=float(.5*(np.mean((pred_a-ya)**2)+np.mean((pred_b-yb)**2)))
                joint_b=fit_joint(za,zb[pt],ybtr,lbt)
                local_b=joint_b[binned(zta,32),binned(ztb[pe],128)]
                local=float(.5*(np.mean((pred_a-ya)**2)+np.mean((local_b-yb)**2)))
                losses[family+"_point"].append(point);losses[family+"_local"].append(local)
            clips.append(float(.5*(np.mean(ate*e>=1)+np.mean(bte*e>=1))))
        pointdiff=np.max(np.abs(np.array(losses["predictable_point"])-np.array(losses["shuffled_point"])))
        rows.append({"seed":seed,**losses,"same_marginal_pointwise_max_mse_difference":float(pointdiff),
                     "common_latent_saturation_fraction":clips,
                     "selected_exposures_test_diagnostic":{k:float(EXPOSURES[np.argmin(v)]) for k,v in losses.items()}})
    curves={k:np.mean([r[k] for r in rows],axis=0).tolist() for k in ["predictable_point","predictable_local","shuffled_point","shuffled_local"]}
    return {"replicates":rows,"mean_mse":curves,
            "best_exposures_test_diagnostic":{k:float(EXPOSURES[np.argmin(v)]) for k,v in curves.items()},
            "histogram_match":"For each replicate, exact same latent and captured bright/dark marginal multisets; only pairing shuffled.",
            "limitation":"Two-pixel known-family prior with separately fitted equal-size local estimators; family recognition by a causal AE and full-image histogram matching are NOT established."}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--outdir",required=True);args=ap.parse_args()
    out=Path(args.outdir);out.mkdir(parents=True,exist_ok=True)
    start=time.perf_counter();p1,p3=pilot_one();p2=pilot_spatial()
    result={"status":"completed_cpu_mechanism_probes","exposures":EXPOSURES.tolist(),
            "config":{"full_well_electrons":FW,"read_noise_sd_electrons":READ,"adc_max_code":ADC,
                      "target":"sqrt(L/(L+0.5))","train_samples_per_fit":TRAIN,"test_samples":TEST,
                      "seeds":SEEDS,"lut_bins":BINS,"joint_bins":[32,128],"analog_digital_gain":1},
            "pilot_1_compensation":p1,"pilot_2_spatial":p2,"pilot_3_transfer":p3,
            "elapsed_seconds":time.perf_counter()-start,
            "scope":"Standalone simplified static monochrome sensor; no neural training, no real camera, no S24, no motion, no Bayer, no reproduction of CaptureTM."}
    (out/"pilot_results.json").write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding="utf-8")
    print(json.dumps({"elapsed_seconds":result["elapsed_seconds"],
        "compensation_best":{k:v["best_exposure_by_test_diagnostic"] for k,v in p1["regimes"].items()},
        "spatial_best":p2["best_exposures_test_diagnostic"],
        "transfer_selections":[r["selected_exposures"] for r in p3]},ensure_ascii=False))
if __name__=="__main__":main()
