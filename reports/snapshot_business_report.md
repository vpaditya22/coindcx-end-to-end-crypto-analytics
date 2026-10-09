# CoinDCX Snapshot Business Analysis

## Data provenance

This analysis uses the **real CoinDCX market snapshot supplied for this project**.
The snapshot contains 58 market records and 35 INR pairs, timestamped
**2026-09-04T12:20:06+00:00**.

Official CoinDCX documentation defines the ticker fields as 24-hour high/low,
24-hour market volume, last price, bid and ask; it also documents public market
and candlestick endpoints. citeturn1search0

## Business question

**How can CoinDCX use market activity and market-quality signals to improve asset
discovery and risk-aware investor experiences?**

## Snapshot findings

- **Highest 24-hour move:** LINK at 5.89%.
- **Lowest 24-hour move:** ARB at -2.69%.
- **Tightest quoted spread:** SOL at 0.2334% of midpoint.
- **Widest quoted spread:** MASK at 4.0351% of midpoint.
- Usable INR quotes: 25.

## Why we do not rank liquidity using price × ticker volume

The supplied ticker's `volume` field is documented by CoinDCX as the market's
24-hour volume, but the ticker documentation does not establish a common
cross-market unit in the supplied response. CoinDCX's candle documentation
explicitly describes candle volume in terms of target currency. citeturn1search0

Therefore, this project **does not present price × ticker volume as an exact INR
turnover measure**. That would risk producing misleading cross-asset comparisons.

For this snapshot, the more defensible microstructure KPI is **quoted bid-ask
spread as a percentage of midpoint**.

## Business interpretation

### 1. Improve asset discovery

Use market-quality signals such as spread, recent price movement and historical
liquidity to make asset discovery more informative than a simple list of tokens.

### 2. Add a risk lens

A large 24-hour move is a useful alert signal, but it is not historical volatility.
The final historical layer should use CoinDCX daily candles to calculate rolling
volatility and maximum drawdown.

### 3. Avoid confusing market activity with revenue

Ticker volume is not CoinDCX revenue, fees, customer profitability or retention.
Those require internal transactional/product data.

### 4. Product opportunity

CoinDCX's H1 2026 report says Indian investors increasingly concentrated portfolios
around Bitcoin, Ethereum, Solana and XRP, while meme tokens accounted for 12.17%
of trading volume and Layer-1 assets 32.87%. It also reports 2.2 crore+ registered
users. citeturn0search0

This supports a testable product hypothesis:

> Build stronger core-asset discovery, systematic-investing and risk-education
> experiences, then validate their impact using internal customer-level metrics.

## Required next historical layer

CoinDCX's official API supports daily candles. citeturn1search0

For each selected INR pair, retrieve approximately 12 months of 1-day candles and
calculate:

- cumulative return
- annualized return
- annualized volatility
- maximum drawdown
- Sharpe-style ratio
- rolling 30-day volatility
- correlation

These historical metrics should be kept separate from this one-time snapshot.

## Limitations

- This snapshot is a single point in time.
- It cannot establish historical performance.
- It cannot identify individual customers.
- It cannot establish CoinDCX revenue or retention.
- Some INR rows have zero bid/ask/volume and should not be treated as liquid markets.
- Crypto markets are highly volatile; this is an analytics project, not investment advice.
