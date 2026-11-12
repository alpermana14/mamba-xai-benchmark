# g2b · timemachine (scan axis: channel) · seed 0

Forecast on the explained split: MSE 0.0006, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.850 | 0.780 | 0.697 | 1.000 | 1.000 | 0.818 | 0.082 | 0.472 | 1.301 | 128.000 | 0.069 | nan |
| IG-U4 | 0.682 | 0.687 | 0.589 | 0.747 | 1.000 | 0.712 | 0.137 | 0.561 | 0.606 | 128.000 | 0.069 | nan |
| IG-U8 | 0.857 | 0.767 | 0.718 | 1.000 | 1.000 | 0.787 | 0.099 | 0.509 | 1.577 | 128.000 | 0.071 | nan |
| IG-U16 | 0.909 | 0.843 | 0.750 | 1.000 | 1.000 | 0.804 | 0.093 | 0.522 | 1.688 | 128.000 | 0.068 | nan |
| SHAP-U4 | 0.677 | 0.683 | 0.611 | 0.720 | 1.000 | 0.714 | 0.139 | 0.550 | 0.628 | 8195 | 0.548 | nan |
| SHAP-U8 | 0.843 | 0.747 | 0.752 | 1.000 | 1.000 | 0.787 | 0.100 | 0.483 | 1.822 | 8195 | 0.579 | nan |
| SHAP-U16 | 0.897 | 0.830 | 0.727 | 1.000 | 1.000 | 0.805 | 0.093 | 0.499 | 1.691 | 13315 | 0.985 | nan |
