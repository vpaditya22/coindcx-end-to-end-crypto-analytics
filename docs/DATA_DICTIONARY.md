# Data Dictionary and Metric Definitions

This document describes the fields created by the current CoinDCX pipeline. It is intended to help reviewers reproduce the analysis and interpret each metric without overstating what public market data can prove.

## Pipeline datasets

| Dataset | Purpose | Main fields |
|---|---|---|
| `data/raw/inr_market_details.csv` | Active INR market metadata discovered from CoinDCX | `asset`, `pair`, `symbol`, `target_name`, `status` |
| `data/raw/daily_candles.csv` | Raw daily candle response with asset/pair labels | API candle fields plus `asset`, `pair`, `target_name` |
| `data/raw/run_metadata.json` | Provenance for a data-ingestion run | UTC download time, requested date range, requested/downloaded assets, row count |
| `data/processed/daily_candles_clean.csv` | Validated candles with engineered features | OHLCV fields, date, daily return, turnover proxy, rolling volatility |
| Metrics output | Per-asset summary statistics produced by the analysis stage | Return, risk, drawdown, Sharpe and turnover-proxy statistics |
| Correlation output | Pairwise correlations of asset daily returns | One column/row per asset |

Actual file names and output locations should be checked against the current configuration and pipeline run.

## Candle fields

| Field | Meaning | Validation / interpretation |
|---|---|---|
| `asset` | Target asset ticker assigned during ingestion | Used to group time series |
| `pair` | CoinDCX market pair identifier | Identifies the traded market |
| `open`, `high`, `low`, `close` | Candle prices | Converted to numeric values; rows with invalid close or inconsistent OHLC bounds are removed |
| `volume` | Candle volume returned by the API | Must be non-negative; check the API's current definition and unit before interpreting it |
| `time` | Candle timestamp in milliseconds | Converted to a UTC date for daily grouping |
| `date` | Normalized UTC calendar date | Duplicate asset/date rows are reduced to the last row after sorting |
| `daily_return` | Percentage price change from the prior observation for the same asset | First observation per asset is null; represented as a decimal, e.g. 0.02 = 2% |
| `turnover_proxy_inr` | `close × volume` | A proxy only. Confirm the API's volume denomination before treating this as INR turnover; it is not CoinDCX revenue |
| `rolling_vol_30d` | 30-observation rolling standard deviation of daily returns, multiplied by √365 | Annualized rolling volatility proxy; early rows are null until enough return observations exist |

## Asset-level metrics

| Metric | Definition in code | Caveat |
|---|---|---|
| `total_return` | Final close / first close − 1 | Depends on the available observation window |
| `annualized_return` | Geometric annualization of start-to-end price change using 365 periods/year | Sensitive to short windows and incomplete history |
| `annualized_volatility` | Standard deviation of observed daily returns × √365 | Assumes daily observations; missing dates can affect interpretation |
| `max_drawdown` | Minimum of close / running maximum close − 1 | Calculated from the observed price path only |
| `sharpe_0rf` | Annualized return / annualized volatility | Uses a 0% risk-free-rate assumption; not a recommendation or forecast |
| `avg_daily_turnover_proxy_inr` | Mean of the candle-level turnover proxy | Valid only as a proxy, subject to the volume-unit caveat |
| `median_daily_turnover_proxy_inr` | Median of the candle-level turnover proxy | More resistant than the mean to extreme observations, but has the same unit caveat |
| `observations` | Number of retained rows for the asset | Not necessarily the number of calendar days in the requested window |

## Data-quality checks currently applied

The cleaning step:
- Requires `asset`, `pair`, `open`, `high`, `low`, `close`, `volume` and `time`.
- Converts OHLCV and timestamp fields to numeric values.
- Removes rows missing asset, date or close, and rows with non-positive close.
- Removes negative-volume rows.
- Applies basic OHLC consistency checks.
- Sorts by asset/date and removes duplicate asset/date observations.

These checks improve consistency but do not prove that the source is complete, that every expected day is present, or that the market data is free from exchange-side errors. Review the validation output after each ingestion run.

## Interpretation guardrails

1. Market prices and candles do not reveal individual customer positions, retention, churn, customer lifetime value or customer-level profitability.
2. Trading volume is not exchange revenue. Do not infer company revenue from price multiplied by volume.
3. A high historical return does not establish future performance or make an asset suitable for every investor.
4. Correlation is calculated from the dates present in the dataset; compare assets over a consistent period before drawing conclusions.
5. Treat all metrics as descriptive analysis of the selected historical window, not investment advice.

## Reproducing the dataset

Run the pipeline stages in the order documented in the repository README: fetch data, clean and validate it, then run the analysis and reporting stages. Record the configured date range and ingestion metadata when comparing results across runs.
