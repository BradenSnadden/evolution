import numpy as np
import random as rand
import math
from TSP import TSP as ClassName

class individual(ClassName):
    
    fitness = 0
    city = ClassName.cities
    
    
    def __init__(self, cities):
        #print(cities[0][1])
        self.city = np.copy(cities)
        
        np.random.shuffle(self.city)
        
        
        
        
    def getSize(self):
        return self.N        
        
    def calcFitness(self):
        total = 0
        #print(np.shape(self.city))
        for i in range(self.N):
            x = self.city[i,0]
            y = self.city[i,1]
            if(i+1 == self.N):
                x1 = self.city[0,0]
                y1 = self.city[0,1]
            else:
                x1 = self.city[i+1,0]
                y1 = self.city[i+1,1]

            total += math.sqrt((x1-x)**2+(y1-y)**2)
        print(total)

        


            
