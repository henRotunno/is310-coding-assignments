import requests
import pyeuropeana
import apikey 
import json


# Pyeuropeana key
apikey.save("europeana_key", "heurnicraess")
euro_key = apikey.load("europeana_key")
europeana_url = "https://www.europeana.eu/api/v2/search.json"



auth_headers = {
    'Authorization': 'Bearer' + euro_key
}

star_url = "https://swapi.dev/api/people/1/"
star_re = requests.get(star_url)
if star_re.status_code == 200:
    star_dat = star_re.json()
    print("SWAPI Data:", json.dumps(star_dat, indent=2))

scan = star_dat['Vader']

results = {
    'query': scan,
    'rows': 5
}
response = requests.get(europeana_url, headers=auth_headers, params=results)

if response.status_code == 200:
    related_data = response.json()
    print(f"Related Europeana Data for '{scan}':", json.dumps(related_data, indent=2))

combined_data = {
            'swapi': star_dat,
            'europeana': related_data
        }
with open('swapi_europeana_data.json', 'w') as json_file:
            json.dump(combined_data, json_file, indent=2)


