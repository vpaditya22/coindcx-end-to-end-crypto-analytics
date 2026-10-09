import sqlite3
import pandas as pd
import config


def main():
    db_path = config.PROCESSED_DIR / "coindcx_analytics.db"

    candles_path = config.PROCESSED_DIR / "daily_candles_clean.csv"
    metrics_path = config.PROCESSED_DIR / "asset_metrics.csv"
    snapshot_path = config.PROCESSED_DIR / "coindcx_inr_snapshot_analysis.csv"

    with sqlite3.connect(db_path) as conn:
        if candles_path.exists():
            pd.read_csv(candles_path).to_sql(
                "daily_candles", conn, if_exists="replace", index=False
            )
        if metrics_path.exists():
            pd.read_csv(metrics_path).to_sql(
                "asset_metrics", conn, if_exists="replace", index=False
            )
        if snapshot_path.exists():
            pd.read_csv(snapshot_path).to_sql(
                "coindcx_inr_snapshot", conn, if_exists="replace", index=False
            )

    print(f"SQLite database created: {db_path}")


if __name__ == "__main__":
    main()
