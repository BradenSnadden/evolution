import numpy as np
from individual import individual as Individual
from TSP import TSP as TSP

class population():

    popList = np.empty((0), dtype=Individual)

    def __init__(self):

        for i in range(10):
            a = Individual(TSP.cities)
            self.popList = np.append(self.popList, a)

    
    