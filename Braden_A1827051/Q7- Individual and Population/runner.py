from individual import individual
from population import population
pop = population()
a = individual()
pop.popList[1] = a

print(individual.calcFitness(pop[1]))

