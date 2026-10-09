# Operations Runbook

## Fresh environment

1. Create and activate a virtual environment.
2. Install `requirements.txt`.
3. Install development dependencies from `requirements-dev.txt`.
4. Run unit tests with `pytest -q`.

## Refresh the data

Run `python -m src.fetch_data`, then `python -m src.clean_data`, then `python -m src.analyze`, then `python -m src.business_report`, then `python -m src.load_sqlite`.

## Common failures

- **HTTP errors:** check CoinDCX API availability and endpoint documentation before retrying.
- **No configured markets:** a configured asset may no longer have an active INR pair.
- **Empty candles:** check the selected date range and API interval/limit rules.
- **Missing analysis outputs:** run the stages in order; the dashboard expects processed metrics and candles.
- **Unexpected KPI values:** inspect raw candles, selected date range, missing dates and volume units before interpreting results.

## Safe handling

Downloaded market data is ignored by Git by default. Review current API terms before publishing raw or derived data. Never commit API keys, credentials, or local environment files.
