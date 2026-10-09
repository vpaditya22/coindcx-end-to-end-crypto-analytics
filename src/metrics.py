import numpy as np
import pandas as pd


def max_drawdown(series: pd.Series) -> float:
    running_max = series.cummax()
    drawdown = series / running_max - 1
    return float(drawdown.min())


def annualized_return(series: pd.Series, periods_per_year: int = 365) -> float:
    if len(series) < 2:
        return np.nan

    total_return = series.iloc[-1] / series.iloc[0]
    years = (len(series) - 1) / periods_per_year

    if total_return <= 0 or years <= 0:
        return np.nan

    return float(total_return ** (1 / years) - 1)


def calculate_asset_metrics(group: pd.DataFrame) -> dict:
    group = group.sort_values("date")
    prices = group["close"].astype(float)
    returns = group["daily_return"].dropna()

    ann_return = annualized_return(prices)
    ann_vol = returns.std() * np.sqrt(365) if len(returns) else np.nan

    sharpe = ann_return / ann_vol if ann_vol and ann_vol > 0 else np.nan

    return {
        "asset": group["asset"].iloc[0],
        "pair": group["pair"].iloc[0],
        "start_date": group["date"].min().date().isoformat(),
        "end_date": group["date"].max().date().isoformat(),
        "observations": len(group),
        "start_price_inr": prices.iloc[0],
        "end_price_inr": prices.iloc[-1],
        "total_return": prices.iloc[-1] / prices.iloc[0] - 1,
        "annualized_return": ann_return,
        "annualized_volatility": ann_vol,
        "max_drawdown": max_drawdown(prices),
        "sharpe_0rf": sharpe,
        "avg_daily_turnover_proxy_inr": group["turnover_proxy_inr"].mean(),
        "median_daily_turnover_proxy_inr": group["turnover_proxy_inr"].median(),
    }


def build_metrics(df: pd.DataFrame) -> pd.DataFrame:
    rows = [calculate_asset_metrics(g) for _, g in df.groupby("asset")]
    return pd.DataFrame(rows).sort_values("sharpe_0rf", ascending=False)


def build_correlation(df: pd.DataFrame) -> pd.DataFrame:
    pivot = df.pivot(index="date", columns="asset", values="daily_return")
    return pivot.corr()
