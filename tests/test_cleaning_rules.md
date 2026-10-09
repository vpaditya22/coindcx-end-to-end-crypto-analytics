# Cleaning-rule test plan

The cleaner should be tested with small, deterministic fixtures before relying on live API data.

- Missing required columns should raise a clear error.
- Numeric strings should convert to numeric values.
- A non-numeric close should be discarded.
- Zero or negative close values should be discarded.
- Negative volume should be discarded.
- Invalid OHLC bounds should be discarded.
- Duplicate asset/date records should resolve deterministically after sorting.
- Daily returns should be computed within each asset, never across assets.
- The output should contain at most one row per asset/date pair.

This checklist complements the executable tests in the `tests/` directory.
