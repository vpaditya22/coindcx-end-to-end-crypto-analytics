# Dashboard Deployment Notes

The Streamlit app reads locally generated files from the configured processed-data directory. A hosted deployment must therefore include a supported way to generate or provide those outputs before the dashboard loads.

Do not commit private datasets or credentials merely to make a deployment work. If adding scheduled ingestion, account for API terms, rate limits, observability and failure handling. Display the data timestamp so viewers can distinguish a current refresh from an older snapshot.
