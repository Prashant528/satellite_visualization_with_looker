from google.oauth2 import service_account
from googleapiclient.discovery import build

class GSheet():
    def __init__(self, spreadsheet_id) -> None:
        self.SPREADSHEET_ID = spreadsheet_id
        self.SERVICE_ACCOUNT_FILE = 'keys/molten-catalyst-443503-a5-c663cf6164b1.json'
        # Authenticate and create the Sheets API service
        self.credentials = service_account.Credentials.from_service_account_file(
            self.SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
        )
        self.service = build('sheets', 'v4', credentials=self.credentials)

    def update_sheets_with_data(self, sheet_range, data ):
        RANGE_NAME = sheet_range
        values = [data.columns.values.tolist()]
        values.extend(data.values.tolist())
        # Prepare the request body
        body = {
            'values': values
        }

        # Write data to the sheet
        result = self.service.spreadsheets().values().update(
            spreadsheetId=self.SPREADSHEET_ID,
            range=RANGE_NAME,
            valueInputOption='RAW',  # or 'USER_ENTERED' for formatted input
            body=body
        ).execute()

        print(f"{result.get('updatedCells')} cells updated.")

    def clear_sheet(self, sheet):
        resultClear = self.service.spreadsheets( ).values( ).clear(
                                        spreadsheetId=self.SPREADSHEET_ID, 
                                        range=sheet, 
                                        body={}).execute()
