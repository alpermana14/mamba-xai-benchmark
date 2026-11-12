# g2a · smamba (scan axis: variate) · seed 0

Forecast on the explained split: MSE 0.0000, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.863 | 0.779 | 0.618 | 1.000 | 1.000 | 0.883 | 0.002 | 0.460 | 0.246 | 128.000 | 0.055 | nan |
| IG-U4 | 0.635 | 0.645 | 0.504 | 1.000 | 1.000 | 0.740 | 0.049 | 0.521 | 0.051 | 128.000 | 0.058 | nan |
| IG-U8 | 0.862 | 0.783 | 0.658 | 1.000 | 1.000 | 0.788 | 0.004 | 0.492 | 0.084 | 128.000 | 0.055 | nan |
| IG-U16 | 0.907 | 0.847 | 0.681 | 1.000 | 1.000 | 0.832 | 0.003 | 0.520 | 0.147 | 128.000 | 0.056 | nan |
| SHAP-U4 | 0.635 | 0.642 | 0.500 | 1.000 | 1.000 | 0.715 | 0.048 | 0.508 | 0.043 | 8195 | 0.434 | nan |
| SHAP-U8 | 0.866 | 0.788 | 0.607 | 1.000 | 1.000 | 0.784 | 0.005 | 0.464 | 0.058 | 8195 | 0.463 | nan |
| SHAP-U16 | 0.902 | 0.865 | 0.564 | 1.000 | 1.000 | 0.845 | 0.003 | 0.416 | 0.125 | 13315 | 0.814 | nan |
