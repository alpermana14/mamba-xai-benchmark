# g2a · timemachine (scan axis: channel) · seed 1

Forecast on the explained split: MSE 0.0010, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.919 | 0.854 | 0.683 | 1.000 | 1.000 | 0.958 | 0.052 | 0.665 | 4.374 | 128.000 | 0.044 | nan |
| IG-U4 | 0.598 | 0.607 | 0.505 | 1.000 | 1.000 | 0.803 | 0.163 | 0.648 | 2.075 | 128.000 | 0.039 | nan |
| IG-U8 | 0.874 | 0.798 | 0.704 | 1.000 | 1.000 | 0.895 | 0.085 | 0.676 | 4.427 | 128.000 | 0.039 | nan |
| IG-U16 | 0.932 | 0.880 | 0.744 | 1.000 | 1.000 | 0.936 | 0.069 | 0.696 | 5.566 | 128.000 | 0.038 | nan |
| SHAP-U4 | 0.587 | 0.607 | 0.530 | 1.000 | 1.000 | 0.805 | 0.167 | 0.611 | 2.098 | 8195 | 0.395 | nan |
| SHAP-U8 | 0.846 | 0.766 | 0.742 | 1.000 | 1.000 | 0.897 | 0.087 | 0.633 | 4.930 | 8195 | 0.430 | nan |
| SHAP-U16 | 0.913 | 0.852 | 0.701 | 1.000 | 1.000 | 0.937 | 0.069 | 0.682 | 6.098 | 13315 | 0.745 | nan |
