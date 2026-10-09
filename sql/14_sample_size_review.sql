-- Review observation counts before ranking assets.
SELECT asset, observations, start_date, end_date,
       CASE
         WHEN observations < 30 THEN 'Very small sample'
         WHEN observations < 180 THEN 'Limited sample'
         ELSE 'Larger sample'
       END AS sample_size_note
FROM asset_metrics
ORDER BY observations ASC;
-- These cutoffs are operational review labels, not statistical guarantees.
