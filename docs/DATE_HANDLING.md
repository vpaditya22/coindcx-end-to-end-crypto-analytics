# Date Handling

CoinDCX candle timestamps are interpreted as Unix epoch milliseconds and converted to UTC. The cleaner then normalizes timestamps to calendar dates for daily grouping.

This matters because a timestamp near midnight can fall on a different date in another timezone. Keep the timezone convention consistent across ingestion, cleaning, duplicate handling and comparisons. If the source changes timestamp units or interval semantics, update both code and tests.
