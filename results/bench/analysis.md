# Benchmark v2 — analysis

## Forecast quality (mean over seeds)

| task | model | seeds | MSE | trivial | skill | oracle | gate passed | s/epoch |
|---|---|---|---|---|---|---|---|---|
| etth1 | itransformer | 3 | 0.0587 ± 0.0006 | 1.918 | 0.969 | – | 3/3 | 0.9 |
| etth1 | plain | 3 | 0.0617 ± 0.0052 | 1.918 | 0.968 | – | 3/3 | 9.3 |
| etth1 | smamba | 3 | 0.0576 ± 0.0002 | 1.918 | 0.970 | – | 3/3 | 2.3 |
| etth1 | timemachine | 3 | 0.0568 ± 0.0012 | 1.918 | 0.970 | – | 3/3 | 3.6 |
| etth1_h192 | itransformer | 3 | 0.0745 ± 0.0008 | 1.938 | 0.962 | – | 3/3 | 0.8 |
| etth1_h192 | plain | 3 | 0.0807 ± 0.0033 | 1.938 | 0.958 | – | 3/3 | 16.3 |
| etth1_h192 | smamba | 3 | 0.0740 ± 0.0008 | 1.938 | 0.962 | – | 3/3 | 1.4 |
| etth1_h192 | timemachine | 3 | 0.0720 ± 0.0005 | 1.938 | 0.963 | – | 3/3 | 1.7 |
| etth1_h336 | itransformer | 3 | 0.0847 ± 0.0012 | 1.969 | 0.957 | – | 3/3 | 0.4 |
| etth1_h336 | plain | 3 | 0.0914 ± 0.0027 | 1.969 | 0.954 | – | 3/3 | 9.7 |
| etth1_h336 | smamba | 3 | 0.0854 ± 0.0005 | 1.969 | 0.957 | – | 3/3 | 1.5 |
| etth1_h336 | timemachine | 3 | 0.0842 ± 0.0009 | 1.969 | 0.957 | – | 3/3 | 1.3 |
| etth1_h720 | itransformer | 3 | 0.0889 ± 0.0014 | 2.025 | 0.956 | – | 3/3 | 0.4 |
| etth1_h720 | plain | 3 | 0.1263 ± 0.0096 | 2.025 | 0.938 | – | 3/3 | 8.6 |
| etth1_h720 | smamba | 3 | 0.0884 ± 0.0024 | 2.025 | 0.956 | – | 3/3 | 1.4 |
| etth1_h720 | timemachine | 3 | 0.0891 ± 0.0024 | 2.025 | 0.956 | – | 3/3 | 1.6 |
| etth2 | itransformer | 3 | 0.1415 ± 0.0043 | 1.551 | 0.909 | – | 3/3 | 0.2 |
| etth2 | plain | 3 | 0.1526 ± 0.0042 | 1.551 | 0.902 | – | 3/3 | 8.4 |
| etth2 | smamba | 3 | 0.1394 ± 0.0013 | 1.551 | 0.910 | – | 3/3 | 1.4 |
| etth2 | timemachine | 3 | 0.1386 ± 0.0032 | 1.551 | 0.911 | – | 3/3 | 1.9 |
| ettm1 | itransformer | 3 | 0.0289 ± 0.0001 | 1.910 | 0.985 | – | 3/3 | 0.9 |
| ettm1 | plain | 3 | 0.0292 ± 0.0004 | 1.910 | 0.985 | – | 3/3 | 33.5 |
| ettm1 | smamba | 3 | 0.0293 ± 0.0002 | 1.910 | 0.985 | – | 3/3 | 5.5 |
| ettm1 | timemachine | 3 | 0.0290 ± 0.0001 | 1.910 | 0.985 | – | 3/3 | 7.0 |
| exchange | itransformer | 3 | 0.1124 ± 0.0129 | 3.372 | 0.967 | – | 3/3 | 0.2 |
| exchange | plain | 3 | 0.1399 ± 0.0246 | 3.372 | 0.959 | – | 3/3 | 4.1 |
| exchange | smamba | 3 | 0.1118 ± 0.0028 | 3.372 | 0.967 | – | 3/3 | 1.2 |
| exchange | timemachine | 3 | 0.1067 ± 0.0075 | 3.372 | 0.968 | – | 3/3 | 1.3 |
| g1 | itransformer | 3 | 0.1030 ± 0.0010 | 1.005 | 0.897 | 0.0500 | 3/3 | 2.2 |
| g1 | plain | 3 | 0.0968 ± 0.0016 | 1.005 | 0.904 | 0.0500 | 3/3 | 63.5 |
| g1 | smamba | 3 | 0.0542 ± 0.0022 | 1.005 | 0.946 | 0.0500 | 3/3 | 9.4 |
| g1 | timemachine | 3 | 0.0579 ± 0.0018 | 1.005 | 0.942 | 0.0500 | 3/3 | 6.8 |
| g2a | itransformer | 3 | 0.0002 ± 0.0001 | 1.000 | 1.000 | – | 3/3 | 0.2 |
| g2a | plain | 3 | 0.0001 ± 0.0000 | 1.000 | 1.000 | – | 3/3 | 6.8 |
| g2a | smamba | 3 | 0.0017 ± 0.0026 | 1.000 | 0.998 | – | 3/3 | 1.7 |
| g2a | timemachine | 3 | 0.0010 ± 0.0000 | 1.000 | 0.999 | – | 3/3 | 2.5 |
| g2b | itransformer | 3 | 0.0002 ± 0.0001 | 1.000 | 1.000 | – | 3/3 | 0.1 |
| g2b | plain | 3 | 0.0001 ± 0.0000 | 1.000 | 1.000 | – | 3/3 | 8.9 |
| g2b | smamba | 3 | 0.0001 ± 0.0001 | 1.000 | 1.000 | – | 3/3 | 2.2 |
| g2b | timemachine | 3 | 0.0007 ± 0.0001 | 1.000 | 0.999 | – | 3/3 | 3.2 |
| g2c | itransformer | 3 | 0.0018 ± 0.0022 | 1.000 | 0.998 | – | 3/3 | 0.2 |
| g2c | plain | 3 | 0.0001 ± 0.0001 | 1.000 | 1.000 | – | 3/3 | 7.2 |
| g2c | smamba | 3 | 0.0052 ± 0.0061 | 1.000 | 0.995 | – | 3/3 | 2.0 |
| g2c | timemachine | 3 | 0.0021 ± 0.0005 | 1.000 | 0.998 | – | 3/3 | 3.4 |
| g3 | itransformer | 3 | 0.0404 ± 0.0009 | 0.958 | 0.958 | 0.0010 | 3/3 | 1.5 |
| g3 | plain | 3 | 0.0300 ± 0.0009 | 0.958 | 0.969 | 0.0010 | 3/3 | 91.0 |
| g3 | smamba | 3 | 0.0405 ± 0.0009 | 0.958 | 0.958 | 0.0010 | 3/3 | 5.3 |
| g3 | timemachine | 3 | 0.0365 ± 0.0003 | 0.958 | 0.962 | 0.0010 | 3/3 | 4.5 |
| weather | itransformer | 3 | 0.4489 ± 0.0108 | 1.238 | 0.637 | – | 3/3 | 1.4 |
| weather | plain | 3 | 0.4662 ± 0.0574 | 1.238 | 0.623 | – | 3/3 | 49.6 |
| weather | smamba | 3 | 0.4304 ± 0.0175 | 1.238 | 0.652 | – | 3/3 | 17.7 |
| weather | timemachine | 3 | 0.4466 ± 0.0284 | 1.238 | 0.639 | – | 3/3 | 31.3 |
| weather_h192 | itransformer | 3 | 0.5756 ± 0.0054 | 1.248 | 0.539 | – | 3/3 | 2.3 |
| weather_h192 | plain | 3 | 0.5505 ± 0.0107 | 1.248 | 0.559 | – | 3/3 | 42.8 |
| weather_h192 | smamba | 3 | 0.5579 ± 0.0039 | 1.248 | 0.553 | – | 3/3 | 15.4 |
| weather_h192 | timemachine | 3 | 0.5594 ± 0.0002 | 1.248 | 0.552 | – | 3/3 | 25.0 |
| weather_h336 | itransformer | 3 | 0.6350 ± 0.0060 | 1.263 | 0.497 | – | 3/3 | 1.5 |
| weather_h336 | plain | 3 | 0.6051 ± 0.0101 | 1.263 | 0.521 | – | 3/3 | 36.0 |
| weather_h336 | smamba | 3 | 0.6257 ± 0.0211 | 1.263 | 0.504 | – | 3/3 | 19.8 |
| weather_h336 | timemachine | 3 | 0.6257 ± 0.0101 | 1.263 | 0.504 | – | 3/3 | 25.8 |
| weather_h720 | itransformer | 3 | 0.9557 ± 0.0162 | 1.304 | 0.267 | – | 3/3 | 1.6 |
| weather_h720 | plain | 3 | 0.8279 ± 0.0130 | 1.304 | 0.365 | – | 3/3 | 30.0 |
| weather_h720 | smamba | 3 | 0.9234 ± 0.0441 | 1.304 | 0.292 | – | 3/3 | 23.1 |
| weather_h720 | timemachine | 3 | 0.8554 ± 0.0173 | 1.304 | 0.344 | – | 3/3 | 22.3 |

## etth1 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.123 | 0.540 | 0.270 | 0.040 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.783 | 0.533 | 0.390 | 0.024 | 129 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.132 | 0.526 | 0.213 | 0.030 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.130 | 0.479 | 0.201 | 0.028 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.134 | 0.433 | 0.236 | 0.041 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.149 | 0.335 | 0.209 | 0.033 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.134 | 0.276 | 0.217 | 0.035 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.160 | 0.172 | 0.193 | 0.023 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.159 | 0.172 | 0.192 | 0.023 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.134 | 0.115 | 0.212 | 0.031 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.729 | 0.049 | 0.558 | 0.058 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.180 | 0.004 | 1.077 | 0.066 | 0.000 |

## etth1 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.846 | 0.523 | 0.471 | 0.049 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.044 | 0.483 | 0.261 | 0.064 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.048 | 0.410 | 0.250 | 0.064 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.151 | 0.407 | 0.198 | 0.057 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.147 | 0.274 | 0.211 | 0.058 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.169 | 0.176 | 0.259 | 0.063 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 1.169 | 0.172 | 0.268 | 0.060 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.142 | 0.170 | 0.262 | 0.061 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.161 | 0.089 | 0.190 | 0.056 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.187 | 0.085 | 0.275 | 0.064 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.144 | 0.084 | 0.196 | 0.058 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.144 | 0.084 | 0.197 | 0.058 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.649 | 0.048 | 0.646 | 0.090 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.231 | 0.005 | 1.054 | 0.072 | 0.000 |

## etth1 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.126 | 0.550 | 0.285 | 0.035 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.114 | 0.538 | 0.213 | 0.023 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.812 | 0.534 | 0.393 | 0.018 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.086 | 0.475 | 0.197 | 0.019 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.144 | 0.471 | 0.239 | 0.036 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.139 | 0.372 | 0.203 | 0.026 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.177 | 0.359 | 0.178 | 0.014 | 1.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.132 | 0.356 | 0.211 | 0.030 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.148 | 0.333 | 0.180 | 0.014 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.148 | 0.326 | 0.181 | 0.014 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.134 | 0.137 | 0.203 | 0.024 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.745 | 0.046 | 0.575 | 0.056 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.173 | 0.004 | 1.097 | 0.064 | 0.000 |

## etth1 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.054 | 0.549 | 0.281 | 0.033 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.055 | 0.545 | 0.315 | 0.031 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.845 | 0.531 | 0.451 | 0.015 | 129 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.055 | 0.516 | 0.235 | 0.024 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.091 | 0.513 | 0.218 | 0.027 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.060 | 0.483 | 0.213 | 0.017 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.088 | 0.473 | 0.214 | 0.023 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.115 | 0.409 | 0.191 | 0.020 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.150 | 0.366 | 0.142 | 0.012 | 1.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.094 | 0.331 | 0.181 | 0.013 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.096 | 0.319 | 0.180 | 0.013 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.670 | 0.047 | 0.642 | 0.054 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.159 | 0.003 | 1.141 | 0.064 | 0.000 |

## etth1_h192 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.056 | 0.554 | 0.358 | 0.043 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.086 | 0.545 | 0.246 | 0.035 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.762 | 0.535 | 0.395 | 0.022 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.083 | 0.503 | 0.231 | 0.028 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.085 | 0.470 | 0.292 | 0.043 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.119 | 0.344 | 0.246 | 0.037 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.098 | 0.338 | 0.248 | 0.037 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.112 | 0.219 | 0.223 | 0.025 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.111 | 0.212 | 0.222 | 0.025 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.081 | 0.172 | 0.234 | 0.034 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.668 | 0.043 | 0.628 | 0.061 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.176 | 0.004 | 1.058 | 0.064 | 0.000 |

## etth1_h192 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.014 | 0.529 | 0.588 | 0.108 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.869 | 0.520 | 0.808 | 0.090 | 129 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.104 | 0.385 | 0.508 | 0.098 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.116 | 0.267 | 0.517 | 0.094 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.019 | 0.205 | 0.595 | 0.103 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 1.086 | 0.133 | 0.520 | 0.086 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.090 | 0.130 | 0.517 | 0.086 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.056 | 0.128 | 0.575 | 0.075 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.144 | 0.105 | 0.487 | 0.088 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.111 | 0.087 | 0.530 | 0.089 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.111 | 0.086 | 0.530 | 0.089 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.073 | 0.072 | 0.560 | 0.078 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.582 | 0.038 | 0.952 | 0.092 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.281 | 0.004 | 1.247 | 0.064 | 0.000 |

## etth1_h192 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.048 | 0.556 | 0.263 | 0.028 | 32.000 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.064 | 0.552 | 0.394 | 0.039 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.085 | 0.549 | 0.312 | 0.039 | 2051 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.790 | 0.534 | 0.380 | 0.015 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.032 | 0.527 | 0.235 | 0.020 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.107 | 0.418 | 0.247 | 0.032 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.076 | 0.411 | 0.221 | 0.013 | 1.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.100 | 0.409 | 0.217 | 0.012 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.076 | 0.402 | 0.222 | 0.013 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.110 | 0.338 | 0.254 | 0.030 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.096 | 0.297 | 0.231 | 0.027 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.668 | 0.042 | 0.648 | 0.062 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.183 | 0.003 | 1.059 | 0.064 | 0.000 |

## etth1_h192 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.028 | 0.560 | 0.356 | 0.037 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.024 | 0.550 | 0.398 | 0.034 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.064 | 0.543 | 0.295 | 0.029 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.045 | 0.536 | 0.285 | 0.030 | 2051 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.845 | 0.533 | 0.461 | 0.015 | 129 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.000 | 0.521 | 0.307 | 0.026 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.005 | 0.500 | 0.265 | 0.017 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.085 | 0.386 | 0.216 | 0.012 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.025 | 0.347 | 0.255 | 0.012 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.069 | 0.343 | 0.251 | 0.020 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.024 | 0.340 | 0.256 | 0.012 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.613 | 0.041 | 0.752 | 0.062 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.177 | 0.003 | 1.150 | 0.062 | 0.000 |

## etth1_h336 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.036 | 0.556 | 0.394 | 0.054 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.036 | 0.535 | 0.269 | 0.040 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.742 | 0.534 | 0.374 | 0.029 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.044 | 0.502 | 0.239 | 0.035 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.074 | 0.496 | 0.306 | 0.053 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.101 | 0.343 | 0.266 | 0.046 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.093 | 0.341 | 0.253 | 0.042 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.068 | 0.228 | 0.231 | 0.033 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.067 | 0.228 | 0.231 | 0.032 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.058 | 0.117 | 0.249 | 0.041 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.639 | 0.041 | 0.635 | 0.074 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.155 | 0.004 | 1.040 | 0.067 | 0.000 |

## etth1_h336 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.832 | 0.532 | 1.472 | 0.329 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.943 | 0.506 | 1.463 | 0.335 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.022 | 0.349 | 1.410 | 0.264 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.030 | 0.241 | 1.407 | 0.243 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.775 | 0.137 | 1.293 | 0.198 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.122 | 0.105 | 1.310 | 0.233 | 1.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.816 | 0.085 | 1.154 | 0.149 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.993 | 0.069 | 1.395 | 0.210 | 1.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.823 | 0.067 | 1.211 | 0.175 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.815 | 0.067 | 1.210 | 0.167 | 2051 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.993 | 0.066 | 1.396 | 0.208 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.664 | 0.051 | 1.190 | 0.143 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.466 | 0.042 | 1.280 | 0.187 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.243 | 0.008 | 1.618 | 0.098 | 0.000 |

## etth1_h336 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.103 | 0.558 | 0.324 | 0.042 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.064 | 0.554 | 0.418 | 0.041 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.985 | 0.542 | 0.283 | 0.026 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.975 | 0.541 | 0.249 | 0.019 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.750 | 0.532 | 0.381 | 0.016 | 129 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.001 | 0.436 | 0.233 | 0.016 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.998 | 0.431 | 0.233 | 0.016 | 1.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.093 | 0.431 | 0.266 | 0.034 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.045 | 0.422 | 0.232 | 0.014 | 1.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.071 | 0.362 | 0.265 | 0.030 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.044 | 0.226 | 0.268 | 0.027 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.642 | 0.038 | 0.675 | 0.069 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.181 | 0.003 | 1.039 | 0.063 | 0.000 |

## etth1_h336 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.039 | 0.565 | 0.397 | 0.043 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.040 | 0.546 | 0.339 | 0.030 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.015 | 0.542 | 0.437 | 0.041 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.836 | 0.533 | 0.460 | 0.016 | 129 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.974 | 0.520 | 0.352 | 0.028 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.055 | 0.519 | 0.345 | 0.036 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.947 | 0.496 | 0.290 | 0.019 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.052 | 0.432 | 0.295 | 0.027 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.030 | 0.386 | 0.237 | 0.015 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.973 | 0.345 | 0.279 | 0.014 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.971 | 0.344 | 0.280 | 0.014 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.605 | 0.041 | 0.800 | 0.070 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.193 | 0.004 | 1.145 | 0.058 | 0.000 |

## etth1_h720 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.977 | 0.548 | 0.321 | 0.045 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.980 | 0.526 | 0.257 | 0.039 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.724 | 0.521 | 0.362 | 0.025 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.999 | 0.509 | 0.239 | 0.035 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.003 | 0.478 | 0.291 | 0.046 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.044 | 0.463 | 0.244 | 0.038 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.032 | 0.404 | 0.255 | 0.044 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.019 | 0.270 | 0.230 | 0.031 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.020 | 0.260 | 0.230 | 0.031 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.037 | 0.173 | 0.247 | 0.037 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.603 | 0.039 | 0.619 | 0.070 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.127 | 0.003 | 0.954 | 0.062 | 0.000 |

## etth1_h720 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.839 | 0.483 | 1.096 | 0.262 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.978 | 0.416 | 1.160 | 0.274 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.029 | 0.299 | 1.160 | 0.248 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.051 | 0.188 | 1.122 | 0.229 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.963 | 0.163 | 1.139 | 0.203 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.902 | 0.122 | 1.120 | 0.177 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.966 | 0.103 | 1.130 | 0.190 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.984 | 0.100 | 1.134 | 0.185 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.152 | 0.079 | 1.112 | 0.215 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.827 | 0.075 | 1.151 | 0.187 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.020 | 0.070 | 1.145 | 0.224 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.020 | 0.068 | 1.147 | 0.220 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.516 | 0.056 | 1.210 | 0.274 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.348 | 0.015 | 1.669 | 0.138 | 0.000 |

## etth1_h720 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.085 | 0.547 | 0.298 | 0.046 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.964 | 0.544 | 0.265 | 0.032 | 32.000 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.025 | 0.542 | 0.382 | 0.045 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.715 | 0.525 | 0.360 | 0.022 | 129 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.922 | 0.524 | 0.235 | 0.028 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.935 | 0.425 | 0.223 | 0.021 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.997 | 0.423 | 0.222 | 0.020 | 1.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.073 | 0.421 | 0.246 | 0.038 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.933 | 0.420 | 0.222 | 0.021 | 1.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.086 | 0.417 | 0.255 | 0.045 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.045 | 0.182 | 0.274 | 0.038 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.647 | 0.046 | 0.627 | 0.075 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.210 | 0.005 | 0.928 | 0.071 | 0.000 |

## etth1_h720 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.983 | 0.553 | 0.418 | 0.046 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.968 | 0.547 | 0.333 | 0.036 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.946 | 0.542 | 0.459 | 0.053 | 32.000 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.804 | 0.520 | 0.456 | 0.020 | 129 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.989 | 0.516 | 0.331 | 0.039 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.862 | 0.516 | 0.315 | 0.038 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.830 | 0.481 | 0.274 | 0.023 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.934 | 0.412 | 0.283 | 0.028 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.871 | 0.387 | 0.219 | 0.016 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.855 | 0.360 | 0.258 | 0.016 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.855 | 0.341 | 0.261 | 0.016 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.549 | 0.037 | 0.772 | 0.076 | 1497 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.206 | 0.004 | 1.102 | 0.067 | 0.000 |

## etth2 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.024 | 0.444 | 0.298 | 0.127 | 2051 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.726 | 0.444 | 0.458 | 0.085 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.032 | 0.326 | 0.339 | 0.152 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.028 | 0.326 | 0.252 | 0.122 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.011 | 0.291 | 0.264 | 0.144 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.039 | 0.264 | 0.241 | 0.125 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.034 | 0.222 | 0.210 | 0.117 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.002 | 0.221 | 0.250 | 0.147 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.788 | 0.130 | 0.426 | 0.148 | 1499 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.054 | 0.117 | 0.248 | 0.132 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.055 | 0.117 | 0.242 | 0.129 | 32.000 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.181 | 0.008 | 0.993 | 0.197 | 0.000 |

## etth2 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.686 | 0.424 | 0.408 | 0.142 | 129 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.821 | 0.197 | 0.455 | 0.183 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.822 | 0.195 | 0.456 | 0.180 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.865 | 0.186 | 0.480 | 0.192 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.819 | 0.178 | 0.474 | 0.174 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.743 | 0.155 | 0.574 | 0.328 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.731 | 0.153 | 0.591 | 0.285 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.817 | 0.152 | 0.476 | 0.174 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.722 | 0.126 | 0.607 | 0.258 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.720 | 0.124 | 0.595 | 0.232 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.691 | 0.116 | 0.636 | 0.245 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.687 | 0.116 | 0.636 | 0.248 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.580 | 0.109 | 0.562 | 0.217 | 1499 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.255 | 0.017 | 0.954 | 0.187 | 0.000 |

## etth2 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.723 | 0.440 | 0.355 | 0.072 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.994 | 0.431 | 0.283 | 0.122 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.038 | 0.420 | 0.207 | 0.096 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.012 | 0.411 | 0.194 | 0.091 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.946 | 0.374 | 0.234 | 0.115 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.005 | 0.334 | 0.182 | 0.099 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.969 | 0.287 | 0.205 | 0.121 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.030 | 0.250 | 0.175 | 0.094 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.078 | 0.220 | 0.170 | 0.104 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.024 | 0.181 | 0.192 | 0.109 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.021 | 0.180 | 0.193 | 0.111 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.790 | 0.126 | 0.451 | 0.144 | 1499 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.204 | 0.008 | 0.944 | 0.170 | 0.000 |

## etth2 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.949 | 0.469 | 0.205 | 0.061 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.973 | 0.465 | 0.181 | 0.059 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.945 | 0.455 | 0.235 | 0.066 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.950 | 0.440 | 0.212 | 0.065 | 2051 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.705 | 0.437 | 0.390 | 0.039 | 129 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.956 | 0.427 | 0.195 | 0.069 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.937 | 0.422 | 0.202 | 0.057 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.993 | 0.352 | 0.143 | 0.047 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.968 | 0.348 | 0.192 | 0.059 | 2051 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.946 | 0.307 | 0.188 | 0.047 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.941 | 0.300 | 0.192 | 0.047 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.767 | 0.127 | 0.477 | 0.128 | 1499 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.149 | 0.005 | 0.944 | 0.146 | 0.000 |

## ettm1 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.953 | 0.536 | 0.810 | 0.044 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.194 | 0.533 | 0.241 | 0.042 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.244 | 0.483 | 0.248 | 0.042 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.203 | 0.365 | 0.197 | 0.041 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.290 | 0.349 | 0.258 | 0.040 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.213 | 0.165 | 0.288 | 0.037 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.348 | 0.138 | 0.216 | 0.039 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.347 | 0.129 | 0.223 | 0.039 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.238 | 0.109 | 0.285 | 0.040 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.222 | 0.059 | 0.359 | 0.036 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.842 | 0.037 | 0.469 | 0.040 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.274 | 0.003 | 1.320 | 0.044 | 0.000 |

## ettm1 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.882 | 0.537 | 0.841 | 0.104 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.110 | 0.444 | 0.444 | 0.103 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.133 | 0.358 | 0.458 | 0.100 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.098 | 0.350 | 0.433 | 0.096 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.120 | 0.234 | 0.547 | 0.094 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.080 | 0.111 | 0.534 | 0.065 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 1.100 | 0.095 | 0.497 | 0.081 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.096 | 0.093 | 0.496 | 0.083 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.142 | 0.081 | 0.486 | 0.089 | 1.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.117 | 0.070 | 0.561 | 0.085 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.116 | 0.066 | 0.566 | 0.085 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.036 | 0.058 | 0.608 | 0.066 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.719 | 0.036 | 0.770 | 0.068 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.275 | 0.003 | 1.293 | 0.047 | 0.000 |

## ettm1 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.939 | 0.538 | 0.611 | 0.048 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.180 | 0.519 | 0.217 | 0.043 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.203 | 0.474 | 0.196 | 0.042 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.233 | 0.422 | 0.210 | 0.040 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.339 | 0.325 | 0.196 | 0.040 | 1.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.183 | 0.323 | 0.223 | 0.041 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.325 | 0.234 | 0.173 | 0.040 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.321 | 0.225 | 0.176 | 0.040 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.190 | 0.174 | 0.217 | 0.035 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.182 | 0.168 | 0.177 | 0.041 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.236 | 0.056 | 0.195 | 0.033 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.841 | 0.040 | 0.440 | 0.036 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.296 | 0.003 | 1.160 | 0.045 | 0.000 |

## ettm1 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.897 | 0.534 | 0.494 | 0.019 | 129 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.197 | 0.481 | 0.224 | 0.024 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.212 | 0.469 | 0.200 | 0.023 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.210 | 0.401 | 0.209 | 0.026 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.244 | 0.389 | 0.187 | 0.022 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.229 | 0.272 | 0.217 | 0.028 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.330 | 0.265 | 0.082 | 0.020 | 1.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.253 | 0.254 | 0.187 | 0.025 | 2051 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.278 | 0.213 | 0.138 | 0.021 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.276 | 0.194 | 0.141 | 0.021 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.288 | 0.150 | 0.174 | 0.023 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.908 | 0.046 | 0.478 | 0.036 | 1498 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.213 | 0.003 | 1.192 | 0.047 | 0.000 |

## exchange · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.718 | 0.735 | 0.304 | 0.068 | 2051 |
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 1.171 | 0.707 | 0.291 | 0.052 | 257 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.813 | 0.514 | 0.403 | 0.097 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.817 | 0.407 | 0.429 | 0.079 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.742 | 0.366 | 0.461 | 0.065 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.790 | 0.334 | 0.495 | 0.067 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.888 | 0.318 | 0.505 | 0.058 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.827 | 0.204 | 0.516 | 0.062 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.899 | 0.194 | 0.589 | 0.052 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.901 | 0.187 | 0.586 | 0.049 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 1.352 | 0.074 | 0.594 | 0.083 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.466 | 0.005 | 0.945 | 0.096 | 0.000 |

## exchange · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 1.301 | 0.711 | 1.024 | 0.223 | 257 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.616 | 0.387 | 1.017 | 0.219 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.863 | 0.213 | 1.133 | 0.220 | 2051 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 1.814 | 0.185 | 1.139 | 0.229 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.782 | 0.173 | 1.112 | 0.227 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 2.022 | 0.155 | 1.127 | 0.214 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.554 | 0.153 | 1.266 | 0.478 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.412 | 0.148 | 1.150 | 0.388 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.642 | 0.114 | 1.117 | 0.211 | 1.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.343 | 0.113 | 1.132 | 0.355 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.268 | 0.104 | 1.114 | 0.269 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.268 | 0.102 | 1.126 | 0.284 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 1.392 | 0.078 | 1.068 | 0.215 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.393 | 0.010 | 1.416 | 0.142 | 0.000 |

## exchange · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 1.231 | 0.710 | 0.348 | 0.014 | 257 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.789 | 0.709 | 0.325 | 0.036 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.811 | 0.634 | 0.363 | 0.026 | 32.000 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.716 | 0.634 | 0.295 | 0.035 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.847 | 0.571 | 0.383 | 0.026 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.663 | 0.500 | 0.383 | 0.027 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.618 | 0.472 | 0.371 | 0.035 | 2051 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.883 | 0.398 | 0.383 | 0.018 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.884 | 0.392 | 0.385 | 0.017 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.855 | 0.384 | 0.351 | 0.016 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.633 | 0.163 | 0.502 | 0.029 | 2051 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 1.232 | 0.071 | 0.607 | 0.072 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.388 | 0.005 | 1.142 | 0.096 | 0.000 |

## exchange · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 1.222 | 0.706 | 0.391 | 0.032 | 257 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 1.585 | 0.556 | 0.481 | 0.108 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 1.570 | 0.549 | 0.198 | 0.037 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 1.512 | 0.500 | 0.281 | 0.042 | 2051 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 1.751 | 0.454 | 0.271 | 0.043 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 1.564 | 0.415 | 0.241 | 0.042 | 2051 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 1.736 | 0.385 | 0.213 | 0.044 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 1.640 | 0.308 | 0.170 | 0.038 | 2051 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 1.823 | 0.289 | 0.174 | 0.025 | 1.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 1.768 | 0.196 | 0.168 | 0.027 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 1.772 | 0.191 | 0.165 | 0.026 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 1.427 | 0.077 | 0.494 | 0.074 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.276 | 0.006 | 1.292 | 0.095 | 0.000 |

## g1 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GxI | 0.837 | 0.803 | 0.538 | nan | nan | nan | nan | 0.343 | 0.335 | 0.140 | 0.621 | 1.000 |
| IG | 0.801 | 0.768 | 0.432 | nan | nan | nan | nan | 0.338 | 0.326 | 0.159 | 0.653 | 32.000 |
| IG-U16 | 0.414 | 0.430 | 0.243 | nan | nan | nan | nan | 0.338 | 0.360 | 0.217 | 0.358 | 32.000 |
| SHAP-U16 | 0.362 | 0.367 | 0.158 | nan | nan | nan | nan | 0.318 | 0.354 | 0.244 | 0.386 | 2051 |
| SHAP-MMD8 | 0.326 | 0.346 | 0.168 | nan | nan | nan | nan | 0.324 | 0.345 | 0.235 | 0.360 | 2051 |
| IG-U8 | 0.296 | 0.280 | 0.173 | nan | nan | nan | nan | 0.311 | 0.325 | 0.223 | 0.302 | 32.000 |
| SHAP-U8 | 0.275 | 0.238 | 0.129 | nan | nan | nan | nan | 0.300 | 0.325 | 0.277 | 0.329 | 2051 |
| IG-U4 | 0.233 | 0.190 | 0.127 | nan | nan | nan | nan | 0.287 | 0.318 | 0.239 | 0.289 | 32.000 |
| SHAP-U4 | 0.209 | 0.161 | 0.100 | nan | nan | nan | nan | 0.276 | 0.307 | 0.256 | 0.320 | 2051 |
| GS-SHAP | 0.183 | 0.143 | 0.101 | nan | nan | nan | nan | 0.209 | 0.230 | 0.291 | 0.389 | 1498 |
| SHAP-C | 0.087 | 0.000 | 0.044 | nan | nan | nan | nan | 0.184 | 0.199 | 0.253 | 0.278 | 65.000 |
| Random | 0.043 | 0.029 | 0.035 | nan | nan | nan | nan | 0.070 | 0.072 | 0.303 | 0.427 | 0.000 |

## g1 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.895 | 0.857 | 0.555 | nan | nan | nan | nan | 0.290 | 0.318 | 0.074 | 1.394 | 32.000 |
| MambaLRP | 0.887 | 0.846 | 0.551 | nan | nan | nan | nan | 0.283 | 0.317 | 0.078 | 1.454 | 1.000 |
| GxI | 0.881 | 0.841 | 0.525 | nan | nan | nan | nan | 0.296 | 0.327 | 0.078 | 1.309 | 1.000 |
| IG-U16 | 0.454 | 0.484 | 0.293 | nan | nan | nan | nan | 0.282 | 0.384 | 0.092 | 0.299 | 32.000 |
| SHAP-U16 | 0.445 | 0.486 | 0.277 | nan | nan | nan | nan | 0.283 | 0.395 | 0.088 | 0.278 | 2051 |
| SHAP-MMD8 | 0.405 | 0.458 | 0.268 | nan | nan | nan | nan | 0.292 | 0.475 | 0.101 | 0.681 | 2051 |
| SHAP-Δ8 | 0.330 | 0.278 | 0.207 | nan | nan | nan | nan | 0.267 | 0.372 | 0.090 | 0.208 | 2051 |
| IG-U8 | 0.323 | 0.296 | 0.206 | nan | nan | nan | nan | 0.268 | 0.374 | 0.095 | 0.220 | 32.000 |
| SHAP-U8 | 0.317 | 0.276 | 0.199 | nan | nan | nan | nan | 0.266 | 0.371 | 0.092 | 0.192 | 2051 |
| SHAP-U4 | 0.257 | 0.193 | 0.149 | nan | nan | nan | nan | 0.247 | 0.407 | 0.103 | 0.163 | 2051 |
| IG-U4 | 0.254 | 0.202 | 0.154 | nan | nan | nan | nan | 0.250 | 0.421 | 0.104 | 0.161 | 32.000 |
| GS-SHAP | 0.200 | 0.162 | 0.121 | nan | nan | nan | nan | 0.192 | 0.377 | 0.180 | 0.366 | 1498 |
| SHAP-C | 0.106 | 0.000 | 0.063 | nan | nan | nan | nan | 0.168 | 0.187 | 0.180 | 0.250 | 65.000 |
| Random | 0.043 | 0.029 | 0.035 | nan | nan | nan | nan | 0.057 | 0.064 | 0.260 | 0.454 | 0.000 |

## g1 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GxI | 0.921 | 0.885 | 0.707 | nan | nan | nan | nan | 0.310 | 0.326 | 0.171 | 0.297 | 1.000 |
| MambaLRP | 0.906 | 0.863 | 0.716 | nan | nan | nan | nan | 0.321 | 0.329 | 0.165 | 0.292 | 1.000 |
| IG | 0.896 | 0.840 | 0.591 | nan | nan | nan | nan | 0.299 | 0.326 | 0.132 | 0.279 | 32.000 |
| IG-U16 | 0.530 | 0.479 | 0.424 | nan | nan | nan | nan | 0.282 | 0.374 | 0.150 | 0.251 | 32.000 |
| SHAP-U16 | 0.530 | 0.481 | 0.370 | nan | nan | nan | nan | 0.286 | 0.372 | 0.156 | 0.246 | 2051 |
| SHAP-MMD8 | 0.446 | 0.451 | 0.334 | nan | nan | nan | nan | 0.299 | 0.358 | 0.148 | 0.276 | 2051 |
| IG-U8 | 0.386 | 0.322 | 0.293 | nan | nan | nan | nan | 0.272 | 0.370 | 0.160 | 0.204 | 32.000 |
| SHAP-U8 | 0.385 | 0.325 | 0.275 | nan | nan | nan | nan | 0.278 | 0.383 | 0.159 | 0.209 | 2051 |
| IG-U4 | 0.302 | 0.253 | 0.211 | nan | nan | nan | nan | 0.257 | 0.344 | 0.152 | 0.196 | 32.000 |
| SHAP-U4 | 0.297 | 0.252 | 0.207 | nan | nan | nan | nan | 0.266 | 0.355 | 0.150 | 0.192 | 2051 |
| GS-SHAP | 0.225 | 0.171 | 0.154 | nan | nan | nan | nan | 0.208 | 0.251 | 0.240 | 0.251 | 1498 |
| SHAP-C | 0.123 | 0.000 | 0.089 | nan | nan | nan | nan | 0.201 | 0.200 | 0.214 | 0.227 | 65.000 |
| Random | 0.043 | 0.029 | 0.035 | nan | nan | nan | nan | 0.060 | 0.058 | 0.273 | 0.326 | 0.000 |

## g1 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG | 0.881 | 0.823 | 0.492 | nan | nan | nan | nan | 0.282 | 0.341 | 0.185 | 207 | 32.000 |
| GxI | 0.860 | 0.818 | 0.579 | nan | nan | nan | nan | 0.301 | 0.321 | 0.130 | 235 | 1.000 |
| MambaLRP | 0.850 | 0.817 | 0.538 | nan | nan | nan | nan | 0.281 | 0.327 | 0.218 | 140 | 1.000 |
| SHAP-U16 | 0.538 | 0.475 | 0.362 | nan | nan | nan | nan | 0.251 | 0.387 | 0.185 | 10.190 | 2051 |
| IG-U16 | 0.534 | 0.471 | 0.383 | nan | nan | nan | nan | 0.255 | 0.386 | 0.182 | 11.546 | 32.000 |
| SHAP-MMD8 | 0.430 | 0.402 | 0.305 | nan | nan | nan | nan | 0.276 | 0.403 | 0.178 | 35.049 | 2051 |
| SHAP-U8 | 0.397 | 0.348 | 0.268 | nan | nan | nan | nan | 0.236 | 0.367 | 0.182 | 2.938 | 2051 |
| IG-U8 | 0.396 | 0.345 | 0.275 | nan | nan | nan | nan | 0.241 | 0.369 | 0.186 | 3.727 | 32.000 |
| IG-U4 | 0.307 | 0.281 | 0.205 | nan | nan | nan | nan | 0.227 | 0.351 | 0.177 | 1.479 | 32.000 |
| SHAP-U4 | 0.305 | 0.277 | 0.201 | nan | nan | nan | nan | 0.229 | 0.354 | 0.177 | 2.392 | 2051 |
| GS-SHAP | 0.222 | 0.167 | 0.152 | nan | nan | nan | nan | 0.199 | 0.381 | 0.224 | 3.511 | 1498 |
| SHAP-C | 0.128 | 0.000 | 0.084 | nan | nan | nan | nan | 0.201 | 0.183 | 0.191 | 0.196 | 65.000 |
| Random | 0.043 | 0.029 | 0.035 | nan | nan | nan | nan | 0.093 | 0.060 | 0.239 | 0.791 | 0.000 |

## g2a · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U16 | 0.902 | 0.873 | 0.435 | 1.000 | nan | nan | nan | 0.803 | 0.255 | 0.005 | 0.057 | 32.000 |
| IG-U8 | 0.856 | 0.785 | 0.431 | 1.000 | nan | nan | nan | 0.735 | 0.414 | 0.006 | 0.075 | 32.000 |
| IG | 0.830 | 0.760 | 0.388 | 1.000 | nan | nan | nan | 0.808 | 0.125 | 0.006 | 0.085 | 32.000 |
| GS-SHAP | 0.828 | 0.769 | 0.271 | 0.873 | nan | nan | nan | 0.816 | 0.499 | 0.095 | 0.135 | 1494 |
| SHAP-MMD8 | 0.813 | 0.751 | 0.278 | 1.000 | nan | nan | nan | 0.715 | 0.370 | 0.006 | 0.055 | 2051 |
| SHAP-U16 | 0.795 | 0.755 | 0.230 | 1.000 | nan | nan | nan | 0.744 | 0.206 | 0.006 | 0.038 | 3331 |
| SHAP-U8 | 0.782 | 0.725 | 0.243 | 0.980 | nan | nan | nan | 0.738 | 0.391 | 0.021 | 0.063 | 2051 |
| GxI | 0.662 | 0.609 | 0.310 | 1.000 | nan | nan | nan | 0.479 | 0.038 | 0.005 | 0.066 | 1.000 |
| IG-U4 | 0.612 | 0.645 | 0.342 | 1.000 | nan | nan | nan | 0.637 | 0.442 | 0.007 | 0.055 | 32.000 |
| SHAP-U4 | 0.572 | 0.591 | 0.218 | 0.913 | nan | nan | nan | 0.633 | 0.413 | 0.036 | 0.075 | 2051 |
| SHAP-C | 0.190 | 0.178 | 0.115 | 0.153 | nan | nan | nan | 0.325 | 0.236 | 0.126 | 0.096 | 8193 |
| Random | 0.056 | 0.053 | 0.050 | 0.080 | nan | nan | nan | 0.003 | 0.001 | 0.382 | 0.120 | 0.000 |

## g2a · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.938 | 0.927 | 0.952 | 0.973 | nan | nan | nan | 0.883 | 0.737 | 0.138 | 1.261 | 1494 |
| SHAP-MMD8 | 0.922 | 0.872 | 0.733 | 1.000 | nan | nan | nan | 0.977 | 0.734 | 0.053 | 1.302 | 2051 |
| IG-U16 | 0.917 | 0.867 | 0.823 | 1.000 | nan | nan | nan | 0.959 | 0.753 | 0.060 | 1.282 | 32.000 |
| SHAP-U16 | 0.897 | 0.864 | 0.623 | 1.000 | nan | nan | nan | 0.968 | 0.671 | 0.061 | 1.393 | 3331 |
| IG | 0.874 | 0.802 | 0.733 | 1.000 | nan | nan | nan | 0.998 | 0.564 | 0.033 | 1.283 | 32.000 |
| SHAP-Δ8 | 0.869 | 0.810 | 0.668 | 1.000 | nan | nan | nan | 0.936 | 0.693 | 0.080 | 1.038 | 2051 |
| IG-U8 | 0.865 | 0.800 | 0.778 | 1.000 | nan | nan | nan | 0.933 | 0.746 | 0.082 | 0.946 | 32.000 |
| SHAP-U8 | 0.864 | 0.808 | 0.666 | 1.000 | nan | nan | nan | 0.935 | 0.710 | 0.080 | 1.030 | 2051 |
| MambaLRP | 0.856 | 0.778 | 0.691 | 1.000 | nan | nan | nan | 1.001 | 0.493 | 0.036 | 1.291 | 1.000 |
| GxI | 0.825 | 0.754 | 0.481 | 1.000 | nan | nan | nan | 0.880 | 0.288 | 0.155 | 0.992 | 1.000 |
| SHAP-U4 | 0.627 | 0.642 | 0.540 | 1.000 | nan | nan | nan | 0.849 | 0.704 | 0.156 | 0.298 | 2051 |
| IG-U4 | 0.626 | 0.636 | 0.566 | 1.000 | nan | nan | nan | 0.842 | 0.712 | 0.163 | 0.293 | 32.000 |
| SHAP-C | 0.200 | 0.193 | 0.190 | 0.153 | nan | nan | nan | 0.566 | 0.455 | 0.442 | 0.264 | 8193 |
| Random | 0.056 | 0.053 | 0.050 | 0.080 | nan | nan | nan | 0.109 | 0.003 | 0.923 | 0.341 | 0.000 |

## g2a · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.759 | 0.707 | 0.645 | 0.740 | nan | nan | nan | 0.864 | 0.712 | 0.106 | 0.224 | 1494 |
| IG-U16 | 0.680 | 0.625 | 0.530 | 0.773 | nan | nan | nan | 0.919 | 0.617 | 0.006 | 0.139 | 32.000 |
| SHAP-MMD8 | 0.663 | 0.599 | 0.387 | 0.780 | nan | nan | nan | 0.979 | 0.499 | 0.006 | 0.148 | 2051 |
| IG | 0.657 | 0.589 | 0.500 | 0.760 | nan | nan | nan | 0.972 | 0.621 | 0.004 | 0.204 | 32.000 |
| IG-U8 | 0.655 | 0.583 | 0.509 | 0.767 | nan | nan | nan | 0.865 | 0.571 | 0.009 | 0.109 | 32.000 |
| SHAP-U16 | 0.629 | 0.583 | 0.270 | 0.740 | nan | nan | nan | 0.972 | 0.471 | 0.007 | 0.123 | 3331 |
| SHAP-U8 | 0.623 | 0.560 | 0.353 | 0.727 | nan | nan | nan | 0.865 | 0.506 | 0.009 | 0.115 | 2051 |
| MambaLRP | 0.537 | 0.444 | 0.533 | 0.747 | nan | nan | nan | 0.723 | 0.448 | 0.005 | 0.195 | 1.000 |
| IG-U4 | 0.483 | 0.467 | 0.381 | 0.753 | nan | nan | nan | 0.813 | 0.558 | 0.075 | 0.084 | 32.000 |
| SHAP-U4 | 0.460 | 0.455 | 0.326 | 0.713 | nan | nan | nan | 0.810 | 0.503 | 0.076 | 0.083 | 2051 |
| GxI | 0.456 | 0.415 | 0.304 | 0.733 | nan | nan | nan | 0.795 | 0.230 | 0.042 | 0.192 | 1.000 |
| SHAP-C | 0.166 | 0.142 | 0.145 | 0.120 | nan | nan | nan | 0.466 | 0.311 | 0.382 | 0.125 | 8193 |
| Random | 0.056 | 0.053 | 0.050 | 0.080 | nan | nan | nan | 0.012 | 0.001 | 0.977 | 0.150 | 0.000 |

## g2a · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-MMD8 | 0.939 | 0.869 | 0.714 | 1.000 | nan | nan | nan | 0.950 | 0.731 | 0.064 | 6.708 | 2051 |
| IG-U16 | 0.934 | 0.887 | 0.746 | 1.000 | nan | nan | nan | 0.934 | 0.713 | 0.070 | 4.015 | 32.000 |
| GS-SHAP | 0.932 | 0.924 | 0.867 | 0.973 | nan | nan | nan | 0.876 | 0.679 | 0.136 | 1.314 | 1494 |
| IG | 0.921 | 0.850 | 0.687 | 1.000 | nan | nan | nan | 0.955 | 0.673 | 0.053 | 3.201 | 32.000 |
| SHAP-U16 | 0.913 | 0.865 | 0.593 | 1.000 | nan | nan | nan | 0.937 | 0.661 | 0.073 | 3.739 | 3331 |
| IG-U8 | 0.880 | 0.799 | 0.708 | 1.000 | nan | nan | nan | 0.898 | 0.685 | 0.083 | 2.779 | 32.000 |
| SHAP-U8 | 0.857 | 0.770 | 0.714 | 1.000 | nan | nan | nan | 0.900 | 0.641 | 0.086 | 3.298 | 2051 |
| MambaLRP | 0.819 | 0.728 | 0.560 | 1.000 | nan | nan | nan | 0.924 | 0.564 | 0.068 | 2.688 | 1.000 |
| GxI | 0.791 | 0.722 | 0.486 | 0.993 | nan | nan | nan | 0.880 | 0.356 | 0.102 | 2.518 | 1.000 |
| IG-U4 | 0.628 | 0.637 | 0.528 | 1.000 | nan | nan | nan | 0.814 | 0.659 | 0.149 | 1.147 | 32.000 |
| SHAP-U4 | 0.618 | 0.637 | 0.549 | 1.000 | nan | nan | nan | 0.816 | 0.660 | 0.151 | 1.281 | 2051 |
| SHAP-C | 0.200 | 0.193 | 0.188 | 0.153 | nan | nan | nan | 0.519 | 0.391 | 0.425 | 0.258 | 8193 |
| Random | 0.056 | 0.053 | 0.050 | 0.080 | nan | nan | nan | 0.075 | 0.004 | 0.932 | 0.637 | 0.000 |

## g2b · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.951 | 0.929 | 0.458 | 0.991 | nan | nan | nan | 0.574 | 0.234 | 0.028 | 0.013 | 1494 |
| IG-U16 | 0.940 | 0.889 | 0.616 | 1.000 | nan | nan | nan | 0.562 | 0.152 | 0.013 | 0.008 | 32.000 |
| IG-U8 | 0.882 | 0.807 | 0.596 | 1.000 | nan | nan | nan | 0.476 | 0.186 | 0.017 | 0.008 | 32.000 |
| IG | 0.852 | 0.772 | 0.559 | 1.000 | nan | nan | nan | 0.569 | 0.030 | 0.009 | 0.010 | 32.000 |
| SHAP-MMD8 | 0.834 | 0.781 | 0.430 | 1.000 | nan | nan | nan | 0.420 | 0.181 | 0.016 | 0.008 | 2051 |
| SHAP-U8 | 0.824 | 0.761 | 0.369 | 1.000 | nan | nan | nan | 0.400 | 0.134 | 0.018 | 0.007 | 2051 |
| SHAP-U16 | 0.785 | 0.714 | 0.319 | 1.000 | nan | nan | nan | 0.387 | 0.048 | 0.014 | 0.007 | 3331 |
| GxI | 0.733 | 0.657 | 0.480 | 1.000 | nan | nan | nan | 0.241 | 0.006 | 0.015 | 0.009 | 1.000 |
| IG-U4 | 0.674 | 0.698 | 0.491 | 0.978 | nan | nan | nan | 0.435 | 0.271 | 0.035 | 0.017 | 32.000 |
| SHAP-U4 | 0.662 | 0.706 | 0.371 | 0.982 | nan | nan | nan | 0.383 | 0.221 | 0.037 | 0.015 | 2051 |
| SHAP-C | 0.200 | 0.239 | 0.167 | 0.133 | nan | nan | nan | 0.030 | 0.016 | 0.183 | 0.066 | 8193 |
| Random | 0.106 | 0.100 | 0.100 | 0.064 | nan | nan | nan | 0.004 | 0.001 | 0.396 | 0.051 | 0.000 |

## g2b · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.968 | 0.948 | 0.976 | 1.000 | nan | nan | nan | 0.777 | 0.672 | 0.225 | 0.294 | 1494 |
| IG-U16 | 0.910 | 0.849 | 0.855 | 1.000 | nan | nan | nan | 0.877 | 0.529 | 0.130 | 0.239 | 32.000 |
| SHAP-MMD8 | 0.895 | 0.823 | 0.794 | 1.000 | nan | nan | nan | 0.889 | 0.528 | 0.117 | 0.257 | 2051 |
| IG-U8 | 0.876 | 0.803 | 0.823 | 1.000 | nan | nan | nan | 0.841 | 0.522 | 0.156 | 0.214 | 32.000 |
| IG | 0.867 | 0.788 | 0.778 | 1.000 | nan | nan | nan | 0.942 | 0.359 | 0.091 | 0.225 | 32.000 |
| SHAP-U16 | 0.865 | 0.811 | 0.675 | 1.000 | nan | nan | nan | 0.886 | 0.442 | 0.129 | 0.252 | 3331 |
| SHAP-Δ8 | 0.865 | 0.801 | 0.740 | 1.000 | nan | nan | nan | 0.846 | 0.462 | 0.147 | 0.238 | 2051 |
| SHAP-U8 | 0.860 | 0.803 | 0.729 | 1.000 | nan | nan | nan | 0.842 | 0.475 | 0.152 | 0.233 | 2051 |
| MambaLRP | 0.849 | 0.764 | 0.739 | 1.000 | nan | nan | nan | 0.942 | 0.298 | 0.094 | 0.227 | 1.000 |
| GxI | 0.830 | 0.753 | 0.614 | 1.000 | nan | nan | nan | 0.766 | 0.158 | 0.248 | 0.208 | 1.000 |
| SHAP-U4 | 0.674 | 0.705 | 0.612 | 0.938 | nan | nan | nan | 0.744 | 0.557 | 0.225 | 0.265 | 2051 |
| IG-U4 | 0.670 | 0.709 | 0.631 | 0.982 | nan | nan | nan | 0.736 | 0.557 | 0.234 | 0.257 | 32.000 |
| SHAP-C | 0.200 | 0.222 | 0.195 | 0.142 | nan | nan | nan | 0.369 | 0.275 | 0.575 | 0.444 | 8193 |
| Random | 0.106 | 0.100 | 0.100 | 0.064 | nan | nan | nan | 0.099 | 0.003 | 0.918 | 0.230 | 0.000 |

## g2b · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.848 | 0.790 | 0.702 | 0.829 | nan | nan | nan | 0.743 | 0.554 | 0.106 | 0.051 | 1494 |
| SHAP-MMD8 | 0.685 | 0.628 | 0.501 | 0.827 | nan | nan | nan | 0.836 | 0.387 | 0.046 | 0.093 | 2051 |
| IG-U16 | 0.643 | 0.589 | 0.610 | 0.598 | nan | nan | nan | 0.780 | 0.556 | 0.035 | 0.053 | 32.000 |
| IG-U8 | 0.615 | 0.570 | 0.580 | 0.549 | nan | nan | nan | 0.742 | 0.449 | 0.037 | 0.063 | 32.000 |
| IG | 0.609 | 0.567 | 0.603 | 0.627 | nan | nan | nan | 0.808 | 0.331 | 0.017 | 0.087 | 32.000 |
| SHAP-U8 | 0.605 | 0.580 | 0.419 | 0.693 | nan | nan | nan | 0.812 | 0.305 | 0.052 | 0.077 | 2051 |
| GxI | 0.593 | 0.557 | 0.484 | 0.800 | nan | nan | nan | 0.768 | 0.154 | 0.118 | 0.071 | 1.000 |
| MambaLRP | 0.581 | 0.527 | 0.580 | 0.622 | nan | nan | nan | 0.768 | 0.330 | 0.012 | 0.062 | 1.000 |
| SHAP-U16 | 0.572 | 0.539 | 0.354 | 0.698 | nan | nan | nan | 0.801 | 0.272 | 0.057 | 0.054 | 3331 |
| SHAP-U4 | 0.514 | 0.513 | 0.399 | 0.491 | nan | nan | nan | 0.728 | 0.505 | 0.185 | 0.047 | 2051 |
| IG-U4 | 0.505 | 0.499 | 0.463 | 0.451 | nan | nan | nan | 0.676 | 0.518 | 0.179 | 0.046 | 32.000 |
| SHAP-C | 0.171 | 0.169 | 0.159 | 0.098 | nan | nan | nan | 0.347 | 0.258 | 0.519 | 0.432 | 8193 |
| Random | 0.106 | 0.100 | 0.100 | 0.064 | nan | nan | nan | 0.010 | 0.001 | 0.984 | 0.151 | 0.000 |

## g2b · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.960 | 0.946 | 0.885 | 1.000 | nan | nan | nan | 0.754 | 0.569 | 0.166 | 1.235 | 1494 |
| IG-U16 | 0.922 | 0.847 | 0.744 | 1.000 | nan | nan | nan | 0.813 | 0.520 | 0.110 | 2.080 | 32.000 |
| SHAP-MMD8 | 0.896 | 0.812 | 0.759 | 1.000 | nan | nan | nan | 0.830 | 0.523 | 0.099 | 2.847 | 2051 |
| SHAP-U16 | 0.893 | 0.823 | 0.653 | 1.000 | nan | nan | nan | 0.812 | 0.457 | 0.111 | 2.222 | 3331 |
| IG | 0.873 | 0.802 | 0.686 | 1.000 | nan | nan | nan | 0.829 | 0.462 | 0.098 | 1.625 | 32.000 |
| IG-U8 | 0.864 | 0.770 | 0.719 | 1.000 | nan | nan | nan | 0.792 | 0.506 | 0.120 | 2.417 | 32.000 |
| SHAP-U8 | 0.841 | 0.747 | 0.746 | 1.000 | nan | nan | nan | 0.792 | 0.463 | 0.121 | 2.956 | 2051 |
| GxI | 0.705 | 0.651 | 0.537 | 0.973 | nan | nan | nan | 0.694 | 0.194 | 0.181 | 1.562 | 1.000 |
| IG-U4 | 0.670 | 0.690 | 0.578 | 0.804 | nan | nan | nan | 0.706 | 0.527 | 0.168 | 0.789 | 32.000 |
| SHAP-U4 | 0.661 | 0.686 | 0.602 | 0.791 | nan | nan | nan | 0.708 | 0.505 | 0.169 | 0.784 | 2051 |
| MambaLRP | 0.635 | 0.615 | 0.623 | 0.742 | nan | nan | nan | 0.714 | 0.353 | 0.132 | 1.479 | 1.000 |
| SHAP-C | 0.199 | 0.250 | 0.191 | 0.164 | nan | nan | nan | 0.322 | 0.238 | 0.467 | 0.336 | 8193 |
| Random | 0.106 | 0.100 | 0.100 | 0.064 | nan | nan | nan | 0.058 | 0.003 | 0.893 | 0.455 | 0.000 |

## g2c · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| IG-U16 | 0.819 | 0.715 | 0.405 | 1.000 | nan | nan | nan | 0.806 | 0.278 | 0.004 | 0.065 | 32.000 |
| IG-U8 | 0.804 | 0.701 | 0.401 | 1.000 | nan | nan | nan | 0.708 | 0.442 | 0.005 | 0.081 | 32.000 |
| IG | 0.734 | 0.666 | 0.367 | 1.000 | nan | nan | nan | 0.793 | 0.164 | 0.004 | 0.060 | 32.000 |
| GS-SHAP | 0.717 | 0.574 | 0.253 | 0.633 | nan | nan | nan | 0.764 | 0.465 | 0.097 | 0.144 | 1494 |
| SHAP-MMD8 | 0.670 | 0.603 | 0.255 | 0.913 | nan | nan | nan | 0.669 | 0.324 | 0.019 | 0.056 | 2051 |
| SHAP-U8 | 0.642 | 0.576 | 0.216 | 0.887 | nan | nan | nan | 0.638 | 0.362 | 0.033 | 0.096 | 2051 |
| SHAP-U16 | 0.633 | 0.603 | 0.205 | 0.933 | nan | nan | nan | 0.666 | 0.177 | 0.015 | 0.061 | 3331 |
| GxI | 0.626 | 0.586 | 0.292 | 0.993 | nan | nan | nan | 0.436 | 0.045 | 0.005 | 0.074 | 1.000 |
| IG-U4 | 0.586 | 0.633 | 0.307 | 0.973 | nan | nan | nan | 0.653 | 0.417 | 0.006 | 0.025 | 32.000 |
| SHAP-U4 | 0.477 | 0.461 | 0.186 | 0.773 | nan | nan | nan | 0.594 | 0.383 | 0.079 | 0.111 | 2051 |
| SHAP-C | 0.180 | 0.156 | 0.096 | 0.133 | nan | nan | nan | 0.346 | 0.269 | 0.208 | 0.199 | 8193 |
| Random | 0.056 | 0.048 | 0.051 | 0.073 | nan | nan | nan | 0.002 | 0.000 | 0.354 | 0.122 | 0.000 |

## g2c · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.932 | 0.919 | 0.868 | 0.980 | nan | nan | nan | 0.875 | 0.720 | 0.137 | 1.671 | 1494 |
| IG-U16 | 0.847 | 0.751 | 0.737 | 1.000 | nan | nan | nan | 0.945 | 0.680 | 0.062 | 1.523 | 32.000 |
| SHAP-MMD8 | 0.835 | 0.744 | 0.621 | 1.000 | nan | nan | nan | 0.965 | 0.658 | 0.056 | 1.622 | 2051 |
| SHAP-U16 | 0.822 | 0.758 | 0.511 | 1.000 | nan | nan | nan | 0.959 | 0.557 | 0.060 | 1.667 | 3331 |
| SHAP-U8 | 0.816 | 0.750 | 0.554 | 1.000 | nan | nan | nan | 0.925 | 0.643 | 0.082 | 1.164 | 2051 |
| SHAP-Δ8 | 0.813 | 0.743 | 0.553 | 1.000 | nan | nan | nan | 0.927 | 0.626 | 0.081 | 1.248 | 2051 |
| IG-U8 | 0.813 | 0.725 | 0.695 | 1.000 | nan | nan | nan | 0.913 | 0.691 | 0.087 | 1.111 | 32.000 |
| IG | 0.796 | 0.706 | 0.658 | 1.000 | nan | nan | nan | 0.982 | 0.520 | 0.039 | 1.573 | 32.000 |
| MambaLRP | 0.765 | 0.677 | 0.606 | 1.000 | nan | nan | nan | 0.992 | 0.434 | 0.044 | 1.645 | 1.000 |
| GxI | 0.686 | 0.641 | 0.393 | 1.000 | nan | nan | nan | 0.821 | 0.167 | 0.191 | 1.180 | 1.000 |
| SHAP-U4 | 0.591 | 0.608 | 0.454 | 1.000 | nan | nan | nan | 0.833 | 0.652 | 0.155 | 0.369 | 2051 |
| IG-U4 | 0.581 | 0.608 | 0.493 | 1.000 | nan | nan | nan | 0.818 | 0.652 | 0.168 | 0.357 | 32.000 |
| SHAP-C | 0.197 | 0.184 | 0.168 | 0.173 | nan | nan | nan | 0.562 | 0.452 | 0.426 | 0.239 | 8193 |
| Random | 0.056 | 0.048 | 0.051 | 0.073 | nan | nan | nan | 0.102 | 0.004 | 0.918 | 0.353 | 0.000 |

## g2c · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.833 | 0.774 | 0.540 | 0.840 | nan | nan | nan | 0.822 | 0.593 | 0.086 | 0.075 | 1494 |
| MambaLRP | 0.751 | 0.667 | 0.625 | 0.980 | nan | nan | nan | 0.757 | 0.449 | 0.003 | 0.208 | 1.000 |
| IG-U16 | 0.733 | 0.697 | 0.506 | 0.867 | nan | nan | nan | 0.852 | 0.579 | 0.004 | 0.194 | 32.000 |
| IG-U8 | 0.719 | 0.657 | 0.492 | 0.867 | nan | nan | nan | 0.774 | 0.517 | 0.017 | 0.162 | 32.000 |
| SHAP-U8 | 0.706 | 0.648 | 0.337 | 0.873 | nan | nan | nan | 0.727 | 0.404 | 0.019 | 0.110 | 2051 |
| SHAP-U16 | 0.691 | 0.651 | 0.272 | 0.900 | nan | nan | nan | 0.836 | 0.362 | 0.005 | 0.068 | 3331 |
| SHAP-MMD8 | 0.684 | 0.610 | 0.375 | 0.880 | nan | nan | nan | 0.832 | 0.393 | 0.004 | 0.090 | 2051 |
| IG | 0.651 | 0.619 | 0.460 | 0.800 | nan | nan | nan | 0.883 | 0.468 | 0.004 | 0.210 | 32.000 |
| SHAP-U4 | 0.523 | 0.540 | 0.308 | 0.847 | nan | nan | nan | 0.699 | 0.429 | 0.075 | 0.087 | 2051 |
| IG-U4 | 0.517 | 0.513 | 0.368 | 0.860 | nan | nan | nan | 0.716 | 0.498 | 0.072 | 0.108 | 32.000 |
| GxI | 0.473 | 0.464 | 0.308 | 0.800 | nan | nan | nan | 0.642 | 0.147 | 0.065 | 0.136 | 1.000 |
| SHAP-C | 0.181 | 0.144 | 0.142 | 0.153 | nan | nan | nan | 0.407 | 0.261 | 0.297 | 0.085 | 8193 |
| Random | 0.056 | 0.048 | 0.051 | 0.073 | nan | nan | nan | 0.011 | 0.000 | 0.866 | 0.134 | 0.000 |

## g2c · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | 0.933 | 0.923 | 0.847 | 0.980 | nan | nan | nan | 0.989 | 0.798 | 0.213 | 3.835 | 1494 |
| SHAP-MMD8 | 0.921 | 0.856 | 0.586 | 1.000 | nan | nan | nan | 1.022 | 0.809 | 0.135 | 18.738 | 2051 |
| IG-U16 | 0.918 | 0.863 | 0.746 | 1.000 | nan | nan | nan | 0.992 | 0.854 | 0.115 | 10.356 | 32.000 |
| IG | 0.895 | 0.834 | 0.697 | 1.000 | nan | nan | nan | 1.025 | 0.823 | 0.105 | 11.953 | 32.000 |
| SHAP-U16 | 0.889 | 0.839 | 0.455 | 1.000 | nan | nan | nan | 1.006 | 0.802 | 0.145 | 12.706 | 3331 |
| IG-U8 | 0.858 | 0.782 | 0.702 | 1.000 | nan | nan | nan | 0.945 | 0.782 | 0.123 | 8.179 | 32.000 |
| SHAP-U8 | 0.855 | 0.787 | 0.541 | 1.000 | nan | nan | nan | 0.952 | 0.745 | 0.146 | 10.105 | 2051 |
| GxI | 0.804 | 0.732 | 0.595 | 0.980 | nan | nan | nan | 0.972 | 0.595 | 0.138 | 5.940 | 1.000 |
| MambaLRP | 0.713 | 0.641 | 0.559 | 0.980 | nan | nan | nan | 0.937 | 0.599 | 0.124 | 6.544 | 1.000 |
| SHAP-U4 | 0.606 | 0.612 | 0.481 | 1.000 | nan | nan | nan | 0.887 | 0.735 | 0.219 | 4.877 | 2051 |
| IG-U4 | 0.604 | 0.608 | 0.509 | 1.000 | nan | nan | nan | 0.883 | 0.726 | 0.213 | 4.175 | 32.000 |
| SHAP-C | 0.198 | 0.180 | 0.184 | 0.173 | nan | nan | nan | 0.598 | 0.422 | 0.511 | 0.288 | 8193 |
| Random | 0.056 | 0.048 | 0.051 | 0.073 | nan | nan | nan | 0.151 | 0.007 | 1.035 | 2.508 | 0.000 |

## g3 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | nan | nan | nan | nan | 0.553 | 0.322 | 0.047 | 0.368 | 0.363 | 0.315 | 0.515 | 1498 |
| GxI | nan | nan | nan | nan | 0.398 | 0.158 | 0.057 | 0.668 | 0.364 | 0.090 | 0.641 | 1.000 |
| SHAP-U4 | nan | nan | nan | nan | 0.382 | 0.122 | 0.048 | 0.566 | 0.520 | 0.161 | 0.575 | 2051 |
| IG | nan | nan | nan | nan | 0.379 | 0.132 | 0.050 | 0.666 | 0.426 | 0.085 | 0.619 | 32.000 |
| IG-U16 | nan | nan | nan | nan | 0.379 | 0.132 | 0.050 | 0.594 | 0.608 | 0.134 | 0.587 | 32.000 |
| IG-U4 | nan | nan | nan | nan | 0.379 | 0.132 | 0.050 | 0.566 | 0.522 | 0.169 | 0.580 | 32.000 |
| IG-U8 | nan | nan | nan | nan | 0.379 | 0.132 | 0.050 | 0.581 | 0.627 | 0.143 | 0.602 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | 0.378 | 0.136 | 0.049 | 0.587 | 0.620 | 0.128 | 0.584 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | 0.376 | 0.136 | 0.051 | 0.595 | 0.662 | 0.125 | 0.277 | 2051 |
| SHAP-C | nan | nan | nan | nan | 0.367 | 0.163 | 0.067 | 0.449 | 0.323 | 0.284 | 0.165 | 257 |
| SHAP-U16 | nan | nan | nan | nan | 0.356 | 0.135 | 0.057 | 0.597 | 0.614 | 0.118 | 0.573 | 2051 |
| Random | nan | nan | nan | nan | -0.062 | -0.003 | 0.254 | 0.096 | 0.027 | 0.591 | 0.510 | 0.000 |

## g3 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | nan | nan | nan | nan | 0.522 | 0.385 | 0.062 | 0.407 | 0.339 | 0.381 | 0.529 | 1498 |
| GxI | nan | nan | nan | nan | 0.426 | 0.218 | 0.080 | 0.684 | 0.340 | 0.126 | 0.775 | 1.000 |
| IG | nan | nan | nan | nan | 0.386 | 0.176 | 0.080 | 0.690 | 0.353 | 0.140 | 0.762 | 32.000 |
| IG-U16 | nan | nan | nan | nan | 0.386 | 0.176 | 0.080 | 0.631 | 0.634 | 0.195 | 0.659 | 32.000 |
| IG-U4 | nan | nan | nan | nan | 0.386 | 0.176 | 0.080 | 0.604 | 0.551 | 0.233 | 0.633 | 32.000 |
| IG-U8 | nan | nan | nan | nan | 0.386 | 0.176 | 0.080 | 0.621 | 0.635 | 0.208 | 0.671 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | 0.386 | 0.175 | 0.077 | 0.628 | 0.645 | 0.205 | 0.675 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | 0.380 | 0.171 | 0.075 | 0.599 | 0.692 | 0.244 | 0.392 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | 0.369 | 0.170 | 0.074 | 0.605 | 0.555 | 0.229 | 0.642 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | 0.351 | 0.181 | 0.077 | 0.633 | 0.656 | 0.193 | 0.661 | 2051 |
| SHAP-C | nan | nan | nan | nan | 0.347 | 0.216 | 0.098 | 0.467 | 0.348 | 0.334 | 0.258 | 257 |
| SHAP-Δ8 | nan | nan | nan | nan | 0.346 | 0.186 | 0.085 | 0.624 | 0.691 | 0.205 | 0.455 | 2051 |
| MambaLRP | nan | nan | nan | nan | 0.345 | 0.211 | 0.078 | 0.694 | 0.404 | 0.134 | 0.801 | 1.000 |
| Random | nan | nan | nan | nan | -0.062 | -0.003 | 0.254 | 0.136 | 0.043 | 0.617 | 0.557 | 0.000 |

## g3 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | nan | nan | nan | nan | 0.536 | 0.299 | 0.069 | 0.317 | 0.354 | 0.319 | 0.595 | 1498 |
| MambaLRP | nan | nan | nan | nan | 0.480 | 0.144 | 0.024 | 0.650 | 0.414 | 0.110 | 0.479 | 1.000 |
| SHAP-U16 | nan | nan | nan | nan | 0.325 | 0.206 | 0.072 | 0.568 | 0.602 | 0.147 | 0.443 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | 0.313 | 0.186 | 0.065 | 0.553 | 0.518 | 0.190 | 0.455 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | 0.293 | 0.188 | 0.070 | 0.576 | 0.656 | 0.154 | 0.311 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | 0.280 | 0.197 | 0.068 | 0.565 | 0.617 | 0.160 | 0.476 | 2051 |
| GxI | nan | nan | nan | nan | 0.236 | 0.151 | 0.071 | 0.652 | 0.311 | 0.103 | 0.479 | 1.000 |
| IG | nan | nan | nan | nan | 0.198 | 0.195 | 0.070 | 0.649 | 0.359 | 0.097 | 0.482 | 32.000 |
| IG-U16 | nan | nan | nan | nan | 0.198 | 0.195 | 0.070 | 0.579 | 0.592 | 0.151 | 0.468 | 32.000 |
| IG-U4 | nan | nan | nan | nan | 0.198 | 0.195 | 0.070 | 0.551 | 0.522 | 0.193 | 0.474 | 32.000 |
| IG-U8 | nan | nan | nan | nan | 0.198 | 0.195 | 0.070 | 0.564 | 0.593 | 0.170 | 0.467 | 32.000 |
| SHAP-C | nan | nan | nan | nan | 0.194 | 0.201 | 0.126 | 0.439 | 0.330 | 0.273 | 0.198 | 257 |
| Random | nan | nan | nan | nan | -0.062 | -0.003 | 0.254 | 0.090 | 0.030 | 0.549 | 0.548 | 0.000 |

## g3 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GS-SHAP | nan | nan | nan | nan | 0.553 | 0.296 | 0.053 | 0.403 | 0.431 | 0.305 | 0.589 | 1498 |
| MambaLRP | nan | nan | nan | nan | 0.290 | 0.128 | 0.054 | 0.671 | 0.411 | 0.103 | 0.658 | 1.000 |
| SHAP-MMD8 | nan | nan | nan | nan | 0.288 | 0.128 | 0.063 | 0.612 | 0.675 | 0.136 | 0.287 | 2051 |
| SHAP-U16 | nan | nan | nan | nan | 0.278 | 0.133 | 0.062 | 0.626 | 0.661 | 0.118 | 0.708 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | 0.271 | 0.129 | 0.061 | 0.614 | 0.678 | 0.128 | 0.668 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | 0.263 | 0.127 | 0.062 | 0.589 | 0.572 | 0.158 | 0.665 | 2051 |
| IG-U4 | nan | nan | nan | nan | 0.250 | 0.126 | 0.066 | 0.589 | 0.574 | 0.161 | 0.661 | 32.000 |
| IG-U16 | nan | nan | nan | nan | 0.250 | 0.126 | 0.066 | 0.623 | 0.651 | 0.133 | 0.727 | 32.000 |
| IG | nan | nan | nan | nan | 0.250 | 0.126 | 0.066 | 0.676 | 0.410 | 0.088 | 0.715 | 32.000 |
| IG-U8 | nan | nan | nan | nan | 0.250 | 0.126 | 0.066 | 0.608 | 0.668 | 0.141 | 0.675 | 32.000 |
| SHAP-C | nan | nan | nan | nan | 0.237 | 0.145 | 0.089 | 0.464 | 0.349 | 0.275 | 0.178 | 257 |
| GxI | nan | nan | nan | nan | 0.233 | 0.186 | 0.120 | 0.666 | 0.359 | 0.095 | 0.693 | 1.000 |
| Random | nan | nan | nan | nan | -0.062 | -0.003 | 0.254 | 0.103 | 0.040 | 0.599 | 0.566 | 0.000 |

## weather · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.605 | 0.551 | 0.143 | 0.094 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.674 | 0.484 | 0.120 | 0.133 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.712 | 0.332 | 0.178 | 0.143 | 2691 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.714 | 0.312 | 0.182 | 0.121 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.577 | 0.309 | 0.229 | 0.247 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.575 | 0.243 | 0.248 | 0.260 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.748 | 0.223 | 0.252 | 0.136 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.603 | 0.183 | 0.255 | 0.251 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.625 | 0.104 | 0.267 | 0.237 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.462 | 0.103 | 0.289 | 0.302 | 1496 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.582 | 0.098 | 0.289 | 0.247 | 1.000 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.152 | 0.006 | 0.578 | 0.183 | 0.000 |

## weather · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.609 | 0.549 | 0.270 | 0.200 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.670 | 0.305 | 0.307 | 0.293 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.676 | 0.253 | 0.280 | 0.267 | 2691 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.684 | 0.235 | 0.289 | 0.293 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.677 | 0.233 | 0.290 | 0.295 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.439 | 0.201 | 0.460 | 0.387 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.670 | 0.183 | 0.278 | 0.281 | 5379 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.418 | 0.127 | 0.435 | 0.404 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.406 | 0.101 | 0.431 | 0.416 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.406 | 0.093 | 0.404 | 0.407 | 1496 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.431 | 0.083 | 0.419 | 0.412 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.391 | 0.072 | 0.458 | 0.394 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.360 | 0.068 | 0.485 | 0.430 | 1.000 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.164 | 0.011 | 0.613 | 0.206 | 0.000 |

## weather · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.581 | 0.526 | 0.163 | 0.086 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.635 | 0.421 | 0.125 | 0.153 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.460 | 0.315 | 0.303 | 0.278 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.653 | 0.312 | 0.149 | 0.128 | 2691 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.647 | 0.304 | 0.144 | 0.114 | 2691 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.511 | 0.245 | 0.275 | 0.248 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.659 | 0.233 | 0.146 | 0.120 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.523 | 0.213 | 0.249 | 0.221 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.571 | 0.154 | 0.230 | 0.210 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.555 | 0.128 | 0.229 | 0.224 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.520 | 0.121 | 0.259 | 0.244 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.423 | 0.083 | 0.325 | 0.346 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.168 | 0.005 | 0.561 | 0.181 | 0.000 |

## weather · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.597 | 0.543 | 0.146 | 0.074 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.641 | 0.471 | 0.122 | 0.155 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.541 | 0.367 | 0.224 | 0.189 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.612 | 0.316 | 0.152 | 0.137 | 2691 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.615 | 0.315 | 0.155 | 0.131 | 2691 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.532 | 0.299 | 0.223 | 0.209 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.624 | 0.262 | 0.164 | 0.130 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.538 | 0.246 | 0.235 | 0.190 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.623 | 0.158 | 0.190 | 0.143 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.559 | 0.126 | 0.195 | 0.157 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.545 | 0.118 | 0.206 | 0.175 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.420 | 0.098 | 0.375 | 0.383 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.163 | 0.007 | 0.569 | 0.193 | 0.000 |

## weather_h192 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.606 | 0.552 | 0.144 | 0.075 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.671 | 0.494 | 0.102 | 0.098 | 2051 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.582 | 0.312 | 0.204 | 0.197 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.700 | 0.301 | 0.166 | 0.092 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.717 | 0.290 | 0.155 | 0.109 | 2691 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.579 | 0.234 | 0.201 | 0.200 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.746 | 0.213 | 0.228 | 0.106 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.600 | 0.200 | 0.216 | 0.163 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.623 | 0.113 | 0.247 | 0.149 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.576 | 0.105 | 0.268 | 0.172 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.426 | 0.087 | 0.309 | 0.246 | 1495 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.153 | 0.006 | 0.572 | 0.180 | 0.000 |

## weather_h192 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.647 | 0.577 | 0.285 | 0.258 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.704 | 0.461 | 0.312 | 0.311 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.706 | 0.390 | 0.285 | 0.266 | 2691 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.728 | 0.365 | 0.308 | 0.297 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.729 | 0.359 | 0.313 | 0.290 | 2691 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.710 | 0.289 | 0.292 | 0.281 | 5379 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.415 | 0.177 | 0.498 | 0.424 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.379 | 0.130 | 0.478 | 0.433 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.461 | 0.115 | 0.360 | 0.348 | 1495 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.380 | 0.102 | 0.477 | 0.426 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.397 | 0.089 | 0.457 | 0.417 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.359 | 0.078 | 0.486 | 0.410 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.325 | 0.072 | 0.512 | 0.448 | 1.000 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.170 | 0.011 | 0.631 | 0.218 | 0.000 |

## weather_h192 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.600 | 0.548 | 0.158 | 0.065 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.664 | 0.510 | 0.105 | 0.110 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.660 | 0.284 | 0.141 | 0.091 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.445 | 0.282 | 0.331 | 0.282 | 32.000 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.687 | 0.253 | 0.136 | 0.100 | 2691 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.478 | 0.233 | 0.310 | 0.256 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.495 | 0.207 | 0.268 | 0.219 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.715 | 0.189 | 0.154 | 0.084 | 5379 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.528 | 0.127 | 0.273 | 0.191 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.524 | 0.120 | 0.261 | 0.198 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.486 | 0.110 | 0.291 | 0.242 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.410 | 0.076 | 0.359 | 0.254 | 1495 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.159 | 0.006 | 0.584 | 0.174 | 0.000 |

## weather_h192 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.604 | 0.553 | 0.139 | 0.060 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.652 | 0.501 | 0.100 | 0.099 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.626 | 0.389 | 0.120 | 0.086 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.632 | 0.374 | 0.126 | 0.094 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.587 | 0.358 | 0.178 | 0.146 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.640 | 0.306 | 0.157 | 0.081 | 5379 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.575 | 0.291 | 0.150 | 0.130 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.576 | 0.227 | 0.160 | 0.117 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.631 | 0.163 | 0.131 | 0.087 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.602 | 0.131 | 0.129 | 0.094 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.583 | 0.122 | 0.142 | 0.101 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.414 | 0.093 | 0.386 | 0.265 | 1495 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.133 | 0.007 | 0.591 | 0.176 | 0.000 |

## weather_h336 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.639 | 0.580 | 0.136 | 0.092 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.695 | 0.508 | 0.132 | 0.125 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.741 | 0.337 | 0.169 | 0.152 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.607 | 0.330 | 0.205 | 0.219 | 32.000 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.735 | 0.319 | 0.181 | 0.113 | 2691 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.618 | 0.218 | 0.209 | 0.213 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.775 | 0.193 | 0.236 | 0.144 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.634 | 0.181 | 0.218 | 0.190 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.645 | 0.111 | 0.230 | 0.164 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.596 | 0.102 | 0.261 | 0.184 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.440 | 0.077 | 0.295 | 0.250 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.135 | 0.006 | 0.620 | 0.167 | 0.000 |

## weather_h336 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.650 | 0.586 | 0.268 | 0.243 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.692 | 0.533 | 0.287 | 0.274 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.690 | 0.444 | 0.261 | 0.232 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.699 | 0.432 | 0.276 | 0.266 | 2691 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.698 | 0.432 | 0.273 | 0.278 | 2691 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.692 | 0.373 | 0.275 | 0.246 | 5379 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.398 | 0.156 | 0.462 | 0.400 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.383 | 0.118 | 0.445 | 0.386 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.394 | 0.107 | 0.416 | 0.422 | 1.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.370 | 0.088 | 0.438 | 0.386 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.358 | 0.085 | 0.428 | 0.356 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.326 | 0.077 | 0.469 | 0.403 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.346 | 0.071 | 0.335 | 0.345 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.140 | 0.008 | 0.635 | 0.161 | 0.000 |

## weather_h336 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.619 | 0.570 | 0.188 | 0.091 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.681 | 0.490 | 0.148 | 0.157 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.682 | 0.319 | 0.184 | 0.125 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.709 | 0.283 | 0.169 | 0.140 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.432 | 0.275 | 0.388 | 0.315 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.454 | 0.200 | 0.358 | 0.306 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.479 | 0.174 | 0.324 | 0.260 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.741 | 0.168 | 0.203 | 0.132 | 5379 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.520 | 0.149 | 0.304 | 0.233 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.499 | 0.099 | 0.319 | 0.232 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.462 | 0.093 | 0.348 | 0.273 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.434 | 0.069 | 0.325 | 0.305 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.172 | 0.006 | 0.613 | 0.173 | 0.000 |

## weather_h336 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.649 | 0.595 | 0.179 | 0.099 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.697 | 0.515 | 0.139 | 0.168 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.678 | 0.373 | 0.165 | 0.140 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.681 | 0.347 | 0.185 | 0.164 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.579 | 0.347 | 0.290 | 0.233 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.589 | 0.300 | 0.271 | 0.205 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.664 | 0.262 | 0.176 | 0.139 | 5379 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.580 | 0.226 | 0.246 | 0.193 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.660 | 0.143 | 0.176 | 0.145 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.596 | 0.114 | 0.203 | 0.141 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.574 | 0.108 | 0.215 | 0.159 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.458 | 0.084 | 0.398 | 0.290 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.150 | 0.008 | 0.643 | 0.189 | 0.000 |

## weather_h720 · itransformer (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.664 | 0.594 | 0.268 | 0.251 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.691 | 0.567 | 0.304 | 0.287 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.675 | 0.381 | 0.328 | 0.249 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.645 | 0.341 | 0.331 | 0.296 | 2691 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.666 | 0.257 | 0.336 | 0.275 | 5379 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.421 | 0.236 | 0.436 | 0.421 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.385 | 0.154 | 0.444 | 0.420 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.376 | 0.122 | 0.432 | 0.388 | 32.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.375 | 0.087 | 0.347 | 0.338 | 1496 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.393 | 0.071 | 0.415 | 0.377 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.362 | 0.068 | 0.446 | 0.408 | 1.000 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.148 | 0.012 | 0.533 | 0.216 | 0.000 |

## weather_h720 · plain (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.618 | 0.539 | 0.267 | 0.245 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.662 | 0.508 | 0.303 | 0.279 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.664 | 0.428 | 0.265 | 0.262 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.669 | 0.427 | 0.257 | 0.277 | 2691 |
| SHAP-Δ8 | nan | nan | nan | nan | nan | nan | nan | 0.670 | 0.422 | 0.264 | 0.284 | 2691 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.667 | 0.378 | 0.255 | 0.267 | 5379 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.397 | 0.193 | 0.466 | 0.394 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.375 | 0.133 | 0.462 | 0.376 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.360 | 0.109 | 0.456 | 0.369 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.338 | 0.099 | 0.454 | 0.359 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.381 | 0.091 | 0.434 | 0.396 | 1.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.307 | 0.089 | 0.481 | 0.393 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.316 | 0.085 | 0.342 | 0.383 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.154 | 0.011 | 0.586 | 0.207 | 0.000 |

## weather_h720 · smamba (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.673 | 0.612 | 0.328 | 0.241 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.701 | 0.527 | 0.332 | 0.297 | 2051 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.646 | 0.323 | 0.360 | 0.235 | 2691 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.677 | 0.302 | 0.362 | 0.305 | 2691 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.401 | 0.228 | 0.554 | 0.479 | 32.000 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.641 | 0.206 | 0.387 | 0.285 | 5379 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.392 | 0.188 | 0.538 | 0.464 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.453 | 0.164 | 0.496 | 0.402 | 1.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.395 | 0.157 | 0.527 | 0.454 | 32.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.422 | 0.093 | 0.501 | 0.435 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.404 | 0.088 | 0.512 | 0.447 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.448 | 0.082 | 0.422 | 0.366 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.216 | 0.011 | 0.691 | 0.239 | 0.000 |

## weather_h720 · timemachine (3 seeds, 150 windows)

| method | ap | prec_at_k | mass_in_gt | player_iou | feat_spearman | feat_pearson | noise_share | del_aopc_mean | del_aopc_interp | ins_aopc_mean | ins_aopc_interp | n_evals |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SHAP-C | nan | nan | nan | nan | nan | nan | nan | 0.622 | 0.570 | 0.155 | 0.077 | 2051 |
| SHAP-U4 | nan | nan | nan | nan | nan | nan | nan | 0.661 | 0.515 | 0.146 | 0.130 | 2051 |
| SHAP-U8 | nan | nan | nan | nan | nan | nan | nan | 0.649 | 0.407 | 0.165 | 0.137 | 2691 |
| SHAP-MMD8 | nan | nan | nan | nan | nan | nan | nan | 0.643 | 0.402 | 0.178 | 0.126 | 2691 |
| SHAP-U16 | nan | nan | nan | nan | nan | nan | nan | 0.650 | 0.367 | 0.165 | 0.117 | 5379 |
| IG-U4 | nan | nan | nan | nan | nan | nan | nan | 0.541 | 0.358 | 0.257 | 0.185 | 32.000 |
| IG-U8 | nan | nan | nan | nan | nan | nan | nan | 0.549 | 0.288 | 0.223 | 0.168 | 32.000 |
| IG-U16 | nan | nan | nan | nan | nan | nan | nan | 0.546 | 0.238 | 0.218 | 0.166 | 32.000 |
| MambaLRP | nan | nan | nan | nan | nan | nan | nan | 0.609 | 0.158 | 0.174 | 0.136 | 1.000 |
| IG | nan | nan | nan | nan | nan | nan | nan | 0.559 | 0.104 | 0.195 | 0.141 | 32.000 |
| GxI | nan | nan | nan | nan | nan | nan | nan | 0.537 | 0.101 | 0.220 | 0.153 | 1.000 |
| GS-SHAP | nan | nan | nan | nan | nan | nan | nan | 0.350 | 0.062 | 0.384 | 0.288 | 1496 |
| Random | nan | nan | nan | nan | nan | nan | nan | 0.128 | 0.005 | 0.630 | 0.174 | 0.000 |

## Pre-registered comparisons (Holm within cell; verdict needs p_holm < 0.05 and same sign in all seeds)

| task | model | A | B | metric | n | mean(A−B) | p_holm | A better in seeds | verdict |
|---|---|---|---|---|---|---|---|---|---|
| etth1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.227 | 6.1e-25 | 0/3 | B better |
| etth1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.405 | 1.4e-25 | 0/3 | B better |
| etth1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.287 | 2.2e-24 | 0/3 | B better |
| etth1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.421 | 1.4e-25 | 0/3 | B better |
| etth1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.191 | 1.4e-12 | 0/3 | B better |
| etth1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.017 | 3.6e-04 | 3/3 | A better |
| etth1 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.005 | 1.0e+00 | 2/3 | no difference |
| etth1 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.017 | 4.9e-07 | 3/3 | A better |
| etth1 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.004 | 1.0e+00 | 2/3 | no difference |
| etth1 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.017 | 4.5e-07 | 3/3 | A better |
| etth1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.004 | 1.0e+00 | 2/3 | no difference |
| etth1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.000 | 1.0e+00 | 2/3 | no difference |
| etth1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | +0.002 | 9.0e-01 | 2/3 | no difference |
| etth1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.027 | 5.8e-06 | 3/3 | A better |
| etth1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.123 | 1.9e-22 | 0/3 | B better |
| etth1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.493 | 3.2e-25 | 0/3 | B better |
| etth1 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.128 | 1.8e-21 | 0/3 | B better |
| etth1 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.519 | 3.2e-25 | 0/3 | B better |
| etth1 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.231 | 7.0e-17 | 0/3 | B better |
| etth1 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.018 | 2.1e-02 | 3/3 | A better |
| etth1 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.033 | 3.7e-01 | 3/3 | no difference |
| etth1 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.028 | 9.7e-11 | 3/3 | A better |
| etth1 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.026 | 5.0e-01 | 3/3 | no difference |
| etth1 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.029 | 5.5e-11 | 3/3 | A better |
| etth1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.310 | 5.2e-25 | 0/3 | B better |
| etth1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.388 | 2.3e-25 | 0/3 | B better |
| etth1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.326 | 1.3e-24 | 0/3 | B better |
| etth1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.394 | 2.3e-25 | 0/3 | B better |
| etth1 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.166 | 1.1e-10 | 0/3 | B better |
| etth1 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.024 | 2.2e-02 | 3/3 | A better |
| etth1 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.046 | 5.5e-04 | 3/3 | A better |
| etth1 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.055 | 2.3e-25 | 3/3 | A better |
| etth1 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.034 | 5.5e-03 | 3/3 | A better |
| etth1 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.056 | 2.3e-25 | 3/3 | A better |
| etth1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.467 | 2.3e-25 | 0/3 | B better |
| etth1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.422 | 2.3e-25 | 0/3 | B better |
| etth1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.426 | 2.3e-25 | 0/3 | B better |
| etth1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.418 | 2.3e-25 | 0/3 | B better |
| etth1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.043 | 1.7e-01 | 1/3 | no difference |
| etth1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.033 | 8.5e-11 | 3/3 | A better |
| etth1_h192 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.295 | 1.5e-24 | 0/3 | B better |
| etth1_h192 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.430 | 1.4e-25 | 0/3 | B better |
| etth1_h192 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.301 | 1.5e-24 | 0/3 | B better |
| etth1_h192 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.451 | 1.4e-25 | 0/3 | B better |
| etth1_h192 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.201 | 8.0e-13 | 0/3 | B better |
| etth1_h192 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.033 | 2.4e-08 | 3/3 | A better |
| etth1_h192 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.018 | 3.2e-01 | 3/3 | no difference |
| etth1_h192 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.033 | 2.8e-23 | 3/3 | A better |
| etth1_h192 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.019 | 1.5e-01 | 3/3 | no difference |
| etth1_h192 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.034 | 3.0e-23 | 3/3 | A better |
| etth1_h192 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.004 | 7.7e-01 | 2/3 | no difference |
| etth1_h192 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.004 | 3.2e-01 | 1/3 | no difference |
| etth1_h192 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | +0.006 | 9.8e-01 | 2/3 | no difference |
| etth1_h192 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.030 | 5.7e-06 | 3/3 | A better |
| etth1_h192 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.090 | 3.8e-19 | 0/3 | B better |
| etth1_h192 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.474 | 3.2e-25 | 0/3 | B better |
| etth1_h192 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.092 | 4.0e-19 | 0/3 | B better |
| etth1_h192 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.508 | 3.2e-25 | 0/3 | B better |
| etth1_h192 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.255 | 5.9e-19 | 0/3 | B better |
| etth1_h192 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.014 | 3.6e-01 | 1/3 | no difference |
| etth1_h192 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.007 | 9.6e-01 | 3/3 | no difference |
| etth1_h192 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.024 | 2.4e-05 | 3/3 | A better |
| etth1_h192 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | -0.002 | 9.3e-01 | 1/3 | no difference |
| etth1_h192 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.024 | 2.4e-05 | 3/3 | A better |
| etth1_h192 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.376 | 5.0e-25 | 0/3 | B better |
| etth1_h192 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.439 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.297 | 1.9e-24 | 0/3 | B better |
| etth1_h192 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.442 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.218 | 1.1e-14 | 0/3 | B better |
| etth1_h192 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.062 | 5.2e-12 | 3/3 | A better |
| etth1_h192 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.039 | 2.2e-03 | 3/3 | A better |
| etth1_h192 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.059 | 4.2e-25 | 3/3 | A better |
| etth1_h192 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.046 | 2.6e-04 | 3/3 | A better |
| etth1_h192 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.061 | 5.8e-25 | 3/3 | A better |
| etth1_h192 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.503 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.451 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.496 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.432 | 2.3e-25 | 0/3 | B better |
| etth1_h192 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.015 | 2.9e-03 | 2/3 | no difference |
| etth1_h192 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.045 | 1.1e-12 | 3/3 | A better |
| etth1_h336 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.302 | 3.1e-25 | 0/3 | B better |
| etth1_h336 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.462 | 1.4e-25 | 0/3 | B better |
| etth1_h336 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.301 | 4.1e-25 | 0/3 | B better |
| etth1_h336 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.453 | 1.4e-25 | 0/3 | B better |
| etth1_h336 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.193 | 1.8e-12 | 0/3 | B better |
| etth1_h336 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.057 | 9.7e-11 | 3/3 | A better |
| etth1_h336 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.038 | 7.1e-11 | 3/3 | A better |
| etth1_h336 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.129 | 3.4e-25 | 3/3 | A better |
| etth1_h336 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.036 | 2.2e-10 | 3/3 | A better |
| etth1_h336 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.129 | 3.4e-25 | 3/3 | A better |
| etth1_h336 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.000 | 1.0e+00 | 2/3 | no difference |
| etth1_h336 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.008 | 2.6e-01 | 0/3 | no difference |
| etth1_h336 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.018 | 1.2e-03 | 0/3 | B better |
| etth1_h336 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.002 | 1.0e+00 | 2/3 | no difference |
| etth1_h336 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.043 | 1.3e-17 | 0/3 | B better |
| etth1_h336 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.351 | 1.1e-23 | 0/3 | B better |
| etth1_h336 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.025 | 4.3e-10 | 0/3 | B better |
| etth1_h336 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.357 | 7.3e-24 | 0/3 | B better |
| etth1_h336 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.282 | 3.5e-22 | 0/3 | B better |
| etth1_h336 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.199 | 3.0e-22 | 0/3 | B better |
| etth1_h336 | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.014 | 1.7e-01 | 1/3 | no difference |
| etth1_h336 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.044 | 7.7e-10 | 3/3 | A better |
| etth1_h336 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | -0.010 | 1.8e-01 | 1/3 | no difference |
| etth1_h336 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.046 | 5.2e-10 | 3/3 | A better |
| etth1_h336 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.393 | 4.9e-25 | 0/3 | B better |
| etth1_h336 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.451 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.323 | 9.1e-25 | 0/3 | B better |
| etth1_h336 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.429 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.180 | 1.2e-13 | 0/3 | B better |
| etth1_h336 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.086 | 2.9e-12 | 3/3 | A better |
| etth1_h336 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.041 | 9.3e-03 | 3/3 | A better |
| etth1_h336 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.057 | 1.9e-19 | 3/3 | A better |
| etth1_h336 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.042 | 5.3e-03 | 3/3 | A better |
| etth1_h336 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.059 | 1.9e-19 | 3/3 | A better |
| etth1_h336 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.478 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.450 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.505 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.434 | 2.3e-25 | 0/3 | B better |
| etth1_h336 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.026 | 3.8e-02 | 2/3 | no difference |
| etth1_h336 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.066 | 6.0e-14 | 3/3 | A better |
| etth1_h720 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.365 | 1.4e-25 | 0/3 | B better |
| etth1_h720 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.428 | 1.4e-25 | 0/3 | B better |
| etth1_h720 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.424 | 1.4e-25 | 0/3 | B better |
| etth1_h720 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.441 | 1.4e-25 | 0/3 | B better |
| etth1_h720 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.063 | 1.3e-03 | 0/3 | B better |
| etth1_h720 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.064 | 5.6e-18 | 3/3 | A better |
| etth1_h720 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.010 | 1.8e-02 | 2/3 | no difference |
| etth1_h720 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.132 | 1.1e-23 | 3/3 | A better |
| etth1_h720 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.009 | 3.2e-02 | 2/3 | no difference |
| etth1_h720 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.132 | 3.8e-24 | 3/3 | A better |
| etth1_h720 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.003 | 8.4e-01 | 2/3 | no difference |
| etth1_h720 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.017 | 1.3e-02 | 0/3 | B better |
| etth1_h720 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.018 | 7.4e-02 | 0/3 | no difference |
| etth1_h720 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.064 | 9.1e-03 | 3/3 | A better |
| etth1_h720 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.065 | 1.3e-14 | 0/3 | B better |
| etth1_h720 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.386 | 1.2e-23 | 0/3 | B better |
| etth1_h720 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.044 | 2.1e-09 | 0/3 | B better |
| etth1_h720 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.468 | 7.5e-25 | 0/3 | B better |
| etth1_h720 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.199 | 3.4e-15 | 0/3 | B better |
| etth1_h720 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.045 | 3.0e-01 | 1/3 | no difference |
| etth1_h720 | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.002 | 1.6e-01 | 1/3 | no difference |
| etth1_h720 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.061 | 1.5e-11 | 3/3 | A better |
| etth1_h720 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.003 | 1.6e-01 | 1/3 | no difference |
| etth1_h720 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.064 | 4.0e-12 | 3/3 | A better |
| etth1_h720 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.372 | 3.9e-25 | 0/3 | B better |
| etth1_h720 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.439 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.376 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.426 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.123 | 3.7e-09 | 0/3 | B better |
| etth1_h720 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.109 | 1.7e-15 | 3/3 | A better |
| etth1_h720 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.027 | 1.5e-02 | 2/3 | no difference |
| etth1_h720 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.015 | 6.8e-02 | 3/3 | no difference |
| etth1_h720 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.046 | 1.9e-03 | 3/3 | A better |
| etth1_h720 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.015 | 6.8e-02 | 3/3 | no difference |
| etth1_h720 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.479 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.440 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.510 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.419 | 2.3e-25 | 0/3 | B better |
| etth1_h720 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.031 | 4.1e-03 | 3/3 | A better |
| etth1_h720 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.106 | 5.3e-20 | 3/3 | A better |
| etth2 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.135 | 1.1e-15 | 0/3 | B better |
| etth2 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.251 | 2.0e-21 | 0/3 | B better |
| etth2 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.197 | 1.1e-19 | 0/3 | B better |
| etth2 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.240 | 1.7e-21 | 0/3 | B better |
| etth2 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.035 | 1.0e-02 | 2/3 | no difference |
| etth2 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.017 | 2.7e-01 | 2/3 | no difference |
| etth2 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.007 | 9.4e-01 | 2/3 | no difference |
| etth2 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.029 | 7.8e-06 | 3/3 | A better |
| etth2 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.008 | 9.1e-01 | 2/3 | no difference |
| etth2 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.033 | 2.3e-07 | 3/3 | A better |
| etth2 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.002 | 1.0e+00 | 2/3 | no difference |
| etth2 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.001 | 1.0e+00 | 1/3 | no difference |
| etth2 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | +0.044 | 2.7e-04 | 3/3 | A better |
| etth2 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.005 | 1.0e+00 | 1/3 | no difference |
| etth2 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.043 | 6.2e-06 | 0/3 | B better |
| etth2 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.237 | 8.7e-19 | 0/3 | B better |
| etth2 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.086 | 1.4e-15 | 0/3 | B better |
| etth2 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.243 | 3.3e-19 | 0/3 | B better |
| etth2 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.042 | 4.3e-07 | 3/3 | A better |
| etth2 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.091 | 2.5e-08 | 3/3 | A better |
| etth2 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.040 | 8.0e-06 | 3/3 | A better |
| etth2 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.054 | 1.3e-10 | 3/3 | A better |
| etth2 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.040 | 8.0e-06 | 3/3 | A better |
| etth2 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.057 | 2.0e-11 | 3/3 | A better |
| etth2 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.208 | 4.0e-20 | 0/3 | B better |
| etth2 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.215 | 2.5e-23 | 0/3 | B better |
| etth2 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.285 | 5.6e-23 | 0/3 | B better |
| etth2 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.222 | 3.7e-23 | 0/3 | B better |
| etth2 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.037 | 6.8e-02 | 3/3 | no difference |
| etth2 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.067 | 2.4e-07 | 3/3 | A better |
| etth2 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.045 | 4.1e-05 | 3/3 | A better |
| etth2 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.047 | 4.2e-23 | 3/3 | A better |
| etth2 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.052 | 1.2e-06 | 3/3 | A better |
| etth2 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.052 | 4.2e-23 | 3/3 | A better |
| etth2 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.300 | 1.8e-22 | 0/3 | B better |
| etth2 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.189 | 3.9e-20 | 0/3 | B better |
| etth2 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.338 | 5.7e-24 | 0/3 | B better |
| etth2 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.206 | 9.2e-23 | 0/3 | B better |
| etth2 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.004 | 9.0e-01 | 2/3 | no difference |
| etth2 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.024 | 4.1e-05 | 3/3 | A better |
| ettm1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.127 | 5.4e-20 | 0/3 | B better |
| ettm1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.371 | 1.4e-25 | 0/3 | B better |
| ettm1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.072 | 1.0e-20 | 0/3 | B better |
| ettm1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.395 | 1.4e-25 | 0/3 | B better |
| ettm1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.374 | 1.9e-24 | 0/3 | B better |
| ettm1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.006 | 8.8e-01 | 1/3 | no difference |
| ettm1 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.015 | 9.7e-01 | 2/3 | no difference |
| ettm1 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.026 | 3.2e-11 | 3/3 | A better |
| ettm1 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.011 | 9.7e-01 | 2/3 | no difference |
| ettm1 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.025 | 1.1e-10 | 3/3 | A better |
| ettm1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.002 | 9.7e-01 | 1/3 | no difference |
| ettm1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.004 | 7.2e-01 | 2/3 | no difference |
| ettm1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.017 | 7.2e-01 | 1/3 | no difference |
| ettm1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.020 | 9.2e-02 | 3/3 | no difference |
| ettm1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.075 | 1.2e-21 | 0/3 | B better |
| ettm1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.361 | 3.2e-25 | 0/3 | B better |
| ettm1 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.057 | 8.5e-21 | 0/3 | B better |
| ettm1 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.376 | 3.2e-25 | 0/3 | B better |
| ettm1 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.265 | 4.0e-19 | 0/3 | B better |
| ettm1 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.038 | 8.3e-05 | 0/3 | B better |
| ettm1 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.101 | 2.6e-04 | 3/3 | A better |
| ettm1 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.018 | 1.1e-05 | 3/3 | A better |
| ettm1 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.091 | 5.4e-04 | 3/3 | A better |
| ettm1 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.015 | 1.1e-04 | 3/3 | A better |
| ettm1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.134 | 3.8e-22 | 0/3 | B better |
| ettm1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.349 | 2.3e-25 | 0/3 | B better |
| ettm1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.128 | 3.7e-22 | 0/3 | B better |
| ettm1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.341 | 2.3e-25 | 0/3 | B better |
| ettm1 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.306 | 3.9e-19 | 0/3 | B better |
| ettm1 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.021 | 3.3e-03 | 0/3 | B better |
| ettm1 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.052 | 2.2e-03 | 3/3 | A better |
| ettm1 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.052 | 2.0e-24 | 3/3 | A better |
| ettm1 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.071 | 2.9e-04 | 3/3 | A better |
| ettm1 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.054 | 1.4e-24 | 3/3 | A better |
| ettm1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.226 | 5.1e-24 | 0/3 | B better |
| ettm1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.321 | 2.3e-25 | 0/3 | B better |
| ettm1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.209 | 5.1e-24 | 0/3 | B better |
| ettm1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.345 | 2.3e-25 | 0/3 | B better |
| ettm1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.215 | 1.9e-14 | 0/3 | B better |
| ettm1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.041 | 8.6e-11 | 3/3 | A better |
| exchange | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.261 | 5.4e-24 | 0/3 | B better |
| exchange | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.438 | 3.1e-20 | 0/3 | B better |
| exchange | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.292 | 1.2e-24 | 0/3 | B better |
| exchange | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.390 | 5.6e-21 | 0/3 | B better |
| exchange | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.042 | 1.9e-01 | 2/3 | no difference |
| exchange | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.075 | 2.1e-02 | 1/3 | no difference |
| exchange | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.010 | 3.4e-01 | 3/3 | no difference |
| exchange | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.374 | 2.3e-13 | 3/3 | A better |
| exchange | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.012 | 3.4e-01 | 3/3 | no difference |
| exchange | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.374 | 9.1e-14 | 3/3 | A better |
| exchange | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.012 | 3.4e-01 | 3/3 | no difference |
| exchange | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.032 | 3.0e-01 | 2/3 | no difference |
| exchange | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.028 | 3.4e-01 | 0/3 | no difference |
| exchange | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.049 | 3.4e-01 | 0/3 | no difference |
| exchange | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.135 | 1.4e-19 | 0/3 | B better |
| exchange | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.471 | 9.4e-11 | 0/3 | B better |
| exchange | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.095 | 1.5e-16 | 0/3 | B better |
| exchange | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.390 | 3.4e-10 | 0/3 | B better |
| exchange | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.025 | 1.0e-01 | 3/3 | no difference |
| exchange | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.370 | 1.5e-08 | 3/3 | A better |
| exchange | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.008 | 2.1e-01 | 1/3 | no difference |
| exchange | smamba | MambaLRP | IG | del_aopc_mean | 150 | -0.028 | 7.7e-04 | 1/3 | no difference |
| exchange | smamba | MambaLRP | GxI | del_aopc_interp | 150 | -0.013 | 2.1e-01 | 2/3 | no difference |
| exchange | smamba | MambaLRP | GxI | del_aopc_mean | 150 | -0.028 | 2.6e-04 | 1/3 | no difference |
| exchange | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.401 | 7.6e-25 | 0/3 | B better |
| exchange | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.386 | 1.0e-24 | 0/3 | B better |
| exchange | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.429 | 8.2e-25 | 0/3 | B better |
| exchange | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.430 | 8.7e-25 | 0/3 | B better |
| exchange | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.134 | 7.7e-04 | 1/3 | no difference |
| exchange | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.149 | 3.6e-14 | 0/3 | B better |
| exchange | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.098 | 2.5e-09 | 3/3 | A better |
| exchange | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.051 | 1.8e-08 | 3/3 | A better |
| exchange | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.093 | 3.5e-09 | 3/3 | A better |
| exchange | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.055 | 8.8e-09 | 3/3 | A better |
| exchange | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.338 | 7.3e-25 | 0/3 | B better |
| exchange | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.137 | 1.8e-08 | 0/3 | B better |
| exchange | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.472 | 3.2e-25 | 0/3 | B better |
| exchange | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.144 | 9.5e-11 | 0/3 | B better |
| exchange | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.095 | 1.7e-04 | 2/3 | no difference |
| exchange | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.181 | 5.6e-15 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-MMD8 | ap | 124 | -0.143 | 7.4e-11 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.115 | 1.8e-12 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.114 | 6.4e-09 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-U8 | ap | 124 | -0.092 | 2.0e-09 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.092 | 1.6e-11 | 0/3 | B better |
| g1 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.094 | 3.0e-08 | 0/3 | B better |
| g1 | itransformer | SHAP-U8 | IG-U8 | ap | 124 | -0.021 | 4.8e-03 | 0/3 | B better |
| g1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.011 | 1.8e-01 | 0/3 | no difference |
| g1 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.000 | 5.7e-01 | 1/3 | no difference |
| g1 | plain | MambaLRP | IG | ap | 124 | -0.008 | 7.1e-02 | 0/3 | no difference |
| g1 | plain | MambaLRP | IG | del_aopc_mean | 150 | -0.007 | 1.8e-01 | 1/3 | no difference |
| g1 | plain | MambaLRP | IG | del_aopc_interp | 150 | -0.002 | 1.0e+00 | 1/3 | no difference |
| g1 | plain | MambaLRP | GxI | ap | 124 | +0.005 | 1.0e+00 | 2/3 | no difference |
| g1 | plain | MambaLRP | GxI | del_aopc_mean | 150 | -0.013 | 9.7e-03 | 0/3 | B better |
| g1 | plain | MambaLRP | GxI | del_aopc_interp | 150 | -0.010 | 1.5e-01 | 0/3 | no difference |
| g1 | plain | SHAP-Δ8 | SHAP-U8 | ap | 124 | +0.013 | 4.2e-01 | 3/3 | no difference |
| g1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.001 | 1.0e+00 | 2/3 | no difference |
| g1 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.001 | 1.0e+00 | 2/3 | no difference |
| g1 | plain | SHAP-Δ8 | SHAP-MMD8 | ap | 124 | -0.076 | 9.2e-05 | 0/3 | B better |
| g1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.025 | 8.9e-05 | 0/3 | B better |
| g1 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.103 | 7.1e-03 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-MMD8 | ap | 124 | -0.205 | 1.8e-14 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.100 | 4.0e-16 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.098 | 6.5e-05 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-U8 | ap | 124 | -0.117 | 1.5e-10 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.075 | 8.1e-14 | 0/3 | B better |
| g1 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.007 | 2.0e-02 | 2/3 | no difference |
| g1 | plain | SHAP-U8 | IG-U8 | ap | 124 | -0.006 | 8.4e-01 | 0/3 | no difference |
| g1 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.001 | 1.0e+00 | 0/3 | no difference |
| g1 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.003 | 1.0e+00 | 1/3 | no difference |
| g1 | smamba | MambaLRP | IG | ap | 124 | +0.010 | 4.7e-02 | 2/3 | no difference |
| g1 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.022 | 6.7e-08 | 3/3 | A better |
| g1 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.002 | 1.0e+00 | 1/3 | no difference |
| g1 | smamba | MambaLRP | GxI | ap | 124 | -0.015 | 5.0e-07 | 0/3 | B better |
| g1 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.011 | 3.3e-03 | 3/3 | A better |
| g1 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.003 | 1.0e+00 | 2/3 | no difference |
| g1 | smamba | GS-SHAP | SHAP-MMD8 | ap | 124 | -0.221 | 1.2e-15 | 0/3 | B better |
| g1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.091 | 1.0e-12 | 0/3 | B better |
| g1 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.106 | 3.5e-09 | 0/3 | B better |
| g1 | smamba | GS-SHAP | SHAP-U8 | ap | 124 | -0.160 | 3.7e-13 | 0/3 | B better |
| g1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.070 | 5.1e-10 | 0/3 | B better |
| g1 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.132 | 2.2e-10 | 0/3 | B better |
| g1 | smamba | SHAP-U8 | IG-U8 | ap | 124 | -0.002 | 1.0e+00 | 1/3 | no difference |
| g1 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.007 | 4.7e-02 | 3/3 | A better |
| g1 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.014 | 3.7e-01 | 3/3 | no difference |
| g1 | timemachine | MambaLRP | IG | ap | 124 | -0.031 | 3.5e-06 | 0/3 | B better |
| g1 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | -0.001 | 1.0e+00 | 2/3 | no difference |
| g1 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | -0.014 | 1.9e-01 | 0/3 | no difference |
| g1 | timemachine | MambaLRP | GxI | ap | 124 | -0.010 | 5.3e-03 | 0/3 | B better |
| g1 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | -0.021 | 6.5e-01 | 0/3 | no difference |
| g1 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.006 | 1.0e+00 | 2/3 | no difference |
| g1 | timemachine | GS-SHAP | SHAP-MMD8 | ap | 124 | -0.209 | 4.2e-16 | 0/3 | B better |
| g1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.077 | 3.1e-13 | 0/3 | B better |
| g1 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.022 | 6.1e-06 | 1/3 | no difference |
| g1 | timemachine | GS-SHAP | SHAP-U8 | ap | 124 | -0.176 | 7.7e-15 | 0/3 | B better |
| g1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.037 | 3.5e-06 | 0/3 | B better |
| g1 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.014 | 3.0e-05 | 3/3 | A better |
| g1 | timemachine | SHAP-U8 | IG-U8 | ap | 124 | +0.002 | 1.0e+00 | 2/3 | no difference |
| g1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.005 | 1.1e-02 | 0/3 | B better |
| g1 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.002 | 1.0e+00 | 1/3 | no difference |
| g2a | itransformer | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.015 | 1.8e-03 | 1/3 | no difference |
| g2a | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | +0.101 | 4.0e-03 | 3/3 | A better |
| g2a | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.130 | 1.5e-02 | 3/3 | A better |
| g2a | itransformer | GS-SHAP | SHAP-U8 | ap | 150 | +0.046 | 3.7e-05 | 3/3 | A better |
| g2a | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | +0.078 | 1.9e-03 | 3/3 | A better |
| g2a | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.108 | 2.0e-02 | 3/3 | A better |
| g2a | itransformer | SHAP-U8 | IG-U8 | ap | 150 | -0.074 | 2.1e-15 | 0/3 | B better |
| g2a | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.003 | 6.0e-01 | 2/3 | no difference |
| g2a | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.024 | 4.6e-02 | 1/3 | no difference |
| g2a | plain | MambaLRP | IG | ap | 150 | -0.018 | 2.8e-07 | 0/3 | B better |
| g2a | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.003 | 8.9e-02 | 3/3 | no difference |
| g2a | plain | MambaLRP | IG | del_aopc_interp | 150 | -0.071 | 5.8e-04 | 0/3 | B better |
| g2a | plain | MambaLRP | GxI | ap | 150 | +0.031 | 2.4e-07 | 3/3 | A better |
| g2a | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.121 | 4.8e-25 | 3/3 | A better |
| g2a | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.204 | 2.1e-15 | 3/3 | A better |
| g2a | plain | SHAP-Δ8 | SHAP-U8 | ap | 150 | +0.005 | 1.0e+00 | 2/3 | no difference |
| g2a | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.001 | 6.5e-01 | 2/3 | no difference |
| g2a | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.017 | 1.0e+00 | 1/3 | no difference |
| g2a | plain | SHAP-Δ8 | SHAP-MMD8 | ap | 150 | -0.052 | 2.2e-10 | 0/3 | B better |
| g2a | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.041 | 8.4e-20 | 0/3 | B better |
| g2a | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.041 | 1.0e+00 | 1/3 | no difference |
| g2a | plain | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.017 | 4.1e-07 | 3/3 | A better |
| g2a | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.093 | 4.8e-25 | 0/3 | B better |
| g2a | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.003 | 5.3e-01 | 1/3 | no difference |
| g2a | plain | GS-SHAP | SHAP-U8 | ap | 150 | +0.074 | 2.3e-17 | 3/3 | A better |
| g2a | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.052 | 4.8e-20 | 0/3 | B better |
| g2a | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.027 | 8.9e-02 | 2/3 | no difference |
| g2a | plain | SHAP-U8 | IG-U8 | ap | 150 | -0.001 | 1.0e+00 | 2/3 | no difference |
| g2a | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.002 | 9.6e-02 | 3/3 | no difference |
| g2a | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.036 | 1.6e-02 | 0/3 | B better |
| g2a | smamba | MambaLRP | IG | ap | 150 | -0.120 | 2.5e-22 | 0/3 | B better |
| g2a | smamba | MambaLRP | IG | del_aopc_mean | 150 | -0.249 | 1.8e-20 | 0/3 | B better |
| g2a | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.173 | 3.8e-09 | 0/3 | B better |
| g2a | smamba | MambaLRP | GxI | ap | 150 | +0.082 | 4.3e-05 | 3/3 | A better |
| g2a | smamba | MambaLRP | GxI | del_aopc_mean | 150 | -0.072 | 2.4e-01 | 1/3 | no difference |
| g2a | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.218 | 7.1e-13 | 3/3 | A better |
| g2a | smamba | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.096 | 8.3e-13 | 3/3 | A better |
| g2a | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.115 | 1.8e-14 | 0/3 | B better |
| g2a | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.213 | 4.5e-06 | 3/3 | A better |
| g2a | smamba | GS-SHAP | SHAP-U8 | ap | 150 | +0.136 | 2.4e-17 | 3/3 | A better |
| g2a | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.001 | 8.1e-01 | 1/3 | no difference |
| g2a | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.206 | 1.2e-04 | 3/3 | A better |
| g2a | smamba | SHAP-U8 | IG-U8 | ap | 150 | -0.032 | 8.8e-07 | 0/3 | B better |
| g2a | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.000 | 8.1e-01 | 2/3 | no difference |
| g2a | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.064 | 8.1e-01 | 0/3 | no difference |
| g2a | timemachine | MambaLRP | IG | ap | 150 | -0.102 | 2.5e-24 | 0/3 | B better |
| g2a | timemachine | MambaLRP | IG | del_aopc_mean | 150 | -0.031 | 8.1e-17 | 0/3 | B better |
| g2a | timemachine | MambaLRP | IG | del_aopc_interp | 150 | -0.109 | 6.5e-19 | 0/3 | B better |
| g2a | timemachine | MambaLRP | GxI | ap | 150 | +0.028 | 3.0e-02 | 3/3 | A better |
| g2a | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.045 | 1.4e-11 | 3/3 | A better |
| g2a | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.208 | 1.2e-19 | 3/3 | A better |
| g2a | timemachine | GS-SHAP | SHAP-MMD8 | ap | 150 | -0.008 | 3.3e-01 | 1/3 | no difference |
| g2a | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.074 | 1.5e-24 | 0/3 | B better |
| g2a | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.052 | 3.0e-02 | 0/3 | B better |
| g2a | timemachine | GS-SHAP | SHAP-U8 | ap | 150 | +0.075 | 2.9e-16 | 3/3 | A better |
| g2a | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.023 | 9.4e-05 | 0/3 | B better |
| g2a | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.039 | 3.0e-02 | 3/3 | A better |
| g2a | timemachine | SHAP-U8 | IG-U8 | ap | 150 | -0.024 | 3.3e-10 | 0/3 | B better |
| g2a | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.002 | 1.6e-01 | 3/3 | no difference |
| g2a | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.045 | 1.8e-07 | 0/3 | B better |
| g2b | itransformer | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.117 | 2.1e-23 | 3/3 | A better |
| g2b | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | +0.155 | 7.6e-13 | 3/3 | A better |
| g2b | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.052 | 2.9e-03 | 3/3 | A better |
| g2b | itransformer | GS-SHAP | SHAP-U8 | ap | 150 | +0.127 | 1.1e-23 | 3/3 | A better |
| g2b | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | +0.174 | 3.4e-16 | 3/3 | A better |
| g2b | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.100 | 1.3e-06 | 3/3 | A better |
| g2b | itransformer | SHAP-U8 | IG-U8 | ap | 150 | -0.058 | 1.2e-24 | 0/3 | B better |
| g2b | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.075 | 1.6e-08 | 0/3 | B better |
| g2b | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.053 | 1.8e-07 | 0/3 | B better |
| g2b | plain | MambaLRP | IG | ap | 150 | -0.019 | 4.9e-11 | 0/3 | B better |
| g2b | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.001 | 9.2e-01 | 1/3 | no difference |
| g2b | plain | MambaLRP | IG | del_aopc_interp | 150 | -0.061 | 1.6e-07 | 0/3 | B better |
| g2b | plain | MambaLRP | GxI | ap | 150 | +0.019 | 4.6e-07 | 3/3 | A better |
| g2b | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.176 | 4.8e-25 | 3/3 | A better |
| g2b | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.141 | 5.9e-18 | 3/3 | A better |
| g2b | plain | SHAP-Δ8 | SHAP-U8 | ap | 150 | +0.005 | 4.6e-02 | 2/3 | no difference |
| g2b | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.004 | 1.2e-03 | 2/3 | no difference |
| g2b | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.013 | 4.6e-02 | 1/3 | no difference |
| g2b | plain | SHAP-Δ8 | SHAP-MMD8 | ap | 150 | -0.030 | 3.9e-06 | 0/3 | B better |
| g2b | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.043 | 1.1e-23 | 0/3 | B better |
| g2b | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.067 | 2.7e-07 | 0/3 | B better |
| g2b | plain | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.073 | 2.5e-23 | 3/3 | A better |
| g2b | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.111 | 4.8e-25 | 0/3 | B better |
| g2b | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.143 | 1.3e-20 | 3/3 | A better |
| g2b | plain | GS-SHAP | SHAP-U8 | ap | 150 | +0.107 | 4.8e-25 | 3/3 | A better |
| g2b | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.064 | 7.0e-25 | 0/3 | B better |
| g2b | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.197 | 3.4e-22 | 3/3 | A better |
| g2b | plain | SHAP-U8 | IG-U8 | ap | 150 | -0.015 | 2.2e-08 | 0/3 | B better |
| g2b | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.001 | 3.0e-01 | 1/3 | no difference |
| g2b | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.047 | 5.5e-11 | 0/3 | B better |
| g2b | smamba | MambaLRP | IG | ap | 150 | -0.028 | 3.4e-02 | 2/3 | no difference |
| g2b | smamba | MambaLRP | IG | del_aopc_mean | 150 | -0.039 | 3.9e-01 | 1/3 | no difference |
| g2b | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.000 | 6.5e-01 | 1/3 | no difference |
| g2b | smamba | MambaLRP | GxI | ap | 150 | -0.012 | 3.9e-01 | 1/3 | no difference |
| g2b | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.001 | 3.1e-01 | 1/3 | no difference |
| g2b | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.177 | 4.4e-11 | 3/3 | A better |
| g2b | smamba | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.163 | 3.3e-15 | 3/3 | A better |
| g2b | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.093 | 4.1e-11 | 0/3 | B better |
| g2b | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.167 | 5.3e-05 | 3/3 | A better |
| g2b | smamba | GS-SHAP | SHAP-U8 | ap | 150 | +0.243 | 3.3e-23 | 3/3 | A better |
| g2b | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.069 | 2.8e-09 | 0/3 | B better |
| g2b | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.249 | 3.1e-05 | 3/3 | A better |
| g2b | smamba | SHAP-U8 | IG-U8 | ap | 150 | -0.010 | 3.9e-01 | 1/3 | no difference |
| g2b | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.070 | 1.6e-09 | 3/3 | A better |
| g2b | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.144 | 5.8e-04 | 0/3 | B better |
| g2b | timemachine | MambaLRP | IG | ap | 150 | -0.238 | 3.4e-25 | 0/3 | B better |
| g2b | timemachine | MambaLRP | IG | del_aopc_mean | 150 | -0.115 | 3.4e-25 | 0/3 | B better |
| g2b | timemachine | MambaLRP | IG | del_aopc_interp | 150 | -0.109 | 1.4e-22 | 0/3 | B better |
| g2b | timemachine | MambaLRP | GxI | ap | 150 | -0.070 | 1.5e-07 | 0/3 | B better |
| g2b | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.020 | 4.7e-02 | 3/3 | A better |
| g2b | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.159 | 1.7e-20 | 3/3 | A better |
| g2b | timemachine | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.064 | 7.3e-24 | 3/3 | A better |
| g2b | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.077 | 3.4e-25 | 0/3 | B better |
| g2b | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.046 | 3.8e-04 | 3/3 | A better |
| g2b | timemachine | GS-SHAP | SHAP-U8 | ap | 150 | +0.119 | 3.4e-25 | 3/3 | A better |
| g2b | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.039 | 2.2e-21 | 0/3 | B better |
| g2b | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.107 | 2.6e-08 | 3/3 | A better |
| g2b | timemachine | SHAP-U8 | IG-U8 | ap | 150 | -0.023 | 3.1e-19 | 0/3 | B better |
| g2b | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.000 | 8.3e-01 | 1/3 | no difference |
| g2b | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.043 | 1.7e-09 | 0/3 | B better |
| g2c | itransformer | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.048 | 2.8e-02 | 3/3 | A better |
| g2c | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | +0.095 | 2.1e-03 | 3/3 | A better |
| g2c | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.140 | 8.9e-06 | 3/3 | A better |
| g2c | itransformer | GS-SHAP | SHAP-U8 | ap | 150 | +0.076 | 1.3e-04 | 3/3 | A better |
| g2c | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | +0.126 | 1.8e-06 | 3/3 | A better |
| g2c | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.103 | 3.3e-02 | 3/3 | A better |
| g2c | itransformer | SHAP-U8 | IG-U8 | ap | 150 | -0.163 | 1.5e-17 | 0/3 | B better |
| g2c | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.070 | 1.2e-03 | 0/3 | B better |
| g2c | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.080 | 5.0e-07 | 0/3 | B better |
| g2c | plain | MambaLRP | IG | ap | 150 | -0.031 | 4.1e-09 | 0/3 | B better |
| g2c | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.010 | 1.6e-05 | 3/3 | A better |
| g2c | plain | MambaLRP | IG | del_aopc_interp | 150 | -0.086 | 5.1e-08 | 0/3 | B better |
| g2c | plain | MambaLRP | GxI | ap | 150 | +0.079 | 4.6e-18 | 3/3 | A better |
| g2c | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.171 | 4.8e-25 | 3/3 | A better |
| g2c | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.266 | 1.2e-22 | 3/3 | A better |
| g2c | plain | SHAP-Δ8 | SHAP-U8 | ap | 150 | -0.004 | 9.5e-01 | 1/3 | no difference |
| g2c | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.003 | 9.5e-01 | 3/3 | no difference |
| g2c | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.017 | 9.5e-01 | 0/3 | no difference |
| g2c | plain | SHAP-Δ8 | SHAP-MMD8 | ap | 150 | -0.022 | 6.6e-03 | 0/3 | B better |
| g2c | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | -0.038 | 2.2e-13 | 0/3 | B better |
| g2c | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.032 | 9.5e-01 | 1/3 | no difference |
| g2c | plain | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.098 | 2.1e-19 | 3/3 | A better |
| g2c | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.090 | 7.4e-24 | 0/3 | B better |
| g2c | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.062 | 7.8e-06 | 3/3 | A better |
| g2c | plain | GS-SHAP | SHAP-U8 | ap | 150 | +0.116 | 2.0e-19 | 3/3 | A better |
| g2c | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.049 | 7.8e-16 | 0/3 | B better |
| g2c | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.077 | 6.5e-03 | 3/3 | A better |
| g2c | plain | SHAP-U8 | IG-U8 | ap | 150 | +0.004 | 9.5e-01 | 2/3 | no difference |
| g2c | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.012 | 5.0e-04 | 3/3 | A better |
| g2c | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.048 | 1.2e-03 | 0/3 | B better |
| g2c | smamba | MambaLRP | IG | ap | 150 | +0.101 | 1.6e-01 | 2/3 | no difference |
| g2c | smamba | MambaLRP | IG | del_aopc_mean | 150 | -0.126 | 3.5e-09 | 0/3 | B better |
| g2c | smamba | MambaLRP | IG | del_aopc_interp | 150 | -0.018 | 1.0e+00 | 1/3 | no difference |
| g2c | smamba | MambaLRP | GxI | ap | 150 | +0.278 | 1.4e-22 | 3/3 | A better |
| g2c | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.115 | 1.7e-03 | 2/3 | no difference |
| g2c | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.302 | 2.1e-20 | 3/3 | A better |
| g2c | smamba | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.149 | 8.2e-12 | 3/3 | A better |
| g2c | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.010 | 1.0e+00 | 1/3 | no difference |
| g2c | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | +0.200 | 7.8e-11 | 3/3 | A better |
| g2c | smamba | GS-SHAP | SHAP-U8 | ap | 150 | +0.127 | 1.3e-09 | 3/3 | A better |
| g2c | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | +0.095 | 2.2e-10 | 3/3 | A better |
| g2c | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.189 | 6.7e-09 | 3/3 | A better |
| g2c | smamba | SHAP-U8 | IG-U8 | ap | 150 | -0.013 | 6.4e-02 | 1/3 | no difference |
| g2c | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | -0.047 | 2.0e-03 | 1/3 | no difference |
| g2c | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.113 | 1.3e-05 | 0/3 | B better |
| g2c | timemachine | MambaLRP | IG | ap | 150 | -0.181 | 5.5e-25 | 0/3 | B better |
| g2c | timemachine | MambaLRP | IG | del_aopc_mean | 150 | -0.087 | 5.6e-24 | 0/3 | B better |
| g2c | timemachine | MambaLRP | IG | del_aopc_interp | 150 | -0.224 | 3.2e-24 | 0/3 | B better |
| g2c | timemachine | MambaLRP | GxI | ap | 150 | -0.091 | 6.4e-12 | 0/3 | B better |
| g2c | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | -0.034 | 5.3e-05 | 1/3 | no difference |
| g2c | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.004 | 7.6e-01 | 2/3 | no difference |
| g2c | timemachine | GS-SHAP | SHAP-MMD8 | ap | 150 | +0.012 | 3.2e-04 | 3/3 | A better |
| g2c | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.033 | 4.5e-08 | 0/3 | B better |
| g2c | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.011 | 8.1e-01 | 1/3 | no difference |
| g2c | timemachine | GS-SHAP | SHAP-U8 | ap | 150 | +0.078 | 6.2e-19 | 3/3 | A better |
| g2c | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | +0.037 | 6.4e-14 | 3/3 | A better |
| g2c | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | +0.054 | 7.3e-06 | 3/3 | A better |
| g2c | timemachine | SHAP-U8 | IG-U8 | ap | 150 | -0.003 | 3.3e-01 | 0/3 | no difference |
| g2c | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.008 | 3.8e-03 | 3/3 | A better |
| g2c | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.038 | 1.2e-03 | 0/3 | B better |
| g3 | itransformer | GS-SHAP | SHAP-MMD8 | feat_spearman | 150 | +0.177 | 8.8e-09 | 3/3 | A better |
| g3 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.227 | 6.4e-23 | 0/3 | B better |
| g3 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.299 | 3.9e-17 | 0/3 | B better |
| g3 | itransformer | GS-SHAP | SHAP-U8 | feat_spearman | 150 | +0.175 | 1.0e-08 | 3/3 | A better |
| g3 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.220 | 2.2e-23 | 0/3 | B better |
| g3 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.258 | 1.7e-17 | 0/3 | B better |
| g3 | itransformer | SHAP-U8 | IG-U8 | feat_spearman | 150 | -0.001 | 7.1e-01 | 1/3 | no difference |
| g3 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.006 | 5.3e-01 | 3/3 | no difference |
| g3 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | -0.006 | 7.1e-01 | 1/3 | no difference |
| g3 | plain | MambaLRP | IG | feat_spearman | 150 | -0.041 | 9.4e-01 | 1/3 | no difference |
| g3 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.005 | 1.0e+00 | 1/3 | no difference |
| g3 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.051 | 1.6e-03 | 3/3 | A better |
| g3 | plain | MambaLRP | GxI | feat_spearman | 150 | -0.081 | 5.6e-02 | 0/3 | no difference |
| g3 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.010 | 1.0e+00 | 3/3 | no difference |
| g3 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.064 | 5.0e-05 | 3/3 | A better |
| g3 | plain | SHAP-Δ8 | SHAP-U8 | feat_spearman | 150 | -0.039 | 6.1e-03 | 0/3 | B better |
| g3 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.004 | 1.0e+00 | 1/3 | no difference |
| g3 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.047 | 9.4e-01 | 3/3 | no difference |
| g3 | plain | SHAP-Δ8 | SHAP-MMD8 | feat_spearman | 150 | -0.033 | 9.3e-01 | 1/3 | no difference |
| g3 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.025 | 3.1e-01 | 3/3 | no difference |
| g3 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.000 | 1.0e+00 | 2/3 | no difference |
| g3 | plain | GS-SHAP | SHAP-MMD8 | feat_spearman | 150 | +0.142 | 1.7e-05 | 3/3 | A better |
| g3 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.193 | 5.5e-17 | 0/3 | B better |
| g3 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.353 | 4.6e-20 | 0/3 | B better |
| g3 | plain | GS-SHAP | SHAP-U8 | feat_spearman | 150 | +0.136 | 4.4e-05 | 2/3 | no difference |
| g3 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.221 | 1.8e-19 | 0/3 | B better |
| g3 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.305 | 1.0e-19 | 0/3 | B better |
| g3 | plain | SHAP-U8 | IG-U8 | feat_spearman | 150 | -0.000 | 1.0e+00 | 1/3 | no difference |
| g3 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.007 | 4.4e-01 | 3/3 | no difference |
| g3 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.010 | 1.0e+00 | 3/3 | no difference |
| g3 | smamba | MambaLRP | IG | feat_spearman | 150 | +0.282 | 8.3e-18 | 3/3 | A better |
| g3 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.001 | 1.0e+00 | 2/3 | no difference |
| g3 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.055 | 4.0e-06 | 3/3 | A better |
| g3 | smamba | MambaLRP | GxI | feat_spearman | 150 | +0.243 | 3.5e-13 | 3/3 | A better |
| g3 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | -0.002 | 1.0e+00 | 1/3 | no difference |
| g3 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.103 | 1.1e-11 | 3/3 | A better |
| g3 | smamba | GS-SHAP | SHAP-MMD8 | feat_spearman | 150 | +0.243 | 3.8e-10 | 3/3 | A better |
| g3 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.259 | 3.4e-22 | 0/3 | B better |
| g3 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.302 | 3.6e-16 | 0/3 | B better |
| g3 | smamba | GS-SHAP | SHAP-U8 | feat_spearman | 150 | +0.257 | 3.6e-11 | 3/3 | A better |
| g3 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.248 | 2.0e-22 | 0/3 | B better |
| g3 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.263 | 2.2e-16 | 0/3 | B better |
| g3 | smamba | SHAP-U8 | IG-U8 | feat_spearman | 150 | +0.082 | 1.5e-03 | 3/3 | A better |
| g3 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.001 | 1.0e+00 | 2/3 | no difference |
| g3 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.024 | 1.0e+00 | 3/3 | no difference |
| g3 | timemachine | MambaLRP | IG | feat_spearman | 150 | +0.040 | 1.9e-01 | 2/3 | no difference |
| g3 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | -0.004 | 7.1e-02 | 0/3 | no difference |
| g3 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.001 | 1.0e+00 | 2/3 | no difference |
| g3 | timemachine | MambaLRP | GxI | feat_spearman | 150 | +0.056 | 9.8e-02 | 3/3 | no difference |
| g3 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.006 | 2.5e-01 | 3/3 | no difference |
| g3 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.052 | 3.8e-04 | 3/3 | A better |
| g3 | timemachine | GS-SHAP | SHAP-MMD8 | feat_spearman | 150 | +0.265 | 2.9e-12 | 3/3 | A better |
| g3 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.208 | 5.8e-21 | 0/3 | B better |
| g3 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.245 | 1.8e-10 | 0/3 | B better |
| g3 | timemachine | GS-SHAP | SHAP-U8 | feat_spearman | 150 | +0.281 | 9.1e-13 | 3/3 | A better |
| g3 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.211 | 2.9e-22 | 0/3 | B better |
| g3 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.247 | 7.2e-15 | 0/3 | B better |
| g3 | timemachine | SHAP-U8 | IG-U8 | feat_spearman | 150 | +0.021 | 6.8e-01 | 1/3 | no difference |
| g3 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.007 | 9.8e-02 | 3/3 | no difference |
| g3 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.010 | 1.0e+00 | 2/3 | no difference |
| weather | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.208 | 7.9e-22 | 0/3 | B better |
| weather | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.252 | 3.7e-24 | 0/3 | B better |
| weather | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.228 | 4.2e-22 | 0/3 | B better |
| weather | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.251 | 3.7e-24 | 0/3 | B better |
| weather | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.089 | 5.1e-08 | 3/3 | A better |
| weather | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.138 | 3.0e-18 | 3/3 | A better |
| weather | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.011 | 3.1e-01 | 2/3 | no difference |
| weather | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.040 | 1.7e-04 | 3/3 | A better |
| weather | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.014 | 3.5e-03 | 3/3 | A better |
| weather | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.071 | 1.1e-10 | 3/3 | A better |
| weather | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.002 | 1.0e+00 | 2/3 | no difference |
| weather | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.007 | 6.3e-03 | 3/3 | A better |
| weather | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.018 | 6.8e-01 | 0/3 | no difference |
| weather | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.007 | 1.0e+00 | 2/3 | no difference |
| weather | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.160 | 1.1e-19 | 0/3 | B better |
| weather | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.271 | 5.3e-21 | 0/3 | B better |
| weather | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.140 | 2.6e-19 | 0/3 | B better |
| weather | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.271 | 5.3e-19 | 0/3 | B better |
| weather | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.106 | 2.1e-14 | 3/3 | A better |
| weather | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.259 | 6.3e-20 | 3/3 | A better |
| weather | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.026 | 1.6e-04 | 2/3 | no difference |
| weather | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.016 | 1.3e-02 | 3/3 | A better |
| weather | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.033 | 2.1e-05 | 3/3 | A better |
| weather | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.051 | 5.0e-10 | 3/3 | A better |
| weather | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.221 | 7.5e-22 | 0/3 | B better |
| weather | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.224 | 3.7e-20 | 0/3 | B better |
| weather | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.229 | 3.1e-22 | 0/3 | B better |
| weather | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.230 | 1.4e-20 | 0/3 | B better |
| weather | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.067 | 8.3e-05 | 3/3 | A better |
| weather | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.142 | 3.9e-16 | 3/3 | A better |
| weather | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.033 | 6.2e-06 | 3/3 | A better |
| weather | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.064 | 3.2e-20 | 3/3 | A better |
| weather | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.040 | 7.7e-09 | 3/3 | A better |
| weather | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.078 | 2.1e-21 | 3/3 | A better |
| weather | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.217 | 7.7e-21 | 0/3 | B better |
| weather | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.195 | 6.3e-16 | 0/3 | B better |
| weather | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.219 | 3.0e-22 | 0/3 | B better |
| weather | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.192 | 1.5e-16 | 0/3 | B better |
| weather | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.018 | 9.4e-02 | 3/3 | no difference |
| weather | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.079 | 7.7e-09 | 3/3 | A better |
| weather_h192 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.214 | 5.5e-23 | 0/3 | B better |
| weather_h192 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.274 | 7.3e-22 | 0/3 | B better |
| weather_h192 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.202 | 5.5e-23 | 0/3 | B better |
| weather_h192 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.291 | 7.3e-22 | 0/3 | B better |
| weather_h192 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.056 | 2.9e-03 | 2/3 | no difference |
| weather_h192 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.138 | 9.7e-14 | 3/3 | A better |
| weather_h192 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.012 | 1.8e-02 | 2/3 | no difference |
| weather_h192 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.038 | 2.4e-05 | 3/3 | A better |
| weather_h192 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.017 | 3.1e-04 | 3/3 | A better |
| weather_h192 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.071 | 2.1e-11 | 3/3 | A better |
| weather_h192 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | +0.006 | 1.0e+00 | 3/3 | no difference |
| weather_h192 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.001 | 1.0e+00 | 1/3 | no difference |
| weather_h192 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.026 | 1.1e-01 | 1/3 | no difference |
| weather_h192 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.022 | 9.4e-04 | 3/3 | A better |
| weather_h192 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.275 | 2.9e-22 | 0/3 | B better |
| weather_h192 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.245 | 1.1e-15 | 0/3 | B better |
| weather_h192 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.243 | 5.7e-20 | 0/3 | B better |
| weather_h192 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.268 | 1.0e-17 | 0/3 | B better |
| weather_h192 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.229 | 1.1e-19 | 3/3 | A better |
| weather_h192 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.350 | 5.6e-22 | 3/3 | A better |
| weather_h192 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.006 | 2.0e-01 | 3/3 | no difference |
| weather_h192 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.003 | 8.6e-01 | 2/3 | no difference |
| weather_h192 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.016 | 1.7e-02 | 3/3 | A better |
| weather_h192 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.041 | 7.5e-10 | 3/3 | A better |
| weather_h192 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.208 | 2.6e-23 | 0/3 | B better |
| weather_h192 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.250 | 3.8e-19 | 0/3 | B better |
| weather_h192 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.177 | 1.3e-21 | 0/3 | B better |
| weather_h192 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.278 | 3.3e-20 | 0/3 | B better |
| weather_h192 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.020 | 8.6e-01 | 2/3 | no difference |
| weather_h192 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.209 | 1.2e-17 | 3/3 | A better |
| weather_h192 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.032 | 2.9e-06 | 3/3 | A better |
| weather_h192 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.029 | 1.4e-10 | 3/3 | A better |
| weather_h192 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.042 | 1.0e-09 | 3/3 | A better |
| weather_h192 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.048 | 6.3e-17 | 3/3 | A better |
| weather_h192 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.296 | 7.2e-25 | 0/3 | B better |
| weather_h192 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.212 | 9.7e-18 | 0/3 | B better |
| weather_h192 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.281 | 6.5e-24 | 0/3 | B better |
| weather_h192 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.218 | 3.2e-17 | 0/3 | B better |
| weather_h192 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.084 | 2.9e-06 | 3/3 | A better |
| weather_h192 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.057 | 2.4e-07 | 3/3 | A better |
| weather_h336 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.242 | 3.0e-24 | 0/3 | B better |
| weather_h336 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.295 | 5.3e-23 | 0/3 | B better |
| weather_h336 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.259 | 1.9e-22 | 0/3 | B better |
| weather_h336 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.301 | 9.3e-24 | 0/3 | B better |
| weather_h336 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.119 | 2.0e-07 | 3/3 | A better |
| weather_h336 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.122 | 7.6e-19 | 3/3 | A better |
| weather_h336 | plain | MambaLRP | IG | del_aopc_interp | 150 | +0.022 | 3.3e-03 | 3/3 | A better |
| weather_h336 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.036 | 6.6e-05 | 3/3 | A better |
| weather_h336 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.029 | 9.8e-05 | 3/3 | A better |
| weather_h336 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.068 | 2.3e-12 | 3/3 | A better |
| weather_h336 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.001 | 3.0e-01 | 2/3 | no difference |
| weather_h336 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | -0.001 | 3.0e-01 | 1/3 | no difference |
| weather_h336 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.012 | 1.3e-01 | 0/3 | no difference |
| weather_h336 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.008 | 2.7e-01 | 3/3 | no difference |
| weather_h336 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.373 | 1.5e-23 | 0/3 | B better |
| weather_h336 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.345 | 2.3e-21 | 0/3 | B better |
| weather_h336 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.361 | 2.2e-23 | 0/3 | B better |
| weather_h336 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.354 | 1.7e-21 | 0/3 | B better |
| weather_h336 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.314 | 2.3e-23 | 3/3 | A better |
| weather_h336 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.316 | 9.2e-23 | 3/3 | A better |
| weather_h336 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.050 | 7.8e-07 | 3/3 | A better |
| weather_h336 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.021 | 2.0e-02 | 3/3 | A better |
| weather_h336 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.055 | 7.8e-09 | 3/3 | A better |
| weather_h336 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.058 | 1.5e-09 | 3/3 | A better |
| weather_h336 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.250 | 3.6e-24 | 0/3 | B better |
| weather_h336 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.247 | 1.6e-17 | 0/3 | B better |
| weather_h336 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.215 | 1.9e-23 | 0/3 | B better |
| weather_h336 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.275 | 1.7e-20 | 0/3 | B better |
| weather_h336 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.084 | 7.8e-07 | 3/3 | A better |
| weather_h336 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.255 | 3.4e-22 | 3/3 | A better |
| weather_h336 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.030 | 2.0e-07 | 3/3 | A better |
| weather_h336 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.063 | 7.0e-16 | 3/3 | A better |
| weather_h336 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.036 | 2.8e-09 | 3/3 | A better |
| weather_h336 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.085 | 8.4e-19 | 3/3 | A better |
| weather_h336 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.289 | 6.3e-24 | 0/3 | B better |
| weather_h336 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.221 | 3.1e-18 | 0/3 | B better |
| weather_h336 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.264 | 1.0e-23 | 0/3 | B better |
| weather_h336 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.224 | 1.9e-18 | 0/3 | B better |
| weather_h336 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.048 | 1.6e-03 | 2/3 | no difference |
| weather_h336 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.092 | 3.6e-10 | 3/3 | A better |
| weather_h720 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.294 | 2.4e-24 | 0/3 | B better |
| weather_h720 | itransformer | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.300 | 3.0e-19 | 0/3 | B better |
| weather_h720 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.254 | 3.9e-23 | 0/3 | B better |
| weather_h720 | itransformer | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.270 | 9.8e-19 | 0/3 | B better |
| weather_h720 | itransformer | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.186 | 1.6e-13 | 3/3 | A better |
| weather_h720 | itransformer | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.261 | 5.7e-19 | 3/3 | A better |
| weather_h720 | plain | MambaLRP | IG | del_aopc_interp | 150 | -0.008 | 7.3e-01 | 0/3 | no difference |
| weather_h720 | plain | MambaLRP | IG | del_aopc_mean | 150 | +0.044 | 4.2e-07 | 3/3 | A better |
| weather_h720 | plain | MambaLRP | GxI | del_aopc_interp | 150 | +0.002 | 4.1e-02 | 3/3 | A better |
| weather_h720 | plain | MambaLRP | GxI | del_aopc_mean | 150 | +0.074 | 2.4e-12 | 3/3 | A better |
| weather_h720 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_interp | 150 | -0.005 | 1.0e+00 | 2/3 | no difference |
| weather_h720 | plain | SHAP-Δ8 | SHAP-U8 | del_aopc_mean | 150 | +0.001 | 1.0e+00 | 1/3 | no difference |
| weather_h720 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_interp | 150 | -0.007 | 1.0e+00 | 1/3 | no difference |
| weather_h720 | plain | SHAP-Δ8 | SHAP-MMD8 | del_aopc_mean | 150 | +0.006 | 1.8e-01 | 3/3 | no difference |
| weather_h720 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.343 | 2.0e-22 | 0/3 | B better |
| weather_h720 | plain | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.348 | 4.2e-20 | 0/3 | B better |
| weather_h720 | plain | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.341 | 3.4e-22 | 0/3 | B better |
| weather_h720 | plain | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.353 | 4.2e-20 | 0/3 | B better |
| weather_h720 | plain | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.293 | 5.6e-22 | 3/3 | A better |
| weather_h720 | plain | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.295 | 5.0e-21 | 3/3 | A better |
| weather_h720 | smamba | MambaLRP | IG | del_aopc_interp | 150 | +0.071 | 9.8e-11 | 3/3 | A better |
| weather_h720 | smamba | MambaLRP | IG | del_aopc_mean | 150 | +0.031 | 4.3e-03 | 2/3 | no difference |
| weather_h720 | smamba | MambaLRP | GxI | del_aopc_interp | 150 | +0.076 | 4.1e-12 | 3/3 | A better |
| weather_h720 | smamba | MambaLRP | GxI | del_aopc_mean | 150 | +0.049 | 1.0e-05 | 2/3 | no difference |
| weather_h720 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.241 | 6.5e-22 | 0/3 | B better |
| weather_h720 | smamba | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.199 | 7.8e-13 | 0/3 | B better |
| weather_h720 | smamba | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.220 | 1.9e-20 | 0/3 | B better |
| weather_h720 | smamba | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.230 | 9.4e-13 | 0/3 | B better |
| weather_h720 | smamba | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.114 | 3.8e-07 | 3/3 | A better |
| weather_h720 | smamba | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.285 | 6.5e-17 | 3/3 | A better |
| weather_h720 | timemachine | MambaLRP | IG | del_aopc_interp | 150 | +0.054 | 8.6e-08 | 3/3 | A better |
| weather_h720 | timemachine | MambaLRP | IG | del_aopc_mean | 150 | +0.050 | 6.6e-17 | 3/3 | A better |
| weather_h720 | timemachine | MambaLRP | GxI | del_aopc_interp | 150 | +0.057 | 1.3e-10 | 3/3 | A better |
| weather_h720 | timemachine | MambaLRP | GxI | del_aopc_mean | 150 | +0.071 | 4.2e-21 | 3/3 | A better |
| weather_h720 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_interp | 150 | -0.340 | 3.4e-25 | 0/3 | B better |
| weather_h720 | timemachine | GS-SHAP | SHAP-MMD8 | del_aopc_mean | 150 | -0.293 | 2.9e-22 | 0/3 | B better |
| weather_h720 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_interp | 150 | -0.345 | 4.2e-25 | 0/3 | B better |
| weather_h720 | timemachine | GS-SHAP | SHAP-U8 | del_aopc_mean | 150 | -0.299 | 5.4e-22 | 0/3 | B better |
| weather_h720 | timemachine | SHAP-U8 | IG-U8 | del_aopc_interp | 150 | +0.120 | 8.6e-08 | 3/3 | A better |
| weather_h720 | timemachine | SHAP-U8 | IG-U8 | del_aopc_mean | 150 | +0.100 | 1.9e-13 | 3/3 | A better |

## Verdict tally (A / = / B cells)

| A vs B | data | GT | del_aopc_mean | del_aopc_interp | A under both maskers |
|---|---|---|---|---|---|
| GS-SHAP vs SHAP-MMD8 | G1 | 0/0/4 | 0/0/4 | 0/1/3 | 0/4 |
| GS-SHAP vs SHAP-MMD8 | G2 | 10/2/0 | 3/1/8 | 9/2/1 | 3/12 |
| GS-SHAP vs SHAP-MMD8 | G3 | 4/0/0 | 0/0/4 | 0/0/4 | 0/4 |
| GS-SHAP vs SHAP-MMD8 | public | – | 0/0/8 | 0/0/8 | 0/8 |
| GS-SHAP vs SHAP-MMD8 | public v2.1 | – | 0/0/12 | 0/0/12 | 0/12 |
| GS-SHAP vs SHAP-MMD8 | public v2.2 horizon | – | 0/0/24 | 0/0/24 | 0/24 |
| GS-SHAP vs SHAP-U8 | G1 | 0/0/4 | 0/0/4 | 1/1/2 | 0/4 |
| GS-SHAP vs SHAP-U8 | G2 | 12/0/0 | 5/1/6 | 11/1/0 | 5/12 |
| GS-SHAP vs SHAP-U8 | G3 | 3/1/0 | 0/0/4 | 0/0/4 | 0/4 |
| GS-SHAP vs SHAP-U8 | public | – | 0/0/8 | 0/0/8 | 0/8 |
| GS-SHAP vs SHAP-U8 | public v2.1 | – | 0/0/12 | 0/0/12 | 0/12 |
| GS-SHAP vs SHAP-U8 | public v2.2 horizon | – | 0/0/24 | 0/0/24 | 0/24 |
| SHAP-U8 vs IG-U8 | G1 | 0/3/1 | 1/2/1 | 0/4/0 | 0/4 |
| SHAP-U8 vs IG-U8 | G2 | 0/5/7 | 3/7/2 | 0/2/10 | 0/12 |
| SHAP-U8 vs IG-U8 | G3 | 1/3/0 | 0/4/0 | 0/4/0 | 0/4 |
| SHAP-U8 vs IG-U8 | public | – | 8/0/0 | 3/2/3 | 3/8 |
| SHAP-U8 vs IG-U8 | public v2.1 | – | 5/3/4 | 1/7/4 | 1/12 |
| SHAP-U8 vs IG-U8 | public v2.2 horizon | – | 21/2/1 | 10/5/9 | 10/24 |
| MambaLRP vs IG | G1 | 0/2/1 | 1/2/0 | 0/3/0 | 0/3 |
| MambaLRP vs IG | G2 | 0/2/7 | 1/3/5 | 0/2/7 | 0/9 |
| MambaLRP vs IG | G3 | 1/2/0 | 0/3/0 | 2/1/0 | 0/3 |
| MambaLRP vs IG | public | – | 6/0/0 | 2/4/0 | 2/6 |
| MambaLRP vs IG | public v2.1 | – | 8/1/0 | 5/4/0 | 5/9 |
| MambaLRP vs IG | public v2.2 horizon | – | 15/3/0 | 9/9/0 | 8/18 |
| MambaLRP vs GxI | G1 | 0/1/2 | 1/1/1 | 0/3/0 | 0/3 |
| MambaLRP vs GxI | G2 | 6/1/2 | 5/4/0 | 8/1/0 | 5/9 |
| MambaLRP vs GxI | G3 | 1/2/0 | 0/3/0 | 3/0/0 | 0/3 |
| MambaLRP vs GxI | public | – | 6/0/0 | 4/2/0 | 4/6 |
| MambaLRP vs GxI | public v2.1 | – | 8/1/0 | 5/4/0 | 5/9 |
| MambaLRP vs GxI | public v2.2 horizon | – | 16/2/0 | 13/5/0 | 11/18 |
| SHAP-Δ8 vs SHAP-U8 | G1 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1 |
| SHAP-Δ8 vs SHAP-U8 | G2 | 0/3/0 | 0/3/0 | 0/3/0 | 0/3 |
| SHAP-Δ8 vs SHAP-U8 | G3 | 0/0/1 | 0/1/0 | 0/1/0 | 0/1 |
| SHAP-Δ8 vs SHAP-U8 | public | – | 1/1/0 | 0/2/0 | 0/2 |
| SHAP-Δ8 vs SHAP-U8 | public v2.1 | – | 0/3/0 | 0/3/0 | 0/3 |
| SHAP-Δ8 vs SHAP-U8 | public v2.2 horizon | – | 0/5/1 | 0/6/0 | 0/6 |
| SHAP-Δ8 vs SHAP-MMD8 | G1 | 0/0/1 | 0/0/1 | 0/0/1 | 0/1 |
| SHAP-Δ8 vs SHAP-MMD8 | G2 | 0/0/3 | 0/0/3 | 0/2/1 | 0/3 |
| SHAP-Δ8 vs SHAP-MMD8 | G3 | 0/1/0 | 0/1/0 | 0/1/0 | 0/1 |
| SHAP-Δ8 vs SHAP-MMD8 | public | – | 1/1/0 | 0/2/0 | 0/2 |
| SHAP-Δ8 vs SHAP-MMD8 | public v2.1 | – | 0/3/0 | 1/2/0 | 0/3 |
| SHAP-Δ8 vs SHAP-MMD8 | public v2.2 horizon | – | 3/3/0 | 0/5/1 | 0/6 |

v2: deletion verdict differs between maskers in 58/140 comparisons; opposite significant verdicts (A under one masker, B under the other) in 18/140.

v2.1 replication: deletion verdict differs between maskers in 14/60 comparisons; opposite significant verdicts (A under one masker, B under the other) in 1/60.

v2.2 horizon: deletion verdict differs between maskers in 33/120 comparisons; opposite significant verdicts (A under one masker, B under the other) in 6/120.

## Average rank over 28 v2 cells (primary metric; 1 = best)

| method | mean rank | cells |
|---|---|---|
| IG-U16 | 4.36 | 28 |
| SHAP-MMD8 | 4.79 | 28 |
| IG-U8 | 5.43 | 28 |
| GS-SHAP | 5.71 | 28 |
| IG | 6.29 | 28 |
| SHAP-U8 | 6.32 | 28 |
| SHAP-U16 | 6.50 | 28 |
| SHAP-Δ8 | 7.00 | 7 |
| MambaLRP | 7.19 | 21 |
| SHAP-U4 | 7.36 | 28 |
| IG-U4 | 7.54 | 28 |
| GxI | 7.93 | 28 |
| SHAP-C | 8.89 | 28 |
| Random | 13.00 | 28 |

Friedman over the 12 general methods present in every cell: p = 2.73e-17
MambaLRP rank in Mamba cells: mean 7.19 vs IG 6.69 (21 cells)

## Average rank over 40 cells (v2 + v2.1 replication) (primary metric; 1 = best)

| method | mean rank | cells |
|---|---|---|
| IG-U16 | 5.03 | 40 |
| IG-U8 | 5.05 | 40 |
| SHAP-MMD8 | 5.22 | 40 |
| SHAP-U8 | 6.10 | 40 |
| IG-U4 | 6.17 | 40 |
| SHAP-U4 | 6.17 | 40 |
| SHAP-Δ8 | 6.20 | 10 |
| SHAP-C | 6.67 | 40 |
| SHAP-U16 | 7.20 | 40 |
| IG | 7.38 | 40 |
| GS-SHAP | 7.55 | 40 |
| MambaLRP | 7.57 | 30 |
| GxI | 8.47 | 40 |
| Random | 13.00 | 40 |

Friedman over the 12 general methods present in every cell: p = 1.13e-22
MambaLRP rank in Mamba cells: mean 7.57 vs IG 7.68 (30 cells)

## Masker dependence (RQ2): Kendall tau between method rankings

| task | model | GT metric | tau(del_mean, del_interp) | tau(GT, del_mean) | tau(GT, del_interp) | best by GT | best by del_mean | best by del_interp |
|---|---|---|---|---|---|---|---|---|
| etth1 | itransformer | – | -0.345 | nan | nan | – | GxI | IG-U4 |
| etth1 | plain | – | -0.179 | nan | nan | – | SHAP-U16 | SHAP-C |
| etth1 | smamba | – | -0.182 | nan | nan | – | MambaLRP | IG-U4 |
| etth1 | timemachine | – | -0.424 | nan | nan | – | MambaLRP | SHAP-U4 |
| etth1_h192 | itransformer | – | -0.091 | nan | nan | – | SHAP-U8 | IG-U4 |
| etth1_h192 | plain | – | -0.103 | nan | nan | – | MambaLRP | IG-U4 |
| etth1_h192 | smamba | – | -0.212 | nan | nan | – | SHAP-U8 | IG-U8 |
| etth1_h192 | timemachine | – | 0.121 | nan | nan | – | MambaLRP | SHAP-U4 |
| etth1_h336 | itransformer | – | -0.091 | nan | nan | – | SHAP-MMD8 | IG-U4 |
| etth1_h336 | plain | – | 0.333 | nan | nan | – | MambaLRP | SHAP-C |
| etth1_h336 | smamba | – | 0.121 | nan | nan | – | SHAP-U4 | SHAP-U4 |
| etth1_h336 | timemachine | – | 0.333 | nan | nan | – | SHAP-MMD8 | SHAP-U4 |
| etth1_h720 | itransformer | – | -0.345 | nan | nan | – | SHAP-U8 | IG-U4 |
| etth1_h720 | plain | – | 0.000 | nan | nan | – | MambaLRP | SHAP-C |
| etth1_h720 | smamba | – | 0.030 | nan | nan | – | SHAP-MMD8 | SHAP-U4 |
| etth1_h720 | timemachine | – | 0.485 | nan | nan | – | SHAP-MMD8 | SHAP-U4 |
| etth2 | itransformer | – | -0.309 | nan | nan | – | IG | SHAP-U4 |
| etth2 | plain | – | 0.590 | nan | nan | – | SHAP-U4 | SHAP-C |
| etth2 | smamba | – | -0.152 | nan | nan | – | MambaLRP | SHAP-C |
| etth2 | timemachine | – | 0.182 | nan | nan | – | MambaLRP | IG-U8 |
| ettm1 | itransformer | – | -0.164 | nan | nan | – | GxI | SHAP-C |
| ettm1 | plain | – | 0.128 | nan | nan | – | MambaLRP | SHAP-C |
| ettm1 | smamba | – | -0.030 | nan | nan | – | MambaLRP | SHAP-C |
| ettm1 | timemachine | – | -0.485 | nan | nan | – | MambaLRP | SHAP-C |
| exchange | itransformer | – | -0.455 | nan | nan | – | IG | SHAP-U4 |
| exchange | plain | – | 0.385 | nan | nan | – | SHAP-U16 | SHAP-C |
| exchange | smamba | – | -0.061 | nan | nan | – | IG | SHAP-C |
| exchange | timemachine | – | -0.364 | nan | nan | – | MambaLRP | SHAP-C |
| g1 | itransformer | ap | 0.709 | 0.964 | 0.745 | GxI | GxI | IG-U16 |
| g1 | plain | ap | 0.026 | 0.769 | -0.205 | IG | GxI | SHAP-MMD8 |
| g1 | smamba | ap | 0.121 | 0.818 | 0.121 | GxI | MambaLRP | SHAP-U8 |
| g1 | timemachine | ap | 0.030 | 0.788 | 0.000 | IG | GxI | SHAP-MMD8 |
| g2a | itransformer | ap | 0.055 | 0.600 | 0.018 | IG-U16 | GS-SHAP | GS-SHAP |
| g2a | plain | ap | -0.051 | 0.487 | 0.359 | GS-SHAP | MambaLRP | IG-U16 |
| g2a | smamba | ap | 0.364 | 0.576 | 0.606 | GS-SHAP | SHAP-MMD8 | GS-SHAP |
| g2a | timemachine | ap | 0.394 | 0.606 | 0.667 | SHAP-MMD8 | IG | SHAP-MMD8 |
| g2b | itransformer | ap | 0.345 | 0.745 | 0.236 | GS-SHAP | GS-SHAP | IG-U4 |
| g2b | plain | ap | -0.231 | 0.410 | 0.359 | GS-SHAP | MambaLRP | GS-SHAP |
| g2b | smamba | ap | -0.061 | 0.424 | 0.333 | GS-SHAP | SHAP-MMD8 | IG-U16 |
| g2b | timemachine | ap | 0.242 | 0.515 | 0.424 | GS-SHAP | SHAP-MMD8 | GS-SHAP |
| g2c | itransformer | ap | 0.164 | 0.782 | 0.091 | IG-U16 | IG-U16 | GS-SHAP |
| g2c | plain | ap | -0.128 | 0.359 | 0.462 | GS-SHAP | MambaLRP | GS-SHAP |
| g2c | smamba | ap | 0.333 | 0.424 | 0.485 | GS-SHAP | IG | GS-SHAP |
| g2c | timemachine | ap | 0.667 | 0.697 | 0.667 | GS-SHAP | IG | IG-U16 |
| g3 | itransformer | feat_spearman | 0.164 | -0.135 | -0.405 | GS-SHAP | GxI | SHAP-MMD8 |
| g3 | plain | feat_spearman | 0.051 | -0.080 | -0.374 | GS-SHAP | MambaLRP | SHAP-MMD8 |
| g3 | smamba | feat_spearman | 0.030 | 0.064 | 0.064 | GS-SHAP | GxI | SHAP-MMD8 |
| g3 | timemachine | feat_spearman | 0.000 | 0.000 | 0.286 | GS-SHAP | IG | SHAP-U8 |
| weather | itransformer | – | 0.236 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather | plain | – | 0.641 | nan | nan | – | SHAP-Δ8 | SHAP-C |
| weather | smamba | – | 0.273 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather | timemachine | – | 0.273 | nan | nan | – | SHAP-U4 | SHAP-C |
| weather_h192 | itransformer | – | 0.273 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather_h192 | plain | – | 0.538 | nan | nan | – | SHAP-U8 | SHAP-C |
| weather_h192 | smamba | – | 0.273 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather_h192 | timemachine | – | 0.424 | nan | nan | – | SHAP-U4 | SHAP-C |
| weather_h336 | itransformer | – | 0.309 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather_h336 | plain | – | 0.667 | nan | nan | – | SHAP-U8 | SHAP-C |
| weather_h336 | smamba | – | 0.242 | nan | nan | – | SHAP-U16 | SHAP-C |
| weather_h336 | timemachine | – | 0.515 | nan | nan | – | SHAP-U4 | SHAP-C |
| weather_h720 | itransformer | – | 0.745 | nan | nan | – | SHAP-U4 | SHAP-C |
| weather_h720 | plain | – | 0.564 | nan | nan | – | SHAP-Δ8 | SHAP-C |
| weather_h720 | smamba | – | 0.455 | nan | nan | – | SHAP-U4 | SHAP-C |
| weather_h720 | timemachine | – | 0.576 | nan | nan | – | SHAP-U4 | SHAP-C |

## Resolution vs estimator (RQ4): primary metric

| task | model | IG | IG-U4 | SHAP-U4 | IG-U8 | SHAP-U8 | IG-U16 | SHAP-U16 | SHAP-C |
|---|---|---|---|---|---|---|---|---|---|
| etth1 | itransformer | 0.172 | 0.540 | 0.433 | 0.526 | 0.335 | 0.479 | 0.115 | 0.533 |
| etth1 | plain | 0.084 | 0.483 | 0.410 | 0.407 | 0.176 | 0.274 | 0.085 | 0.523 |
| etth1 | smamba | 0.326 | 0.550 | 0.471 | 0.538 | 0.372 | 0.475 | 0.137 | 0.534 |
| etth1 | timemachine | 0.319 | 0.545 | 0.549 | 0.516 | 0.473 | 0.483 | 0.409 | 0.531 |
| etth1_h192 | itransformer | 0.212 | 0.554 | 0.470 | 0.545 | 0.344 | 0.503 | 0.172 | 0.535 |
| etth1_h192 | plain | 0.087 | 0.529 | 0.205 | 0.385 | 0.130 | 0.267 | 0.072 | 0.520 |
| etth1_h192 | smamba | 0.402 | 0.552 | 0.549 | 0.556 | 0.338 | 0.527 | 0.297 | 0.534 |
| etth1_h192 | timemachine | 0.347 | 0.550 | 0.560 | 0.521 | 0.536 | 0.500 | 0.343 | 0.533 |
| etth1_h336 | itransformer | 0.228 | 0.556 | 0.496 | 0.535 | 0.341 | 0.502 | 0.117 | 0.534 |
| etth1_h336 | plain | 0.066 | 0.506 | 0.137 | 0.349 | 0.067 | 0.241 | 0.051 | 0.532 |
| etth1_h336 | smamba | 0.436 | 0.554 | 0.558 | 0.542 | 0.362 | 0.541 | 0.226 | 0.532 |
| etth1_h336 | timemachine | 0.345 | 0.542 | 0.565 | 0.520 | 0.546 | 0.496 | 0.432 | 0.533 |
| etth1_h720 | itransformer | 0.260 | 0.548 | 0.478 | 0.526 | 0.463 | 0.509 | 0.173 | 0.521 |
| etth1_h720 | plain | 0.068 | 0.416 | 0.163 | 0.299 | 0.100 | 0.188 | 0.075 | 0.483 |
| etth1_h720 | smamba | 0.425 | 0.542 | 0.547 | 0.544 | 0.421 | 0.524 | 0.182 | 0.525 |
| etth1_h720 | timemachine | 0.360 | 0.542 | 0.553 | 0.516 | 0.547 | 0.481 | 0.412 | 0.520 |
| etth2 | itransformer | 0.117 | 0.326 | 0.444 | 0.291 | 0.326 | 0.221 | 0.222 | 0.444 |
| etth2 | plain | 0.116 | 0.155 | 0.186 | 0.153 | 0.195 | 0.126 | 0.178 | 0.424 |
| etth2 | smamba | 0.181 | 0.431 | 0.420 | 0.374 | 0.411 | 0.287 | 0.250 | 0.440 |
| etth2 | timemachine | 0.307 | 0.455 | 0.440 | 0.469 | 0.465 | 0.422 | 0.348 | 0.437 |
| ettm1 | itransformer | 0.129 | 0.533 | 0.365 | 0.483 | 0.109 | 0.349 | 0.059 | 0.536 |
| ettm1 | plain | 0.066 | 0.444 | 0.350 | 0.358 | 0.093 | 0.234 | 0.058 | 0.537 |
| ettm1 | smamba | 0.225 | 0.519 | 0.323 | 0.474 | 0.168 | 0.422 | 0.056 | 0.538 |
| ettm1 | timemachine | 0.213 | 0.481 | 0.401 | 0.469 | 0.254 | 0.389 | 0.150 | 0.534 |
| exchange | itransformer | 0.187 | 0.514 | 0.735 | 0.407 | 0.366 | 0.318 | 0.204 | 0.707 |
| exchange | plain | 0.104 | 0.153 | 0.387 | 0.148 | 0.173 | 0.113 | 0.155 | 0.711 |
| exchange | smamba | 0.392 | 0.709 | 0.634 | 0.634 | 0.500 | 0.571 | 0.163 | 0.710 |
| exchange | timemachine | 0.191 | 0.556 | 0.500 | 0.454 | 0.549 | 0.385 | 0.308 | 0.706 |
| g1 | itransformer | 0.801 | 0.233 | 0.209 | 0.296 | 0.275 | 0.414 | 0.362 | 0.087 |
| g1 | plain | 0.895 | 0.254 | 0.257 | 0.323 | 0.317 | 0.454 | 0.445 | 0.106 |
| g1 | smamba | 0.896 | 0.302 | 0.297 | 0.386 | 0.385 | 0.530 | 0.530 | 0.123 |
| g1 | timemachine | 0.881 | 0.307 | 0.305 | 0.396 | 0.397 | 0.534 | 0.538 | 0.128 |
| g2a | itransformer | 0.830 | 0.612 | 0.572 | 0.856 | 0.782 | 0.902 | 0.795 | 0.190 |
| g2a | plain | 0.874 | 0.626 | 0.627 | 0.865 | 0.864 | 0.917 | 0.897 | 0.200 |
| g2a | smamba | 0.657 | 0.483 | 0.460 | 0.655 | 0.623 | 0.680 | 0.629 | 0.166 |
| g2a | timemachine | 0.921 | 0.628 | 0.618 | 0.880 | 0.857 | 0.934 | 0.913 | 0.200 |
| g2b | itransformer | 0.852 | 0.674 | 0.662 | 0.882 | 0.824 | 0.940 | 0.785 | 0.200 |
| g2b | plain | 0.867 | 0.670 | 0.674 | 0.876 | 0.860 | 0.910 | 0.865 | 0.200 |
| g2b | smamba | 0.609 | 0.505 | 0.514 | 0.615 | 0.605 | 0.643 | 0.572 | 0.171 |
| g2b | timemachine | 0.873 | 0.670 | 0.661 | 0.864 | 0.841 | 0.922 | 0.893 | 0.199 |
| g2c | itransformer | 0.734 | 0.586 | 0.477 | 0.804 | 0.642 | 0.819 | 0.633 | 0.180 |
| g2c | plain | 0.796 | 0.581 | 0.591 | 0.813 | 0.816 | 0.847 | 0.822 | 0.197 |
| g2c | smamba | 0.651 | 0.517 | 0.523 | 0.719 | 0.706 | 0.733 | 0.691 | 0.181 |
| g2c | timemachine | 0.895 | 0.604 | 0.606 | 0.858 | 0.855 | 0.918 | 0.889 | 0.198 |
| g3 | itransformer | 0.379 | 0.379 | 0.382 | 0.379 | 0.378 | 0.379 | 0.356 | 0.367 |
| g3 | plain | 0.386 | 0.386 | 0.369 | 0.386 | 0.386 | 0.386 | 0.351 | 0.347 |
| g3 | smamba | 0.198 | 0.198 | 0.313 | 0.198 | 0.280 | 0.198 | 0.325 | 0.194 |
| g3 | timemachine | 0.250 | 0.250 | 0.263 | 0.250 | 0.271 | 0.250 | 0.278 | 0.237 |
| weather | itransformer | 0.104 | 0.309 | 0.484 | 0.243 | 0.332 | 0.183 | 0.223 | 0.551 |
| weather | plain | 0.072 | 0.201 | 0.305 | 0.127 | 0.233 | 0.101 | 0.183 | 0.549 |
| weather | smamba | 0.128 | 0.315 | 0.421 | 0.245 | 0.312 | 0.213 | 0.233 | 0.526 |
| weather | timemachine | 0.126 | 0.367 | 0.471 | 0.299 | 0.316 | 0.246 | 0.262 | 0.543 |
| weather_h192 | itransformer | 0.113 | 0.312 | 0.494 | 0.234 | 0.290 | 0.200 | 0.213 | 0.552 |
| weather_h192 | plain | 0.078 | 0.177 | 0.461 | 0.130 | 0.359 | 0.102 | 0.289 | 0.577 |
| weather_h192 | smamba | 0.120 | 0.282 | 0.510 | 0.233 | 0.253 | 0.207 | 0.189 | 0.548 |
| weather_h192 | timemachine | 0.131 | 0.358 | 0.501 | 0.291 | 0.374 | 0.227 | 0.306 | 0.553 |
| weather_h336 | itransformer | 0.111 | 0.330 | 0.508 | 0.218 | 0.337 | 0.181 | 0.193 | 0.580 |
| weather_h336 | plain | 0.085 | 0.156 | 0.533 | 0.118 | 0.432 | 0.088 | 0.373 | 0.586 |
| weather_h336 | smamba | 0.099 | 0.275 | 0.490 | 0.200 | 0.283 | 0.174 | 0.168 | 0.570 |
| weather_h336 | timemachine | 0.114 | 0.347 | 0.515 | 0.300 | 0.347 | 0.226 | 0.262 | 0.595 |
| weather_h720 | itransformer | 0.071 | 0.236 | 0.567 | 0.154 | 0.341 | 0.122 | 0.257 | 0.594 |
| weather_h720 | plain | 0.099 | 0.193 | 0.508 | 0.133 | 0.427 | 0.109 | 0.378 | 0.539 |
| weather_h720 | smamba | 0.093 | 0.228 | 0.527 | 0.188 | 0.302 | 0.157 | 0.206 | 0.612 |
| weather_h720 | timemachine | 0.104 | 0.358 | 0.515 | 0.288 | 0.407 | 0.238 | 0.367 | 0.570 |
