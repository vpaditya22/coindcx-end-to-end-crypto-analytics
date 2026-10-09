from pathlib import Path
from datetime import date, timedelta

ROOT = Path(__file__).resolve().parent
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
FIGURE_DIR = ROOT / "outputs" / "figures"
REPORT_DIR = ROOT / "reports"

API_BASE = "https://api.coindcx.com"

# One year of daily market data. The API returns up to 1,000 candles/request.
END_DATE = date.today()
START_DATE = END_DATE - timedelta(days=365)

# Business-oriented asset groups. The ingestion layer will skip an asset if
# an active INR pair is not available on CoinDCX at run time.
CORE_ASSETS = ["BTC", "ETH", "SOL", "XRP"]
SPECULATIVE_ASSETS = ["DOGE", "SHIB", "PEPE"]

ALL_ASSETS = CORE_ASSETS + SPECULATIVE_ASSETS

INTERVAL = "1d"
REQUEST_LIMIT = 1000
REQUEST_TIMEOUT = 30

for folder in [RAW_DIR, PROCESSED_DIR, FIGURE_DIR, REPORT_DIR]:
    folder.mkdir(parents=True, exist_ok=True)
