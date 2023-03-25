import urllib.request
import json

#url = 'https://ergast.com/api/f1/2023/drivers.json'
#result = json.load(urllib.request.urlopen(url))

#driver_table = result['MRData']['DriverTable']

#season = driver_table['season']
#drivers = driver_table['Drivers']

#filtereddrivers = drivers[0:3]

#for driver in filtereddrivers:
   #print(driver['familyName'],driver['givenName'],driver['permanentNumber'])

#url2 = 'https://ergast.com/api/f1/2021/5/results.json'
#result = json.load(urllib.request.urlopen(url2))

#races =  result['MRData']['RaceTable']['Races']
#year = races[0]['season']
#weekend = races[0]['round']
#weekendname = races[0]['raceName']
#print(weekendname)

#results = races[0]['Results']
#podium = results[0:3]
#for pos in podium:
#   print(pos['position'],'.',pos['Driver']['givenName'],pos['Driver']['familyName'],pos['points'],"points")

#print(results[0]['position'],'.',results[0]['Driver']['givenName'],results[0]['Driver']['familyName'],results[0]['points'],"points")
#print(results[1]['position'],'.',results[1]['Driver']['givenName'],results[1]['Driver']['familyName'],results[1]['points'],"points")
#print(results[2]['position'],'.',results[2]['Driver']['givenName'],results[2]['Driver']['familyName'],results[2]['points'],"points")


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
    #Nem tudom mit kéne definiálni amin végigmenjen, mert elég volna csak a számokon.
    #Mégis tudom, de lehet hogy rosszul csinálom
    #for first in round:
    #   print(round,"round's winner:",driver_standings[round]['Driver']['familyName'])
    num = 0
    top = num[0:3]
    for num in top:
       print(round,"round's winner:",driver_standings[num]['Driver']['familyName'])
      
    round = round + 1






