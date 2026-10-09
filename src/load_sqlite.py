import sqlite3
import pandas as pd
import config


def main():
    db_path = config.PROCESSED_DIR / "coindcx_analytics.db"

    candles_path = config.PROCESSED_DIR / "daily_candles_clean.csv"
    metrics_path = config.PROCESSED_DIR / "asset_metrics.csv"
    snapshot_path = config.PROCESSED_DIR / "coindcx_inr_snapshot_analysis.csv"

    inputs = [
        ("daily_candles", candles_path),
        ("asset_metrics", metrics_path),
        ("coindcx_inr_snapshot", snapshot_path),
    ]
    available = [(table, path) for table, path in inputs if path.exists()]
    if not available:
        raise FileNotFoundError(
            "No processed CSV inputs found. Run the cleaning and analysis stages first."
        )

    loaded = {}
    with sqlite3.connect(db_path) as conn:
        for table, path in available:
            frame = pd.read_csv(path)
            frame.to_sql(table, conn, if_exists="replace", index=False)
            loaded[table] = len(frame)

    print(f"SQLite database created: {db_path}")
    for table, rows in loaded.items():
        print(f"  {table}: {rows:,} rows")


if __name__ == "__main__":
    main()
