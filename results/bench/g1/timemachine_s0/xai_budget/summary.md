# g1 · timemachine (scan axis: channel) · seed 0

Forecast on the explained split: MSE 0.0566, trivial 1.0238, skill 0.945, oracle 0.0489
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.893 | 0.823 | 0.546 | 0.290 | 0.173 | 0.334 | 472.902 | 128.000 | 0.063 | nan |
| IG-U4 | 0.336 | 0.313 | 0.225 | 0.231 | 0.165 | 0.314 | 1.620 | 128.000 | 0.062 | nan |
| IG-U8 | 0.431 | 0.368 | 0.303 | 0.250 | 0.169 | 0.382 | 3.636 | 128.000 | 0.062 | nan |
| IG-U16 | 0.587 | 0.512 | 0.421 | 0.261 | 0.165 | 0.399 | 15.393 | 128.000 | 0.063 | nan |
| SHAP-U4 | 0.331 | 0.304 | 0.221 | 0.232 | 0.163 | 0.316 | 3.120 | 8195 | 0.462 | nan |
| SHAP-U8 | 0.430 | 0.371 | 0.300 | 0.244 | 0.168 | 0.404 | 6.545 | 8195 | 0.475 | nan |
| SHAP-U16 | 0.595 | 0.508 | 0.414 | 0.254 | 0.160 | 0.392 | 10.686 | 8195 | 0.488 | nan |
