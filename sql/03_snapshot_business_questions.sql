
-- Snapshot-level business questions

-- 1. Most active INR markets by turnover proxy.
SELECT asset, turnover_proxy_inr
FROM coindcx_inr_snapshot
WHERE liquid_quote = 1
ORDER BY turnover_proxy_inr DESC;

-- 2. Largest 24-hour movers.
SELECT asset, change_24_hour
FROM coindcx_inr_snapshot
WHERE liquid_quote = 1
ORDER BY change_24_hour DESC;

-- 3. Widest quoted spreads.
SELECT asset, spread_pct_mid
FROM coindcx_inr_snapshot
WHERE liquid_quote = 1
ORDER BY spread_pct_mid DESC;

-- 4. Core vs speculative comparison.
SELECT
    segment,
    COUNT(*) AS markets,
    AVG(change_24_hour) AS avg_24h_change,
    AVG(spread_pct_mid) AS avg_spread_pct,
    SUM(turnover_proxy_inr) AS turnover_proxy
FROM coindcx_inr_snapshot
WHERE segment IN ('Core', 'Speculative')
GROUP BY segment;
