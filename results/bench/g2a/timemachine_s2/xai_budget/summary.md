# g2a · timemachine (scan axis: channel) · seed 2

Forecast on the explained split: MSE 0.0010, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.937 | 0.865 | 0.701 | 1.000 | 1.000 | 0.950 | 0.059 | 0.701 | 2.897 | 128.000 | 0.046 | nan |
| IG-U4 | 0.643 | 0.667 | 0.543 | 1.000 | 1.000 | 0.826 | 0.142 | 0.672 | 0.701 | 128.000 | 0.043 | nan |
| IG-U8 | 0.889 | 0.808 | 0.724 | 1.000 | 1.000 | 0.904 | 0.081 | 0.689 | 2.081 | 128.000 | 0.044 | nan |
| IG-U16 | 0.941 | 0.906 | 0.757 | 1.000 | 1.000 | 0.934 | 0.076 | 0.736 | 3.588 | 128.000 | 0.042 | nan |
| SHAP-U4 | 0.630 | 0.667 | 0.573 | 1.000 | 1.000 | 0.830 | 0.142 | 0.891 | 0.882 | 8195 | 0.393 | nan |
| SHAP-U8 | 0.864 | 0.773 | 0.774 | 1.000 | 1.000 | 0.904 | 0.083 | 0.647 | 2.304 | 8195 | 0.440 | nan |
| SHAP-U16 | 0.929 | 0.893 | 0.711 | 1.000 | 1.000 | 0.935 | 0.077 | 0.707 | 3.375 | 13315 | 0.780 | nan |
