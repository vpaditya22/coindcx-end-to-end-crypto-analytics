import json
from pathlib import Path

import pandas as pd

import config


def pct(x):
    return f"{x:.2%}" if pd.notna(x) else "N/A"


def money(x):
    if pd.isna(x):
        return "N/A"
    if x >= 1e7:
        return f"₹{x/1e7:.2f} Cr"
    if x >= 1e5:
        return f"₹{x/1e5:.2f} L"
    return f"₹{x:,.0f}"


def main():
    metrics_path = config.PROCESSED_DIR / "asset_metrics.csv"
    metrics = pd.read_csv(metrics_path)

    facts = json.loads(
        (config.REPORT_DIR / "business_facts.json").read_text(encoding="utf-8")
    )

    lines = []
    lines.append("# CoinDCX Business Analysis\n")
    lines.append(
        "## Executive summary\n"
        "This report combines real CoinDCX public INR market data with official "
        "CoinDCX-reported business context. It does not use fabricated customer "
        "transactions or invented revenue.\n"
    )

    lines.append("## Official business context\n")
    f = facts["facts"]
    lines.append(
        f"- CoinDCX reported **{f['reported_registered_users_h1_2026']} registered users** "
        "in H1 2026.\n"
    )
    lines.append(
        f"- Its H1 2026 report stated **{f['meme_token_volume_share_reported']}** "
        "meme-token volume share and **{f['layer_1_volume_share_reported']}** "
        "Layer-1 asset volume share.\n"
    )
    lines.append(
        "- The same report highlighted Bitcoin, Ethereum, Solana and XRP as recurring "
        "core assets across leading Indian portfolios.\n"
    )

    lines.append("## Quantitative findings\n")

    top_return = metrics.sort_values("total_return", ascending=False).iloc[0]
    lowest_vol = metrics.sort_values("annualized_volatility", ascending=True).iloc[0]
    deepest_dd = metrics.sort_values("max_drawdown", ascending=True).iloc[0]
    top_sharpe = metrics.sort_values("sharpe_0rf", ascending=False).iloc[0]
    top_liquidity = metrics.sort_values(
        "avg_daily_turnover_proxy_inr", ascending=False
    ).iloc[0]

    lines.append(
        f"- **Highest total return in the downloaded period:** {top_return.asset} "
        f"({pct(top_return.total_return)}).\n"
    )
    lines.append(
        f"- **Lowest annualized volatility:** {lowest_vol.asset} "
        f"({pct(lowest_vol.annualized_volatility)}).\n"
    )
    lines.append(
        f"- **Deepest maximum drawdown:** {deepest_dd.asset} "
        f"({pct(deepest_dd.max_drawdown)}).\n"
    )
    lines.append(
        f"- **Highest Sharpe-style score with a 0% risk-free assumption:** "
        f"{top_sharpe.asset} ({top_sharpe.sharpe_0rf:.2f}).\n"
    )
    lines.append(
        f"- **Highest average turnover proxy:** {top_liquidity.asset} "
        f"({money(top_liquidity.avg_daily_turnover_proxy_inr)} per day).\n"
    )

    lines.append("## Business interpretation\n")
    lines.append(
        "1. **Prioritize core-asset discovery.** If the quantitative analysis shows "
        "that BTC/ETH/SOL/XRP combine stronger liquidity with comparatively manageable "
        "risk, they are natural candidates for recurring-investment journeys, portfolio "
        "baskets and educational content.\n"
    )
    lines.append(
        "2. **Make volatility visible.** Assets with very high rolling volatility or "
        "deep drawdowns should receive stronger risk disclosures, volatility indicators "
        "and education rather than being presented only through short-term returns.\n"
    )
    lines.append(
        "3. **Do not equate activity with quality.** A high turnover proxy can indicate "
        "market activity, but it is not the same thing as customer profitability, "
        "company revenue, retention or product-market fit.\n"
    )
    lines.append(
        "4. **Build systematic-investing journeys.** CoinDCX's own annual-report "
        "disclosures around SIP growth make recurring investing a credible product "
        "theme to investigate further with internal customer-level data.\n"
    )

    lines.append("## What additional internal data would unlock\n")
    lines.extend(
        [
            "- User-level deposits and withdrawals\n",
            "- Orders and fills\n",
            "- Trading fees and GST\n",
            "- TDS amounts\n",
            "- Product adoption by user cohort\n",
            "- SIP creation and completion rates\n",
            "- Earn activation and retention\n",
            "- Customer support events\n",
            "- KYC funnel events\n",
        ]
    )

    lines.append("## Limitation\n")
    lines.append(
        "This analysis uses public market data and company-reported aggregate facts. "
        "It cannot establish customer profitability, churn, causality or CoinDCX revenue. "
        "Crypto markets are highly volatile and this project is not investment advice.\n"
    )

    output = "\n".join(lines)
    path = config.REPORT_DIR / "business_summary.md"
    path.write_text(output, encoding="utf-8")
    print(output)
    print(f"\nSaved report to {path}")


if __name__ == "__main__":
    main()
