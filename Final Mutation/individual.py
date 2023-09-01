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
        self.city[self.N+1] = self.city[1]
        
    def calcFitness(self):
        total = 0
        for i in range(self.N):
            x = self.city[i][0]
            y = self.city[i][1]
            x1 = self.city[i+1][0]
            y1 = self.city[i+1][1]

            total += math.sqrt((x1-x)**2+(y1-y)**2)
        print(total)

        


            
