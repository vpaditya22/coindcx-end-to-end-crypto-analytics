-- Show each asset's observation count and date bounds before pairwise comparisons.
SELECT asset, COUNT(*) AS observations,
       MIN(date) AS first_date,
       MAX(date) AS last_date,
       COUNT(DISTINCT date) AS distinct_dates
FROM daily_candles
GROUP BY asset
ORDER BY first_date, asset;
