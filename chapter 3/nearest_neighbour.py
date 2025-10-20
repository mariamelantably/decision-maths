from math import inf
from numpy import argmin

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.adjacency = {}
        self.weights = [[inf for _ in range(len(vertices))] for _ in range(len(vertices))] 
    
    def add(self, source, target, weight):
        if (self.weights[source][target] != inf):
            raise ValueError 
        self.weights[source][target] = weight

def nearest_neighbour(graph):
    visited = []
    v = graph.vertices[0]
    w2 = graph.weights.copy()
    visited.append(v)
    for i in range(len(w2[0])):
        w2[i][v] = inf 
    while (visited != graph.vertices[0]):
        curr = min(w2[v])
        if curr < inf:
            visited.append(argmin(w2[v]))
            v = argmin(w2[v])
            for i in range(len(w2[0])):
                w2[i][v] = inf 
        else:
            break
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
            
