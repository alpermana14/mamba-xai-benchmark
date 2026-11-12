# g1 · plain (scan axis: time) · seed 0

Forecast on the explained split: MSE 0.0986, trivial 1.0238, skill 0.904, oracle 0.0489
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.908 | 0.862 | 0.573 | 0.282 | 0.074 | 0.339 | 1.217 | 128.000 | 0.266 | nan |
| IG-U4 | 0.280 | 0.188 | 0.164 | 0.247 | 0.099 | 0.370 | 0.173 | 128.000 | 0.268 | nan |
| IG-U8 | 0.347 | 0.313 | 0.223 | 0.262 | 0.089 | 0.411 | 0.169 | 128.000 | 0.262 | nan |
| IG-U16 | 0.493 | 0.521 | 0.314 | 0.272 | 0.091 | 0.425 | 0.232 | 128.000 | 0.269 | nan |
| SHAP-U4 | 0.282 | 0.189 | 0.159 | 0.243 | 0.100 | 0.382 | 0.173 | 8195 | 1.768 | nan |
| SHAP-U8 | 0.338 | 0.302 | 0.216 | 0.261 | 0.091 | 0.400 | 0.171 | 8195 | 1.810 | nan |
| SHAP-U16 | 0.479 | 0.519 | 0.304 | 0.272 | 0.084 | 0.430 | 0.226 | 8195 | 1.861 | nan |
