# Mini Multi-Observer Pipeline (US Baby Names Extraction)

A lightweight, robust data engineering pipeline built in Python to programmatically extract, format, and stream cloud data from Google BigQuery directly into localized storage structures. This project utilizes the Google Cloud Public Datasets program to fetch and analyze historical United States naming trends.

---

## 🚀 Features

* **Cloud Data Streaming:** Authenticates and connects directly to Google Cloud Platform (GCP) via the official BigQuery API client.
* **Bypasses Memory Bottlenecks:** Uses a lightweight, low-overhead stream iteration pattern to write data directly to disk, completely bypassing heavy dataframe initialization blocks.
* **Dynamic Header Extraction:** Dynamically reads structural metadata directly from cloud object streams without hardcoding schemas.
* **Environment Isolation:** Fully decoupled environment architecture ensuring zero system pollution.

---

## 🛠️ Tech Stack & Hardware Constraints

* **Language:** Python 3.11 (Tested and Verified)
* **Operating System:** Windows Environment
* **Cloud Platform:** Google Cloud Platform (BigQuery)
* **Dataset:** `bigquery-public-data.usa_names.usa_1910_current`
* **Target Hardware Profile:** Legacy x86 system architectures (e.g., Core 2 Duo / Gigabyte Chipsets)
* **Data Format:** CSV (Comma-Separated Values)

---

## 📦 Installation & Setup

1. **Clone the Repository:**
```bash
   git clone [https://github.com/Patrick-Darwim-de-Assis/mini-multiobs-pipeline.git]
   cd mini-multiobs-pipeline

```

2. **Set Up the Virtual Environment:**

```bash
   # Create the isolated environment
   python -m venv stable_pipeline_env

   # Activate on Windows
   .\stable_pipeline_env\Scripts\Activate

```

3. **Install Dependencies:**

```bash
  pip install google-cloud-bigquery 
```

---

## 🏃‍♂️ Running the Pipeline

Ensure your Google Cloud Service Account credentials are encrypted or exported to your environment path locally, then execute the main execution pipeline script:

```bash
python query_openalex.py

```

### Expected Console Output:

```
[1/4] Initializing BigQuery Client...
[2/4] Executing pipeline query on Google Cloud...
[3/4] Writing data to disk...

[4/4] Data successfully saved to openalex_extracted_data.csv!

--- Preview of local file content ---
(Your extracted CSV data rows will display here)

```

---

## 📂 Project Architecture

* `query_openalex.py` - Core execution script that initializes the BigQuery client, dynamically loads the external SQL query, and handles the local file-writing logic.
* `query.sql` - Externalized SQL query file targeting the Google BigQuery public names dataset.
* `.gitignore` - Protects sensitive local database structures and cloud authorization JSON keys from leaking.
* `openalex_extracted_data.csv` - Local output storage containing the extracted US Baby Names data schema.

```
