# g2c · itransformer (scan axis: none (attention)) · seed 1

Forecast on the explained split: MSE 0.0007, trivial 1.0000, skill 0.999
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.735 | 0.673 | 0.374 | 1.000 | 1.000 | 0.744 | 0.006 | 0.203 | 0.082 | 128.000 | 0.011 | nan |
| IG-U4 | 0.564 | 0.605 | 0.303 | 1.000 | 1.000 | 0.609 | 0.009 | 0.380 | 0.029 | 128.000 | 0.008 | nan |
| IG-U8 | 0.797 | 0.711 | 0.414 | 1.000 | 1.000 | 0.664 | 0.007 | 0.433 | 0.083 | 128.000 | 0.010 | nan |
| IG-U16 | 0.804 | 0.694 | 0.418 | 1.000 | 1.000 | 0.715 | 0.006 | 0.330 | 0.089 | 128.000 | 0.008 | nan |
| SHAP-U4 | 0.472 | 0.442 | 0.212 | 0.780 | 0.780 | 0.615 | 0.146 | 0.361 | 0.185 | 8195 | 0.168 | nan |
| SHAP-U8 | 0.706 | 0.638 | 0.278 | 0.920 | 0.920 | 0.649 | 0.046 | 0.376 | 0.114 | 8195 | 0.185 | nan |
| SHAP-U16 | 0.716 | 0.670 | 0.285 | 0.960 | 0.960 | 0.644 | 0.016 | 0.205 | 0.074 | 13315 | 0.396 | nan |
