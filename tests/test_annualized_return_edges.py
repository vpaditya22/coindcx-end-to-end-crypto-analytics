import numpy as np
import pandas as pd
from src.metrics import annualized_return

def test_annualized_return_requires_two_prices():
    assert np.isnan(annualized_return(pd.Series([100])))

def test_annualized_return_rejects_nonpositive_total_value():
    assert np.isnan(annualized_return(pd.Series([100, 0])))

def test_annualized_return_respects_period_frequency():
    result = annualized_return(pd.Series([100, 200]), periods_per_year=1)
    assert np.isclose(result, 1.0)
