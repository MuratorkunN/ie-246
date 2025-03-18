def tsp_grd(locs, loc_0, distances):
    
    # INITIALIZATION
    current_loc = loc_0
    total_dist, solution = 0, [current_loc]    
    not_visited = set(locs)
    not_visited.remove(loc_0)

    # GREEDY HEURISTIC
    while not_visited:
        next_loc = min(not_visited, key = lambda loc:distances[current_loc, loc])
        solution.append(next_loc)
        not_visited.remove(next_loc)
        total_dist += distances[(current_loc, next_loc)] 
        current_loc = next_loc
    solution.append(loc_0)
    total_dist += distances[(current_loc, loc_0)] 
    
    # RETURNING SOLUTION
    obj_val = total_dist
    result = (obj_val, solution)
    return result