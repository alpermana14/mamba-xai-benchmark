# v2.2 horizon robustness: masker dependence (pre-registered 2026-11-08)

## H = 192 (ETTh1, Weather) (8 cells)

| hypothesis | result | passes |
|---|---|---|
| M1-H | median tau 0.197; best differs 8/8 | yes |
| M2-H | SHAP-C ranks better under interp in 8/8 (sign test p = 3.9e-03) | yes |
| M3 (closed, descriptive) | SHAP-U8 > IG-U8: under mean 7/8, under interp 5/8 | – |
| secondary | MambaLRP better than IG under both maskers in 2/6 cells | – |

| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | SHAP-U8 > IG-U8 (mean / interp) |
|---|---|---|---|---|---|---|
| etth1_h192 | itransformer | -0.091 | SHAP-U8 | IG-U4 | 10 → 3 | yes / no |
| etth1_h192 | plain | -0.103 | MambaLRP | IG-U4 | 12 → 2 | no / no |
| etth1_h192 | smamba | -0.212 | SHAP-U8 | IG-U8 | 11 → 4 | yes / no |
| etth1_h192 | timemachine | 0.121 | MambaLRP | SHAP-U4 | 11 → 5 | yes / yes |
| weather_h192 | itransformer | 0.273 | SHAP-U16 | SHAP-C | 6 → 1 | yes / yes |
| weather_h192 | plain | 0.538 | SHAP-U8 | SHAP-C | 6 → 1 | yes / yes |
| weather_h192 | smamba | 0.273 | SHAP-U16 | SHAP-C | 5 → 1 | yes / yes |
| weather_h192 | timemachine | 0.424 | SHAP-U4 | SHAP-C | 6 → 1 | yes / yes |

## H = 336 (ETTh1, Weather) (8 cells)

| hypothesis | result | passes |
|---|---|---|
| M1-H | median tau 0.321; best differs 7/8 | yes |
| M2-H | SHAP-C ranks better under interp in 8/8 (sign test p = 3.9e-03) | yes |
| M3 (closed, descriptive) | SHAP-U8 > IG-U8: under mean 7/8, under interp 5/8 | – |
| secondary | MambaLRP better than IG under both maskers in 5/6 cells | – |

| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | SHAP-U8 > IG-U8 (mean / interp) |
|---|---|---|---|---|---|---|
| etth1_h336 | itransformer | -0.091 | SHAP-MMD8 | IG-U4 | 10 → 3 | yes / no |
| etth1_h336 | plain | 0.333 | MambaLRP | SHAP-C | 7 → 1 | no / no |
| etth1_h336 | smamba | 0.121 | SHAP-U4 | SHAP-U4 | 11 → 5 | yes / no |
| etth1_h336 | timemachine | 0.333 | SHAP-MMD8 | SHAP-U4 | 11 → 4 | yes / yes |
| weather_h336 | itransformer | 0.309 | SHAP-U16 | SHAP-C | 6 → 1 | yes / yes |
| weather_h336 | plain | 0.667 | SHAP-U8 | SHAP-C | 6 → 1 | yes / yes |
| weather_h336 | smamba | 0.242 | SHAP-U16 | SHAP-C | 5 → 1 | yes / yes |
| weather_h336 | timemachine | 0.515 | SHAP-U4 | SHAP-C | 6 → 1 | yes / yes |

## H = 720 (ETTh1, Weather) (8 cells)

| hypothesis | result | passes |
|---|---|---|
| M1-H | median tau 0.470; best differs 8/8 | yes |
| M2-H | SHAP-C ranks better under interp in 8/8 (sign test p = 3.9e-03) | yes |
| M3 (closed, descriptive) | SHAP-U8 > IG-U8: under mean 7/8, under interp 5/8 | – |
| secondary | MambaLRP better than IG under both maskers in 1/6 cells | – |

| task | model | tau | best (mean) | best (interp) | SHAP-C rank mean → interp | SHAP-U8 > IG-U8 (mean / interp) |
|---|---|---|---|---|---|---|
| etth1_h720 | itransformer | -0.345 | SHAP-U8 | IG-U4 | 10 → 3 | yes / no |
| etth1_h720 | plain | 0.000 | MambaLRP | SHAP-C | 11 → 1 | no / no |
| etth1_h720 | smamba | 0.030 | SHAP-MMD8 | SHAP-U4 | 11 → 4 | yes / no |
| etth1_h720 | timemachine | 0.485 | SHAP-MMD8 | SHAP-U4 | 11 → 4 | yes / yes |
| weather_h720 | itransformer | 0.745 | SHAP-U4 | SHAP-C | 4 → 1 | yes / yes |
| weather_h720 | plain | 0.564 | SHAP-Δ8 | SHAP-C | 6 → 1 | yes / yes |
| weather_h720 | smamba | 0.455 | SHAP-U4 | SHAP-C | 3 → 1 | yes / yes |
| weather_h720 | timemachine | 0.576 | SHAP-U4 | SHAP-C | 5 → 1 | yes / yes |
