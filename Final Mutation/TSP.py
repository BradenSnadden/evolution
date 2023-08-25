class TSP:
    import os
    from pathlib import Path
    import numpy as np

    # change directory to file location
    os.chdir(os.path.dirname(__file__))

    # create cities array from data in tsp file
<<<<<<< HEAD
    cities = np.genfromtxt("tsp.txt", dtype=float, skip_header=6, skip_footer=1)
    cities[:,1:]

    #N = number of rows
    N, num_cols = cities.shape

    print(cities)
=======
    cities = np.genfromtxt("tsp.txt", skip_header=6, skip_footer=1)
>>>>>>> df877e8d7d9692ed6013d640d52a9243246a085e

TSP()