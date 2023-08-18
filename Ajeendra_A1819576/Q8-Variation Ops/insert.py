import numpy as np
import random as random

def insertionMutation(arr):
    
    lenArr = len(arr)  # get length of the input array
    # pick any 2 random alleles (not the same)
    a1 = random.randint(1,lenArr)   
    a2 = random.randint(1,lenArr)
    
    while (a1 >= a2):  # make sure a1 < a2
        a1 = random.randint(1,lenArr)
        a2 = random.randint(1,lenArr)

    print(a1)
    print(a2)


        
arr = np.array([1,2,3,4,5,6,7,8,9])
insertionMutation(arr)
