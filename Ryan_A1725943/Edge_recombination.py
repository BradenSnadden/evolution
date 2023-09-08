import numpy as np
import random
from operator import itemgetter

#Function that calculates links between each element
def calculateEdges(Arr):
    pathEdges = []
    for position in range(len(Arr)):
        #first element in list = neighbour at end of list and from current index+1
        if position == 0:
            pathEdges.append([Arr[position], (Arr[-1], Arr[position+1])])
        #last element in list = neighbour at current index-1 and at start of list
        elif position == len(Arr)-1:
            pathEdges.append([Arr[position], (Arr[position-1], Arr[0])])
        #if it is neither first or last element neighbours at index-1 and index+1
        else:
            pathEdges.append([Arr[position], (Arr[position-1], Arr[position+1])])
    return pathEdges

#Function that sorts the edges array
def sortEdges(edgesArray):
    edgesArray_sorted = sorted(edgesArray, key=itemgetter(0))
    return edgesArray_sorted

#Function that unions both edge arrays
def unionEdges(edgesArray1, edgesArray2):
    Union = []
    sortedEdges1 = sortEdges(edgesArray1)
    sortedEdges2 = sortEdges(edgesArray2)

    for i in range(len(edgesArray1)):
        # store and combine the edges as a list and remove duplicates with set()
        # combinedEdges = list(sorted(set(sortedEdges1[i][1] + sortedEdges2[i][1])))
        #need to deal with duplicates and mark as common edge replace duplicates with -representation?
        combinedEdges = list(sorted(sortedEdges1[i][1] + sortedEdges2[i][1]))
        Union.append([edgesArray1[i][0], combinedEdges])
    

    return Union

def makeEdgeTable(Arr1, Arr2):
    Edges1 = calculateEdges(Arr1)
    Edges2 = calculateEdges(Arr2)
    edgeTable = unionEdges(Edges1,Edges2)
    return edgeTable

def edgeRecombination(Parent1, Parent2):
    Offspring = []
    edgeTable = makeEdgeTable(Parent1, Parent2)
    initial = random.choice([city[0] for city in edgeTable])
    Offspring.append(initial)
    

    return Offspring



Parent1 = np.array([1,2,3,4,5,6,7,8,9])
Parent2 = np.array([9,3,7,8,2,6,5,1,4])
print('-----------------------UNION---------------------------------')
Union = makeEdgeTable(Parent1, Parent2)
print(Union)
# child = edgeRecombination(Parent1, Parent2)
# print(child)