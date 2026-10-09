-- Inspect extreme daily returns for data-quality review.
SELECT asset, date, daily_return, close, volume
FROM daily_candles
WHERE daily_return IS NOT NULL
  AND ABS(daily_return) >= 0.5
ORDER BY ABS(daily_return) DESC;
-- Extreme moves may be real; review source candles before excluding any row.
