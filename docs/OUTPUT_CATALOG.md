# Output Catalog

The pipeline may produce:

- Raw market metadata and daily candle extracts under `data/raw/`
- Clean candles and engineered fields under `data/processed/`
- Asset KPI and return-correlation tables under `data/processed/`
- Generated figures under `outputs/figures/`
- Business summary Markdown under `reports/`
- A local SQLite database under `data/processed/`

Generated outputs are ignored by Git by default. Exact output availability depends on which pipeline stages have run successfully.
