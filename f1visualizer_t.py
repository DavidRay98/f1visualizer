import urllib.request
import matplotlib.pyplot as plot
import json
import sys


year_input = input("Add meg az évet: ")

if not year_input.isnumeric():
  print("Az év nem szám!")
  exit(1)

year = int(year_input)

if year not in range(1950,2024):
  print("Ebben az évben nem rendeztek F1-et!")
  exit(1)

drivers_input = input("Add meg a sofőröket vesszővel elválasztva: ")

drivers = drivers_input.split(",")

has_data = True
round = 1

standings_dict = { }

for driver in drivers:
  standings_dict[driver] = []

while has_data:
    url = f'https://ergast.com/api/f1/{year}/{round}/driverStandings.json'
    result = json.load(urllib.request.urlopen(url))
    data = result['MRData']

    has_data = int(data['total']) > 0

    if not has_data:
      break

    driver_standings = data['StandingsTable']['StandingsLists'][0]['DriverStandings']
    
    for standing in driver_standings:
      driver_code = standing['Driver']['code']
      points = float(standing['points'])

      if driver_code in standings_dict:    
        standings_dict[driver_code].append(points)
      
    round = round + 1


activity = [*range(1, round, 1)]

figure, axes = plot.subplots()

for driver in standings_dict:
  if len(standings_dict[driver]) == len(activity):
    axes.plot(activity, standings_dict[driver], label=driver)
  else:
    print("Az adott versenyzőről (", driver, ") nem áll rendelkezésre adat minden futamról.")


axes.legend()
plot.show()