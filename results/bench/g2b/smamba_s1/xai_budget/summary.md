# g2b · smamba (scan axis: variate) · seed 1

Forecast on the explained split: MSE 0.0000, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.595 | 0.559 | 0.592 | 0.667 | 0.980 | 0.697 | 0.007 | 0.273 | 0.052 | 128.000 | 0.055 | nan |
| IG-U4 | 0.539 | 0.532 | 0.473 | 0.467 | 0.980 | 0.595 | 0.157 | 0.446 | 0.019 | 128.000 | 0.056 | nan |
| IG-U8 | 0.649 | 0.609 | 0.594 | 0.587 | 0.980 | 0.658 | 0.009 | 0.362 | 0.029 | 128.000 | 0.052 | nan |
| IG-U16 | 0.675 | 0.624 | 0.624 | 0.720 | 1.000 | 0.681 | 0.010 | 0.484 | 0.023 | 128.000 | 0.054 | nan |
| SHAP-U4 | 0.557 | 0.569 | 0.451 | 0.567 | 0.960 | 0.653 | 0.136 | 0.463 | 0.024 | 8195 | 0.412 | nan |
| SHAP-U8 | 0.696 | 0.695 | 0.546 | 0.893 | 0.980 | 0.794 | 0.009 | 0.275 | 0.025 | 8195 | 0.442 | nan |
| SHAP-U16 | 0.653 | 0.643 | 0.484 | 0.893 | 0.940 | 0.783 | 0.010 | 0.312 | 0.022 | 13315 | 0.781 | nan |
