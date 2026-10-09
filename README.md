# CoinDCX End-to-End Crypto Market Analytics

## Portfolio project: turning real CoinDCX market data into a business decision

**Business question**

> How should an Indian crypto platform prioritize assets and investor experiences when deciding between core/utility-led assets and higher-speculation assets?

This is a **real-data portfolio project** built around **CoinDCX**, an Indian crypto platform. It does **not** fabricate users, orders, revenue, cohorts, or transactions.

The project combines:

1. **Live/public CoinDCX market data** from its official API
2. **Official CoinDCX investor/transparency reports** for business context
3. Python-based ETL, validation, EDA and statistical analysis
4. A business narrative with recommendations
5. Optional Streamlit dashboard

### Why this is portfolio-worthy

It demonstrates:

- Python
- pandas / NumPy
- REST API ingestion
- Data cleaning and validation
- Financial time-series analysis
- KPI design
- Risk/return analysis
- Correlation analysis
- Rolling volatility and drawdown
- Business storytelling
- Reproducible project structure
- Dashboarding
- Git/GitHub documentation

---

## Important data-integrity rule

CoinDCX does **not** publicly expose a complete anonymized customer-level dataset in the sources used here. Therefore this project does **not** invent:

- DAU/MAU
- customer cohorts
- customer retention
- individual trading behaviour
- customer revenue
- LTV
- churn
- conversion rates

Instead, it analyzes **real exchange-market data** and uses official company-reported aggregate facts only where explicitly cited.

That distinction is important in a professional analytics portfolio.

---

# 1. Business context

CoinDCX's H1 2026 investor report states that investors increasingly concentrated portfolios around Bitcoin, Ethereum, Solana and XRP, while meme-token volume share fell to 12.17% and Layer-1 assets represented 32.87% of trading volume.

CoinDCX also reported more than 2.2 crore registered users in H1 2026.

The business hypothesis for this project is therefore:

> **If utility/core assets are becoming more important while speculative-token share declines, CoinDCX may have an opportunity to emphasize recurring investing, portfolio construction, education and risk-aware discovery around liquid core assets rather than relying primarily on speculative-token activity.**

The Python analysis tests the market-data side of that story by measuring:

- Return
- Volatility
- Maximum drawdown
- Risk-adjusted return
- Liquidity/turnover proxy
- Correlation
- Rolling volatility
- Relative performance

---

# 2. Real sources

### CoinDCX official API documentation
The official API exposes public ticker, market-details, trades, order-book and candlestick endpoints.

- API base: `https://api.coindcx.com`
- Candles endpoint: `/market_data/candles`
- INR market pairs can be discovered from `/exchange/v1/markets_details`

The API documentation says candle intervals include `1m`, `15m`, `1h`, and `1d`, with a maximum of 1,000 records per request.

### CoinDCX H1 2026 Investor Report

Officially reported facts used in the business narrative:

- Bitcoin: 22.43% market dominance in the cited CoinDCX analysis
- Meme-token volume share: 12.17%
- Layer-1 asset volume share: 32.87%
- Average investor age: 30–31
- Registered users: 2.2 crore+
- BTC, ETH, SOL and XRP appeared consistently among top portfolios across major Indian crypto markets

### CoinDCX 2025 Annual Report

Officially reported facts include:

- ₹51,333 crore total spot trading volume
- ₹4,277.75 crore average monthly trading volume
- 5.72 lakh SIPs created in 2025
- SIP-holder growth of 623% from 2024 to 2025
- 3.29 lakh Earn users
- 2+ crore verified users

---

# 3. Architecture

```text
                    ┌──────────────────────┐
                    │ CoinDCX Public API   │
                    │ Market Details       │
                    │ Daily Candles        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │      INGESTION       │
                    │ fetch_data.py         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ RAW CSV / JSON       │
                    │ data/raw             │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ CLEAN + VALIDATE     │
                    │ clean_data.py        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ FEATURE ENGINEERING  │
                    │ metrics.py           │
                    └──────────┬───────────┘
                               │
                               ▼
          ┌────────────────────┴────────────────────┐
          │                                         │
          ▼                                         ▼
┌─────────────────────┐                 ┌─────────────────────┐
│ Statistical Outputs │                 │ Visual Outputs     │
│ KPI tables          │                 │ PNG charts         │
│ correlation matrix  │                 │ performance        │
│ risk metrics        │                 │ volatility         │
└──────────┬──────────┘                 └──────────┬──────────┘
           │                                       │
           └──────────────────┬────────────────────┘
                              ▼
                   ┌──────────────────────┐
                   │ BUSINESS NARRATIVE   │
                   │ business_summary.md  │
                   └──────────────────────┘
```

---

# 4. Repository structure

```text
coindcx-end-to-end-analytics/
│
├── README.md
├── requirements.txt
├── .gitignore
├── config.py
│
├── src/
│   ├── __init__.py
│   ├── fetch_data.py
│   ├── clean_data.py
│   ├── metrics.py
│   ├── analyze.py
│   └── business_report.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── outputs/
│   └── figures/
│
├── reports/
│   ├── business_facts.json
│   └── business_summary.md
│
├── notebooks/
│   └── analysis_walkthrough.ipynb
│
└── app.py
```

---

# 5. Setup

```bash
git clone <your-repository-url>
cd coindcx-end-to-end-analytics

python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Install:

```bash
pip install -r requirements.txt
```

---

# 6. Run the complete pipeline

### Step 1 — Fetch real CoinDCX data

```bash
python -m src.fetch_data
```

This discovers active INR markets and downloads daily candles for the configured assets.

### Step 2 — Clean and validate

```bash
python -m src.clean_data
```

### Step 3 — Run analysis

```bash
python -m src.analyze
```

### Step 4 — Generate business narrative

```bash
python -m src.business_report
```

### Step 5 — Load the SQL database

```bash
python -m src.load_sqlite
```

This creates `data/processed/coindcx_analytics.db` containing the cleaned candle table and asset KPI table.

You can then use the queries in:

```text
sql/02_business_questions.sql
```

### Optional — launch dashboard

```bash
streamlit run app.py
```

---

# 7. Core KPIs

The project calculates:

### Cumulative return

```text
Ending Price / Starting Price - 1
```

### Annualized volatility

```text
Std(daily returns) × √365
```

Crypto trades continuously, so 365 is used rather than 252.

### Maximum drawdown

```text
Price / Running Maximum - 1
```

### Sharpe ratio

```text
Annualized Return / Annualized Volatility
```

A risk-free rate of 0% is used as a simplifying portfolio-analysis assumption. This is not an investment recommendation.

### Liquidity proxy

```text
Daily candle volume × closing price
```

For INR pairs this approximates INR-denominated traded value based on the candle's target-asset volume. It should be treated as a **proxy**, not official exchange revenue or exact platform turnover.

---

# 8. Business recommendations framework

The analysis should not automatically conclude that the highest-return token is the best business opportunity.

Instead, interpret assets across four dimensions:

| Dimension | Business interpretation |
|---|---|
| Return | Growth / investor interest |
| Volatility | Risk and education requirement |
| Drawdown | Potential user-loss experience |
| Liquidity proxy | Market depth/activity proxy |

The preferred product strategy is to identify assets that combine:

- strong liquidity
- manageable risk relative to peers
- sustained investor relevance
- suitability for recurring-investment products

---

# 9. Expected business narrative

The final report should answer:

### Finding 1 — Core assets

Do BTC/ETH/SOL/XRP demonstrate a better combination of liquidity and risk characteristics than speculative assets?

### Finding 2 — Volatility

Which assets create the greatest user-experience risk because of extreme volatility?

### Finding 3 — Diversification

Which assets move together and therefore provide limited diversification?

### Finding 4 — Product opportunity

Could CoinDCX emphasize:

- SIP/recurring investing
- core-asset portfolio baskets
- risk education
- volatility alerts
- drawdown-aware onboarding
- liquidity-aware token discovery

rather than optimizing only for short-term speculative activity?

---

# 10. What NOT to claim

Do not write:

> "CoinDCX users are losing money."

The public market dataset does not identify individual user positions.

Do not write:

> "This token caused CoinDCX revenue to increase."

Market price/volume data alone cannot establish company revenue.

Instead write:

> "The market-data analysis indicates..."

or:

> "CoinDCX's published investor report states..."

This makes the portfolio project analytically credible.

---

# 11. Interview explanation

A strong 60-second explanation:

> "I built an end-to-end analytics project around CoinDCX using real public exchange data rather than a synthetic customer dataset. I automated ingestion of INR market metadata and daily candlestick data through CoinDCX's public API, cleaned and validated the time series, then calculated returns, annualized volatility, maximum drawdown, Sharpe ratio, liquidity proxies and asset correlations. I combined those quantitative results with official CoinDCX investor-report facts to answer a business question: whether an Indian crypto platform should increasingly emphasize core and utility-led investing rather than speculative-token activity. The final output is a reproducible pipeline, KPI tables, visualizations and a Streamlit dashboard."

---

# 12. Skills demonstrated

**Technical**

- Python
- pandas
- NumPy
- requests
- matplotlib
- seaborn
- Streamlit
- REST APIs
- ETL
- Time-series analysis
- Data validation
- Git/GitHub

**Analytics**

- KPI design
- Risk analysis
- Correlation
- Rolling statistics
- Drawdown analysis
- Business segmentation
- Decision-oriented storytelling

**Business**

- Product analytics
- Marketplace analytics
- Fintech analytics
- Risk analytics
- Investment-product strategy

---

# 13. Portfolio positioning

Recommended GitHub repository name:

`coindcx-end-to-end-crypto-analytics`

Recommended resume bullet:

> **Built an end-to-end crypto-market analytics pipeline using real CoinDCX API data; engineered return, volatility, drawdown, Sharpe and liquidity KPIs across INR crypto markets and translated findings into product and investment-experience recommendations.**

Second bullet:

> **Integrated official CoinDCX investor-report metrics with Python time-series analysis to evaluate the shift from speculative-token activity toward core/utility-led investing.**

---

## Disclaimer

This is an educational analytics project, not financial advice. Crypto assets are highly volatile and risky. The analysis does not recommend buying or selling any asset.

CoinDCX API data and terms may change. Check the current official documentation before using the API commercially or redistributing derived market data.


---

# 14. SQL business questions

The project includes a SQLite layer so the portfolio demonstrates both Python and SQL.

Example questions:

- Rank assets by total return.
- Rank assets by risk-adjusted return.
- Find deepest drawdowns.
- Compare core assets.
- Identify high-risk/high-return assets.
- Rank markets using the liquidity proxy.

See `sql/02_business_questions.sql`.

---

# 15. Interview preparation

See:

- `reports/BUSINESS_CASE.md`
- `reports/INTERVIEW_QA.md`
- `GITHUB_CHECKLIST.md`

These explain the business logic, limitations and how to present the project in a Data Analyst/Product Analyst interview.

---

# 16. Important compliance/data note

The repository intentionally does not require committing downloaded CoinDCX market data. CoinDCX's API terms govern use of its Market Data, so review the current terms before redistributing raw or derived datasets. The recommended GitHub approach is to publish the reproducible ingestion and analysis code while keeping downloaded data out of the public repository when required.


---

# 17. Real CoinDCX snapshot included in this analysis

A real CoinDCX market snapshot was supplied for this project and incorporated into:

```text
data/raw/coindcx_snapshot_supplied.csv
data/processed/coindcx_inr_snapshot_analysis.csv
data/processed/inr_market_ranking.csv
data/processed/core_vs_speculative.csv
```

The supplied snapshot contains market-level fields such as last price, 24-hour change, high, low, volume, bid, ask and timestamp.

Because it is a **single snapshot**, this layer focuses on:

- 24-hour market movement
- turnover proxy
- bid-ask spread
- quote quality
- core vs speculative segmentation

It does **not** claim historical volatility, drawdown or Sharpe results.

See `reports/snapshot_business_report.md`.

> **GitHub caution:** The supplied raw snapshot should only be committed to a public repository after reviewing the current CoinDCX API/data terms. The recommended public repository can contain the code and methodology while keeping restricted market data local.


---

# 18. Data integrity note for the supplied snapshot

The supplied CoinDCX ticker snapshot is used for **snapshot/microstructure analysis**.

The project intentionally avoids treating `ticker volume × price` as an exact INR
turnover KPI because the official ticker documentation does not establish a
single cross-market unit for the returned `volume` field. CoinDCX's candle
documentation separately defines candle volume in terms of target currency.

The snapshot analysis therefore emphasizes:

- 24-hour price change
- bid/ask spread
- spread as % of midpoint
- quote availability
- core vs speculative segmentation

Historical return, volatility, drawdown and Sharpe calculations require the
separate daily-candle dataset.

This distinction is deliberate: the portfolio should demonstrate analytical
judgment rather than manufacture a misleading KPI.
