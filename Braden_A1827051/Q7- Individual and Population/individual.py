import numpy as np
import random as rand
import math
from TSP import TSP as ClassName

class individual(ClassName):
    
    city = ClassName.cities
    fitness = 0
    new = np.array([ClassName.N,2])

    def __init__(self):
        
        self.new = np.random.shuffle(self.city)
        print(np.shape(self.new))
        
        
        
    def calcFitness(self):
        total = 0
        print(np.shape(self.city))
        for i in range(self.N):
            x = self.city[i]
            y = self.city[i]
            x1 = self.city[i+1]
            y1 = self.city[i+1]

            total += math.sqrt((x1-x)**2+(y1-y)**2)
        print(total)

        


            
