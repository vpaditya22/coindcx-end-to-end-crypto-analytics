import numpy as np
import pandas as pd
from src.metrics import build_correlation

def test_correlation_identical_return_series_is_one():
    frame = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"] * 2),
        "asset": ["A", "A", "A", "B", "B", "B"],
        "daily_return": [0.01, -0.02, 0.03, 0.01, -0.02, 0.03],
    })
    corr = build_correlation(frame)
    assert np.isclose(corr.loc["A", "B"], 1.0)
