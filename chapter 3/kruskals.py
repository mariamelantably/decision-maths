class Graph:
    def __init__(self, vertices):
        #an edge is represented as a tuple with start vertex, end vertex, weight
        self.edges = [] #use a sorted list of edges, bc this is the easiest representation w.r.t. kruskal's algorithm
        self.vertices = vertices
        self.parents = dict() 
        for v in vertices: #initialise every vertex as its own parent
            self.parents[v] = v
    
    def add(self, edge):
        self.edges = insert(self.edges, edge)
    
    #this part is for the union-find algorithm, that helps in detecting cycles in the graph
    def find(self, vertex):
        if self.parents[vertex] == vertex:
            return vertex
        else:
            x = self.parents[vertex]
            return self.find(x)
        
    def union(self, x, y):
        self.parents[self.find(y)] = self.find(x)

#inserts l into an already sorted array of tuples, i.e. sorts edges by their weights 
def insert(arr, l):
    i = len(arr)-1
    arr.append(l)
    while arr[i][2] > l[2] and i >= 0:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = l
    return arr

def kruskals(g : Graph) -> Graph:
    newG = Graph(g.vertices)
    arr = g.edges.copy()
    while len(g.vertices) - 1 != len(newG.edges) or arr == []:
        #take first element (guarenteed to not make a cycle, due to processing after addition)
        x = arr[0]
        #add it in, and append both to vertices added
        if newG.find(x[0]) != newG.find(x[1]):
            newG.add(x)
            newG.union(x[0], x[1])
        arr = arr[1:]
    return newG 



newGraph = Graph(["A", "B", "C", "D", "E"])
newGraph.add(("A", "B", 10))
newGraph.add(("A", "D", 4))
newGraph.add(("B", "C", 5))
newGraph.add(("B", "E", 13))
newGraph.add(("C", "D", 9))
newGraph.add(("C", "E", 8))
newGraph.add(("D", "E", 7))
x = kruskals(newGraph)
print(x.vertices, x.edges)
