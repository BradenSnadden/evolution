import numpy as np
import random as rand
import population
import math

class individual(population):
    
    city = np.array()
    fitness = 0

    def __init__(self, n):
        self.seq = np.random.permutation(self.N)
        for i in range(N):
            self.city[self.seq[i]] = cities[i]
        self.city[N+1] = self.city[1]
        
    def calcFitness(self):
        total = 0
        for i in range(N):
            x = self.city[i][0]
            y = self.city[i][1]
            x1 = self.city[i+1][0]
            y1 = self.city[i+1][1]

            total += math.sqrt((x1-x)**2+(y1-y)**2)
        


            
