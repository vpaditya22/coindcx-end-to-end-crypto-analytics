# Dashboard Guide

Launch the dashboard after generating the processed datasets:

```bash
streamlit run app.py
```

The dashboard currently displays asset-level KPI comparisons, normalized historical price performance and rolling annualized volatility. Values reflect the last successful local pipeline run.

If the dashboard reports missing analysis files, run ingestion, cleaning and analysis first. Do not interpret a blank chart as zero return; it can indicate missing data or an incomplete pipeline run.
