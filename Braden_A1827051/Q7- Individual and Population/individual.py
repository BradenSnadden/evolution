import numpy as np
import random as rand
import math
from TSP import TSP as ClassName

class individual(ClassName):
    
    city = ClassName.cities
    fitness = 0

    def __init__(self):
        self.seq = np.random.permutation(self.N)
        for i in range(1,self.N):
            self.city[self.seq[i]][0] = self.cities[i][0]
            self.city[self.seq[i]][1] = self.cities[i][1]
        self.city = np.append(self.city, self.city[1])
        
        
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

        


            
