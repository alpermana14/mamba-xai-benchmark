"""
Convert the SHAPformer synthetic data (official data.zip, KIT: data/synthetic/*.json)
into one .npz for src.bench.tasks.g3. The JSON files are arrays of samples
{x_enc: {feature: [168]}, x_dec: {feature: [168]}, y: [168], explanation: {...}}; they
are parsed one sample at a time because train.json is 3.2 GB.

    python -m scripts.prepare_shapformer
    -> dataset/external/shapformer/synthetic.npz
       {split}_enc [N, 8, 168]  load + 7 covariates (ENC order), past
       {split}_dec [N, 7, 168]  covariates (DEC order), future
       {split}_y   [N, 168]     future load
       gt_expl [N, 6, 168], gt_base [N, 336], gt_expl_keys   ground-truth SHAP values (test_ground_truth.json)
"""

import json
from pathlib import Path

import numpy as np

SRC = Path("dataset/external/shapformer/data/synthetic")
OUT = Path("dataset/external/shapformer/synthetic.npz")
ENC = ["load", "hourofday", "dayofweek", "month", "holiday", "temperature", "noise1", "noise2"]
DEC = ENC[1:]


def iter_samples(path: Path, chunk: int = 1 << 24):
    dec = json.JSONDecoder()
    with open(path, encoding="utf-8") as fh:
        buf, pos = fh.read(chunk), 0
        pos = buf.index("[") + 1
        while True:
            while True:
                while pos < len(buf) and buf[pos] in " \t\r\n,":
                    pos += 1
                if pos < len(buf):
                    break
                more = fh.read(chunk)
                if not more:
                    return
                buf, pos = more, 0
            if buf[pos] == "]":
                return
            try:
                obj, end = dec.raw_decode(buf, pos)
            except json.JSONDecodeError:
                more = fh.read(chunk)
                if not more:
                    raise
                buf, pos = buf[pos:] + more, 0
                continue
            yield obj
            pos = end


def convert(path: Path, with_gt: bool = False) -> dict:
    enc, dec, y, expl, base, keys = [], [], [], [], [], None
    for s in iter_samples(path):
        enc.append([s["x_enc"][k] for k in ENC])
        dec.append([s["x_dec"][k] for k in DEC])
        y.append(s["y"])
        if with_gt:
            keys = keys or [k for k in s["explanation"] if k != "base"]
            expl.append([s["explanation"][k] for k in keys])
            base.append(s["explanation"]["base"])
    out = {"enc": np.asarray(enc, np.float32), "dec": np.asarray(dec, np.float32), "y": np.asarray(y, np.float32)}
    if with_gt:
        out.update(expl=np.asarray(expl, np.float32), base=np.asarray(base, np.float32), expl_keys=np.array(keys))
    print(f"{path.name}: {len(y)} samples", flush=True)
    return out


def main():
    arrays = {}
    for split, name in (("gt", "test_ground_truth.json"), ("train", "train.json"), ("dev", "dev.json"),
                        ("test", "test.json")):
        d = convert(SRC / name, with_gt=split == "gt")
        arrays.update({f"{split}_{k}": v for k, v in d.items()})
    arrays["gt_expl_keys"] = arrays.pop("gt_expl_keys")
    np.savez(OUT, **arrays)
    print({k: v.shape for k, v in arrays.items()})


if __name__ == "__main__":
    main()
