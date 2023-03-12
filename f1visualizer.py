print("hello dave")

import urllib.request
import json

url = 'https://ergast.com/api/f1/2023/drivers.json'
result = json.load(urllib.request.urlopen(url))
result["MRData"]


