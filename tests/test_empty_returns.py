import numpy as np
import pandas as pd
from src.metrics import calculate_asset_metrics

def test_single_observation_produces_undefined_annualized_return():
    frame = pd.DataFrame({
        "asset": ["BTC"], "pair": ["BTCINR"],
        "date": pd.to_datetime(["2025-01-01"]), "close": [100.0],
        "daily_return": [np.nan], "turnover_proxy_inr": [1000.0],
    })
    result = calculate_asset_metrics(frame)
    assert np.isnan(result["annualized_return"])
    assert result["observations"] == 1
