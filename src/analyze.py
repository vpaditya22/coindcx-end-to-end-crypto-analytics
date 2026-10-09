import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import config
from src.metrics import build_metrics, build_correlation


def save_performance_chart(df):
    pivot = df.pivot(index="date", columns="asset", values="close").sort_index()
    normalized = pivot / pivot.iloc[0] * 100

    plt.figure(figsize=(13, 7))
    normalized.plot(ax=plt.gca())
    plt.title("CoinDCX INR Assets — Normalized Price Performance")
    plt.xlabel("Date")
    plt.ylabel("Index (Start = 100)")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(config.FIGURE_DIR / "01_normalized_performance.png", dpi=180)
    plt.close()


def save_volatility_chart(df):
    pivot = (
        df.pivot(index="date", columns="asset", values="rolling_vol_30d")
        .sort_index()
    )

    plt.figure(figsize=(13, 7))
    pivot.plot(ax=plt.gca())
    plt.title("30-Day Rolling Annualized Volatility")
    plt.xlabel("Date")
    plt.ylabel("Annualized volatility")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(config.FIGURE_DIR / "02_rolling_volatility.png", dpi=180)
    plt.close()


def save_drawdown_chart(df):
    lines = {}
    for asset, group in df.groupby("asset"):
        group = group.sort_values("date")
        lines[asset] = group["close"] / group["close"].cummax() - 1

    dd = pd.DataFrame(lines, index=df["date"].drop_duplicates().sort_values())

    plt.figure(figsize=(13, 7))
    dd.plot(ax=plt.gca())
    plt.title("Drawdown From Previous Peak")
    plt.xlabel("Date")
    plt.ylabel("Drawdown")
    plt.grid(alpha=0.25)
    plt.tight_layout()
    plt.savefig(config.FIGURE_DIR / "03_drawdown.png", dpi=180)
    plt.close()


def save_correlation(corr):
    plt.figure(figsize=(9, 7))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="RdBu_r", center=0)
    plt.title("Daily Return Correlation")
    plt.tight_layout()
    plt.savefig(config.FIGURE_DIR / "04_correlation.png", dpi=180)
    plt.close()


def main():
    input_path = config.PROCESSED_DIR / "daily_candles_clean.csv"
    df = pd.read_csv(input_path, parse_dates=["date"])

    metrics = build_metrics(df)
    correlation = build_correlation(df)

    metrics.to_csv(config.PROCESSED_DIR / "asset_metrics.csv", index=False)
    correlation.to_csv(config.PROCESSED_DIR / "return_correlation.csv")

    save_performance_chart(df)
    save_volatility_chart(df)
    save_drawdown_chart(df)
    save_correlation(correlation)

    print("\nAsset KPI table:")
    print(metrics.to_string(index=False))

    print("\nCorrelation:")
    print(correlation.round(2).to_string())

    print("\nAnalysis complete.")


if __name__ == "__main__":
    main()
