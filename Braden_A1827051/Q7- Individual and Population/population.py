import numpy as np
from individual import individual as Individual

class population():

    popList = np.empty([], dtype=Individual)

    def __init__(self):
        a = Individual()
        b = Individual()
        c = Individual()
        
        np.append(self.popList, a)
        np.append(self.popList, b)
        np.append(self.popList, c)
    
    