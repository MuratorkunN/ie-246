def sumofall(nestedlist):
    total = 0
    for i in nestedlist:
        if type(i) == int:  
            total += i
        else:  
            total += sumofall(i)
    return total

print(sumofall([15, [6, 7, [5, 22, [4], 36], 11], 8, 
          [16, 33], 13, [2, [1, [0, 14, 20], 19, 21], 3], 22]))

#it works :)
