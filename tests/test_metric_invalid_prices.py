import numpy as np
import pandas as pd
from src.metrics import max_drawdown, annualized_return

def test_drawdown_invalid_nonpositive_price_returns_nan():
    assert np.isnan(max_drawdown(pd.Series([100, 0, 90])))

def test_annualized_return_rejects_nonpositive_prices():
    assert np.isnan(annualized_return(pd.Series([100, -1, 10])))
