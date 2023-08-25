import random

def inversion_mutation(permutation):
    # Ensure the permutation has at least two elements
    if len(permutation) < 2:
        return permutation

    # Select two distinct positions in the permutation
    position1, position2 = random.sample(range(len(permutation)), 2)
    start = min(position1, position2)
    end = max(position1, position2)

    # Perform inversion by reversing the elements between the selected positions

    return permutation[:start] + list(reversed(permutation[start:end+1])) + permutation[end+1:]

def cycle_crossover(parent1, parent2):
    cycles = [-1] * len(parent1)
    cycle_no = 1
    cyclestart = (i for i,v in enumerate(cycles) if v < 0)

    for pos in cyclestart:

        while cycles[pos] < 0:
            cycles[pos] = cycle_no
            pos = parent1.index(parent2[pos])

        cycle_no += 1

    child1 = [parent1[i] if n%2 else parent2[i] for i,n in enumerate(cycles)]
    child2 = [parent2[i] if n%2 else parent1[i] for i,n in enumerate(cycles)]

    return child1, child2