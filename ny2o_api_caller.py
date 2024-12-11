from locations import locations
import requests

base_url = 'https://api.n2yo.com/rest/v1/satellite/'

with open('keys/ny2o_key.txt', 'r') as file:
    ny2o_api_key = file.read().strip()

responses = []

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
        responses.append(response.json())
        print(f"Fetched data successfully for {name}")
    else:
        print(f"Failed to fetch data for {name}. Status code: {response.status_code}")
