import pandas as pd
import streamlit as st
import plotly.express as px

import config


st.set_page_config(
    page_title="CoinDCX Market Analytics",
    page_icon="₿",
    layout="wide",
)

st.title("CoinDCX — End-to-End Crypto Market Analytics")
st.caption(
    "Real CoinDCX INR market data + official CoinDCX business context. "
    "Educational analytics only."
)

metrics_path = config.PROCESSED_DIR / "asset_metrics.csv"
data_path = config.PROCESSED_DIR / "daily_candles_clean.csv"

if not metrics_path.exists() or not data_path.exists():
    st.error(
        "Analysis files are missing. Run the pipeline first: "
        "`python -m src.fetch_data`, `python -m src.clean_data`, "
        "`python -m src.analyze`."
    )
    st.stop()

metrics = pd.read_csv(metrics_path)
df = pd.read_csv(data_path, parse_dates=["date"])

c1, c2, c3, c4 = st.columns(4)
c1.metric("Assets analysed", len(metrics))
c2.metric("Best total return", metrics.loc[metrics.total_return.idxmax(), "asset"])
c3.metric(
    "Lowest volatility",
    metrics.loc[metrics.annualized_volatility.idxmin(), "asset"],
)
c4.metric("Highest Sharpe-style score", metrics.loc[metrics.sharpe_0rf.idxmax(), "asset"])

st.subheader("Asset KPI table")
display = metrics.copy()
for col in [
    "total_return",
    "annualized_return",
    "annualized_volatility",
    "max_drawdown",
]:
    display[col] = display[col].map(lambda x: f"{x:.2%}")
display["sharpe_0rf"] = display["sharpe_0rf"].map(lambda x: f"{x:.2f}")
st.dataframe(display, use_container_width=True)

st.subheader("Normalized performance")
pivot = df.pivot(index="date", columns="asset", values="close").sort_index()
normalized = pivot / pivot.iloc[0] * 100
fig = px.line(normalized, title="Start = 100")
fig.update_yaxes(title="Index")
st.plotly_chart(fig, use_container_width=True)

st.subheader("30-day rolling annualized volatility")
vol = df.pivot(index="date", columns="asset", values="rolling_vol_30d").sort_index()
fig2 = px.line(vol, title="Rolling volatility")
fig2.update_yaxes(tickformat=".0%")
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Business lens")
st.markdown(
    """
**Decision question:** should a crypto platform emphasize core/utility-led assets
and systematic investing experiences rather than relying primarily on speculative activity?

Use the KPI table to compare return, risk, drawdown and the turnover proxy.
Remember that public market data cannot prove user retention, revenue or customer profitability.
"""
)
