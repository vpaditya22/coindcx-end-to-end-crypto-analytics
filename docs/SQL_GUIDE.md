# SQL Guide

The SQLite database is intended for repeatable analytical queries after the Python pipeline has generated cleaned candles and asset metrics.

Typical workflow:

1. Run the fetch, clean and analyze stages.
2. Run `python -m src.load_sqlite`.
3. Open `data/processed/coindcx_analytics.db` with SQLite-compatible tooling.
4. Run queries in `sql/02_business_questions.sql`.
5. Check the date range and metric definitions before interpreting results.

The database is generated locally and is not committed as a binary artifact.
