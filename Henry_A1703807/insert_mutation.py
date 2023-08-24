# Python3 program to perform Insert Mutation

import random
import numpy as np

def insert_mutation(array):
    swapRange = random.sample(range(0,array.size),2)
    elementToMove = array[swapRange[1]]

    array = np.delete(array,swapRange[1])
    array = np.insert(array,swapRange[0],elementToMove)

    return array
 
# Main
population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(insert_mutation(population))