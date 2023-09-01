class TSP:
    import os
    from pathlib import Path
    import numpy as np

    # change directory to file location
    os.chdir(os.path.dirname(__file__))

    # create cities array from data in tsp file
    cities = np.genfromtxt("tsp.txt", dtype=float, skip_header=6, skip_footer=1)
    # remove node number (i.e first column of data)
    cities = np.delete(cities, 0, axis=1)

    #N = number of rows, num_cols = number of columns
    N, num_cols = cities.shape

TSP()