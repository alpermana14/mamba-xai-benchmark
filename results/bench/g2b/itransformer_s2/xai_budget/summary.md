# g2b · itransformer (scan axis: none (attention)) · seed 2

Forecast on the explained split: MSE 0.0003, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.867 | 0.790 | 0.565 | 1.000 | 1.000 | 0.632 | 0.015 | 0.054 | 0.013 | 128.000 | 0.007 | nan |
| IG-U4 | 0.678 | 0.703 | 0.488 | 1.000 | 1.000 | 0.472 | 0.067 | 0.285 | 0.031 | 128.000 | 0.005 | nan |
| IG-U8 | 0.889 | 0.818 | 0.593 | 1.000 | 1.000 | 0.530 | 0.032 | 0.201 | 0.015 | 128.000 | 0.006 | nan |
| IG-U16 | 0.945 | 0.888 | 0.620 | 1.000 | 1.000 | 0.608 | 0.024 | 0.225 | 0.014 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.671 | 0.705 | 0.429 | 1.000 | 1.000 | 0.452 | 0.068 | 0.265 | 0.022 | 8195 | 0.158 | nan |
| SHAP-U8 | 0.879 | 0.810 | 0.494 | 1.000 | 1.000 | 0.496 | 0.032 | 0.168 | 0.014 | 8195 | 0.186 | nan |
| SHAP-U16 | 0.923 | 0.867 | 0.491 | 1.000 | 1.000 | 0.552 | 0.024 | 0.146 | 0.013 | 13315 | 0.386 | nan |
