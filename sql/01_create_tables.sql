
-- SQLite analytical layer
-- The Python pipeline creates the SQLite database and loads these tables.

DROP TABLE IF EXISTS daily_candles;
CREATE TABLE daily_candles (
    asset TEXT NOT NULL,
    pair TEXT NOT NULL,
    date TEXT NOT NULL,
    open REAL,
    high REAL,
    low REAL,
    close REAL NOT NULL,
    volume REAL,
    daily_return REAL,
    turnover_proxy_inr REAL,
    rolling_vol_30d REAL,
    PRIMARY KEY (asset, date)
);

DROP TABLE IF EXISTS asset_metrics;
CREATE TABLE asset_metrics (
    asset TEXT PRIMARY KEY,
    pair TEXT,
    start_date TEXT,
    end_date TEXT,
    observations INTEGER,
    start_price_inr REAL,
    end_price_inr REAL,
    total_return REAL,
    annualized_return REAL,
    annualized_volatility REAL,
    max_drawdown REAL,
    sharpe_0rf REAL,
    avg_daily_turnover_proxy_inr REAL,
    median_daily_turnover_proxy_inr REAL
);
