# Continuous Integration

The GitHub Actions workflows run on pushes, pull requests and manual dispatch.

- `.github/workflows/tests.yml` installs the project and development dependencies, then runs pytest.
- `.github/workflows/lint.yml` runs Ruff against the application, configuration, source and test code.

A green workflow is a useful regression signal, but it does not prove the external CoinDCX API is currently available or that the full live-data pipeline succeeds.
