# v2.1 replication: masker dependence (pre-registered 2026-11-04)

## Confirmatory: new cells (12 cells)

| hypothesis | result | passes |
|---|---|---|
| M1 | median tau -0.106; best differs 12/12 | yes |
| M2 | SHAP-C ranks better under interp in 12/12 (sign test p = 2.4e-04) | yes |
| M3 | SHAP-U8 > IG-U8: under mean 6/12, under interp 5/12 | no |
| secondary | MambaLRP better than IG under both maskers in 5/9 cells | – |

| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | SHAP-U8 > IG-U8 (mean / interp) |
|---|---|---|---|---|---|---|
| etth2 | itransformer | -0.309 | IG | SHAP-U4 | 11 → 2 | yes / yes |
| etth2 | plain | 0.590 | SHAP-U4 | SHAP-C | 12 → 1 | yes / yes |
| etth2 | smamba | -0.152 | MambaLRP | SHAP-C | 12 → 1 | yes / yes |
| etth2 | timemachine | 0.182 | MambaLRP | IG-U8 | 12 → 5 | yes / no |
| ettm1 | itransformer | -0.164 | GxI | SHAP-C | 10 → 1 | no / no |
| ettm1 | plain | 0.128 | MambaLRP | SHAP-C | 12 → 1 | no / no |
| ettm1 | smamba | -0.030 | MambaLRP | SHAP-C | 11 → 1 | no / no |
| ettm1 | timemachine | -0.485 | MambaLRP | SHAP-C | 12 → 1 | yes / no |
| exchange | itransformer | -0.455 | IG | SHAP-U4 | 11 → 2 | no / no |
| exchange | plain | 0.385 | SHAP-U16 | SHAP-C | 11 → 1 | yes / yes |
| exchange | smamba | -0.061 | IG | SHAP-C | 12 → 1 | no / no |
| exchange | timemachine | -0.364 | MambaLRP | SHAP-C | 12 → 1 | no / yes |

## Discovery: original public cells (not evidence) (8 cells)

| hypothesis | result | passes |
|---|---|---|
| M1 | median tau 0.028; best differs 8/8 | yes |
| M2 | SHAP-C ranks better under interp in 8/8 (sign test p = 3.9e-03) | yes |
| M3 | SHAP-U8 > IG-U8: under mean 8/8, under interp 4/8 | yes |
| secondary | MambaLRP better than IG under both maskers in 2/6 cells | – |

| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | SHAP-U8 > IG-U8 (mean / interp) |
|---|---|---|---|---|---|---|
| etth1 | itransformer | -0.345 | GxI | IG-U4 | 10 → 2 | yes / no |
| etth1 | plain | -0.179 | SHAP-U16 | SHAP-C | 12 → 1 | yes / no |
| etth1 | smamba | -0.182 | MambaLRP | IG-U4 | 11 → 3 | yes / no |
| etth1 | timemachine | -0.424 | MambaLRP | SHAP-U4 | 11 → 3 | yes / no |
| weather | itransformer | 0.236 | SHAP-U16 | SHAP-C | 6 → 1 | yes / yes |
| weather | plain | 0.641 | SHAP-Δ8 | SHAP-C | 6 → 1 | yes / yes |
| weather | smamba | 0.273 | SHAP-U16 | SHAP-C | 5 → 1 | yes / yes |
| weather | timemachine | 0.273 | SHAP-U4 | SHAP-C | 6 → 1 | yes / yes |
