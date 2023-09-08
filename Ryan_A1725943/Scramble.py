import random
import numpy as np

#function to perform a scramble mutation
def scrambleMutation(Arr):
    # Generate random indices to slice from
    i1, i2 = random.sample(range(0, len(Arr) + 1), 2)
    #Ensure that i1 is < i2
    if i1 > i2:
        i1, i2 = i2, i1
    # Slice mutated child from index i1 to i2
    subArray = Arr[i1:i2]
    # shuffle sub array
    random.shuffle(subArray)
    # Replace the selected slice with shuffled sub array
    Arr[i1:i2] = subArray
    return Arr

#test
original = np.array([0,1,2,3,4,5,6,7,8,9])
print("Original:", original)
Scrambled = scrambleMutation(original)
print("Scrambled:", Scrambled)

