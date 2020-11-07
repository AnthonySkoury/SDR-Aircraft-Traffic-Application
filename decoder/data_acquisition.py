import requests

try:
	print('Requesting data from localhost')
	url = 'http://127.0.0.1:8080/data.json'
	feedback = requests.get(url)
	acquired_data = feedback.json()
	print(acquired_data)

except Exception as e:
    print(f'Error while parsing URL occurred: {e}')