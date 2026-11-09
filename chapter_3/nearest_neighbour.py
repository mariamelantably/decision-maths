from math import inf
from numpy import argmin
from collections import defaultdict
from prims import Graph

def nearest_neighbour(graph : Graph, source):
    visited = []
    v = source
    vertices = graph.set.keys()
    w2 = defaultdict(defaultdict(int))
    visited.append(v)
    for i in vertices:
        w2[i][v] = inf 
    while (visited != graph.vertices[0]):
        curr = min(w2[v])
        if curr < inf:
            visited.append(argmin(w2[v]))
            v = argmin(w2[v])
            for i in range(len(w2[0])):
                w2[i][v] = inf 
        else:
            x
    return visited

newGraph = Graph([0, 1, 2, 3, 4])
newGraph.add(0, 1, 10)
newGraph.add(0, 3, 4)
newGraph.add(1, 2, 5)
newGraph.add(1, 4, 13)
newGraph.add(2, 3, 9)
newGraph.add(2, 4, 8)
newGraph.add(3, 4, 7)
x = nearest_neighbour(newGraph)
print(x)
            
