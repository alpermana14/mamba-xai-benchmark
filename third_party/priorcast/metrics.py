"""Standard forecasting metrics: MSE, MAE, MASE."""

import numpy as np


def mse(pred: np.ndarray, true: np.ndarray) -> float:
    return float(np.mean((pred - true) ** 2))


def mae(pred: np.ndarray, true: np.ndarray) -> float:
    return float(np.mean(np.abs(pred - true)))


def mase(pred: np.ndarray, true: np.ndarray, context: np.ndarray, freq: int = 1) -> float:
    """
    Mean Absolute Scaled Error.
    Scales MAE by the in-sample naive seasonal forecast error.
    pred, true: [C, H]
    context:    [C, T]  (in-sample history)
    """
    naive_err = np.mean(np.abs(context[:, freq:] - context[:, :-freq]))
    return mae(pred, true) / (naive_err + 1e-8)


def compute_all(
    pred: np.ndarray,
    true: np.ndarray,
    context: np.ndarray,
    freq: int = 1,
) -> dict:
    return {
        "MSE": mse(pred, true),
        "MAE": mae(pred, true),
        "MASE": mase(pred, true, context, freq),
    }
