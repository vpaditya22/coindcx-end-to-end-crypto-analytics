# Metric Test Matrix

| Behavior | Test coverage |
|---|---|
| Peak-to-trough drawdown | `test_metrics.py`, `test_max_drawdown_edges.py`, `test_max_drawdown_properties.py` |
| Annualized return boundaries | `test_annualized_return_edges.py`, `test_empty_returns.py` |
| Asset-level output contract | `test_metrics_contract.py` |
| Correlation of aligned returns | `test_correlation.py` |
| Duplicate keys and missing schema | `test_metric_validation.py` |
| SQLite loader without inputs | `test_load_sqlite.py` |

Run `pytest -q` from the repository root. Tests should remain deterministic and must not depend on the live CoinDCX API.
