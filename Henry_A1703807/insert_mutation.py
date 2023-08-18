# Python3 program to perform insert Mutation
import random
import numpy as np

def insertMutation(array):
    swapRange = random.sample(range(0,array.size),2)
    elementToMove = array[swapRange[1]]

    array = np.delete(array,swapRange[1])
    array = np.insert(array,swapRange[0],elementToMove)

    return array
 
# Main
population = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(insertMutation(population))