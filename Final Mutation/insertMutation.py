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
    
    # reverse loop through the array and swap the values until it reaches 1 position in front of a1
    for i in range(a2-2, a1-1, -1): 
        temp = arr[i+1]
        arr[i+1] = arr[i]
        arr[i] = temp
        
    return(arr)

array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
#array = np.array([3, 2, 9, 4, 8, 7, 6, 5, 1])
insertMutationArr = insertionMutation(array)
print(insertMutationArr)
