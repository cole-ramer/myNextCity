import requests
from bs4 import BeautifulSoup
import csv
# Gets the walk score for all cities
def getAllWalkData(states):
    # List of all states
    states = [
        "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
        "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
        "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
        "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
        "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
    ]
    for state in states:
        getState(state)
# Gets
def getState(state: str):
    url = f"https://www.walkscore.com/{state}"
    response = requests.get(url)
    
    cities = []
    zipCodes = []
    walkScore = []
    transitScore = []
    bikeScore = []
    population = []

    # Initialize the data list with headers
    data = [
        ["City", "State", "Zip Code", "Walk Score", "Transit Score", "Bike Score", "Population"]
    ]
    
    soup = BeautifulSoup(response.content, "html.parser")
    rows = soup.find_all(class_="city-list-item")
    
    for r in rows:
        cols = r.find_all('td')
        
        cities.append(cols[0].text.strip())
        zipCodes.append(cols[1].text.strip())
        walkScore.append(0 if cols[2].text == '--' else int(cols[2].text.strip()))
        transitScore.append(0 if cols[3].text == '--' else int(cols[3].text.strip()))
        bikeScore.append(0 if cols[4].text == '--' else int(cols[4].text.strip()))
        population.append(cols[5].text.strip())
    
    # Populate the data list with rows
    for i in range(len(cities)):
        data.append([cities[i], state, zipCodes[i], walkScore[i], transitScore[i], bikeScore[i], population[i]])
    # File path
    file_name = "C:/Users/coler/OneDrive/Documents/Personal Projects/myNextCity/backend/Datasets/walkScoreData - Sheet1.csv"
    
    # Open the CSV file in append mode
    with open(file_name, mode='a', newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        
        # Write the data rows
        writer.writerows(data[1:])  # Skip the header when appending

if __name__ == "__main__":
   getAllWalkData()
#dotenv_path = find_dotenv()
#load_dotenv(dotenv_path)
#API_KEY = os.getenv('WALKSCORE_API_KEY')
# url = "https://api.walkscore.com/score"
# params = {
#     "format": "json",
#     "address": "6520 North Kenmore Ave Chicago, IL",  # Decoded address
#     "lat": 42.00044,
#     "lon": -87.65778,
#     "transit": 1,
#     "bike": 1,
#     "wsapikey": API_KEY
# }
# response = requests.get(url, params=params)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print(f"Error: {response.status_code}, {response.text}")