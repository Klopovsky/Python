from urllib import response
import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

HEADER = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'

for url in ['https://api.github.com', 'https://api.github.com/invalid']:
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error: {err}')
    else:
        print('Success!')


#print(requests.get(url))
response = requests.get(url)
print(response.status_code)
