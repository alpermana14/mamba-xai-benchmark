# g2c · itransformer (scan axis: none (attention)) · seed 2

Forecast on the explained split: MSE 0.0004, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.741 | 0.658 | 0.362 | 1.000 | 1.000 | 0.892 | 0.003 | 0.170 | 0.052 | 128.000 | 0.007 | nan |
| IG-U4 | 0.603 | 0.643 | 0.308 | 1.000 | 1.000 | 0.692 | 0.004 | 0.440 | 0.030 | 128.000 | 0.005 | nan |
| IG-U8 | 0.816 | 0.712 | 0.392 | 1.000 | 1.000 | 0.770 | 0.004 | 0.479 | 0.105 | 128.000 | 0.006 | nan |
| IG-U16 | 0.822 | 0.711 | 0.401 | 1.000 | 1.000 | 0.835 | 0.003 | 0.266 | 0.059 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.565 | 0.582 | 0.192 | 0.920 | 0.920 | 0.675 | 0.023 | 0.425 | 0.047 | 8195 | 0.171 | nan |
| SHAP-U8 | 0.752 | 0.683 | 0.235 | 0.980 | 0.980 | 0.746 | 0.004 | 0.485 | 0.079 | 8195 | 0.222 | nan |
| SHAP-U16 | 0.753 | 0.687 | 0.253 | 1.000 | 1.000 | 0.790 | 0.003 | 0.239 | 0.050 | 13315 | 0.461 | nan |
