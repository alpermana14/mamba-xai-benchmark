# g1 · smamba (scan axis: variate) · seed 0

Forecast on the explained split: MSE 0.0526, trivial 1.0238, skill 0.949, oracle 0.0489
50 windows; sanity on 0 windows (lower = passes)

| method | ap | prec_at_k | mass_in_gt | del_aopc_mean | ins_aopc_mean | del_aopc_interp | ins_aopc_interp | n_evals | seconds | sanity_spearman |
|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.840 | 0.747 | 0.613 | 0.291 | 0.146 | 0.306 | 0.315 | 128.000 | 0.023 | nan |
| IG-U4 | 0.308 | 0.231 | 0.213 | 0.249 | 0.159 | 0.279 | 0.199 | 128.000 | 0.019 | nan |
| IG-U8 | 0.405 | 0.331 | 0.304 | 0.265 | 0.163 | 0.389 | 0.201 | 128.000 | 0.018 | nan |
| IG-U16 | 0.550 | 0.495 | 0.439 | 0.272 | 0.158 | 0.382 | 0.261 | 128.000 | 0.018 | nan |
| SHAP-U4 | 0.304 | 0.231 | 0.211 | 0.255 | 0.163 | 0.295 | 0.204 | 8195 | 0.215 | nan |
| SHAP-U8 | 0.406 | 0.341 | 0.290 | 0.272 | 0.161 | 0.404 | 0.210 | 8195 | 0.243 | nan |
| SHAP-U16 | 0.560 | 0.495 | 0.404 | 0.278 | 0.160 | 0.399 | 0.268 | 8195 | 0.261 | nan |
