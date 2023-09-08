from individual import individual
from population import population
from insert_mutation import insert_mutation

from orderCrossover import orderCrossover
import numpy as np
pop = population()
pop.popList[0].calcFitness()
# pop.popList[4].calcFitness()
insert_mutation(pop.popList[0].city)
orderCrossover(pop.popList[0].city, pop.popList[1].city)



