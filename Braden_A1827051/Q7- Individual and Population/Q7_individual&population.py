import numpy as np


class Individual:

    def __init__(self, n):
        self.length = n
        self.generate()
        
    def generate(self):
        self.seq = np.random.permutation(self.length)

class Population:
    def __init__(self, n):
        self.size = n
    
    def init_pop(self):
        self.pop_list = [Individual(self.size) for _ in range(self.size)]

if __name__ == "__main__":
    i = Individual(420)
    i.generate()
    print(i.seq)
