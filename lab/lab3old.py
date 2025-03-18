from enumeration import permutations
import math

def completition_time(processes):
    completition = []
    for i in processes:
        process = 0
        for j in range(i):
            process += processes[j]
        completition.append(process)
    return completition

print(completition_time([1,2,3,4]))
    
print(permutations([1,2,3,4]))

myorder = permutations([0,1,2,3,4,5])

def tardiness(process, due):
    myorder = process
    i = 0
    while i < len(process):
        myorder[i] = i
        i += 1
    myorder = permutations(myorder)
    mintardiness = math.inf
    minorder = []
    for orders in myorder:
        myprocess = []
        mydue = []
        mycompletition = []
        for j in orders:
            myprocess.append(process[j])
            mydue.append(due[j])
        mycompletition = completition_time(myprocess)
        tardiness = 0
        for k in orders:
            if mycompletition[k] <= mydue[k]:
                tardiness += 0
            else:
                tardiness += mycompletition[k] - mydue[k]
        print(tardiness)
        if tardiness < mintardiness:
            mintardiness = tardiness
            minorder = orders
    return (minorder, mintardiness)

print (tardiness([3,3,4,4,5,1], [5,10,6,12,13,13]))
