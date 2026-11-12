# g1 · smamba (scan axis: variate) · seed 2

Forecast on the explained split: MSE 0.0532, trivial 1.0334, skill 0.948, oracle 0.0475
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.908 | 0.864 | 0.609 | 0.240 | 0.122 | 0.286 | 0.214 | 128.000 | 0.030 | nan |
| IG-U4 | 0.342 | 0.323 | 0.239 | 0.220 | 0.133 | 0.362 | 0.215 | 128.000 | 0.027 | nan |
| IG-U8 | 0.419 | 0.376 | 0.321 | 0.228 | 0.143 | 0.339 | 0.235 | 128.000 | 0.027 | nan |
| IG-U16 | 0.573 | 0.514 | 0.465 | 0.233 | 0.133 | 0.355 | 0.242 | 128.000 | 0.029 | nan |
| SHAP-U4 | 0.341 | 0.322 | 0.241 | 0.226 | 0.132 | 0.373 | 0.212 | 8195 | 0.233 | nan |
| SHAP-U8 | 0.416 | 0.365 | 0.317 | 0.228 | 0.140 | 0.368 | 0.240 | 8195 | 0.240 | nan |
| SHAP-U16 | 0.574 | 0.524 | 0.455 | 0.233 | 0.130 | 0.370 | 0.228 | 8195 | 0.267 | nan |
