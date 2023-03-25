import urllib.request
import json


has_data = True
round = 1

while has_data:
    url = f'https://ergast.com/api/f1/2023/{round}/driverStandings.json'
    result = json.load(urllib.request.urlopen(url))
    data = result['MRData']

    has_data = int(data['total']) > 0

    if not has_data:
      break

    driver_standings = data['StandingsTable']['StandingsLists'][0]['DriverStandings']

    for i in range(0, 3):
        standing = driver_standings[i]
        print(standing['position'])
    
    for standing in driver_standings[0:3]:
       print(standing['position'])

    round = round + 1

#print(results[0]['position'],'.',results[0]['Driver']['givenName'],results[0]['Driver']['familyName'],results[0]['points'],"points")
#print(results[1]['position'],'.',results[1]['Driver']['givenName'],results[1]['Driver']['familyName'],results[1]['points'],"points")
#print(results[2]['position'],'.',results[2]['Driver']['givenName'],results[2]['Driver']['familyName'],results[2]['points'],"points")


