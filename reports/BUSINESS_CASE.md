# Business Case: CoinDCX Core-Asset & Systematic-Investing Strategy

## Executive question

**As Indian crypto investors become more focused on large-cap and utility-led assets, where should CoinDCX concentrate product discovery, education and systematic-investing experiences?**

## Hypotheses

### H1 — Core assets have stronger risk/liquidity characteristics
BTC, ETH, SOL and XRP may provide a stronger combination of liquidity and risk-adjusted performance than highly speculative assets.

### H2 — Volatility is a product-experience problem
Assets with extreme rolling volatility and deep drawdowns require stronger risk communication and education.

### H3 — Market activity is not the same as customer value
A market with high traded value does not automatically imply higher CoinDCX revenue, retention or profitability.

### H4 — Systematic investing is a credible product direction
CoinDCX's own public reporting shows strong growth in SIP activity. This creates a business reason to investigate systematic-investing journeys further using internal customer-level data.

---

## Analysis framework

### Step 1 — Market universe

Discover active INR markets from CoinDCX's public market-details endpoint rather than hard-coding exchange symbols.

### Step 2 — Time-series data

Pull daily OHLCV candles for selected assets.

### Step 3 — Quality checks

- Missing prices
- Negative volume
- Invalid OHLC relationships
- Duplicate asset/date observations
- Date ordering

### Step 4 — Feature engineering

- Daily return
- 30-day rolling volatility
- INR turnover proxy

### Step 5 — Decision metrics

- Total return
- Annualized return
- Annualized volatility
- Maximum drawdown
- Sharpe-style ratio
- Average/median turnover proxy

### Step 6 — Business segmentation

Compare:

**Core**
- BTC
- ETH
- SOL
- XRP

**Speculative**
- DOGE
- SHIB
- PEPE

The exact set of available INR markets can change, so the pipeline skips unavailable markets rather than fabricating observations.

---

## Product recommendations

### 1. Core Portfolio
Create a discovery experience centered on liquid core assets with clear risk indicators.

### 2. SIP / Recurring Investing
Use the market-risk analysis to design recurring-investment journeys around assets that demonstrate sustainable liquidity and acceptable risk characteristics.

### 3. Risk Lens
Show:

- 30-day volatility
- historical maximum drawdown
- recent drawdown
- liquidity proxy

next to asset discovery.

### 4. Education Layer
For very volatile assets, provide contextual explanations instead of presenting short-term percentage gains in isolation.

### 5. Diversification
Use correlation analysis to avoid presenting highly correlated assets as if they provide large diversification benefits.

---

## What an internal data scientist should validate next

The public analysis should be treated as a market-level diagnostic. To turn it into a production product decision, combine it with internal:

- user cohorts
- orders/fills
- trading fees
- deposits/withdrawals
- SIP creation/completion
- product activation
- KYC funnel
- customer support contacts
- retention/churn
- customer profitability

Then test:

> Do users exposed to core-asset education and systematic-investing features have better retention, activity quality and long-term value?

That would turn this portfolio project into a true product-analytics experiment.
