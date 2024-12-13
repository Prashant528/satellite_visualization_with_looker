from locations import locations
import pandas as pd
import requests

def api_caller():
    base_url = 'https://api.n2yo.com/rest/v1/satellite/'

    with open('keys/ny2o_key.txt', 'r') as file:
        ny2o_api_key = file.read().strip()

    meta_info_columns = ['seen_from', 'category', 'transactionscount', 'satcount']
    meta_info_df = pd.DataFrame(columns=meta_info_columns)
    sat_info_columns = ['seen_from', 'satid', 'satname', 'launchDate', 'satlat', 'satlng', 'satalt']
    sat_info_df = pd.DataFrame(columns=sat_info_columns)

    for location in locations:
        name = location['name']
        lat = location['lat']
        long = location['long']
        alt=  location['alt']
        radius = location['radius']
        sat_cat = location['sat_cat']

        api_info = f'above/{lat}/{long}/{alt}/{radius}/{sat_cat}'

        full_api_url = base_url + api_info + '&apiKey=' + ny2o_api_key

        response = requests.get(full_api_url)
        if response.status_code == 200:
            content = response.json()
            loc_info_df = pd.DataFrame([content['info']])
            loc_sat_df = pd.DataFrame(content['above'])
            loc_info_df['seen_from'] = name
            loc_sat_df['seen_from'] = name
            meta_info_df = pd.concat([meta_info_df,loc_info_df ], ignore_index=True)
            sat_info_df = pd.concat([sat_info_df, loc_sat_df], ignore_index=True)
            print(f"Fetched data successfully for {name}")
        else:
            print(f"Failed to fetch data for {name}. Status code: {response.status_code}")

    return meta_info_df, sat_info_df