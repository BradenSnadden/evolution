from individual import individual
from population import population
from insert_mutation import insert_mutation
from partially_mapped_crossover import partially_mapped_crossover
from orderCrossover import orderCrossover
import numpy as np
pop = population()
print(np.shape(pop.popList))
pop.popList[0].calcFitness()
# pop.popList[4].calcFitness()
insert_mutation(pop.popList[0].city)
orderCrossover(pop.popList[0].city, pop.popList[1].city)



