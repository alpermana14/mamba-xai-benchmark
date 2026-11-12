# g2a · timemachine (scan axis: channel) · seed 0

Forecast on the explained split: MSE 0.0009, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.907 | 0.830 | 0.679 | 1.000 | 1.000 | 0.957 | 0.049 | 0.653 | 2.385 | 128.000 | 0.048 | nan |
| IG-U4 | 0.644 | 0.638 | 0.536 | 1.000 | 1.000 | 0.813 | 0.143 | 0.657 | 0.666 | 128.000 | 0.039 | nan |
| IG-U8 | 0.878 | 0.790 | 0.696 | 1.000 | 1.000 | 0.894 | 0.083 | 0.691 | 1.829 | 128.000 | 0.040 | nan |
| IG-U16 | 0.930 | 0.874 | 0.738 | 1.000 | 1.000 | 0.931 | 0.066 | 0.708 | 2.890 | 128.000 | 0.039 | nan |
| SHAP-U4 | 0.638 | 0.645 | 0.561 | 1.000 | 1.000 | 0.814 | 0.144 | 0.641 | 0.911 | 8195 | 0.398 | nan |
| SHAP-U8 | 0.864 | 0.776 | 0.720 | 1.000 | 1.000 | 0.895 | 0.086 | 0.659 | 2.345 | 8195 | 0.417 | nan |
| SHAP-U16 | 0.919 | 0.858 | 0.665 | 1.000 | 1.000 | 0.936 | 0.068 | 0.684 | 2.790 | 13315 | 0.755 | nan |
