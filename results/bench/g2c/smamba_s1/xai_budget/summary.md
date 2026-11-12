# g2c · smamba (scan axis: variate) · seed 1

Forecast on the explained split: MSE 0.0000, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.554 | 0.531 | 0.412 | 0.640 | 0.640 | 0.977 | 0.004 | 0.686 | 0.154 | 128.000 | 0.033 | nan |
| IG-U4 | 0.421 | 0.400 | 0.307 | 0.660 | 0.660 | 0.819 | 0.142 | 0.654 | 0.165 | 128.000 | 0.030 | nan |
| IG-U8 | 0.608 | 0.538 | 0.422 | 0.680 | 0.680 | 0.885 | 0.042 | 0.666 | 0.130 | 128.000 | 0.031 | nan |
| IG-U16 | 0.609 | 0.583 | 0.439 | 0.680 | 0.680 | 0.951 | 0.006 | 0.693 | 0.138 | 128.000 | 0.029 | nan |
| SHAP-U4 | 0.404 | 0.377 | 0.282 | 0.620 | 0.620 | 0.816 | 0.136 | 0.674 | 0.110 | 8195 | 0.319 | nan |
| SHAP-U8 | 0.587 | 0.550 | 0.336 | 0.660 | 0.660 | 0.882 | 0.043 | 0.672 | 0.119 | 8195 | 0.364 | nan |
| SHAP-U16 | 0.591 | 0.582 | 0.289 | 0.700 | 0.700 | 0.960 | 0.006 | 0.711 | 0.125 | 13315 | 0.642 | nan |
