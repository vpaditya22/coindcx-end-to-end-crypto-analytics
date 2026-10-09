-- Find assets whose start and end prices are identical in the selected window.
SELECT asset, start_date, end_date, start_price_inr, end_price_inr, total_return
FROM asset_metrics
WHERE start_price_inr = end_price_inr
ORDER BY asset;
