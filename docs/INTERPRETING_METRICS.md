# Interpreting Metrics

## Return
Return is a historical price change, not a forecast. Always state the observation window.

## Volatility
Volatility measures variability of returns, not the probability or size of every possible loss.

## Maximum drawdown
Drawdown is the largest observed peak-to-trough decline in the selected price path. It does not guarantee a maximum future loss.

## Sharpe-style ratio
This project divides annualized return by annualized volatility using a 0% risk-free assumption. Small samples, extreme returns and near-zero volatility can make this ratio unstable.

## Correlation
Correlation captures linear co-movement in the observed sample. It is not causation and may rise during market stress.

## Turnover proxy
Price multiplied by candle volume is only a proxy until the unit and denomination of volume are verified for the relevant pair and API endpoint.
