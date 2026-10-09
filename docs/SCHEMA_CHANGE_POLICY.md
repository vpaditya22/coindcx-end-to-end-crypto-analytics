# Output Schema Change Policy

When changing a processed dataset:

1. Update the producer and its tests.
2. Update the data dictionary.
3. Search SQL queries, the SQLite loader, report generator and dashboard for consumers.
4. Regenerate representative outputs where permitted.
5. Document renamed, added or removed columns.
6. Avoid silently changing units or meanings under an existing column name.
7. Include a clear commit message describing the schema impact.
