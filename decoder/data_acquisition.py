import time
import datetime
import json
import requests
from requests.exceptions import HTTPError

t = 0
tot = 0
incr = 1
s_p = " seconds passed"
t_s = 0

url = 'http://127.0.0.1:8080/data.json'
url_2 = 'http://localhost:8080/api/aircraft/'
url_3 = 'http://localhost:8080/api/datarecord/'

try:
    print('Requesting data from localhost')
    feedback = requests.get(url)
    acquired_data = feedback.json()
    while True:
        tot += incr
        data_1 = []
        data_2 = []
        for i in acquired_data:
            data1 = {}
            data2 = {}
            data1['icao'] = i['hex']
            data2['icao'] = i['hex']
            #data1['squawk'] = i['squawk']
            data1['callsign'] = i['flight']
            data2['latitude'] = i['lat']
            data2['longitude'] = i['lon']
            #data2['validposition'] = i['validposition']
            data2['altitude'] = i['altitude']
            #data2['vert_rate'] = i['vert_rate']
            #data2['track'] = i['track']
            #data2['validtrack'] = i['validtrack']
            data2['ground_speed'] = i['speed']
            #data2['messages'] = i['messages']
            #data2['seen'] = i['seen']
            data_1.append(data1)
            data_2.append(data2)
            send_back_1 = requests.post(url_2,data=data1)
            send_back_2 = requests.post(url_3,data=data2)

        time.sleep(incr)

except HTTPError as http_err:
    print(f'HTTP error event occured: {http_err}')
except Exception as err:
    print(f'Miscellaneous erorr occured: {err}')