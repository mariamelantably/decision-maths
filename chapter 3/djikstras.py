from math import inf

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []
        self.adjacency = {}
        self.weights = [[None for i in range(len(vertices))] for i in range(len(vertices))] 
    
    def add(self, source, target, weight):
        if (self.weights[source][target] != None):
            raise ValueError 
        self.weights[source][target] = weight
        
        
        

def extract_min(queue, distances):
    m = inf
    m_index = -1
    for i in range(len(queue)):
        if distances[i] < m:
            m = distances[i]
            m_index = i
    return m_index



def djikstras(graph : Graph, source):
    d = {}
    pi = {}
    for v in graph.vertices:
        d[v] = inf
        pi[v] = None
    d[source] = 0
    queue = graph.vertices.copy()
    while queue != []:
        s = extract_min(queue, d)
        u = queue[s]
        queue.pop(s)
        for v in range(len(graph.weights[u])):
            g = graph.weights[u][v]
            if g != None:
                if d[u] + g < d[v]:
                    d[v] = d[u] + g
                    pi[v] = u
    return d, pi

newGraph = Graph([0, 1, 2, 3, 4])
newGraph.add(0, 1, 10)
newGraph.add(0, 3, 4)
newGraph.add(1, 2, 5)
newGraph.add(1, 4, 13)
newGraph.add(2, 3, 9)
newGraph.add(2, 4, 8)
newGraph.add(3, 4, 7)
x = djikstras(newGraph, 1)
print(x[0])
print(x[1])

            
