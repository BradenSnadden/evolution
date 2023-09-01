from individual import individual
from population import population
import numpy as np
pop = population()
print(np.shape(pop.popList))
print(pop.popList[1].calcFitness())

