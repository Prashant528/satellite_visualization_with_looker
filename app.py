from ny2o_api_caller import api_caller
from sheets_updater import update_sheets_with_data

spreadsheet_id = '1TUBDCIEyPqv8Hfx6pARoGfH_csbCR0Gk0ZIqLa4IpzA'

if __name__=='__main__':
    meta_info_df, sat_info_df = api_caller()
    meta_sheet_range = 'meta_info'
    sat_sheet_range = 'sat_info'
    update_sheets_with_data(spreadsheet_id, meta_sheet_range, meta_info_df)
    update_sheets_with_data(spreadsheet_id, sat_sheet_range, sat_info_df)

