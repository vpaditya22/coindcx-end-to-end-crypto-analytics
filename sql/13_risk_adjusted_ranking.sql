-- Rank only rows with a defined Sharpe-style metric.
-- This avoids treating undefined scores as zero.
SELECT asset, sharpe_0rf, total_return, annualized_volatility, max_drawdown, observations
FROM asset_metrics
WHERE sharpe_0rf IS NOT NULL
ORDER BY sharpe_0rf DESC;
