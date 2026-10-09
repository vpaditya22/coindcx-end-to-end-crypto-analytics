# Error Handling Expectations

- External HTTP failures should be surfaced with enough context to identify the endpoint and asset.
- Empty candle responses should be recorded distinctly from request failures.
- Missing required columns should fail fast with a clear message.
- Invalid rows should be excluded by documented rules and counted where possible.
- Empty analysis inputs should not produce misleading rankings.
- SQL loading should fail clearly when no processed inputs exist.
- Do not silently replace missing metrics with zero.
