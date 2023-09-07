import random
import numpy as np

# Helper function to read coordinates from a file
def read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith("NODE_COORD_SECTION"):
                break
        for line in file:
            if line.strip() == "EOF":
                break
            parts = line.strip().split()
            x, y = map(float, parts[1:])
            coordinates.append((x, y))
    return coordinates

# Helper function to calculate distance between two points
def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2) # Euclidean algorithm

# Initialize a population of tours
def initialize_population(num_individuals, num_cities):
    population = []
    for _ in range(num_individuals):
        tour = list(range(num_cities))
        random.shuffle(tour)
        population.append(tour)
    return population

# Evaluate the fitness of a tour (total tour length)
def evaluate_tour(tour, coordinates):
    total_distance = 0.0
    num_cities = len(tour)
    for i in range(num_cities):
        from_city = tour[i]
        to_city = tour[(i + 1) % num_cities]
        total_distance += calculate_distance(coordinates[from_city], coordinates[to_city])
    return total_distance

def apply_inver_over(tour, coordinates, mutation_probability):
    num_cities = len(tour)
    c = random.randint(0, num_cities - 1)
    S_prime = tour.copy()
    next_city = None

    while True:
        if random.random() <= mutation_probability:
            remaining_cities = list(set(S_prime) - {c})
            c_prime = random.choice(remaining_cities)  # Randomly select a city c' from remaining cities in S'
        else:
            other_individual = random.choice(population)
            index_c_in_other = other_individual.index(c)
            if index_c_in_other == 0:
                c_prime = other_individual[-1]  # If c is the first city in the other individual, set c' to the last city
            else:
                c_prime = other_individual[index_c_in_other - 1]  # Otherwise, set c' to the 'next' city to c in the other individual

        if c_prime == next_city:
            break  # Exit the loop if c' is the same as the previously selected city

        index_c = S_prime.index(c)
        index_c_prime = S_prime.index(c_prime)

        if index_c < index_c_prime:
            # Invert the section from the next city of city c to the city c' in S'
            S_prime[index_c:index_c_prime+1] = S_prime[index_c:index_c_prime+1][::-1]
        else:
            # Invert the section from the next city of city c' to the city c in S'
            S_prime[index_c_prime:index_c+1] = S_prime[index_c_prime:index_c+1][::-1]

        tour_length_prime = evaluate_tour(S_prime, coordinates)

        if tour_length_prime < evaluate_tour(tour, coordinates):
            tour = S_prime.copy()  # If the new tour is better, update the tour

        next_city = c_prime

    return tour

# File path to the TSP data (e.g., "pcb442.tsp")
file_path = "pcb442.tsp"

# Load coordinates and initialize parameters
coordinates = read_coordinates(file_path)
num_cities = len(coordinates)
population_size = 1
mutation_probability = 0.2
iterations = 30  # Number of iterations
generations = 20000  # Number of generations per iteration

# Initialize the population
population = initialize_population(population_size, num_cities)

# Track the best tour and its length
best_tour = population[0]
best_tour_length = evaluate_tour(best_tour, coordinates)
no_improvement_count = 0
max_no_improvement = 20  # Adjust as needed

# Initialize an empty NumPy array to store fitness values for all generations
all_fitness_values = np.array([])

# Main loop
for iteration in range(iterations):  # Iterate over total iterations
    fitness_values = np.array([])  # To store fitness values for calculating median

    for generation in range(generations):
        # Apply Inver-Over to the entire population once per generation
        population = [apply_inver_over(individual, coordinates, mutation_probability) for individual in population]

        # Evaluate the fitness of the population and append to fitness_values
        generation_fitness = np.array([evaluate_tour(tour, coordinates) for tour in population])
        fitness_values = np.append(fitness_values, generation_fitness)

        # Find the best tour in the population
        best_tour_index = np.argmin(generation_fitness)
        new_best_tour = population[best_tour_index]
        new_best_tour_length = generation_fitness[best_tour_index]

        # Check for improvement
        if new_best_tour_length < best_tour_length:
            best_tour = new_best_tour
            best_tour_length = new_best_tour_length
            no_improvement_count = 0
        else:
            no_improvement_count += 1

    # Calculate the median fitness after collecting fitness values for the current generation
    median_fitness = np.median(all_fitness_values)

    # Print the current best and median fitness for the current iteration
    print(f"Iteration {iteration + 1}: Best Fitness = {best_tour_length} Median Fitness = {median_fitness}")

    # Add Current best to all fitness values
    all_fitness_values = np.append(all_fitness_values, best_tour_length)

# Print the best tour and its length
print("Best Tour:", best_tour)
print("Best Tour Length:", best_tour_length)