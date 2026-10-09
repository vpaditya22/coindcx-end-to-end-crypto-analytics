# Unit Conventions

- Prices are denominated in the selected market pair's quote currency; this project selects INR pairs.
- Returns and drawdowns are decimal fractions in CSV outputs; 0.05 represents 5%.
- Volatility is annualized using a 365-day multiplier on daily-return standard deviation.
- Timestamps from candle records are interpreted as epoch milliseconds and normalized to UTC dates.
- The turnover field is explicitly a proxy and should not be interpreted as official exchange turnover without verified volume units.
