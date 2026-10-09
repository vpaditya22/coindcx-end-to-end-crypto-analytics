# Pull Request Review Checklist

- Does the change solve one clearly stated problem?
- Are edge cases and failure behavior handled?
- Are metric units, time windows and assumptions clear?
- Are tests deterministic and independent of live API availability?
- Do downstream reports, SQL queries and dashboard consumers still match the schema?
- Are generated datasets and secrets excluded?
- Does the documentation describe implemented behavior accurately?
