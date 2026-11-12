# g2b · smamba (scan axis: variate) · seed 2

Forecast on the explained split: MSE 0.0000, trivial 1.0000, skill 1.000
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | player_iou | player_top1_hit | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.669 | 0.638 | 0.584 | 0.800 | 0.880 | 0.801 | 0.031 | 0.297 | 0.176 | 128.000 | 0.063 | nan |
| IG-U4 | 0.460 | 0.471 | 0.386 | 0.487 | 0.700 | 0.607 | 0.203 | 0.441 | 0.088 | 128.000 | 0.065 | nan |
| IG-U8 | 0.601 | 0.565 | 0.513 | 0.620 | 0.800 | 0.704 | 0.086 | 0.361 | 0.142 | 128.000 | 0.066 | nan |
| IG-U16 | 0.650 | 0.618 | 0.553 | 0.660 | 0.780 | 0.759 | 0.074 | 0.519 | 0.118 | 128.000 | 0.059 | nan |
| SHAP-U4 | 0.441 | 0.438 | 0.352 | 0.573 | 0.640 | 0.658 | 0.262 | 0.382 | 0.103 | 8195 | 0.472 | nan |
| SHAP-U8 | 0.592 | 0.573 | 0.429 | 0.680 | 0.780 | 0.763 | 0.090 | 0.269 | 0.126 | 8195 | 0.493 | nan |
| SHAP-U16 | 0.636 | 0.612 | 0.392 | 0.680 | 0.800 | 0.804 | 0.141 | 0.419 | 0.113 | 13315 | 0.833 | nan |
