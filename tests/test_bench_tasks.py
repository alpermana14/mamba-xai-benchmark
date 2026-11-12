import numpy as np
import pytest

from scripts.bench_analyze import holm
from src.bench.tasks import build_task


@pytest.fixture(scope="module")
def g1():
    return build_task("g1", 0)


def test_g1_target_last_and_ground_truth_on_drivers(g1):
    assert g1.channels[-1] == "y" and g1.target == len(g1.channels) - 1
    drivers = {g1.channels.index("x_lag"), g1.channels.index("x_evt")}
    for i in range(0, 2000, 97):
        gt = g1.gt_cells(i)
        assert set(np.flatnonzero(gt.any(1))) <= drivers
    assert not g1.score_mask[g1.meta["regime_channel"]].any()
    assert g1.X["train"].shape[1:] == (6, 96) and g1.Y["test"].shape[1] == 24


def test_g1_target_is_the_future_of_the_last_channel(g1):
    s = g1.meta["starts"]["val"]
    j = np.flatnonzero(s == s[0] + g1.H)[0]                     # window starting H steps later
    assert np.allclose(g1.Y["val"][0], g1.X["val"][j, -1, g1.L - g1.H:])


@pytest.mark.parametrize("name", ["g2a", "g2b", "g2c"])
def test_g2_ground_truth_marks_the_pulses(name):
    t = build_task(name, 0)
    X = t.X["test"]
    gt = np.stack([t.gt_cells(i) for i in range(len(X))])
    assert not gt[:, -1].any() and (X[:, -1] == 0).all()         # empty target channel
    assert np.abs(X[gt]).mean() > 2 * np.abs(X[~gt & t.score_mask]).mean()
    assert set(np.unique(t.Y["train"])) == {-1.0, 1.0}


def test_holm():
    p = np.array([0.01, 0.04, np.nan, 0.03])
    assert np.allclose(holm(p)[[0, 1, 3]], [0.03, 0.06, 0.06]) and np.isnan(holm(p)[2])


def test_weather_sentinels_are_interpolated():
    t = build_task("weather", 0)
    assert t.channels[-1] == "OT" and min(v.min() for v in t.X.values()) > -10
    assert 0.3 < t.Y["test"].std() < 3                              # OT not squashed by the -9999 sentinels


@pytest.mark.parametrize("name", ["etth2", "ettm1", "exchange"])
def test_replication_tasks_have_ot_last(name):
    t = build_task(name, 0)
    assert t.channels[-1] == "OT" and t.X["test"].shape[1:] == (len(t.channels), 96) and t.Y["test"].shape[1] == 96
    assert np.isfinite(t.X["train"]).all()


def test_horizon_tasks_extend_the_horizon_only():
    base, long = build_task("etth1", 0), build_task("etth1_h336", 0)
    assert long.name == "etth1_h336" and long.H == 336 and long.Y["test"].shape[1] == 336
    assert long.L == base.L and long.channels == base.channels
    assert np.allclose(long.X["train"][0], base.X["train"][0])          # same windows, longer targets
