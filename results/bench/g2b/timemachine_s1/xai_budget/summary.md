# g2b · timemachine (scan axis: channel) · seed 1

Forecast on the explained split: MSE 0.0008, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.891 | 0.820 | 0.668 | 1.000 | 1.000 | 0.836 | 0.109 | 0.441 | 2.687 | 128.000 | 0.043 | nan |
| IG-U4 | 0.663 | 0.694 | 0.568 | 0.853 | 1.000 | 0.697 | 0.195 | 0.494 | 1.166 | 128.000 | 0.043 | nan |
| IG-U8 | 0.872 | 0.779 | 0.714 | 1.000 | 1.000 | 0.794 | 0.134 | 0.505 | 4.556 | 128.000 | 0.042 | nan |
| IG-U16 | 0.931 | 0.854 | 0.734 | 1.000 | 1.000 | 0.817 | 0.122 | 0.525 | 3.264 | 128.000 | 0.044 | nan |
| SHAP-U4 | 0.650 | 0.684 | 0.611 | 0.840 | 1.000 | 0.698 | 0.194 | 0.465 | 1.115 | 8195 | 0.398 | nan |
| SHAP-U8 | 0.844 | 0.751 | 0.786 | 1.000 | 1.000 | 0.796 | 0.137 | 0.442 | 5.895 | 8195 | 0.429 | nan |
| SHAP-U16 | 0.915 | 0.831 | 0.723 | 1.000 | 1.000 | 0.817 | 0.123 | 0.492 | 3.617 | 13315 | 0.799 | nan |
