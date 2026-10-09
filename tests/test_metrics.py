import pandas as pd
from src.metrics import max_drawdown, annualized_return


def test_max_drawdown():
    s = pd.Series([100, 120, 90, 110])
    assert round(max_drawdown(s), 4) == -0.25


def test_annualized_return_positive():
    s = pd.Series([100, 110])
    assert annualized_return(s) > 0
