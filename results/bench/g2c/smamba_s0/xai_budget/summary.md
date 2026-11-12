# g2c · smamba (scan axis: variate) · seed 0

Forecast on the explained split: MSE 0.0120, trivial 1.0000, skill 0.988
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.827 | 0.773 | 0.536 | 1.000 | 1.000 | 0.899 | 0.001 | 0.268 | 0.286 | 128.000 | 0.032 | nan |
| IG-U4 | 0.599 | 0.627 | 0.425 | 1.000 | 1.000 | 0.729 | 0.008 | 0.427 | 0.035 | 128.000 | 0.028 | nan |
| IG-U8 | 0.835 | 0.755 | 0.567 | 1.000 | 1.000 | 0.767 | 0.002 | 0.443 | 0.212 | 128.000 | 0.028 | nan |
| IG-U16 | 0.880 | 0.832 | 0.581 | 1.000 | 1.000 | 0.868 | 0.002 | 0.539 | 0.319 | 128.000 | 0.028 | nan |
| SHAP-U4 | 0.591 | 0.640 | 0.365 | 0.960 | 0.960 | 0.658 | 0.006 | 0.329 | 0.061 | 8195 | 0.325 | nan |
| SHAP-U8 | 0.779 | 0.690 | 0.469 | 1.000 | 1.000 | 0.725 | 0.002 | 0.287 | 0.117 | 8195 | 0.347 | nan |
| SHAP-U16 | 0.827 | 0.731 | 0.444 | 1.000 | 1.000 | 0.816 | 0.002 | 0.303 | 0.129 | 13315 | 0.635 | nan |
