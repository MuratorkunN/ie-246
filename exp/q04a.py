import pandas as pd
import numpy as np

def maxcov_grd(cities, p, nhood_dict):
    grd_order = sorted(cities, key = lambda city:len(nhood_dict[city]), reverse=True)
    served_cities = set()
    facility_cities = []
    for i in range(p):
        city = grd_order[i]
        facility_cities.append(city)
        served_cities.add(city)
        for neighbor in nhood_dict[city]:
            served_cities.add(neighbor)
    result = (len(served_cities), facility_cities, served_cities)
    return result

# Load neighborhood data as a matrix.
nhood_df = pd.read_excel("q04_neighborhood_data.xlsx", header=None)
n = len(nhood_df)
nhood_matrix = np.array(nhood_df.iloc[1:, 1:])
nhood_df
my_cities = tuple(range(nhood_matrix.shape[0]))

# How many facilities are to be opened?
my_p = 3

# Create neighborhood dictionary, keys as cities, values as lists of neighbor cities.
my_nhood_dict = {}
for city in my_cities:
    my_nhood_dict[city] = [city_2 for city_2 in my_cities 
                           if nhood_matrix[city, city_2] == 1]

# Solve using heuristic approach.
my_result = maxcov_grd(my_cities, my_p, my_nhood_dict)
print(my_result)