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

url2 = 'https://ergast.com/api/f1/2021/5/results.json'
result = json.load(urllib.request.urlopen(url2))

race_table = result['MRData']['RaceTable']    
season = race_table['season']
round =  race_table['round']
races =  race_table['Races']
year = races['season']
weekend = races['round']
weekendname = races['raceName']
print(weekendname)

# A kövi blokkban tuti elcsesztem a struktúrát, mert belekavarodok a szintekbe 
results = races['Results']
pos = results['position']
podium = results[0:3]
for happy in podium:
   print(happy['position'],happy['Driver']['FamilyName'],happy['points'])


#Így most majdnem az összes sort feldolgoztam. Erre szükség van, vagy lehet kapásból úgy belépni mint az mrdata - > racetable esetében?
#valahogy biztos lehetne szebben, hogy bekérni számot és akkor az annyiadik futam adatait kiírni, de ehhez azért még kevés vagyok

