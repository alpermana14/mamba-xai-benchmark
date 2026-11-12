# v2.2 B: estimator budget (pre-registered 2026-11-08)

B1: SHAP-U8 (4x samples) not better than IG-U8 (32 steps) in 16/16 cells (pass if >= 14 of 16): PASS
verdicts: {'no difference': 10, 'B better': 6}

| task | model | n | mean(SHAP-U8 x4 − IG-U8) | p | verdict |
|---|---|---|---|---|---|
| g1 | itransformer | 124 | -0.018 | 6.2e-03 | B better |
| g1 | plain | 124 | -0.004 | 2.3e-01 | no difference |
| g1 | smamba | 124 | -0.000 | 5.7e-01 | no difference |
| g1 | timemachine | 124 | +0.001 | 1.7e-01 | no difference |
| g2a | itransformer | 150 | -0.038 | 7.1e-08 | B better |
| g2a | plain | 150 | +0.008 | 1.2e-02 | no difference |
| g2a | smamba | 150 | -0.017 | 2.1e-02 | no difference |
| g2a | timemachine | 150 | -0.022 | 1.6e-10 | B better |
| g2b | itransformer | 150 | -0.013 | 7.6e-13 | B better |
| g2b | plain | 150 | +0.003 | 6.6e-01 | no difference |
| g2b | smamba | 150 | +0.026 | 1.3e-04 | no difference |
| g2b | timemachine | 150 | -0.017 | 2.5e-16 | B better |
| g2c | itransformer | 150 | -0.092 | 7.0e-12 | B better |
| g2c | plain | 150 | +0.013 | 6.2e-02 | no difference |
| g2c | smamba | 150 | +0.002 | 2.4e-01 | no difference |
| g2c | timemachine | 150 | +0.004 | 4.2e-01 | no difference |

Mean AP change (high budget − default), windows pooled over models and seeds

| method | g1 | g2a | g2b | g2c |
|---|---|---|---|---|
| IG | +0.0000 | +0.0001 | +0.0000 | -0.0002 |
| IG-U4 | +0.0000 | -0.0001 | -0.0000 | -0.0002 |
| IG-U8 | +0.0001 | -0.0001 | -0.0000 | -0.0000 |
| IG-U16 | +0.0000 | -0.0001 | -0.0000 | -0.0004 |
| SHAP-U4 | +0.0014 | +0.0040 | +0.0046 | +0.0115 |
| SHAP-U8 | +0.0018 | +0.0156 | +0.0265 | +0.0254 |
| SHAP-U16 | +0.0040 | +0.0330 | +0.0592 | +0.0500 |

Map convergence: median Spearman between default and high-budget maps (seed 0, first 10 explained windows per cell)

| method | g1 | g2a | g2b | g2c |
|---|---|---|---|---|
| IG-U8 | 1.000 | 1.000 | 1.000 | 1.000 |
| SHAP-U8 | 0.851 | 0.517 | 0.622 | 0.477 |
