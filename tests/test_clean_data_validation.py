import numpy as np
import pandas as pd
import pytest

from src import clean_data


COLUMNS = ["asset", "pair", "open", "high", "low", "close", "volume", "time"]


def _candle(asset, close=100.0, volume=10.0, time=1704067200000):
    return {
        "asset": asset,
        "pair": f"{asset}INR",
        "open": close,
        "high": close + 2,
        "low": close - 2,
        "close": close,
        "volume": volume,
        "time": time,
    }


def _configure_paths(tmp_path, monkeypatch, rows):
    raw_dir = tmp_path / "raw"
    processed_dir = tmp_path / "processed"
    raw_dir.mkdir()
    processed_dir.mkdir()
    pd.DataFrame(rows, columns=COLUMNS).to_csv(
        raw_dir / "daily_candles.csv", index=False
    )
    monkeypatch.setattr(clean_data.config, "RAW_DIR", raw_dir)
    monkeypatch.setattr(clean_data.config, "PROCESSED_DIR", processed_dir)
    return processed_dir


def test_cleaner_removes_non_finite_rows_and_reports_counts(tmp_path, monkeypatch, capsys):
    valid = _candle("BTC")
    infinite = _candle("ETH")
    infinite["close"] = np.inf
    missing = _candle("SOL")
    missing["volume"] = np.nan

    processed_dir = _configure_paths(
        tmp_path, monkeypatch, [valid, infinite, missing]
    )

    clean_data.main()

    result = pd.read_csv(processed_dir / "daily_candles_clean.csv")
    assert result["asset"].tolist() == ["BTC"]
    assert "input_rows: 3" in capsys.readouterr().out
    assert "rows_removed: 2" in capsys.readouterr().out


def test_cleaner_fails_when_no_valid_rows_remain(tmp_path, monkeypatch):
    invalid = _candle("BTC")
    invalid["close"] = np.inf
    _configure_paths(tmp_path, monkeypatch, [invalid])

    with pytest.raises(ValueError, match="No valid candle rows remain"):
        clean_data.main()
