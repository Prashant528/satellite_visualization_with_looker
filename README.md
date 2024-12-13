# Real time satellite visualization on Looker.
Try it live here: [https://lookerstudio.google.com/reporting/3ef7ff37-839d-4807-ad43-6461e0131cfd]

## Features:
1. Real time data pulled from n2yo.com satellite data APIs using GCP composer (every 15 minutes).
2. Filter using locations (10 locations currently due to API rate limit).
3. Filter using satellite names.

## Technologies used:
1. Satellite data API: [https://www.n2yo.com/]
2. Python scripts to extract and process data.
3. Google Cloud Platform Composer (Apache Airflow) to schedule and run Python scripts every 15 mins.
4. Google Sheets to store the data.
5. Looker Studio to visualize the data.

