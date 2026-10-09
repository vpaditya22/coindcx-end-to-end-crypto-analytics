# CoinDCX — Market & Product Analytics Case Study

## Problem

CoinDCX operates in a market where investor behaviour is shifting toward more
structured and utility-led allocation. The project asks how market data can
inform asset discovery, risk communication and systematic-investing product
strategy.

## Data

- Real CoinDCX ticker snapshot supplied for analysis: 58 total markets
  (35 INR pairs)
- Snapshot timestamp: 2026-09-04T12:20:06+00:00
- Official CoinDCX H1 2026 report
- CoinDCX public API documentation

## Analysis

### Snapshot layer
- 24-hour price movement
- bid/ask availability
- quoted spread
- spread % of midpoint
- core vs speculative segmentation

### Historical layer
Run the API ingestion pipeline for daily candles to calculate:
- return
- volatility
- drawdown
- Sharpe-style ratio
- correlation
- rolling risk

## Business recommendation

Prioritize a **risk-aware core-asset discovery and systematic-investing experience**,
while using high-volatility assets with stronger contextual education and
disclosures.

This is a hypothesis for product testing—not a claim of causality.

## What would validate the recommendation?

Use internal CoinDCX data to test:
- SIP adoption
- SIP completion
- repeat investing
- 30/90/180-day retention
- trading activity quality
- contribution margin
- support contacts
- customer risk outcomes

## Why this is a strong analyst project

It demonstrates that the analyst can:
1. obtain real data,
2. validate its meaning,
3. avoid invalid metrics,
4. quantify market behaviour,
5. translate findings into product hypotheses,
6. state limitations clearly,
7. identify the internal data needed to prove the business case.
