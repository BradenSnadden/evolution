import numpy as np
import random as random

def orderCrossover(arr1, arr2):
    
    lenArr = len(arr1)  # get length of the input array

    # pick any 2 random alleles (not the same)
    a1 = random.randint(0,lenArr-1)   
    a2 = random.randint(0,lenArr-1)
    
    while (a1 >= a2):  # make sure a1 < a2
        a1 = random.randint(0,lenArr-1)
        a2 = random.randint(0,lenArr-1)

    print(a1+1) 
    print(a2)

    arr3 = np.zeros((lenArr,2)) # initialise child array
    
    arr3[a1:a2] = arr1[a1:a2]  # copy all elements initially from parent 1 to child array

    j = a2  # set index for the end

    for i in range(0, lenArr, 1):
        if ( arr2[(i+a2) % lenArr] not in arr3 ): # check that the corresponding element in parent 2 does not match child array elements
            arr3[j] = arr2[(i+a2) % lenArr] # if true, then child array element equals that element
            j = (j+1) % lenArr # decrease end index such that all elements in parent 2 are checked and order is preserved
    
    
    return arr3    


arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
arr2 = np.array([9, 3, 7, 8, 2, 6, 5, 1, 4])

orderCrossoverArr = orderCrossover(arr1, arr2)
print(orderCrossoverArr)




