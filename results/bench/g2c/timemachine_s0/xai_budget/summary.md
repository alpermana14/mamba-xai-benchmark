# g2c · timemachine (scan axis: channel) · seed 0

Forecast on the explained split: MSE 0.0025, trivial 1.0000, skill 0.998
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.893 | 0.831 | 0.704 | 1.000 | 1.000 | 1.154 | 0.121 | 0.941 | 2.454 | 128.000 | 0.073 | nan |
| IG-U4 | 0.616 | 0.627 | 0.514 | 1.000 | 1.000 | 0.998 | 0.245 | 0.822 | 2.116 | 128.000 | 0.072 | nan |
| IG-U8 | 0.860 | 0.772 | 0.707 | 1.000 | 1.000 | 1.056 | 0.143 | 0.875 | 2.328 | 128.000 | 0.071 | nan |
| IG-U16 | 0.917 | 0.869 | 0.752 | 1.000 | 1.000 | 1.124 | 0.140 | 0.963 | 2.450 | 128.000 | 0.075 | nan |
| SHAP-U4 | 0.617 | 0.630 | 0.506 | 1.000 | 1.000 | 0.998 | 0.257 | 0.825 | 1.576 | 8195 | 0.608 | nan |
| SHAP-U8 | 0.865 | 0.784 | 0.625 | 1.000 | 1.000 | 1.066 | 0.169 | 0.847 | 3.722 | 8195 | 0.640 | nan |
| SHAP-U16 | 0.912 | 0.871 | 0.590 | 1.000 | 1.000 | 1.133 | 0.156 | 0.943 | 3.622 | 13315 | 1.069 | nan |
