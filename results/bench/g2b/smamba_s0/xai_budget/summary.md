# g2b · smamba (scan axis: variate) · seed 0

Forecast on the explained split: MSE 0.0001, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.562 | 0.504 | 0.633 | 0.413 | 1.000 | 0.925 | 0.013 | 0.422 | 0.033 | 128.000 | 0.034 | nan |
| IG-U4 | 0.515 | 0.494 | 0.530 | 0.400 | 1.000 | 0.826 | 0.176 | 0.666 | 0.030 | 128.000 | 0.027 | nan |
| IG-U8 | 0.595 | 0.537 | 0.631 | 0.440 | 1.000 | 0.865 | 0.016 | 0.623 | 0.017 | 128.000 | 0.031 | nan |
| IG-U16 | 0.603 | 0.524 | 0.653 | 0.413 | 1.000 | 0.899 | 0.022 | 0.665 | 0.020 | 128.000 | 0.028 | nan |
| SHAP-U4 | 0.565 | 0.544 | 0.515 | 0.373 | 1.000 | 0.869 | 0.177 | 0.704 | 0.035 | 8195 | 0.320 | nan |
| SHAP-U8 | 0.635 | 0.586 | 0.566 | 0.547 | 1.000 | 0.914 | 0.016 | 0.605 | 0.018 | 8195 | 0.346 | nan |
| SHAP-U16 | 0.609 | 0.552 | 0.527 | 0.493 | 1.000 | 0.932 | 0.020 | 0.543 | 0.019 | 13315 | 0.645 | nan |
