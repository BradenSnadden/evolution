import random

def fitness_proportional_selection(population, fitness_scores):
    # Calculate the sum of fitness scores
    total_fitness = sum(fitness_scores)

    # Generate a random value between 0 and the total fitness
    rand_value = random.uniform(0, total_fitness)

    # Initialize variables for tracking the cumulative fitness
    cumulative_fitness = 0
    selected_index = 0

    # Iterate through the population to find the selected individual
    for i, fitness in enumerate(fitness_scores):
        cumulative_fitness += fitness
        if cumulative_fitness >= rand_value:
            selected_index = i
            break

    # Return the selected individual
    return population[selected_index]


def tournament_selection(population, fitness_scores, tournament_size=2):
    # Ensure the tournament size is within the population size
    tournament_size = min(tournament_size, len(population))
    
    # Randomly select 'tournament_size' individuals from the population
    tournament_individuals = random.sample(population, tournament_size)

    # Find the individual with the highest fitness in the tournament
    tournament_fitness_scores = [fitness_scores[population.index(individual)] for individual in tournament_individuals]
    winner_index = tournament_fitness_scores.index(max(tournament_fitness_scores))
    
    # Return the selected individual
    return tournament_individuals[winner_index]

