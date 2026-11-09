from math import inf
from numpy import argmin
from collections import defaultdict
from prims import Graph

# Returns the weight of the tour from source using the nearest neighbour algorithm 
def nearest_neighbour(graph : Graph, source):
    visited = []
    v = source
    sum_weights = 0
    vertices = graph.set.keys()
    w2 = defaultdict(defaultdict(int))
    visited.append(v)
    for (v, lis) in graph.set():
        for u in lis:
            w2[v][u[1]] = u[2] 
    for i in vertices:
        w2[i][v] = inf 
    while (visited != vertices):
        curr = min(w2[v])
        if curr < inf:
            visited.append(argmin(w2[v]))
            sum_weights += curr
            v = argmin(w2[v])
            for i in range(len(vertices)):
                w2[i][v] = inf 
        else:
            break
    sum_to_start = inf
    for edge in graph.set[v]:
        if edge[1] == source: 
            sum_to_start = edge[2]
    return sum_weights + sum_to_start

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
            
