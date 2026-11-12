# g1 · timemachine (scan axis: channel) · seed 2

Forecast on the explained split: MSE 0.0571, trivial 1.0334, skill 0.945, oracle 0.0475
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.858 | 0.811 | 0.490 | 0.231 | 0.164 | 0.295 | 28.705 | 128.000 | 0.037 | nan |
| IG-U4 | 0.346 | 0.335 | 0.224 | 0.200 | 0.153 | 0.309 | 0.982 | 128.000 | 0.037 | nan |
| IG-U8 | 0.426 | 0.391 | 0.288 | 0.210 | 0.168 | 0.351 | 2.086 | 128.000 | 0.038 | nan |
| IG-U16 | 0.554 | 0.475 | 0.396 | 0.220 | 0.164 | 0.358 | 5.441 | 128.000 | 0.038 | nan |
| SHAP-U4 | 0.346 | 0.335 | 0.224 | 0.201 | 0.154 | 0.322 | 0.734 | 8195 | 0.344 | nan |
| SHAP-U8 | 0.431 | 0.396 | 0.288 | 0.206 | 0.165 | 0.349 | 2.021 | 8195 | 0.354 | nan |
| SHAP-U16 | 0.567 | 0.492 | 0.394 | 0.217 | 0.160 | 0.354 | 3.097 | 8195 | 0.373 | nan |
