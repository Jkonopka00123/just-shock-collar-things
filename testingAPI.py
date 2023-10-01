import requests
import json
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import time
duration = 2
url = "https://do.pishock.com/api/apioperate/"
temp = {"Username": "puppy73", "Name": "TG_Bot_Script", "Code": "17519CD8GAP", "Intensity": "6", "Duration": duration, "Apikey": "5c678926-d19e-4f86-42ad-21f5a76126db", "Op": "0"}
r = requests.post(url, json=temp)
print(r)
# jsonData = json.dumps(temp)
# payload = {'json_payload': jsonData, 'apikey': 'YOUR_API_KEY_HERE'}
# r = requests.get(url, data=payload)
# requests.pos
# curl -d '{"Username":"puppy73","Name":"TG_Bot_Script","Code":"17519CD8GAP","Intensity":"6","Duration":"1","Apikey":"5c678926-d19e-4f86-42ad-21f5a76126db","Op":"0"}' -H 'Content-Type: application/json' https://do.pishock.com/api/apioperate





# page = ''
# while page == '':
#     try:
#         page = requests.get(url)
#         break
#     except:
#         print("Connection refused by the server..")
#         print("Let me sleep for 5 seconds")
#         print("ZZzzzz...")
#         time.sleep(5)
#         print("Was a nice sleep, now let me continue...")
#         continue

# session = requests.Session()
# retry = Retry(connect=3, backoff_factor=0.5)
# adapter = HTTPAdapter(max_retries=retry)
# session.mount('http://', adapter)
# session.mount('https://', adapter)

# session.get(url)
# response = requests.get(url)
# print(response.status_code)
#
#
# try:
#     r = requests.get('https://api.open-notify.org/astros.json')
#     r.raise_for_status()
# except requests.exceptions.HTTPError as err:
#     raise SystemExit(err)