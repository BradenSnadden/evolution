import numpy as np
from individual import individual as Individual

class population():

    popList = np.empty(0, dtype=Individual)

    def __init__(self):
        a = Individual()
        b = Individual()
        c = Individual()
        self.popList=np.append(self.popList, a)
        self.popList=np.append(self.popList, b)
        self.popList=np.append(self.popList, c)
    
    