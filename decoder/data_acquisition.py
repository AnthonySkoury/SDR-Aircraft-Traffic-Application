import time
import datetime
import json
import requests
from requests.exceptions import HTTPError

import urllib.request
from urllib.request import urlopen
from datetime import datetime
import email.utils as eut

import sys, os


url = 'http://127.0.0.1:8080/data.json'
url_2 = 'http://localhost:8000/api/aircraft/'
url_3 = 'http://localhost:8000/api/datarecord/'

def get_packet():
    return requests.get(url)

def parse_aircraft(data):
    aircraft_data = {}
    aircraft_data['icao'] = data['hex']
    aircraft_data['squawk'] = data['squawk']
    aircraft_data['callsign'] = data['flight'].rstrip()
    return aircraft_data

def parse_datarecord(data, date_map_f):
    datarecord_data = {}
    datarecord_data['icao'] = data['hex']
    datarecord_data['latitude'] = data['lat']
    datarecord_data['longitude'] = data['lon']
    datarecord_data['valid_position'] = bool(data['validposition'])
    datarecord_data['altitude'] = data['altitude']
    datarecord_data['vertical_rate'] = data['vert_rate']
    datarecord_data['track'] = data['track']
    datarecord_data['valid_track'] = bool(data['validtrack'])
    datarecord_data['ground_speed'] = data['speed']
    datarecord_data['count_messages'] = data['messages']
    datarecord_data['tracked_seconds'] = data['seen']
    datarecord_data['timestamp'] = date_map_f
    return datarecord_data

def post_aircraft(no_dupes, icaos_long_lat, aircraft_data):
    # check if airplane is in dictionary to see if it's necessary to add the aircraft
    if(not icaos_long_lat.get(aircraft_data['icao'])):
        # request to add the aircraft and add it into the set
        send_back_1 = requests.post(url=url_2, json=aircraft_data)
        icaos_long_lat[aircraft_data['icao']] = (-1,-1)
        if(send_back_1.reason == 'Bad Request'):
            print('Aircraft POST Response: ', send_back_1.status_code, send_back_1.reason, send_back_1.content)

def post_datarecord(no_dupes, icaos_long_lat, datarecord_data):
    # request to add data record
    # check if long and lat are different than the most recent one to avoid dupes
    if(no_dupes and icaos_long_lat.get(datarecord_data['icao']) and (icaos_long_lat.get(datarecord_data['icao']) != (datarecord_data['longitude'], datarecord_data['latitude']))):
        icaos_long_lat[datarecord_data['icao']] = (datarecord_data['longitude'], datarecord_data['latitude'])
        send_back_2 = requests.post(url=url_3, json=datarecord_data)
        if(send_back_2.reason == 'Bad Request'):
            print('DataRecord POST Response: ', send_back_2.status_code, send_back_2.reason, send_back_2.content)

    if(not no_dupes and icaos_long_lat.get(datarecord_data['icao'])):
        icaos_long_lat[datarecord_data['icao']] = (datarecord_data['longitude'], datarecord_data['latitude'])
        send_back_2 = requests.post(url=url_3, json=datarecord_data)
        if(send_back_2.reason == 'Bad Request'):
            print('DataRecord POST Response: ', send_back_2.status_code, send_back_2.reason, send_back_2.content)

# producer thread test code
# queue = []
# while True:
#     feedback = requests.get(url)
#     acquired_data = feedback.json()
#     last_mod = feedback.headers['last-modified']
#     print(last_mod)
#     queue.append((last_mod, acquired_data))


def main():

    # flag to know if the database should not store records with the same long and lat pair
    no_dupes = True

    try:
        print('Requesting data from localhost')
        # dictionary used to record most recent longitude and latitude pair for an icao to know if it is a duplicate transmission
        icaos_long_lat = {}
        while True:

            feedback = get_packet()
            acquired_data = feedback.json()
            last_mod = feedback.headers['last-modified']
            date_map = eut.parsedate(last_mod)
            # create date in valid DB format
            date_map_f = str(date_map[0]) + '-' + str(date_map[1]) + '-' + str(date_map[2]) + 'T' + str(date_map[3]) + ':' + str(date_map[4]) + ':' + str(date_map[5]) + 'Z'

            aircraft_list = []
            datarecord_list = []
            date_map = []

            for data in acquired_data:
                aircraft_data = parse_aircraft(data)
                datarecord_data = parse_datarecord(data, date_map_f)

                aircraft_list.append(aircraft_data)
                datarecord_list.append(datarecord_data)

                # send each object at a time for now since there's currently a bug sending a list of objects
                post_aircraft(no_dupes, icaos_long_lat, aircraft_data)
                post_datarecord(no_dupes, icaos_long_lat, datarecord_data)

            # send_back_1 = requests.post(url=url_2, json=aircraft_list)
            # send_back_2 = requests.post(url=url_3, json=datarecord_list)

            print('One round done at time: ', last_mod, ' Converted time: ', date_map_f)

    except HTTPError as http_err:
        print(f'HTTP error event occured: {http_err}')
    except Exception as err:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(f'Miscellaneous erorr occured: {err}')

if __name__ == "__main__":
    main()