from individual import individual
from population import population
pop = population()
pop.popList[1] = individual()

print(pop[1].calcFitness())

