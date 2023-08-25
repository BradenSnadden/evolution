import os
from pathlib import Path
import numpy as np

os.chdir(os.path.dirname(__file__))

#f = open('tsp.txt', 'r')
#file_contents = f.read()
#print (file_contents)

cities = np.genfromtxt("tsp.txt", skip_header=6, skip_footer=1)
print(cities)

#f.close()


#print("hello world")



#class TSP:
    #cities = []
    #for line in f.readlines():
       # cities.append(line.split(' '))

       # print(cities)

