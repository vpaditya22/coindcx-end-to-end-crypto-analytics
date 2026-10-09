import pandas as pd
import pytest
from src.metrics import calculate_asset_metrics

def test_empty_group_raises_clear_error():
    frame = pd.DataFrame(columns=[
        "asset", "pair", "date", "close", "daily_return", "turnover_proxy_inr"
    ])
    with pytest.raises(ValueError, match="empty asset group"):
        calculate_asset_metrics(frame)
