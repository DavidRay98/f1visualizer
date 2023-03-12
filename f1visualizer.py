import urllib.request
import json

url = 'https://ergast.com/api/f1/2023/drivers.json'
result = json.load(urllib.request.urlopen(url))

driver_table = result['MRData']['DriverTable']

season = driver_table['season']
drivers = driver_table['Drivers']

print(drivers)