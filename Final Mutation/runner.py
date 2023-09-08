from individual import individual
from population import population
from insert_mutation import insert_mutation
import random as random

from orderCrossover import orderCrossover
import numpy as np


all = np.empty((0), dtype=population)

pop = population()
all = np.append(all,pop)
for i in range(20):
    all =np.append(all,pop) 
all2 = np.copy(all)
all3 = np.copy(all)
all[0].popList[0].calcFitness()
# pop.popList[4].calcFitness()
insert_mutation(pop.popList[0].city)
orderCrossover(pop.popList[0].city, pop.popList[1].city)

for i in range(20000):
    for j in range(9):
        for k in range(20):
            if(random.randint(1,100) < 15):
                all[k].popList[j].city = insert_mutation(all[k].popList[j].city)
                all[k].popList[j].city = orderCrossover(all[k].popList[j].city, all[k].popList[j+1].city )
    if i % 10 == 0:
        bestFitness = 10000000
        for m in range(9):
            hold = all[k].popList[m].calcFitness()
            if hold < bestFitness:
                bestFitness = hold
    print("     ", i ,"      ")
    print(bestFitness)



all[0].popList[0].calcFitness()

