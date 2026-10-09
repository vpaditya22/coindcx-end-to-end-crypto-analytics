# Interview Story

## 30-second version

I built a reproducible analytics pipeline around CoinDCX public market data. It ingests INR market candles, validates and transforms them, calculates return and risk metrics, stores results in CSV/SQLite, and presents findings through charts and a dashboard.

## Technical deep dive

Explain the ingestion boundary, cleaning rules, date normalization, per-asset return calculation, annualization assumptions, data-quality caveats and test strategy.

## Business deep dive

Explain how return, volatility, drawdown and co-movement can inform risk education and asset discovery. Be explicit that public market data cannot prove customer retention, revenue or profitability.

## Trade-offs to discuss

- Reproducible snapshots versus always-live data
- More assets versus API request cost and data completeness
- Simple metrics versus assumptions and interpretation risk
- Dashboard convenience versus tested, reusable analysis functions
