import time
import json
import requests
from requests.exceptions import HTTPError

 t = 0

try:
	print('Requesting data from localhost')
	url = 'http://127.0.0.1:8080/data.json'
	feedback = requests.get(url)
	acquired_data = feedback.json()
	while True:
		t = t + 1
		print(acquired_data)
		#print(feedback.status_code)
		print(t + 'seconds passed')
		time.sleep(10)

except Exception as e:
    print(f'Error while parsing URL occurred: {e}')