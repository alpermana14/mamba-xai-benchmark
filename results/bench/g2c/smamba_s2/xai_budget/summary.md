# g2c · smamba (scan axis: variate) · seed 2

Forecast on the explained split: MSE 0.0036, trivial 1.0000, skill 0.996
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.569 | 0.553 | 0.432 | 0.760 | 0.760 | 0.773 | 0.006 | 0.450 | 0.205 | 128.000 | 0.032 | nan |
| IG-U4 | 0.528 | 0.508 | 0.372 | 0.920 | 0.920 | 0.601 | 0.067 | 0.414 | 0.123 | 128.000 | 0.030 | nan |
| IG-U8 | 0.713 | 0.679 | 0.486 | 0.920 | 0.920 | 0.671 | 0.008 | 0.439 | 0.144 | 128.000 | 0.027 | nan |
| IG-U16 | 0.708 | 0.676 | 0.497 | 0.920 | 0.920 | 0.737 | 0.005 | 0.508 | 0.122 | 128.000 | 0.028 | nan |
| SHAP-U4 | 0.593 | 0.630 | 0.395 | 1.000 | 1.000 | 0.647 | 0.074 | 0.324 | 0.078 | 8195 | 0.309 | nan |
| SHAP-U8 | 0.798 | 0.734 | 0.494 | 1.000 | 1.000 | 0.695 | 0.004 | 0.391 | 0.096 | 8195 | 0.346 | nan |
| SHAP-U16 | 0.819 | 0.764 | 0.435 | 1.000 | 1.000 | 0.806 | 0.003 | 0.477 | 0.089 | 13315 | 0.621 | nan |
