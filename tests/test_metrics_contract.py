import pandas as pd
from src.metrics import calculate_asset_metrics

def test_asset_metrics_returns_expected_fields():
    frame = pd.DataFrame({
        "asset": ["BTC", "BTC", "BTC"],
        "pair": ["B-BTC_INR"] * 3,
        "date": pd.to_datetime(["2025-01-01", "2025-01-02", "2025-01-03"]),
        "close": [100.0, 110.0, 105.0],
        "daily_return": [None, 0.1, -0.0454545],
        "turnover_proxy_inr": [1000.0, 1100.0, 1050.0],
    })
    result = calculate_asset_metrics(frame)
    assert result["asset"] == "BTC"
    assert result["observations"] == 3
    assert result["max_drawdown"] < 0
    assert result["start_date"] == "2025-01-01"
