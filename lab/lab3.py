from enumeration import permutations
import math

def opt(process_times, due_times):
    
    jobs = range(len(process_times))
    allorders = permutations(jobs)
    best = None
    mintardiness = math.inf
    
    
    for order in allorders:
        totaltardiness = 0
        currenttime = 0
        for i in order:
            completetime = currenttime + process_times[i]
            totaltardiness += max(0, completetime - due_times[i])
            currenttime += process_times[i]
        if totaltardiness < mintardiness:
            mintardiness = totaltardiness
            bestorder = order
    return (bestorder,mintardiness)

print(opt([3,3,4,4,5,1], [5,10,6,12,13,13]))