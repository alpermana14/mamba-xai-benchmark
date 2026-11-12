# g1 · plain (scan axis: time) · seed 1

Forecast on the explained split: MSE 0.0961, trivial 0.9582, skill 0.900, oracle 0.0535
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.899 | 0.866 | 0.552 | 0.382 | 0.058 | 0.368 | 1.511 | 128.000 | 0.138 | nan |
| IG-U4 | 0.197 | 0.127 | 0.130 | 0.317 | 0.123 | 0.479 | 0.129 | 128.000 | 0.133 | nan |
| IG-U8 | 0.286 | 0.226 | 0.181 | 0.343 | 0.095 | 0.392 | 0.171 | 128.000 | 0.136 | nan |
| IG-U16 | 0.421 | 0.431 | 0.264 | 0.366 | 0.088 | 0.410 | 0.321 | 128.000 | 0.138 | nan |
| SHAP-U4 | 0.208 | 0.135 | 0.124 | 0.312 | 0.121 | 0.417 | 0.134 | 8195 | 0.982 | nan |
| SHAP-U8 | 0.288 | 0.218 | 0.174 | 0.338 | 0.087 | 0.394 | 0.154 | 8195 | 1.011 | nan |
| SHAP-U16 | 0.420 | 0.443 | 0.251 | 0.359 | 0.076 | 0.397 | 0.285 | 8195 | 1.028 | nan |
