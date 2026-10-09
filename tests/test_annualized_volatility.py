import numpy as np
import pandas as pd

def test_daily_return_annualization_convention():
    returns = pd.Series([0.01, -0.01, 0.02, -0.02])
    annualized = returns.std() * np.sqrt(365)
    assert annualized > returns.std()
    assert np.isclose(annualized, returns.std() * np.sqrt(365))
