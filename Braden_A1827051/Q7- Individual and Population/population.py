import numpy as np
from individual import individual as Individual
from TSP import TSP as TSP

class population():

    popList = np.empty(0, dtype=Individual)

    def __init__(self):
        a = Individual(TSP.cities)
        
        b = Individual(TSP.cities)
        c = Individual(TSP.cities)
        self.popList=np.append(self.popList, a)
        self.popList=np.append(self.popList, b)
        self.popList=np.append(self.popList, c)
    
    