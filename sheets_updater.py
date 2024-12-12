from google.oauth2 import service_account
from googleapiclient.discovery import build

def update_sheets_with_data(spreadsheet_id, sheet_range, data ):
    # Path to your service account key file
    SERVICE_ACCOUNT_FILE = 'keys/molten-catalyst-443503-a5-c663cf6164b1.json'

    # Google Sheet ID and range
    SPREADSHEET_ID = spreadsheet_id
    RANGE_NAME = sheet_range


    # Authenticate and create the Sheets API service
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
    )
    service = build('sheets', 'v4', credentials=credentials)

    values = [data.columns.values.tolist()]
    values.extend(data.values.tolist())
    # Prepare the request body
    body = {
        'values': values
    }

    # Write data to the sheet
    result = service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',  # or 'USER_ENTERED' for formatted input
        body=body
    ).execute()

    print(f"{result.get('updatedCells')} cells updated.")
