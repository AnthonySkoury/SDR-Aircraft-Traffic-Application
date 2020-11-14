import time
import json
import requests
from requests.exceptions import HTTPError

t = 0
tot = 0
incr = 10
s_p = " seconds passed"

try:
    print('Requesting data from localhost')
    url = 'http://127.0.0.1:8080/data.json'
    feedback = requests.get(url)
    acquired_data = feedback.json()
    while True:
        tot += incr
        print(acquired_data)
        send_back = json.dumps(acquired_data, indent = 13)

        with open("acquired_data.json","w") as outfile:
            outfile.write(send_back)

        print(str(tot) + s_p)
        time.sleep(incr)

except HTTPError as http_err:
    print(f'HTTP error event occured: {http_err}')
except Exception as err:
    print(f'Miscellaneous erorr occured: {err}')