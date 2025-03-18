import numpy as np
from math import inf
from q03a import tsp_grd

my_matrix = np.array([inf, 31, 56, 76, 55, 31, inf, 39, 66, 59, 56, 39, 
                      inf, 28, 36, 76, 66, 28, inf, 32, 55, 59, 36, 32, inf]).reshape(5, 5)
my_locs = ("A", "B", "C", "D", "E")
my_distances = {(loc_i, loc_j):my_matrix[i, j] for i, loc_i in enumerate(my_locs) 
            for j, loc_j in enumerate(my_locs)}

print(tsp_grd(my_locs, "A", my_distances))
print(tsp_grd(my_locs, "B", my_distances))
print(tsp_grd(my_locs, "C", my_distances))
print(tsp_grd(my_locs, "D", my_distances))
print(tsp_grd(my_locs, "E", my_distances))