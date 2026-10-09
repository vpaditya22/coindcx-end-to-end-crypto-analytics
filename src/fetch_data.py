import json
import time
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd
import requests

import config


SESSION = requests.Session()
SESSION.headers.update({"User-Agent": "coindcx-analytics-portfolio/1.0"})


def get_json(url: str, params=None):
    response = SESSION.get(url, params=params, timeout=config.REQUEST_TIMEOUT)
    response.raise_for_status()
    return response.json()


def discover_inr_pairs():
    url = f"{config.API_BASE}/exchange/v1/markets_details"
    rows = get_json(url)

    records = []
    for row in rows:
        if (
            row.get("status") == "active"
            and row.get("base_currency_short_name") == "INR"
        ):
            records.append(
                {
                    "asset": row.get("target_currency_short_name"),
                    "pair": row.get("pair"),
                    "symbol": row.get("symbol"),
                    "target_name": row.get("target_currency_name"),
                    "status": row.get("status"),
                }
            )

    df = pd.DataFrame(records).drop_duplicates("asset")
    df.to_csv(config.RAW_DIR / "inr_market_details.csv", index=False)
    return df


def fetch_candles(pair: str, start_ms: int, end_ms: int):
    url = f"{config.API_BASE}/market_data/candles"
    params = {
        "pair": pair,
        "interval": config.INTERVAL,
        "startTime": start_ms,
        "endTime": end_ms,
        "limit": config.REQUEST_LIMIT,
    }
    data = get_json(url, params=params)

    if not data:
        return pd.DataFrame()

    return pd.DataFrame(data)


def main():
    print("Discovering active CoinDCX INR markets...")
    markets = discover_inr_pairs()

    selected = markets[markets["asset"].isin(config.ALL_ASSETS)].copy()

    if selected.empty:
        raise RuntimeError(
            "None of the configured assets currently have an active INR market."
        )

    print("Available configured assets:")
    print(selected[["asset", "pair", "target_name"]].to_string(index=False))

    start_ms = int(
        datetime(
            config.START_DATE.year,
            config.START_DATE.month,
            config.START_DATE.day,
            tzinfo=timezone.utc,
        ).timestamp()
        * 1000
    )
    end_ms = int(
        datetime(
            config.END_DATE.year,
            config.END_DATE.month,
            config.END_DATE.day,
            23,
            59,
            59,
            tzinfo=timezone.utc,
        ).timestamp()
        * 1000
    )

    all_frames = []

    for _, row in selected.iterrows():
        print(f"Fetching {row['asset']} ({row['pair']})...")
        candles = fetch_candles(row["pair"], start_ms, end_ms)

        if candles.empty:
            print(f"  No candle data returned for {row['asset']}.")
            continue

        candles["asset"] = row["asset"]
        candles["pair"] = row["pair"]
        candles["target_name"] = row["target_name"]
        all_frames.append(candles)

        time.sleep(0.25)

    if not all_frames:
        raise RuntimeError("No candle data was downloaded.")

    raw = pd.concat(all_frames, ignore_index=True)
    raw.to_csv(config.RAW_DIR / "daily_candles.csv", index=False)

    metadata = {
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "start_date": str(config.START_DATE),
        "end_date": str(config.END_DATE),
        "assets_requested": config.ALL_ASSETS,
        "assets_downloaded": sorted(raw["asset"].unique().tolist()),
        "row_count": int(len(raw)),
    }

    (config.RAW_DIR / "run_metadata.json").write_text(
        json.dumps(metadata, indent=2),
        encoding="utf-8",
    )

    print(f"Saved {len(raw):,} rows to {config.RAW_DIR / 'daily_candles.csv'}")


if __name__ == "__main__":
    main()
