import urllib.request
import matplotlib.pyplot as plt
import json

has_data = True
round = 1

standings_dict_initialized = False
standings_dict = { }

while has_data:
    url = f'https://ergast.com/api/f1/2021/{round}/driverStandings.json'
    result = json.load(urllib.request.urlopen(url))
    data = result['MRData']

    has_data = int(data['total']) > 0

    if not has_data:
      break

    driver_standings = data['StandingsTable']['StandingsLists'][0]['DriverStandings']

    if not standings_dict_initialized:
      for standing in driver_standings:
        driver_code = standing['Driver']['code']
        standings_dict[driver_code] = []

      standings_dict_initialized = True
    
    for standing in driver_standings:
      driver_code = standing['Driver']['code']
      points = float(standing['points'])

      if driver_code not in standings_dict:
        standings_dict[driver_code] = []
        
      standings_dict[driver_code].append(points)
      
    round = round + 1


activity = [*range(1, 23, 1)]

fig, ax = plt.subplots()

for key in standings_dict:
  if len(standings_dict[key]) == len(activity):
    ax.plot(activity, standings_dict[key], label=key)


ax.legend()
plt.show()