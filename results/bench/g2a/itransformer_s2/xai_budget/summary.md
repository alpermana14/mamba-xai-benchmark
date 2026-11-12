# g2a · itransformer (scan axis: none (attention)) · seed 2

Forecast on the explained split: MSE 0.0002, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.805 | 0.717 | 0.386 | 1.000 | 1.000 | 0.766 | 0.007 | 0.147 | 0.090 | 128.000 | 0.010 | nan |
| IG-U4 | 0.615 | 0.673 | 0.352 | 1.000 | 1.000 | 0.656 | 0.007 | 0.405 | 0.039 | 128.000 | 0.009 | nan |
| IG-U8 | 0.832 | 0.762 | 0.434 | 1.000 | 1.000 | 0.714 | 0.006 | 0.376 | 0.060 | 128.000 | 0.010 | nan |
| IG-U16 | 0.866 | 0.831 | 0.435 | 1.000 | 1.000 | 0.762 | 0.006 | 0.167 | 0.052 | 128.000 | 0.010 | nan |
| SHAP-U4 | 0.582 | 0.615 | 0.232 | 0.820 | 0.820 | 0.675 | 0.056 | 0.407 | 0.095 | 8195 | 0.171 | nan |
| SHAP-U8 | 0.808 | 0.733 | 0.269 | 0.980 | 0.980 | 0.723 | 0.013 | 0.353 | 0.047 | 8195 | 0.198 | nan |
| SHAP-U16 | 0.837 | 0.793 | 0.290 | 1.000 | 1.000 | 0.745 | 0.006 | 0.138 | 0.038 | 13315 | 0.398 | nan |
