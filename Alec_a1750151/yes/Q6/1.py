import os
from pathlib import Path
#import numpy as np

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

os.getcwd()

#f = open('tsp.txt', 'r')



#cities = numpy.genfromtxt(fname = f, skip_header=7)
#print(cities)

#class TSP:
    #cities = []
    #for line in f.readlines():
       # cities.append(line.split(' '))

       # print(cities)

