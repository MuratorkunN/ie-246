import pandas as pd
import numpy as np
from enumeration import combinations

def calculate_obj(subset, nhood_dict):
    """Assumes subset as a list that contains facility located cities and 
          nhood_dict as a neighborhood dictionary that has cities as keys and a 
          list of their neighbors as values. 
       Counts the number of served for given subset."""
    served = set()                        # A set to collect all served cities.
    for city in subset:
        for neighbor in nhood_dict[city]: # Add the neighbors of the facility one by one.
            served.add(neighbor)          # You can add only unique elements to a set.
    result = (len(served), served)
    return result

def maxcov_exh_enum(cities, p, nhood_dict):
    """Solves the maximum coverage problem optimally by using combination
           function that calculates all possible combinations of facility
           locations."""
    subsets = combinations(cities, p)

    # Calculate the cities served by each facility combination
    max_obj = 0
    best_subset = None
    best_served_cities = None
    for subset in subsets:
        result = calculate_obj(subset, nhood_dict)
        value = result[0]
        served_cities = result[1]
        # value, served_cities = result may replace the two command lines above.
        if value > max_obj:
            max_obj = value
            best_subset = subset
            best_served_cities = served_cities

    best_result = (max_obj, best_subset, best_served_cities)
    return best_result

# Load neighborhood data as a matrix.
nhood_df = pd.read_excel("q04_neighborhood_data.xlsx", header=None)
n = len(nhood_df)
nhood_matrix = np.array(nhood_df.iloc[1:, 1:])
my_cities = tuple(range(len(nhood_matrix)))

# How many facilities are to be opened?
my_p = 3

# Create neighborhood dictionary, keys as cities, values as lists of neighbor cities.
my_nhood_dict = {}
for city in my_cities:
    my_nhood_dict[city] = [city_2 for city_2 in my_cities
                           if nhood_matrix[city, city_2] == 1]

# Solve using exhaustive enumeration.
my_result = maxcov_exh_enum(my_cities, my_p, my_nhood_dict)
print(my_result)