import numpy as np
import pandas as pd
from math import inf
from q03a import tsp_grd

my_df = pd.read_csv("q03_distances_data.csv", header=None)
my_matrix = np.array(my_df)
n = my_matrix.shape[0]
for i in range(n):
    my_matrix[i, i] = inf
my_locs = tuple(range(n))
my_distances = {(loc_i, loc_j):my_matrix[i, j] for i, loc_i in enumerate(my_locs) 
            for j, loc_j in enumerate(my_locs)}

best_cycle, best_distance = None, inf

for i in my_locs:
    obj_val, solution = tsp_grd(my_locs, i, my_distances)
    if obj_val < best_distance:
        best_distance = obj_val
        best_cycle = solution

print(best_distance)
print(best_cycle)