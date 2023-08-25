class TSP:
    import os
    from pathlib import Path
    import numpy as np

    os.chdir(os.path.dirname(__file__))

    cities = np.genfromtxt("tsp.txt", skip_header=6, skip_footer=1)
    print(cities)

TSP()