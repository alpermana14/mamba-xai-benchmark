# g1 · itransformer (scan axis: none (attention)) · seed 0

Forecast on the explained split: MSE 0.1040, trivial 1.0238, skill 0.898, oracle 0.0489
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.803 | 0.767 | 0.465 | 0.333 | 0.156 | 0.330 | 0.512 | 128.000 | 0.009 | nan |
| IG-U4 | 0.248 | 0.185 | 0.133 | 0.280 | 0.196 | 0.332 | 0.270 | 128.000 | 0.007 | nan |
| IG-U8 | 0.303 | 0.280 | 0.183 | 0.314 | 0.172 | 0.336 | 0.259 | 128.000 | 0.007 | nan |
| IG-U16 | 0.435 | 0.446 | 0.258 | 0.344 | 0.165 | 0.352 | 0.311 | 128.000 | 0.007 | nan |
| SHAP-U4 | 0.206 | 0.130 | 0.101 | 0.260 | 0.240 | 0.303 | 0.306 | 8195 | 0.123 | nan |
| SHAP-U8 | 0.275 | 0.241 | 0.139 | 0.294 | 0.233 | 0.333 | 0.305 | 8195 | 0.139 | nan |
| SHAP-U16 | 0.358 | 0.380 | 0.188 | 0.312 | 0.214 | 0.365 | 0.325 | 8195 | 0.152 | nan |
