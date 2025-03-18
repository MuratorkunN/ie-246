from enumeration import permutations
import math

def completition_time(processes):
    completition = []
    for i in range(len(processes)):
        process = 0
        for j in range(i + 1):
            process += processes[j]
        completition.append(process)
    return completition

#print(completition_time([3,3,4,4,5,1]))
    
#print(permutations([1,2,3,4]))

myorder = permutations([0,1,2,3,4,5])

def tardiness(process, due):
    myorder = process.copy()
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
            #print(k)
            if mycompletition[k] <= mydue[k]:
                tardiness += 0
            else:
                tardiness += (mycompletition[k] - mydue[k])
        if tardiness < mintardiness:
            mintardiness = tardiness
            minorder = orders
    return (minorder, mintardiness)

print (tardiness([3,3,4,4,5,1], [5,10,6,12,13,13]))
