from google.cloud import bigquery

try:
    # 1. Initialize the client (it automatically detects your variable)
    client = bigquery.Client()
    
    # 2. Run a tiny, free query against a public dataset to verify access
    query_job = client.query("SELECT 'Connection Successful!' AS status")
    results = query_job.result()
    
    # 3. Print the output
    for row in results:
        print(f"🎉 Success: {row.status}")

except Exception as e:
    print(f"❌ Authentication failed. Error details:\n{e}")