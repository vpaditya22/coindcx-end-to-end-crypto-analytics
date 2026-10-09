import numpy as np
import pandas as pd

import config


NUMERIC_COLUMNS = ["open", "high", "low", "close", "volume", "time"]


def main():
    input_path = config.RAW_DIR / "daily_candles.csv"
    output_path = config.PROCESSED_DIR / "daily_candles_clean.csv"

    df = pd.read_csv(input_path)

    required = {"asset", "pair", *NUMERIC_COLUMNS}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")

    for col in NUMERIC_COLUMNS:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df["date"] = pd.to_datetime(df["time"], unit="ms", utc=True).dt.date
    df["date"] = pd.to_datetime(df["date"])

    df = df.dropna(subset=["asset", "date", "close"])
    df = df[df["close"] > 0]
    df = df[df["volume"] >= 0]

    # Basic OHLC integrity checks.
    df = df[df["high"] >= df["low"]]
    df = df[df["high"] >= df["open"]]
    df = df[df["high"] >= df["close"]]
    df = df[df["low"] <= df["open"]]
    df = df[df["low"] <= df["close"]]

    df = df.sort_values(["asset", "date"])
    df = df.drop_duplicates(["asset", "date"], keep="last")

    # Feature engineering.
    df["daily_return"] = df.groupby("asset")["close"].pct_change()
    df["turnover_proxy_inr"] = df["close"] * df["volume"]

    df["rolling_vol_30d"] = (
        df.groupby("asset")["daily_return"]
        .rolling(30)
        .std()
        .reset_index(level=0, drop=True)
        * np.sqrt(365)
    )

    df.to_csv(output_path, index=False)

    validation = {
        "rows": len(df),
        "assets": sorted(df["asset"].unique().tolist()),
        "duplicate_asset_date": int(df.duplicated(["asset", "date"]).sum()),
        "missing_close": int(df["close"].isna().sum()),
        "negative_volume": int((df["volume"] < 0).sum()),
    }

    print("Validation summary:")
    for key, value in validation.items():
        print(f"  {key}: {value}")

    print(f"Saved cleaned dataset to {output_path}")


if __name__ == "__main__":
    main()
