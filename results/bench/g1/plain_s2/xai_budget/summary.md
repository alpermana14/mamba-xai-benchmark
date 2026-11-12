# g1 · plain (scan axis: time) · seed 2

Forecast on the explained split: MSE 0.0958, trivial 1.0334, skill 0.907, oracle 0.0475
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.877 | 0.844 | 0.538 | 0.205 | 0.091 | 0.247 | 1.454 | 128.000 | 0.137 | nan |
| IG-U4 | 0.287 | 0.292 | 0.168 | 0.184 | 0.090 | 0.414 | 0.180 | 128.000 | 0.129 | nan |
| IG-U8 | 0.338 | 0.352 | 0.215 | 0.198 | 0.099 | 0.318 | 0.321 | 128.000 | 0.138 | nan |
| IG-U16 | 0.449 | 0.501 | 0.300 | 0.209 | 0.096 | 0.318 | 0.346 | 128.000 | 0.138 | nan |
| SHAP-U4 | 0.284 | 0.256 | 0.165 | 0.185 | 0.087 | 0.423 | 0.191 | 8195 | 1.004 | nan |
| SHAP-U8 | 0.333 | 0.327 | 0.212 | 0.197 | 0.094 | 0.318 | 0.271 | 8195 | 0.985 | nan |
| SHAP-U16 | 0.444 | 0.498 | 0.296 | 0.212 | 0.102 | 0.326 | 0.332 | 8195 | 1.013 | nan |
