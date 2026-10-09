-- Rank drawdowns from shallowest to deepest for transparent interpretation.
SELECT asset, max_drawdown, total_return, observations
FROM asset_metrics
WHERE max_drawdown IS NOT NULL
ORDER BY max_drawdown DESC;
