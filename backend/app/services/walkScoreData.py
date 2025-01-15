import requests
import os
from dotenv import find_dotenv, load_dotenv 
dotenv_path = find_dotenv()
load_dotenv(dotenv_path)
API_KEY = os.getenv('WALKSCORE_API_KEY')
url = "https://api.walkscore.com/score"
params = {
    "format": "json",
    "address": "6520 North Kenmore Ave Chicago, IL",  # Decoded address
    "lat": 42.00044,
    "lon": -87.65778,
    "transit": 1,
    "bike": 1,
    "wsapikey": API_KEY
}
response = requests.get(url, params=params)
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}, {response.text}")