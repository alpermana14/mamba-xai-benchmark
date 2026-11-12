# g2c · timemachine (scan axis: channel) · seed 2

Forecast on the explained split: MSE 0.0016, trivial 1.0000, skill 0.998
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.939 | 0.873 | 0.742 | 1.000 | 1.000 | 0.930 | 0.092 | 0.762 | 9.425 | 128.000 | 0.061 | nan |
| IG-U4 | 0.625 | 0.628 | 0.543 | 1.000 | 1.000 | 0.807 | 0.185 | 0.671 | 3.737 | 128.000 | 0.061 | nan |
| IG-U8 | 0.876 | 0.806 | 0.737 | 1.000 | 1.000 | 0.858 | 0.103 | 0.726 | 5.402 | 128.000 | 0.058 | nan |
| IG-U16 | 0.948 | 0.893 | 0.787 | 1.000 | 1.000 | 0.888 | 0.088 | 0.793 | 6.928 | 128.000 | 0.061 | nan |
| SHAP-U4 | 0.627 | 0.640 | 0.535 | 1.000 | 1.000 | 0.809 | 0.187 | 0.690 | 4.734 | 8195 | 0.498 | nan |
| SHAP-U8 | 0.882 | 0.813 | 0.655 | 1.000 | 1.000 | 0.868 | 0.112 | 0.725 | 8.411 | 8195 | 0.522 | nan |
| SHAP-U16 | 0.942 | 0.893 | 0.603 | 1.000 | 1.000 | 0.922 | 0.114 | 0.771 | 9.100 | 13315 | 0.877 | nan |
