import requests
import pandas as pd

url = "https://hbr.org/service/search/more-results/1/411"

querystring = {"format":"json","term":"connection"}

payload = ""
headers = {"cookie": "_hbr_u=eyJpZCI6IjQ2NTQzZTI2NGVhZWU5YjViNjI4ZGVlM2MwZWE4MjM2IiwibGFzdFZpc2l0ZWQiOjE2OTE3ODQ4ODk3MjN9; hbr_user_experience=Sync_Adobe_Launch; HBR_SESSION_ID_N=MDQ2Y2RlMzAtMTRkOS00MDk3LTlkMGItN2IyMTQ4YzU0Yjhl"}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

data = response.json()

res = []

for p in data['entry']:
    res.append(p)
print(len(res))

df = pd.json_normalize(res)
df.to_excel('test.xlsx')