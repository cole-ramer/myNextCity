import csv
import core.utils as utils
cities = [] # List of all cities
states = [] # List of all states
costOfLiving = [] # List of all cost of living indexes
citiesKey = [] # List of key's for all cities in format city,state ex: Austin,TX
# Reads csv of cost of living data and transforms the columns into rows
with open ("../../Datasets/advisorsmith_cost_of_living_index.csv", mode = 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cities.append(row['City'])
        states.append(row['State'])
        citiesKey.append(f"{row['City']},{row['State']}")
        costOfLiving.append(float(row['Cost of Living Index']))
costOfLiving = utils.normalize(costOfLiving)

    


    

