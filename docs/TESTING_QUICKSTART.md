# Testing Quickstart

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run the suite:

```bash
pytest -q
```

Run Ruff:

```bash
ruff check src tests app.py config.py
```

Unit tests should use deterministic fixtures and must not require internet access or live CoinDCX responses.
