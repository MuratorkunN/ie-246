
def tsp(locs, loc_0, distances):
    remaining_locs = [loc for loc in locs if loc != loc_0]
    
    total_distance = 0
    path = [loc_0]
    
    current_loc = loc_0
    while len(remaining_locs) > 0 :
        next_loc = min(remaining_locs, key=lambda loc: distances[current_loc][loc])
        distance = distances[current_loc][next_loc]
        
        total_distance += distance
        path.append(next_loc)
        current_loc = next_loc
        remaining_locs.remove(next_loc)
    
    path.append(loc_0)
    total_distance += distance[current_loc][loc_0]
    
    return total_distance, path