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
print(all[0].popList[0].calcFitness())
for i in range (442):
    print(all[0].popList[0].city[i][0])





# case 1 
pop_1 = population()

pop_list_0 = []
# print("len",len(pop.popList[0].city))
for i in range(len(pop_1.popList[0].city)):
    pop_list_0.append(pop.popList[0].city[i][0])
# print(pop_list_0)
tmp = insert_mutation(np.array(pop_list_0))
# tmp2 = cycle_crossover(pop.popList[0].city,pop.popList[1].city)

print("tmp,",tmp)
# print("tmp2,",tmp2)

# case 2

pop_list_1 = []
pop_list_2 = []
pop_2 = population()
pop_3 = population()
# print("len",len(pop.popList[1].city))
for i in range(len(pop_2.popList[0].city)):
    pop_list_1.append(pop_2.popList[0].city[i][0])
# print(pop_list_0)
for i in range(len(pop_3.popList[0].city)):
    pop_list_2.append(pop_3.popList[0].city[i][0])

tmp2 = orderCrossover(pop_list_1, pop_list_2)

print("tmp2,",tmp2)






# # pop.popList[4].calcFitness()
# #insert_mutation(pop.popList[0].city)
# #orderCrossover(pop.popList[0].city, pop.popList[1].city)

# # for i in range(20000):
# #     for j in range(9):
# #         for k in range(20):
# #             if(random.randint(1,100) < 15):
# #                 all[k].popList[j].city = np.copy(insert_mutation(all[k].popList[j].city))
# #                 all[k].popList[j].city = np.copy(orderCrossover(all[k].popList[j].city, all[k].popList[j+1].city ))
# #     if i % 10 == 0:
# #         bestFitness = 10000000
# #         for m in range(9):
# #             hold = all[k].popList[m].calcFitness()
# #             if hold < bestFitness:
# #                 bestFitness = hold
# #     print("     ", i ,"      ")
# #     print(bestFitness)



# # all[0].popList[0].calcFitness()

