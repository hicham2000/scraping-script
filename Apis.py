import requests
import pandas as pd

import requests

url = "https://www.dhm.com.au/Umbraco/api/LocationsApi/Search"

querystring = {"BId":"1"}

payload = ""
response = requests.request("GET", url, data=payload, params=querystring)

print(response.text)
res = []
data = response.json()

for p in data['Result']['Locations']:
    res.append(p)


df = pd.json_normalize(res)
df.to_excel('example.xlsx')