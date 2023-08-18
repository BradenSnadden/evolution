import numpy as np
import random as rand
import population

class individual(population):
    
    city = np.array()

    def seed(self):
        for i in range(N):
            x = rand.randrange(1,N)
            while (cities[x] == -1):
                if (x > N):
                    x = 0
                x += 1
            self.city[i] = cities[x]
            cities[x] = -1
            i += 1


            
