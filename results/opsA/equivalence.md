# Opsi A: equivalence of the reference forward, our zoo backend and the mamba_ssm kernel

| check | max abs diff | verdict |
|---|---|---|
| (i) ref vs kernel, value, S-Mamba shape | 2.98e-08 | pass |
| (i) ref vs kernel, input gradient, S-Mamba shape | 2.07e-07 | pass |
| (ii) PurePyTorchMamba vs kernel, S-Mamba shape | 2.98e-08 | pass |
| speed S-Mamba shape kernel | 0.35 ms | – |
| speed S-Mamba shape reference | 0.96 ms | – |
| (i) ref vs kernel, value, TimeMachine shape | 7.15e-07 | pass |
| (i) ref vs kernel, input gradient, TimeMachine shape | 8.94e-07 | pass |
| speed TimeMachine shape kernel | 0.33 ms | – |
| speed TimeMachine shape reference | 27.67 ms | – |
| (i) ref vs kernel, value, generic | 1.04e-07 | pass |
| (i) ref vs kernel, input gradient, generic | 2.72e-07 | pass |
| (ii) PurePyTorchMamba vs kernel, generic | 1.04e-07 | pass |
| speed generic kernel | 0.35 ms | – |
| speed generic reference | 5.59 ms | – |
| (iii) wrapper equals official forward, smamba etth1 | 0.00e+00 | pass |
| (iii) LRP mode keeps forward value, smamba etth1 | 1.22e-07 | pass |
| (iii) MambaLRP differs from GxI, smamba etth1 | 1.04e-01 | pass |
| (iii) sum of relevance / f(x), smamba etth1 | -0.355 | descriptive |
| (iii) LRP mode keeps forward value, timemachine etth1 | 9.22e-08 | pass |
| (iii) MambaLRP differs from GxI, timemachine etth1 | 2.75e-02 | pass |
| (iii) sum of relevance / f(x), timemachine etth1 | -0.055 | descriptive |
| (iii) wrapper equals official forward, smamba weather | 0.00e+00 | pass |
| (iii) LRP mode keeps forward value, smamba weather | 2.30e-07 | pass |
| (iii) MambaLRP differs from GxI, smamba weather | 8.14e-02 | pass |
| (iii) sum of relevance / f(x), smamba weather | 0.922 | descriptive |
| (iii) LRP mode keeps forward value, timemachine weather | 2.28e-07 | pass |
| (iii) MambaLRP differs from GxI, timemachine weather | 1.13e-02 | pass |
| (iii) sum of relevance / f(x), timemachine weather | 1.248 | descriptive |

**Overall: all checks pass**
