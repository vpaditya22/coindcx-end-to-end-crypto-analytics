# Interview Questions & Model Answers

## 1. Why did you choose CoinDCX?

**Answer:**
I wanted to work with a real Indian fintech/crypto business rather than a synthetic dataset. CoinDCX provides public market-data APIs and publishes business/investor information, which allowed me to build a reproducible market analytics pipeline while being transparent about the limits of public customer data.

## 2. Why didn't you analyse customer churn?

**Answer:**
Customer-level churn requires customer-level data. CoinDCX's public API does not give me a complete anonymized customer transaction history for this project. I deliberately avoided fabricating users or transactions. I used public market data and official aggregate company disclosures instead.

## 3. Why use daily returns?

**Answer:**
Daily returns standardize price changes and make assets with very different price levels comparable. They are also the input for volatility, correlation and risk-adjusted performance calculations.

## 4. Why annualize volatility using 365?

**Answer:**
Crypto markets trade continuously, including weekends. For a daily crypto-return series, 365 is a more natural annualization convention than the 252 trading days commonly used for traditional equity markets.

## 5. What is maximum drawdown?

**Answer:**
It is the largest percentage fall from a previous running peak to a subsequent trough. It helps quantify the severity of a loss experience rather than only looking at average returns.

## 6. Why use Sharpe ratio?

**Answer:**
It provides a simple risk-adjusted performance comparison by relating annualized return to annualized volatility. I used a 0% risk-free assumption for this educational project and explicitly labelled it as a simplifying assumption.

## 7. What is your liquidity proxy?

**Answer:**
I approximate daily INR traded value as close price multiplied by target-asset volume from the candle. It is useful for relative market-activity comparison, but it is not CoinDCX revenue and should not be treated as exact exchange turnover.

## 8. What was your most important data-quality step?

**Answer:**
I validated OHLC relationships, removed duplicate asset-date observations, checked missing values, ensured positive prices and non-negative volume, and sorted the data chronologically before calculating returns.

## 9. What would you do with more data?

**Answer:**
I would add order-book depth, bid-ask spread, trade-level data and longer historical windows. With internal data, I would add customer cohorts, fee revenue, SIP behaviour, retention and profitability.

## 10. What business decision does the project support?

**Answer:**
It supports a product strategy where core assets, systematic investing and risk-aware education can be prioritized based on market characteristics. The analysis does not claim that one token will outperform in the future.

## 11. What is the biggest limitation?

**Answer:**
The largest limitation is that market-level data cannot prove customer-level outcomes. I can identify market behaviour and product hypotheses, but I cannot infer CoinDCX customer churn, LTV or revenue from public candle data alone.

## 12. If a manager asks for one KPI, what would you choose?

**Answer:**
For this specific market strategy, I would use a combination rather than a single KPI: risk-adjusted return, drawdown and liquidity. For the actual product, I would pair those with customer metrics such as recurring-investment completion, retention and contribution margin.

## 13. How would you productionize this?

**Answer:**
I would schedule API ingestion, store immutable raw data, create validated staging tables, build a warehouse model, add data-quality tests, orchestrate the pipeline, and publish the KPI layer to a BI dashboard.

## 14. Why is this better than a crypto price-prediction project?

**Answer:**
Price prediction focuses heavily on model accuracy. This project demonstrates the broader analyst workflow: data acquisition, cleaning, KPI design, statistical analysis, visualization, business framing, limitations and recommendations. That is closer to what a business/data analyst does in an organization.
