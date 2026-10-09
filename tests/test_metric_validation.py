import pandas as pd
import pytest
from src.metrics import calculate_asset_metrics, build_correlation

def test_metrics_reject_missing_required_columns():
    with pytest.raises(ValueError, match="Missing metric columns"):
        calculate_asset_metrics(pd.DataFrame({"asset": ["BTC"]}))

def test_correlation_rejects_duplicate_asset_date_rows():
    frame = pd.DataFrame({
        "date": pd.to_datetime(["2025-01-01", "2025-01-01"]),
        "asset": ["BTC", "BTC"],
        "daily_return": [0.01, 0.02],
    })
    with pytest.raises(ValueError, match="Duplicate date/asset"):
        build_correlation(frame)

def test_correlation_empty_input_returns_empty_frame():
    result = build_correlation(pd.DataFrame(columns=["date", "asset", "daily_return"]))
    assert result.empty
