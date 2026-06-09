import os
import warnings
import csv # Built-in, lightweight, and bypasses memory blocks

# Force hardware override before loading heavy libraries
os.environ["NPY_DISABLE_CPU_FEATURES"] = "X86_V2"
warnings.filterwarnings("ignore", category=UserWarning)

from google.cloud import bigquery
import pandas as pd

def run_openalex_pipeline():
    print("[1/4] Initializing BigQuery Client...")
    client = bigquery.Client()

    #sql_query = """
    #SELECT 
    #    state,
    #    gender,
    #     year,
    #     name,
    #     number
    # FROM 
    #     `bigquery-public-data.usa_names.usa_1910_current`
    # LIMIT 5
    # """

    print("[2/4] Executing pipeline query on Google Cloud...")
    with open("query.sql", "r", encoding="utf-8") as f:
        sql_query = f.read()
    
    query_job = client.query(sql_query)

    #print("[3/5] Formatting results into a clean DataFrame...")
    #results = query_job.result(timeout=30)
    
    # Convert rows to a list
    #rows = list(results)
    #print(f"DEBUG: Raw rows received from Google: {len(rows)}")

    #if len(rows) == 0:
    #    print("\n WARNING: Google Cloud returned 0 rows for this query!")
    #    print("Your pipeline is working perfectly, but the dataset is currently empty.")
    #    return

    #rows_dict = [dict(row) for row in rows]
    #df = pd.DataFrame(rows_dict)

    #print(f"[4/5] Success! Total rows retrieved: {len(df)}")
    #print("\n--- Preview of extracted data ---")
    #print(df.head())

    # Define the output file name
    output_filename = "openalex_extracted_data.csv"

    # Write directly to CSV using built-in Python tools (Bypasses Pandas entirely)
    print("[3/4] Writing data to disk...")
    with open(output_filename, mode="w", newline="", encoding="utf-8") as f:
    # Get columns dynamically from the first row's keys
        #fieldnames = list(rows[0].keys())
        #writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer = None

        # Loop directly over the results stream row-by-row
        for row in query_job:
            # Initialize the writer dynamically on the very first row
            if writer is None:
                fieldnames = list(row.keys())
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
            
            writer.writerow(dict(row))

        # Write header and the data rows
        #writer.writeheader()
        #for row in rows:
        #    writer.writerow(dict(row))

    # Save to a local CSV file
    #output_filename = "openalex_extracted_data.csv"
    #df.to_csv(output_filename, index=False)
    print(f"\n[4/4] Data successfully saved to {output_filename}!")

    # Print a raw preview to prove it's done
    print("\n--- Preview of local file content ---")
    with open(output_filename, "r", encoding="utf-8") as f:
        print("".join(f.readlines()[:6]))

if __name__ == "__main__":
    run_openalex_pipeline()