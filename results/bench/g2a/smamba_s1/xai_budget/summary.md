# g2a · smamba (scan axis: variate) · seed 1

Forecast on the explained split: MSE 0.0047, trivial 1.0000, skill 0.995
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.556 | 0.499 | 0.422 | 0.640 | 0.640 | 1.084 | 0.008 | 0.711 | 0.203 | 128.000 | 0.040 | nan |
| IG-U4 | 0.391 | 0.343 | 0.298 | 0.640 | 0.640 | 0.877 | 0.146 | 0.596 | 0.091 | 128.000 | 0.037 | nan |
| IG-U8 | 0.544 | 0.490 | 0.422 | 0.660 | 0.660 | 0.956 | 0.019 | 0.703 | 0.112 | 128.000 | 0.037 | nan |
| IG-U16 | 0.553 | 0.510 | 0.442 | 0.680 | 0.680 | 1.028 | 0.011 | 0.673 | 0.120 | 128.000 | 0.038 | nan |
| SHAP-U4 | 0.365 | 0.340 | 0.258 | 0.520 | 0.520 | 0.906 | 0.147 | 0.567 | 0.078 | 8195 | 0.372 | nan |
| SHAP-U8 | 0.533 | 0.467 | 0.335 | 0.580 | 0.580 | 0.962 | 0.019 | 0.679 | 0.124 | 8195 | 0.420 | nan |
| SHAP-U16 | 0.528 | 0.497 | 0.287 | 0.620 | 0.620 | 1.083 | 0.013 | 0.692 | 0.152 | 13315 | 0.737 | nan |
