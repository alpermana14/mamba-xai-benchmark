# g2b · timemachine (scan axis: channel) · seed 2

Forecast on the explained split: MSE 0.0007, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.879 | 0.806 | 0.691 | 1.000 | 1.000 | 0.833 | 0.102 | 0.474 | 0.886 | 128.000 | 0.045 | nan |
| IG-U4 | 0.665 | 0.689 | 0.576 | 0.813 | 1.000 | 0.709 | 0.174 | 0.527 | 0.594 | 128.000 | 0.042 | nan |
| IG-U8 | 0.864 | 0.764 | 0.726 | 1.000 | 1.000 | 0.794 | 0.125 | 0.502 | 1.118 | 128.000 | 0.040 | nan |
| IG-U16 | 0.927 | 0.844 | 0.749 | 1.000 | 1.000 | 0.817 | 0.114 | 0.514 | 1.287 | 128.000 | 0.041 | nan |
| SHAP-U4 | 0.659 | 0.688 | 0.605 | 0.787 | 1.000 | 0.712 | 0.174 | 0.515 | 0.622 | 8195 | 0.390 | nan |
| SHAP-U8 | 0.852 | 0.747 | 0.769 | 1.000 | 1.000 | 0.796 | 0.125 | 0.496 | 1.316 | 8195 | 0.435 | nan |
| SHAP-U16 | 0.913 | 0.825 | 0.728 | 1.000 | 1.000 | 0.816 | 0.115 | 0.492 | 1.292 | 13315 | 0.733 | nan |
