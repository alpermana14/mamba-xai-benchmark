# g1 · timemachine (scan axis: channel) · seed 1

Forecast on the explained split: MSE 0.0599, trivial 0.9582, skill 0.937, oracle 0.0535
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.893 | 0.836 | 0.443 | 0.325 | 0.218 | 0.394 | 117.287 | 128.000 | 0.056 | nan |
| IG-U4 | 0.240 | 0.196 | 0.168 | 0.250 | 0.213 | 0.430 | 1.836 | 128.000 | 0.057 | nan |
| IG-U8 | 0.331 | 0.279 | 0.236 | 0.264 | 0.219 | 0.375 | 5.458 | 128.000 | 0.058 | nan |
| IG-U16 | 0.462 | 0.426 | 0.334 | 0.284 | 0.219 | 0.402 | 13.802 | 128.000 | 0.057 | nan |
| SHAP-U4 | 0.239 | 0.193 | 0.165 | 0.255 | 0.210 | 0.420 | 1.771 | 8195 | 0.433 | nan |
| SHAP-U8 | 0.331 | 0.279 | 0.232 | 0.261 | 0.216 | 0.371 | 3.365 | 8195 | 0.450 | nan |
| SHAP-U16 | 0.461 | 0.421 | 0.326 | 0.280 | 0.216 | 0.395 | 14.054 | 8195 | 0.467 | nan |
