# Reproducibility

For a reproducible run, record:

- Git commit SHA
- Python version and dependency versions
- Configured start and end dates
- CoinDCX API request interval and requested assets
- Ingestion timestamp from `data/raw/run_metadata.json`
- Row counts before and after cleaning
- Assets and date coverage in processed candles
- Test command and result
- Any API errors, missing markets or manual data substitutions

Market data changes over time, so a rerun is not expected to reproduce the exact same numbers unless the same source snapshot is retained and permitted to be redistributed.
