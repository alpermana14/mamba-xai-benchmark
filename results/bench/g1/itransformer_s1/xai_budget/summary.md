# g1 · itransformer (scan axis: none (attention)) · seed 1

Forecast on the explained split: MSE 0.1020, trivial 0.9582, skill 0.894, oracle 0.0535
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.840 | 0.808 | 0.427 | 0.410 | 0.178 | 0.368 | 0.842 | 128.000 | 0.007 | nan |
| IG-U4 | 0.213 | 0.166 | 0.117 | 0.335 | 0.277 | 0.353 | 0.335 | 128.000 | 0.005 | nan |
| IG-U8 | 0.266 | 0.218 | 0.162 | 0.353 | 0.255 | 0.357 | 0.326 | 128.000 | 0.006 | nan |
| IG-U16 | 0.398 | 0.413 | 0.231 | 0.405 | 0.252 | 0.376 | 0.375 | 128.000 | 0.005 | nan |
| SHAP-U4 | 0.189 | 0.136 | 0.096 | 0.331 | 0.270 | 0.370 | 0.368 | 8195 | 0.133 | nan |
| SHAP-U8 | 0.261 | 0.232 | 0.131 | 0.351 | 0.276 | 0.368 | 0.338 | 8195 | 0.158 | nan |
| SHAP-U16 | 0.368 | 0.347 | 0.177 | 0.373 | 0.232 | 0.361 | 0.368 | 8195 | 0.198 | nan |
