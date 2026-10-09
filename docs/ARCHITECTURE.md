# Architecture

## Data flow

1. **Discover markets** from CoinDCX's public market-details endpoint.
2. **Ingest candles** for configured assets and a configured UTC date window.
3. **Persist raw extracts** separately from transformed data.
4. **Clean and validate** numeric values, OHLC bounds, duplicate asset/date rows and missing essentials.
5. **Engineer features** such as daily returns and rolling volatility.
6. **Calculate KPIs** at asset level and a cross-asset return-correlation matrix.
7. **Publish outputs** as CSV tables, charts, a Markdown business report and a SQLite database.
8. **Explore results** through the optional Streamlit dashboard.

## Design principles

- Keep API ingestion separate from analysis so metrics can be rerun without re-downloading.
- Keep raw and processed data separate for traceability.
- Prefer deterministic transformations and small unit tests.
- Label proxies and assumptions explicitly.
- Do not infer customer-level outcomes or exchange revenue from public market data.

## Main entry points

- `src/fetch_data.py`: external data acquisition
- `src/clean_data.py`: data quality and feature engineering
- `src/metrics.py`: reusable statistical functions
- `src/analyze.py`: tables and charts
- `src/business_report.py`: narrative report
- `src/load_sqlite.py`: analytical database
- `app.py`: interactive dashboard
