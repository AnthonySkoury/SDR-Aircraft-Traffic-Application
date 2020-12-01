import time
import datetime
import json
import requests
from requests.exceptions import HTTPError

import urllib.request
from urllib.request import urlopen
from datetime import datetime
import email.utils as eut

t = 0
tot = 0
incr = 1
s_p = " seconds passed"
t_s = 0

url = 'http://127.0.0.1:8080/data.json'
url_2 = 'http://localhost:8000/api/aircraft/'
url_3 = 'http://localhost:8000/api/datarecord/'

# producer thread test code
# queue = []
# while True:
#     feedback = requests.get(url)
#     acquired_data = feedback.json()
#     last_mod = feedback.headers['last-modified']
#     print(last_mod)
#     queue.append((last_mod, acquired_data))

icaos = set()

try:
    print('Requesting data from localhost')
    while True:    
        feedback = requests.get(url)
        acquired_data = feedback.json()
        last_mod = feedback.headers['last-modified']
        date_map = eut.parsedate(last_mod)
        # create date in valid DB format
        date_map_f = str(date_map[0]) + '-' + str(date_map[1]) + '-' + str(date_map[2]) + 'T' + str(date_map[3]) + ':' + str(date_map[4]) + ':' + str(date_map[5]) + 'Z'

        # print(last_mod)
        tot += incr
        data_1 = []
        data_2 = []
        date_map = []
        for i in acquired_data:
            data1 = {}
            data2 = {}
            data1["icao"] = i["hex"]
            data2["icao"] = i["hex"]
            data1['squawk'] = i['squawk']
            data1["callsign"] = i["flight"].rstrip()
            # print(data1["callsign"], len(data1["callsign"]))
            data2["latitude"] = i["lat"]
            data2["longitude"] = i["lon"]
            #data2['validposition'] = i['validposition']
            data2["altitude"] = i["altitude"]
            #data2['vert_rate'] = i['vert_rate']
            #data2['track'] = i['track']
            #data2['validtrack'] = i['validtrack']
            data2["ground_speed"] = i["speed"]
            #data2['messages'] = i['messages']
            #data2['seen'] = i['seen']
            # data1['last-modified'] = date_map_f
            data2["timestamp"] = date_map_f

            data_1.append(data1)
            data_2.append(data2)

            # send each object at a time for now since there's currently a bug sending a list of objects

            # check if airplane is in set to see if it's necessary to add the aircraft
            if(data1["icao"] not in icaos):
                # request to add the aircraft and add it into the set
                send_back_1 = requests.post(url=url_2, json=data1)
                icaos.add(data1["icao"])
                if(send_back_1.reason == "Bad Request"):
                    print("Aircraft POST Response: ", send_back_1.status_code, send_back_1.reason, send_back_1.content)

            # request to add data record
            send_back_2 = requests.post(url=url_3, json=data2)
            if(send_back_2.reason == "Bad Request"):
                print("DataRecord POST Response: ", send_back_2.status_code, send_back_2.reason, send_back_2.content)  

        # send_back_1 = requests.post(url=url_2, json=data_1)
        # send_back_2 = requests.post(url=url_3, json=data_2)

        #time.sleep(incr)
        print('One round done at time: ', last_mod, ' Converted time: ', date_map_f)

except HTTPError as http_err:
    print(f'HTTP error event occured: {http_err}')
except Exception as err:
    print(f'Miscellaneous erorr occured: {err}')