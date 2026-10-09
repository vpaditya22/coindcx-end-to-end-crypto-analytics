import numpy as np
import pandas as pd
from src.metrics import build_correlation

def test_correlation_requires_at_least_two_overlapping_returns():
    frame = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-01", "2025-01-02"]),
        "asset": ["A", "A", "B", "B"],
        "daily_return": [0.01, np.nan, 0.02, 0.03],
    })
    corr = build_correlation(frame)
    assert np.isnan(corr.loc["A", "B"])
