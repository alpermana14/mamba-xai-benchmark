"""
CMamba-aligned dataset loader for zero-shot evaluation.

Splits, normalization, and sliding-window logic match CMamba's data_loader.py
(https://github.com/zclzcl0223/CMamba) exactly:

  - ETTh (h1/h2)  : fixed border  train=12mo / val=4mo / test=8mo  (hourly)
  - ETTm (m1/m2)  : fixed border  train=12mo / val=4mo / test=8mo  (15-min)
  - Custom         : 70 / 10 / 20 percent split
  - StandardScaler : fitted on TRAIN portion only, then applied to all splits
  - Features M     : all columns except 'date'
  - label_len = 0  : seq_y starts exactly at seq_len (no decoder overlap)
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import Dataset, DataLoader


# ---------------------------------------------------------------------------
# Dataset registry — maps dataset name to (csv_path, split_type)
# ---------------------------------------------------------------------------
DATASET_CONFIGS = {
    # name          split_type   channels
    "ETTh1":   ("ETTh",   7),
    "ETTh2":   ("ETTh",   7),
    "ETTm1":   ("ETTm",   7),
    "ETTm2":   ("ETTm",   7),
    "Weather": ("custom", 21),
    "ECL":     ("custom", 321),
    "Traffic": ("custom", 862),
    "Exchange":("custom", 8),
    "ILI":     ("custom", 7),
}

# Standard prediction horizons per dataset (matching CMamba.sh)
HORIZONS = {
    "ETTh1":    [96, 192, 336, 720],
    "ETTh2":    [96, 192, 336, 720],
    "ETTm1":    [96, 192, 336, 720],
    "ETTm2":    [96, 192, 336, 720],
    "Weather":  [96, 192, 336, 720],
    "ECL":      [96, 192, 336, 720],
    "Traffic":  [96, 192, 336, 720],
    "Exchange": [96, 192, 336, 720],
    "ILI":      [24, 36, 48, 60],   # weekly-ish data, shorter horizons
}


def _compute_borders(split_type: str, total_len: int, seq_len: int,
                     split_mode: str = "cmamba"):
    """
    Returns (border1s, border2s).
    border1s[i] = start index of split i
    border2s[i] = end   index of split i
    i=0 → train, i=1 → val, i=2 → test

    split_mode:
      "cmamba" — CMamba/Informer convention: ETT datasets use fixed
                 12/4/8-month borders, others 70/10/20.
      "tsfm"   — TSFM-Bench (arXiv 2410.11802) convention: ETT datasets use
                 a 6:2:2 ratio split, others 7:1:2 (same as cmamba's custom).
    """
    if split_type in ("ETTh", "ETTm") and split_mode == "tsfm":
        num_train = int(total_len * 0.6)
        num_test  = int(total_len * 0.2)
        num_vali  = total_len - num_train - num_test
        border1s = [0, num_train - seq_len, total_len - num_test - seq_len]
        border2s = [num_train, num_train + num_vali, total_len]
        return border1s, border2s

    if split_type == "ETTh":
        train_end  = 12 * 30 * 24              # 8640
        val_end    = train_end + 4 * 30 * 24   # 11520
        test_end   = train_end + 8 * 30 * 24   # 17280
        border1s = [0, train_end - seq_len, val_end - seq_len]
        border2s = [train_end, val_end, test_end]

    elif split_type == "ETTm":
        train_end  = 12 * 30 * 24 * 4              # 34560
        val_end    = train_end + 4 * 30 * 24 * 4   # 46080
        test_end   = train_end + 8 * 30 * 24 * 4   # 69120
        border1s = [0, train_end - seq_len, val_end - seq_len]
        border2s = [train_end, val_end, test_end]

    else:  # custom: 70 / 10 / 20
        num_train = int(total_len * 0.7)
        num_test  = int(total_len * 0.2)
        num_vali  = total_len - num_train - num_test
        border1s = [0, num_train - seq_len, total_len - num_test - seq_len]
        border2s = [num_train, num_train + num_vali, total_len]

    return border1s, border2s


class TSForecastDataset(Dataset):
    """
    Sliding-window forecasting dataset matching CMamba's Dataset_ETT_hour /
    Dataset_Custom exactly (label_len=0, features='M').

    seq_x : [seq_len, C]   — normalised context
    seq_y : [pred_len, C]  — normalised target
    """

    def __init__(
        self,
        csv_path: str,
        split_type: str,     # "ETTh" | "ETTm" | "custom"
        flag: str,           # "train" | "val" | "test"
        seq_len: int,
        pred_len: int,
        scaler: StandardScaler | None = None,  # pass fitted scaler for val/test
        split_mode: str = "cmamba",
    ):
        df_raw = pd.read_csv(csv_path)
        # Drop date column, keep all numeric channels (features='M')
        cols = [c for c in df_raw.columns if c != "date"]
        data_np = df_raw[cols].values.astype(np.float32)   # [T, C]
        T = len(data_np)

        split_idx = {"train": 0, "val": 1, "test": 2}[flag]
        border1s, border2s = _compute_borders(split_type, T, seq_len, split_mode)
        b1, b2 = border1s[split_idx], border2s[split_idx]

        # Scaler: fit on TRAIN portion, reuse for val/test
        if scaler is None:
            scaler = StandardScaler()
            scaler.fit(data_np[border1s[0]:border2s[0]])
        self.scaler = scaler

        self.data = scaler.transform(data_np)   # [T, C] — full scaled series
        self.seq_len  = seq_len
        self.pred_len = pred_len
        self.b1 = b1
        self.b2 = b2
        self.num_channels = len(cols)

    def __len__(self):
        # Same formula as CMamba
        return self.b2 - self.b1 - self.seq_len - self.pred_len + 1

    def __getitem__(self, idx):
        s = self.b1 + idx
        seq_x = self.data[s          : s + self.seq_len]            # [seq_len, C]
        seq_y = self.data[s + self.seq_len : s + self.seq_len + self.pred_len]  # [pred_len, C]
        # Transpose to [C, T] convention used by M-Mamba4Cast
        return (
            torch.from_numpy(seq_x.T),   # [C, seq_len]
            torch.from_numpy(seq_y.T),   # [C, pred_len]
        )


def build_test_loader(
    csv_path: str,
    dataset_name: str,
    seq_len: int,
    pred_len: int,
    batch_size: int = 32,
    split_mode: str = "cmamba",
) -> DataLoader:
    """
    Build a test DataLoader (split_mode: "cmamba" or "tsfm").
    Scaler is always fitted on the training portion of that CSV.
    """
    split_type = DATASET_CONFIGS[dataset_name][0]

    # Fit scaler on training split
    train_ds = TSForecastDataset(csv_path, split_type, "train", seq_len, pred_len,
                                 split_mode=split_mode)
    test_ds  = TSForecastDataset(csv_path, split_type, "test",  seq_len, pred_len,
                                 scaler=train_ds.scaler, split_mode=split_mode)

    return DataLoader(test_ds, batch_size=batch_size, shuffle=False, drop_last=False)
