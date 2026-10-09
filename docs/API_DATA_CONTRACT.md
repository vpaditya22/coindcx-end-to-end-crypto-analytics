# API Data Contract

## Market discovery

The ingestion stage expects a list of market-detail objects and filters for active INR markets. It uses target asset ticker and pair identifier to label downloaded candles.

## Candle retrieval

The ingestion stage requests candles using pair, interval, start time, end time and limit parameters. A successful response should be a JSON list of candle-like records.

## Defensive expectations

- Raise HTTP errors rather than silently treating failed requests as valid empty datasets.
- Handle empty candle responses explicitly.
- Keep requested and downloaded asset lists in run metadata.
- Validate numeric fields after ingestion.
- Re-check official CoinDCX documentation if response fields or parameter names change.

This describes the shape expected by the current code; it is not a guarantee that the external API will remain unchanged.
