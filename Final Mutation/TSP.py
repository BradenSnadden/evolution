class TSP:
    import os
    from pathlib import Path
    import numpy as np

    # change directory to file location
    os.chdir(os.path.dirname(__file__))

    # create cities array from data in tsp file
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 7c6b7fdae6b97ac7b5f236a0dee8ade4a27ec028
    cities = np.genfromtxt("tsp.txt", dtype=float, skip_header=6, skip_footer=1)
    cities[:,1:]

    #N = number of rows
    N, num_cols = cities.shape

    print(cities)
<<<<<<< HEAD
=======
    cities = np.genfromtxt("tsp.txt", skip_header=6, skip_footer=1)
>>>>>>> df877e8d7d9692ed6013d640d52a9243246a085e
=======
>>>>>>> 7c6b7fdae6b97ac7b5f236a0dee8ade4a27ec028

TSP()