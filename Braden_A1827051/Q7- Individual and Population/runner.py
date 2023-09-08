from individual import individual
from population import population
import numpy as np
pop = population()
print(np.shape(pop.popList))
pop.popList[0].calcFitness()
pop.popList[4].calcFitness()

