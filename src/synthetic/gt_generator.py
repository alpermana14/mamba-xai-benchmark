"""
Multivariate series with planted dependencies, for scoring attributions (plan §3.3).

Channels
  0 y        target
  1 x_lag    AR(1) driver.    y(t) += a * r(t) * x_lag(t - k_lag)      (regime-gated, fixed lag)
  2 x_evt    sparse spikes.   y(t) += b * sum_j w_j * x_evt(t - d_evt - j)   (event, short pulse)
  3 r        observed regime indicator (slow on/off square wave + noise)
  4 dis_ar   AR(1) distractor, same law as x_lag, no effect
  5 dis_evt  spike distractor, same law as x_evt, no effect

With k_lag, d_evt >= H every relevant input lies inside the lookback, so the
ground truth for "mean forecast of y over the horizon" is exact:
  - x_lag cells at positions L + h - k_lag for every h whose forecast step is in regime on;
  - x_evt cells that hold a spike and whose pulse lands inside the forecast window.
The x_lag region is fixed per window; the x_evt cells move with the spikes, which is
where an input-adaptive segmentation should help.
"""

from dataclasses import dataclass, asdict

import numpy as np

CHANNELS = ["y", "x_lag", "x_evt", "r", "dis_ar", "dis_evt"]
TARGET, LAG, EVT, REGIME = 0, 1, 2, 3


@dataclass
class GTConfig:
    length: int = 20000
    phi: float = 0.5           # AR(1) coefficient of x_lag / dis_ar
    k_lag: int = 30
    a: float = 1.0
    d_evt: int = 48
    b: float = 1.0
    spike_p: float = 0.04
    spike_amp: float = 3.0
    pulse: tuple = (0.5, 1.0, 0.5)   # weights for j = -1, 0, 1
    regime_mean_len: int = 300
    regime_min_len: int = 150
    noise_y: float = 0.1
    noise_r: float = 0.05
    seed: int = 0


def _ar1(rng, n, phi):
    e = rng.standard_normal(n) * np.sqrt(1 - phi ** 2)
    x = np.empty(n)
    x[0] = rng.standard_normal()
    for t in range(1, n):
        x[t] = phi * x[t - 1] + e[t]
    return x


def _spikes(rng, n, p, amp):
    s = (rng.random(n) < p).astype(float)
    return s * (amp + 0.1 * rng.standard_normal(n))


def _regime(rng, n, mean_len, min_len):
    r = np.empty(n)
    t, state = 0, int(rng.random() < 0.5)
    while t < n:
        dur = min_len + int(rng.exponential(mean_len - min_len))
        r[t:t + dur] = state
        t += dur
        state = 1 - state
    return r


class GTSeries:
    def __init__(self, cfg: GTConfig = GTConfig()):
        self.cfg = cfg
        rng = np.random.default_rng(cfg.seed)
        n = cfg.length
        x_lag = _ar1(rng, n, cfg.phi)
        x_evt = _spikes(rng, n, cfg.spike_p, cfg.spike_amp)
        r = _regime(rng, n, cfg.regime_mean_len, cfg.regime_min_len)
        dis_ar = _ar1(rng, n, cfg.phi)
        dis_evt = _spikes(rng, n, cfg.spike_p, cfg.spike_amp)

        y = cfg.noise_y * rng.standard_normal(n)
        lagged = np.zeros(n)
        lagged[cfg.k_lag:] = x_lag[:-cfg.k_lag]
        y += cfg.a * r * lagged
        for j, w in zip((-1, 0, 1), cfg.pulse):
            shift = cfg.d_evt + j
            ev = np.zeros(n)
            ev[shift:] = x_evt[:-shift]
            y += cfg.b * w * ev

        self.regime = r
        self.is_spike = x_evt != 0
        r_obs = r + cfg.noise_r * rng.standard_normal(n)
        self.data = np.stack([y, x_lag, x_evt, r_obs, dis_ar, dis_evt], axis=1).astype(np.float32)

    def gt_mask(self, start: int, L: int, H: int) -> np.ndarray:
        """[C, L] bool: cells that drive mean_h y(start+L+h)."""
        c = self.cfg
        m = np.zeros((len(CHANNELS), L), dtype=bool)
        for h in range(H):
            tau = start + L + h
            if self.regime[tau] > 0.5:
                p = L + h - c.k_lag
                if 0 <= p < L:
                    m[LAG, p] = True
            for j in (-1, 0, 1):
                p = L + h - c.d_evt - j
                if 0 <= p < L and self.is_spike[start + p]:
                    m[EVT, p] = True
        return m

    def oracle_forecast(self, starts: np.ndarray, L: int, H: int) -> np.ndarray:
        """
        [n, H] raw-scale forecast of y from the true equations, assuming the regime at
        the last observed step persists over the horizon (the only unknowable part
        besides noise). Its MSE is the reference a trained model should approach.
        """
        c = self.cfg
        t = np.asarray(starts)[:, None] + L + np.arange(H)                  # forecast time steps
        r_last = self.regime[np.asarray(starts) + L - 1][:, None]
        yhat = c.a * r_last * self.data[t - c.k_lag, LAG]
        for j, w in zip((-1, 0, 1), c.pulse):
            yhat = yhat + c.b * w * self.data[t - c.d_evt - j, EVT]
        return yhat

    @staticmethod
    def score_mask(L: int) -> np.ndarray:
        """[C, L] bool: cells that count when scoring (the regime channel is a gate, so it is excluded)."""
        m = np.ones((len(CHANNELS), L), dtype=bool)
        m[REGIME] = False
        return m

    def config_dict(self) -> dict:
        return asdict(self.cfg)
