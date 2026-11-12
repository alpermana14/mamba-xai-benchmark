# g2a · itransformer (scan axis: none (attention)) · seed 1

Forecast on the explained split: MSE 0.0002, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.851 | 0.784 | 0.390 | 1.000 | 1.000 | 0.843 | 0.002 | 0.149 | 0.061 | 128.000 | 0.005 | nan |
| IG-U4 | 0.582 | 0.607 | 0.327 | 1.000 | 1.000 | 0.603 | 0.003 | 0.384 | 0.058 | 128.000 | 0.004 | nan |
| IG-U8 | 0.851 | 0.783 | 0.432 | 1.000 | 1.000 | 0.712 | 0.002 | 0.414 | 0.094 | 128.000 | 0.004 | nan |
| IG-U16 | 0.930 | 0.898 | 0.435 | 1.000 | 1.000 | 0.816 | 0.002 | 0.339 | 0.045 | 128.000 | 0.004 | nan |
| SHAP-U4 | 0.530 | 0.532 | 0.216 | 0.880 | 0.880 | 0.617 | 0.074 | 0.351 | 0.156 | 8195 | 0.148 | nan |
| SHAP-U8 | 0.767 | 0.708 | 0.285 | 0.960 | 0.960 | 0.759 | 0.033 | 0.424 | 0.110 | 8195 | 0.183 | nan |
| SHAP-U16 | 0.864 | 0.818 | 0.293 | 1.000 | 1.000 | 0.778 | 0.002 | 0.292 | 0.034 | 13315 | 0.383 | nan |
