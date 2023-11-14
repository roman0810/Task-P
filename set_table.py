import pandas as pd
import json

adr = []
lat = []
lon = []

with open('response.json') as json_file:
    data = json.load(json_file)

    for place in data[0]['items']:
    	adr.append(place['address'])
    	lat.append(place['coordinates'][0])
    	lon.append(place['coordinates'][1])

dt = {'address': adr , 'lat': lat , 'lon': lon}
a = pd.DataFrame(dt)

a.to_excel("/Users/romanvisotsky/Desktop/adr.xlsx")