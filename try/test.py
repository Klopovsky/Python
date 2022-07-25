from urllib import response
import requests
from requests.exceptions import HTTPError

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Unknown error: {err}')
    else:
        print('Success!')


#print(requests.get(url))
response = requests.get(url)
print(response.status_code)
print(response.headers)
print(response.cookies)
print(response.request)
print(response.raw)
print(response._content)
