# g1 · itransformer (scan axis: none (attention)) · seed 2

Forecast on the explained split: MSE 0.1030, trivial 1.0334, skill 0.900, oracle 0.0475
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.761 | 0.729 | 0.404 | 0.272 | 0.144 | 0.276 | 0.611 | 128.000 | 0.006 | nan |
| IG-U4 | 0.238 | 0.220 | 0.132 | 0.247 | 0.243 | 0.270 | 0.260 | 128.000 | 0.005 | nan |
| IG-U8 | 0.322 | 0.343 | 0.175 | 0.265 | 0.241 | 0.281 | 0.322 | 128.000 | 0.005 | nan |
| IG-U16 | 0.409 | 0.432 | 0.240 | 0.265 | 0.233 | 0.351 | 0.389 | 128.000 | 0.006 | nan |
| SHAP-U4 | 0.244 | 0.225 | 0.109 | 0.239 | 0.260 | 0.251 | 0.296 | 8195 | 0.140 | nan |
| SHAP-U8 | 0.300 | 0.271 | 0.139 | 0.252 | 0.287 | 0.282 | 0.319 | 8195 | 0.182 | nan |
| SHAP-U16 | 0.378 | 0.367 | 0.189 | 0.261 | 0.285 | 0.346 | 0.408 | 8195 | 0.202 | nan |
