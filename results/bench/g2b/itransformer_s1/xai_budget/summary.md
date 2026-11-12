# g2b · itransformer (scan axis: none (attention)) · seed 1

Forecast on the explained split: MSE 0.0001, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.837 | 0.761 | 0.563 | 1.000 | 1.000 | 0.528 | 0.006 | 0.016 | 0.006 | 128.000 | 0.006 | nan |
| IG-U4 | 0.648 | 0.684 | 0.492 | 0.933 | 1.000 | 0.421 | 0.017 | 0.223 | 0.007 | 128.000 | 0.005 | nan |
| IG-U8 | 0.864 | 0.782 | 0.609 | 1.000 | 1.000 | 0.424 | 0.008 | 0.197 | 0.005 | 128.000 | 0.005 | nan |
| IG-U16 | 0.935 | 0.867 | 0.620 | 1.000 | 1.000 | 0.532 | 0.005 | 0.160 | 0.006 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.649 | 0.688 | 0.391 | 1.000 | 1.000 | 0.413 | 0.017 | 0.201 | 0.006 | 8195 | 0.146 | nan |
| SHAP-U8 | 0.844 | 0.764 | 0.444 | 1.000 | 1.000 | 0.382 | 0.008 | 0.158 | 0.004 | 8195 | 0.178 | nan |
| SHAP-U16 | 0.889 | 0.824 | 0.430 | 1.000 | 1.000 | 0.439 | 0.006 | 0.058 | 0.005 | 13315 | 0.390 | nan |
