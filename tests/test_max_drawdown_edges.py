import numpy as np
import pandas as pd
from src.metrics import max_drawdown

def test_drawdown_no_decline_is_zero():
    assert max_drawdown(pd.Series([10, 11, 12])) == 0.0

def test_drawdown_starts_from_first_peak():
    assert np.isclose(max_drawdown(pd.Series([100, 80, 90])), -0.2)

def test_drawdown_uses_running_peak():
    assert np.isclose(max_drawdown(pd.Series([100, 120, 90, 110, 60])), -0.5)
