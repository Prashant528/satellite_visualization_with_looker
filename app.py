from ny2o_api_caller import api_caller
from sheets_updater import GSheet
from parse_api_responses import combine_sat_lat_long

spreadsheet_id = '1TUBDCIEyPqv8Hfx6pARoGfH_csbCR0Gk0ZIqLa4IpzA'

def main():
    google_sheet = GSheet(spreadsheet_id)
    meta_info_df, sat_info_df = api_caller()
    meta_sheet_range = 'meta_info'
    sat_sheet_range = 'sat_info'
    sat_cordinates_df = combine_sat_lat_long(sat_info_df)
    #clear the sheets for new update
    google_sheet.clear_sheet(meta_sheet_range)
    google_sheet.clear_sheet(sat_sheet_range)
    #update sheets with new data
    google_sheet.update_sheets_with_data(meta_sheet_range, meta_info_df)
    google_sheet.update_sheets_with_data(sat_sheet_range, sat_info_df)


if __name__=='__main__':
    main()