# Reproducing an Analysis

1. Check out the commit being reviewed.
2. Create a clean virtual environment and install runtime/development dependencies.
3. Run `pytest -q`.
4. Review the configured asset list and date window.
5. Run ingestion, cleaning, analysis, reporting and SQLite loading in sequence.
6. Save the console validation output alongside the run metadata.
7. Compare generated output schemas and date coverage before comparing KPI values.
8. Record any API changes or missing assets.
