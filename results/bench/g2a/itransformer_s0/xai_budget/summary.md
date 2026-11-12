# g2a · itransformer (scan axis: none (attention)) · seed 0

Forecast on the explained split: MSE 0.0003, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.835 | 0.780 | 0.387 | 1.000 | 1.000 | 0.817 | 0.008 | 0.078 | 0.102 | 128.000 | 0.007 | nan |
| IG-U4 | 0.638 | 0.655 | 0.346 | 1.000 | 1.000 | 0.653 | 0.011 | 0.536 | 0.068 | 128.000 | 0.006 | nan |
| IG-U8 | 0.886 | 0.808 | 0.426 | 1.000 | 1.000 | 0.782 | 0.009 | 0.455 | 0.073 | 128.000 | 0.006 | nan |
| IG-U16 | 0.911 | 0.892 | 0.434 | 1.000 | 1.000 | 0.834 | 0.008 | 0.258 | 0.077 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.636 | 0.652 | 0.229 | 1.000 | 1.000 | 0.670 | 0.010 | 0.524 | 0.057 | 8195 | 0.158 | nan |
| SHAP-U8 | 0.880 | 0.805 | 0.271 | 1.000 | 1.000 | 0.798 | 0.008 | 0.448 | 0.060 | 8195 | 0.184 | nan |
| SHAP-U16 | 0.901 | 0.884 | 0.296 | 1.000 | 1.000 | 0.818 | 0.008 | 0.223 | 0.069 | 13315 | 0.390 | nan |
