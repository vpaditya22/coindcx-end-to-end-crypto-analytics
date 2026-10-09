# SQL Query Smoke-Test Plan

After generating the SQLite database, execute each query file against a disposable database copy.

- Confirm all referenced tables and columns exist.
- Confirm queries run when the tables contain representative rows.
- Confirm empty tables return empty result sets rather than fabricated values.
- Confirm null KPIs are not silently converted to zero.
- Confirm proxy-related query labels do not call the proxy revenue or verified turnover.

Future automated integration tests can load a small fixture database and execute every SQL file.
