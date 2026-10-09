# Known Limitations

- Public endpoints and response schemas may change.
- A configured asset may not have an active INR market for the entire period.
- The current pipeline uses one selected market pair per asset, so pair selection affects the series.
- Missing dates can affect return, annualization and correlation interpretations.
- Annualization assumes daily observations across 365 days per year.
- A close-times-volume value is not verified exchange turnover or revenue.
- Public market data does not include individual customer behavior.
- Dashboard values are only as current as the most recent successful pipeline run.
