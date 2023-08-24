# Python3 program to perform Swap Mutation

import random
import numpy as np

def swap_mutation(array):
    swapRange = random.sample(range(0,array.size),2)
    array[swapRange[1]], array[swapRange[0]] = array[swapRange[0]], array[swapRange[1]]
    return array
 
# Main
population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(swap_mutation(population))