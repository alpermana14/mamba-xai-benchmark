# g2c · timemachine (scan axis: channel) · seed 1

Forecast on the explained split: MSE 0.0024, trivial 1.0000, skill 0.998
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.852 | 0.799 | 0.643 | 1.000 | 1.000 | 0.990 | 0.104 | 0.768 | 23.985 | 128.000 | 0.046 | nan |
| IG-U4 | 0.570 | 0.568 | 0.471 | 1.000 | 1.000 | 0.843 | 0.207 | 0.685 | 6.673 | 128.000 | 0.040 | nan |
| IG-U8 | 0.838 | 0.767 | 0.661 | 1.000 | 1.000 | 0.921 | 0.121 | 0.745 | 16.808 | 128.000 | 0.041 | nan |
| IG-U16 | 0.889 | 0.826 | 0.699 | 1.000 | 1.000 | 0.960 | 0.113 | 0.806 | 21.635 | 128.000 | 0.040 | nan |
| SHAP-U4 | 0.577 | 0.573 | 0.476 | 1.000 | 1.000 | 0.851 | 0.207 | 0.690 | 8.761 | 8195 | 0.392 | nan |
| SHAP-U8 | 0.838 | 0.767 | 0.639 | 1.000 | 1.000 | 0.926 | 0.126 | 0.731 | 18.261 | 8195 | 0.430 | nan |
| SHAP-U16 | 0.889 | 0.821 | 0.611 | 1.000 | 1.000 | 0.979 | 0.121 | 0.780 | 24.968 | 13315 | 0.756 | nan |
