# g2b · itransformer (scan axis: none (attention)) · seed 0

Forecast on the explained split: MSE 0.0001, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.853 | 0.767 | 0.549 | 1.000 | 1.000 | 0.548 | 0.005 | 0.021 | 0.012 | 128.000 | 0.007 | nan |
| IG-U4 | 0.696 | 0.708 | 0.492 | 1.000 | 1.000 | 0.412 | 0.020 | 0.306 | 0.013 | 128.000 | 0.005 | nan |
| IG-U8 | 0.893 | 0.822 | 0.587 | 1.000 | 1.000 | 0.473 | 0.010 | 0.164 | 0.005 | 128.000 | 0.005 | nan |
| IG-U16 | 0.941 | 0.912 | 0.609 | 1.000 | 1.000 | 0.545 | 0.009 | 0.071 | 0.005 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.693 | 0.710 | 0.380 | 1.000 | 1.000 | 0.388 | 0.021 | 0.283 | 0.029 | 8195 | 0.146 | nan |
| SHAP-U8 | 0.885 | 0.816 | 0.413 | 1.000 | 1.000 | 0.437 | 0.010 | 0.169 | 0.005 | 8195 | 0.181 | nan |
| SHAP-U16 | 0.917 | 0.868 | 0.410 | 1.000 | 1.000 | 0.465 | 0.009 | 0.041 | 0.004 | 13315 | 0.402 | nan |
