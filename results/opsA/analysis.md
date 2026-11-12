# Opsi A: RQ1 and RQ2 on the official S-Mamba and TimeMachine (H = 96)

Pre-registered 2026-11-11 (plan §12). Operationalisation in the docstring of `scripts/opsA_analyze.py`.

## Runs and inclusion

| task | model | seed | test MSE | paper | ratio | included | params |
|---|---|---|---|---|---|---|---|
| etth1 | S-Mamba | 0 | 0.3864 | 0.386 | 1.001 | True | 1,150,624 |
| etth1 | S-Mamba | 1 | 0.3885 | 0.386 | 1.006 | True | 1,150,624 |
| etth1 | S-Mamba | 2 | 0.3858 | 0.386 | 0.999 | True | 1,150,624 |
| etth1 | TimeMachine | 0 | 0.3696 | 0.364 | 1.016 | True | 1,425,858 |
| etth1 | TimeMachine | 1 | 0.3720 | 0.364 | 1.022 | True | 1,425,858 |
| etth1 | TimeMachine | 2 | 0.3714 | 0.364 | 1.020 | True | 1,425,858 |
| weather | S-Mamba | 0 | 0.1668 | 0.165 | 1.011 | True | 6,638,400 |
| weather | S-Mamba | 1 | 0.1641 | 0.165 | 0.994 | True | 6,638,400 |
| weather | S-Mamba | 2 | 0.1644 | 0.165 | 0.996 | True | 6,638,400 |
| weather | TimeMachine | 0 | 0.1610 | 0.164 | 0.982 | True | 206,238 |
| weather | TimeMachine | 1 | 0.1650 | 0.164 | 1.006 | True | 206,238 |
| weather | TimeMachine | 2 | 0.1638 | 0.164 | 0.999 | True | 206,238 |

## HA1: MambaLRP − IG, deletion AOPC (higher = more faithful)

| task | model | masker | n | mean diff (official) | per seed | p_holm | passes | zoo diff | zoo verdict |
|---|---|---|---|---|---|---|---|---|---|
| etth1 | S-Mamba | mean | 150 | -0.0159 | {0: -0.0139, 1: -0.0197, 2: -0.0142} | 1.1e-06 | False | +0.0282 | A better |
| etth1 | S-Mamba | interp | 150 | +0.0135 | {0: 0.0411, 1: 0.0062, 2: -0.0068} | 1.0e+00 | False | +0.0333 | no difference |
| etth1 | TimeMachine | mean | 150 | -0.0209 | {0: -0.021, 1: -0.0242, 2: -0.0177} | 9.4e-19 | False | +0.0548 | A better |
| etth1 | TimeMachine | interp | 150 | -0.0005 | {0: 0.0019, 1: -0.0005, 2: -0.003} | 1.0e+00 | False | +0.0464 | A better |
| weather | S-Mamba | mean | 150 | +0.0005 | {0: -0.0003, 1: 0.0019, 2: -0.0002} | 5.5e-01 | False | +0.0156 | A better |
| weather | S-Mamba | interp | 150 | +0.0018 | {0: 0.0013, 1: 0.0016, 2: 0.0024} | 3.3e-02 | True | +0.0258 | no difference |
| weather | TimeMachine | mean | 150 | +0.0001 | {0: -0.0001, 1: 0.0001, 2: 0.0004} | 5.5e-01 | False | +0.0641 | A better |
| weather | TimeMachine | interp | 150 | -0.0002 | {0: -0.0003, 1: 0.0, 2: -0.0002} | 9.8e-01 | False | +0.0328 | A better |

**HA1 verdict: 0/4 confirmatory cells pass (FAIL; criterion >= 3/4).**

## HA2 (rankings differ between maskers) and HA3 (SHAP-C gains under interpolation)

| task | model | tau(mean, interp) | best mean | best interp | SHAP-C rank mean → interp | zoo tau | zoo best mean → interp |
|---|---|---|---|---|---|---|---|
| etth1 | S-Mamba | +0.487 | SHAP-U4 | IG-U4 | 11 → 2 | -0.182 | MambaLRP → IG-U4 |
| etth1 | TimeMachine | +0.359 | SHAP-MMD8 | SHAP-U4 | 11 → 8 | -0.424 | MambaLRP → SHAP-U4 |
| weather | S-Mamba | +0.564 | SHAP-U16 | SHAP-C | 5 → 1 | +0.273 | SHAP-U16 → SHAP-C |
| weather | TimeMachine | +0.000 | SHAP-U8 | SHAP-U4 | 9 → 8 | +0.273 | SHAP-U4 → SHAP-C |

**HA2 verdict: best differs in 4/4, median tau +0.423 (PASS; criterion >= 3/4 and median tau < 0.5).**

**HA3 verdict: SHAP-C better under interp in 4/4 (PASS; criterion 4/4).**

## Method means per cell (3 seeds pooled)

### etth1 · S-Mamba

| method    |   del_aopc_mean |   del_aopc_interp |   ins_aopc_mean |   ins_aopc_interp |   n_evals |   seconds |
|:----------|----------------:|------------------:|----------------:|------------------:|----------:|----------:|
| Random    |           0.192 |             0.003 |           1.129 |             0.059 |     0.000 |     0.000 |
| GxI       |           0.940 |             0.204 |           0.358 |             0.018 |     1.000 |     0.012 |
| IG        |           0.940 |             0.199 |           0.358 |             0.018 |    32.000 |     0.011 |
| IG-U4     |           1.052 |             0.569 |           0.213 |             0.026 |    32.000 |     0.011 |
| IG-U8     |           0.990 |             0.511 |           0.275 |             0.024 |    32.000 |     0.011 |
| IG-U16    |           0.963 |             0.451 |           0.328 |             0.023 |    32.000 |     0.011 |
| SHAP-C    |           0.847 |             0.540 |           0.491 |             0.015 |   129.000 |     0.015 |
| SHAP-U4   |           1.099 |             0.523 |           0.183 |             0.023 |  2051.000 |     0.047 |
| SHAP-U8   |           1.090 |             0.471 |           0.176 |             0.024 |  2051.000 |     0.051 |
| SHAP-U16  |           1.093 |             0.328 |           0.182 |             0.023 |  2051.000 |     0.047 |
| SHAP-MMD8 |           1.095 |             0.491 |           0.184 |             0.026 |  2051.000 |     0.098 |
| GS-SHAP   |           0.598 |             0.049 |           0.614 |             0.041 |  1498.353 |     0.877 |
| MambaLRP  |           0.924 |             0.212 |           0.368 |             0.018 |     1.000 |     0.015 |

### etth1 · TimeMachine

| method    |   del_aopc_mean |   del_aopc_interp |   ins_aopc_mean |   ins_aopc_interp |   n_evals |   seconds |
|:----------|----------------:|------------------:|----------------:|------------------:|----------:|----------:|
| Random    |           0.212 |             0.003 |           1.142 |             0.056 |     0.000 |     0.000 |
| GxI       |           0.899 |             0.544 |           0.440 |             0.014 |     1.000 |     0.013 |
| IG        |           0.898 |             0.544 |           0.441 |             0.015 |    32.000 |     0.105 |
| IG-U4     |           0.979 |             0.564 |           0.357 |             0.035 |    32.000 |     0.100 |
| IG-U8     |           0.976 |             0.560 |           0.294 |             0.024 |    32.000 |     0.100 |
| IG-U16    |           0.920 |             0.553 |           0.393 |             0.019 |    32.000 |     0.078 |
| SHAP-C    |           0.872 |             0.530 |           0.481 |             0.009 |   129.000 |     0.124 |
| SHAP-U4   |           1.068 |             0.569 |           0.248 |             0.023 |  2051.000 |     1.915 |
| SHAP-U8   |           1.072 |             0.232 |           0.219 |             0.025 |  2051.000 |     2.004 |
| SHAP-U16  |           1.082 |             0.214 |           0.234 |             0.023 |  2051.000 |     2.005 |
| SHAP-MMD8 |           1.108 |             0.474 |           0.209 |             0.024 |  2051.000 |     2.002 |
| GS-SHAP   |           0.666 |             0.046 |           0.641 |             0.046 |  1498.353 |     1.913 |
| MambaLRP  |           0.877 |             0.543 |           0.459 |             0.016 |     1.000 |     0.097 |

### weather · S-Mamba

| method    |   del_aopc_mean |   del_aopc_interp |   ins_aopc_mean |   ins_aopc_interp |   n_evals |   seconds |
|:----------|----------------:|------------------:|----------------:|------------------:|----------:|----------:|
| Random    |           0.011 |             0.000 |           0.062 |             0.011 |     0.000 |     0.000 |
| GxI       |           0.039 |             0.005 |           0.029 |             0.018 |     1.000 |     0.015 |
| IG        |           0.042 |             0.005 |           0.026 |             0.013 |    32.000 |     0.015 |
| IG-U4     |           0.038 |             0.025 |           0.030 |             0.025 |    32.000 |     0.015 |
| IG-U8     |           0.041 |             0.020 |           0.027 |             0.021 |    32.000 |     0.015 |
| IG-U16    |           0.044 |             0.016 |           0.025 |             0.017 |    32.000 |     0.015 |
| SHAP-C    |           0.061 |             0.056 |           0.009 |             0.005 |  2051.000 |     0.163 |
| SHAP-U4   |           0.066 |             0.055 |           0.007 |             0.005 |  2051.000 |     0.171 |
| SHAP-U8   |           0.067 |             0.044 |           0.007 |             0.005 |  2691.000 |     0.229 |
| SHAP-U16  |           0.068 |             0.032 |           0.006 |             0.004 |  5379.000 |     0.437 |
| SHAP-MMD8 |           0.067 |             0.041 |           0.007 |             0.004 |  2691.000 |     0.305 |
| GS-SHAP   |           0.035 |             0.005 |           0.030 |             0.010 |  1496.447 |     0.927 |
| MambaLRP  |           0.042 |             0.007 |           0.026 |             0.015 |     1.000 |     0.034 |

### weather · TimeMachine

| method    |   del_aopc_mean |   del_aopc_interp |   ins_aopc_mean |   ins_aopc_interp |   n_evals |   seconds |
|:----------|----------------:|------------------:|----------------:|------------------:|----------:|----------:|
| Random    |           0.012 |             0.000 |           0.065 |             0.011 |     0.000 |     0.000 |
| GxI       |           0.070 |             0.064 |           0.005 |             0.000 |     1.000 |     0.015 |
| IG        |           0.070 |             0.064 |           0.005 |             0.000 |    32.000 |     0.066 |
| IG-U4     |           0.068 |             0.064 |           0.006 |             0.001 |    32.000 |     0.069 |
| IG-U8     |           0.069 |             0.064 |           0.006 |             0.001 |    32.000 |     0.068 |
| IG-U16    |           0.070 |             0.064 |           0.005 |             0.001 |    32.000 |     0.070 |
| SHAP-C    |           0.070 |             0.063 |           0.007 |             0.000 |  2051.000 |     1.580 |
| SHAP-U4   |           0.071 |             0.065 |           0.003 |             0.001 |  2051.000 |     1.549 |
| SHAP-U8   |           0.072 |             0.054 |           0.003 |             0.001 |  2691.000 |     2.123 |
| SHAP-U16  |           0.071 |             0.034 |           0.003 |             0.000 |  5379.000 |     4.103 |
| SHAP-MMD8 |           0.072 |             0.053 |           0.003 |             0.001 |  2691.000 |     2.132 |
| GS-SHAP   |           0.034 |             0.007 |           0.031 |             0.009 |  1496.447 |     1.649 |
| MambaLRP  |           0.070 |             0.064 |           0.005 |             0.000 |     1.000 |     0.035 |

