from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to your service account key file
SERVICE_ACCOUNT_FILE = 'keys/molten-catalyst-443503-a5-c663cf6164b1.json'

# Google Sheet ID and range
SPREADSHEET_ID = '1TUBDCIEyPqv8Hfx6pARoGfH_csbCR0Gk0ZIqLa4IpzA'
RANGE_NAME = 'Sheet2!A1'

# Sample data to insert
data = [
    ['Name', 'Age', 'Country'],  # Headers
    ['Alice', 30, 'USA'],
    ['Bob', 25, 'UK'],
    ['Charlie', 35, 'Canada']
]

# Authenticate and create the Sheets API service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=credentials)

# Prepare the request body
body = {
    'values': data
}

# Write data to the sheet
result = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=RANGE_NAME,
    valueInputOption='RAW',  # or 'USER_ENTERED' for formatted input
    body=body
).execute()

print(f"{result.get('updatedCells')} cells updated.")
