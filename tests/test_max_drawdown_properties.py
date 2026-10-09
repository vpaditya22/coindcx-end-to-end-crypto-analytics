import pandas as pd
from src.metrics import max_drawdown

def test_max_drawdown_never_positive_for_positive_prices():
    prices = pd.Series([10, 14, 13, 15, 12, 15])
    assert max_drawdown(prices) <= 0

def test_max_drawdown_is_zero_for_constant_series():
    assert max_drawdown(pd.Series([7, 7, 7])) == 0
