# g2a · smamba (scan axis: variate) · seed 2

Forecast on the explained split: MSE 0.0004, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.553 | 0.491 | 0.459 | 0.640 | 0.640 | 0.948 | 0.002 | 0.692 | 0.159 | 128.000 | 0.034 | nan |
| IG-U4 | 0.421 | 0.408 | 0.341 | 0.600 | 0.600 | 0.823 | 0.032 | 0.555 | 0.109 | 128.000 | 0.029 | nan |
| IG-U8 | 0.557 | 0.476 | 0.447 | 0.640 | 0.640 | 0.851 | 0.004 | 0.518 | 0.131 | 128.000 | 0.032 | nan |
| IG-U16 | 0.579 | 0.521 | 0.466 | 0.640 | 0.640 | 0.898 | 0.003 | 0.662 | 0.148 | 128.000 | 0.029 | nan |
| SHAP-U4 | 0.389 | 0.373 | 0.316 | 0.560 | 0.560 | 0.817 | 0.032 | 0.450 | 0.137 | 8195 | 0.314 | nan |
| SHAP-U8 | 0.514 | 0.444 | 0.378 | 0.580 | 0.580 | 0.855 | 0.005 | 0.371 | 0.121 | 8195 | 0.340 | nan |
| SHAP-U16 | 0.552 | 0.493 | 0.312 | 0.640 | 0.640 | 0.982 | 0.003 | 0.608 | 0.175 | 13315 | 0.630 | nan |
