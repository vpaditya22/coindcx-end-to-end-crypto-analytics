
-- 1. Rank assets by total return.
SELECT asset, total_return
FROM asset_metrics
ORDER BY total_return DESC;

-- 2. Rank assets by risk-adjusted return.
SELECT asset, sharpe_0rf, annualized_volatility, max_drawdown
FROM asset_metrics
ORDER BY sharpe_0rf DESC;

-- 3. Identify assets with the deepest drawdowns.
SELECT asset, max_drawdown
FROM asset_metrics
ORDER BY max_drawdown ASC;

-- 4. Identify the most active markets using the turnover proxy.
SELECT asset, avg_daily_turnover_proxy_inr
FROM asset_metrics
ORDER BY avg_daily_turnover_proxy_inr DESC;

-- 5. Core-asset comparison.
SELECT
    asset,
    total_return,
    annualized_volatility,
    max_drawdown,
    sharpe_0rf,
    avg_daily_turnover_proxy_inr
FROM asset_metrics
WHERE asset IN ('BTC', 'ETH', 'SOL', 'XRP')
ORDER BY sharpe_0rf DESC;

-- 6. High-risk / high-return candidates.
SELECT asset, total_return, annualized_volatility, max_drawdown
FROM asset_metrics
WHERE annualized_volatility >=
      (SELECT AVG(annualized_volatility) FROM asset_metrics)
ORDER BY total_return DESC;
