from individual import individual
from population import population
import insertMutation
import numpy as np
pop = population()
print(np.shape(pop.popList))
pop.popList[0].calcFitness()
# pop.popList[4].calcFitness()
pop.popList[0].swap

