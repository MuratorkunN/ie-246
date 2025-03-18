import numpy as np


def Craps():
    sequence = []

    rng = np.random.default_rng()

    first_roll = sum(rng.integers(low = 1, high = 7, size =2))

    sequence.append(first_roll)

    if first_roll in {7, 11}:
        print("WIN")
        print(sequence)
        return sequence

    if first_roll is {2, 3, 12}:
        print("LOSE")
        print(sequence)
        return sequence
    
    while True:
        second_roll = sum(rng.integers(low = 1, high = 7, size =2))
        sequence.append(second_roll)
        
        if second_roll in {7}:
            print ("LOSE")
            print(sequence)
            return sequence
        
        if second_roll == first_roll:
            print("WIN")
            print(sequence)
            return sequence
        
        
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()
Craps()

    
    