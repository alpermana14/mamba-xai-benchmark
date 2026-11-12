# g2c · itransformer (scan axis: none (attention)) · seed 0

Forecast on the explained split: MSE 0.0044, trivial 1.0000, skill 0.996
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.724 | 0.664 | 0.362 | 1.000 | 1.000 | 0.760 | 0.003 | 0.114 | 0.043 | 128.000 | 0.010 | nan |
| IG-U4 | 0.592 | 0.650 | 0.307 | 0.920 | 0.920 | 0.660 | 0.004 | 0.436 | 0.016 | 128.000 | 0.009 | nan |
| IG-U8 | 0.802 | 0.687 | 0.394 | 1.000 | 1.000 | 0.700 | 0.003 | 0.425 | 0.055 | 128.000 | 0.009 | nan |
| IG-U16 | 0.826 | 0.731 | 0.392 | 1.000 | 1.000 | 0.881 | 0.003 | 0.235 | 0.042 | 128.000 | 0.008 | nan |
| SHAP-U4 | 0.507 | 0.508 | 0.188 | 0.760 | 0.760 | 0.614 | 0.098 | 0.394 | 0.109 | 8195 | 0.170 | nan |
| SHAP-U8 | 0.679 | 0.610 | 0.242 | 0.880 | 0.880 | 0.663 | 0.043 | 0.397 | 0.089 | 8195 | 0.191 | nan |
| SHAP-U16 | 0.722 | 0.675 | 0.253 | 0.920 | 0.920 | 0.768 | 0.024 | 0.200 | 0.061 | 13315 | 0.399 | nan |
