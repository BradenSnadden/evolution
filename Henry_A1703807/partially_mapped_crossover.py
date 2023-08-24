# Python3 program to perform Partially Mapped Crossover (PMX)

import random
import numpy as np

def partially_mapped_crossover(parent1, parent2):

    rng = np.random.default_rng()

    # Randomly Select Cutoff Points
    seg_cutoff_1, seg_cutoff_2 = np.sort(rng.choice(np.arange(len(parent1)+1), size=2, replace=False))

    def PMX_single_offspring(parent1, parent2):
        offspring = np.zeros(len(parent1), dtype=parent1.dtype)

        # Copy the segment (to be mapped) from parent1
        offspring[seg_cutoff_1:seg_cutoff_2] = parent1[seg_cutoff_1:seg_cutoff_2]

        # copy leftover from parent2 (if it's not already there)
        for i in np.concatenate([np.arange(0,seg_cutoff_1), np.arange(seg_cutoff_2,len(parent1))]):
            candidate = parent2[i]
            while candidate in parent1[seg_cutoff_1:seg_cutoff_2]: # to allow for several successive mappings
                # print(f"Candidate {candidate} not valid in position {i}") # Debug Tool
                candidate = parent2[np.where(parent1 == candidate)[0][0]]
            offspring[i] = candidate
        return offspring

    offspring1 = PMX_single_offspring(parent1, parent2)
    offspring2 = PMX_single_offspring(parent2, parent1)
    return offspring1, offspring2
 
# Main
parent1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
parent2 = np.array([9, 3, 7, 8, 2, 6, 5, 1, 4])

print(partially_mapped_crossover(parent1,parent2))
