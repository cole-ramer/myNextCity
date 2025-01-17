import csv
import pandas as pd
states_acronyms = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY"
}
crimeData = [["City","State", "Population", "Total Crime", "Crime Rate"]]


def getState(state: str):
    stateAcronym = states_acronyms[state]
    # Because FBI files use underscores
    state = state.replace(" ", "_")
    file_path = f"backend/Datasets/crimeStates/{state}_Offense_Type_by_Agency_2023.xlsx"
    sheet_name = f"2023 {stateAcronym}"
    cleaned_data = pd.read_excel(file_path, sheet_name= sheet_name, skiprows= 3)
    cleaned_data =cleaned_data.rename(columns= {
        'Agency Name': 'City',
        'Population1': 'Population',
        'Total\nOffenses': 'Total Crime'
    })
    cleaned_data = cleaned_data[[
        'Agency Type',
        'City',
        'Population',
        'Total Crime'
    ]]
    for _, row in cleaned_data.iterrows():
        if row['Agency Type'] != 'Cities' and pd.notna(row['Agency Type']):
            break
        if pd.notna(row['Population']) and pd.notna(row['Total Crime']):
            crimeData.append([row['City'], stateAcronym, int(row['Population']), int(row['Total Crime']), float(row['Total Crime']/row['Population'])])
def printToCVS (data):
    file_path = "backend/Datasets/crimeData.csv"
    with open (file_path, mode='w',newline='') as csvFile:
       writer = csv.writer(csvFile)
       print(data)
       writer.writerows(data)
def getAllStates ():
    for state in states_acronyms.keys():
        getState(state)

if __name__ == "__main__":
    getAllStates()
    printToCVS(crimeData)

