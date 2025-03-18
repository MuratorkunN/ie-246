import pandas as pd
import numpy as np

df = pd.read_excel("q04_neighborhood_data.xlsx", index_col=0)

print(df[0][0])

cities = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

nhood_dict = {}

for i in cities:
    neighbors = []
    for j in cities:
        if df[i][j] == 1:
            neighbors.append(j)
    nhood_dict[i] = neighbors
    
def mxcov_grd(cities, p, nhood_dict):
    facilities = []
    covered = set()
    opened = 0
    
    sorted_cities = sorted(cities, key = lambda city:len(nhood_dict[city]), reverse=True)
    
    while opened < p:
        facility = sorted_cities[opened]  #max(cities, key=lambda city: len(nhood_dict[city]))
        
        facilities.append(facility)
        for city in nhood_dict[facility]:
            covered.add(city)
        opened += 1
        
    return len(covered), facilities, covered

print(mxcov_grd(cities, 5, nhood_dict))