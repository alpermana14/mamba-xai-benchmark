# g1 · smamba (scan axis: variate) · seed 1

Forecast on the explained split: MSE 0.0567, trivial 0.9582, skill 0.941, oracle 0.0535
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.939 | 0.908 | 0.550 | 0.366 | 0.129 | 0.387 | 0.308 | 128.000 | 0.021 | nan |
| IG-U4 | 0.256 | 0.205 | 0.180 | 0.301 | 0.165 | 0.390 | 0.172 | 128.000 | 0.022 | nan |
| IG-U8 | 0.336 | 0.260 | 0.255 | 0.321 | 0.174 | 0.382 | 0.175 | 128.000 | 0.020 | nan |
| IG-U16 | 0.470 | 0.429 | 0.369 | 0.342 | 0.158 | 0.384 | 0.251 | 128.000 | 0.021 | nan |
| SHAP-U4 | 0.253 | 0.203 | 0.182 | 0.313 | 0.154 | 0.405 | 0.161 | 8195 | 0.225 | nan |
| SHAP-U8 | 0.337 | 0.270 | 0.256 | 0.328 | 0.173 | 0.399 | 0.162 | 8195 | 0.231 | nan |
| SHAP-U16 | 0.473 | 0.435 | 0.363 | 0.342 | 0.154 | 0.392 | 0.250 | 8195 | 0.260 | nan |
