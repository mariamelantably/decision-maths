from collections import defaultdict
class Graph:
    def __init__(self):
        self.set = defaultdict(list) #use a dictionary, with each vertex as the keys and the edges being a list
    
    def add(self, vertex, edge):
        self.set[vertex] = insert(self.set[vertex], edge)

#inserts l into an already sorted array of tuples, i.e. sorts edges by their weights 
def insert(arr, l):
    i = len(arr)-1
    arr.append(l)
    while arr[i][2] > l[2] and i >= 0:
        arr[i+1] = arr[i]
        i -= 1
    arr[i+1] = l
    return arr

#merges two already sorted lists
def merge(arr1, arr2):
    for i in arr1:
        arr2 = insert(arr2, i)
    return arr2


#prims algorithm takes a graph and finds the minimum spanning tree
def prims(g : Graph) -> Graph:
    added = [list(g.set.keys())[0]] 
    newG = Graph()
    vertices_to_consider = g.set[added[-1]]
    while len(added) < len(g.set):
        #take the first item from vertices_to_consider (guaranteed to not make a cycle), add it and its duplicate in
        new = vertices_to_consider[0]
        newG.add(new[0], new)
        newG.add(new[1], (new[1], new[0], new[2]))
        #update added with that one
        added.append(new[1])
        #remove the first one from vertices to consider,
        vertices_to_consider = vertices_to_consider[1:]
        #map over all the sets, and remove any vertices with the new vertex as the end vertex
        for x in list(g.set.keys()):
            g.set[x] = list(filter(lambda a: a[1] != new[1], g.set[x]))
        #merge vertices to consider with the new vertex's set (merge means they'll be sorted)
        vertices_to_consider = merge(vertices_to_consider, g.set[added[-1]])
        try:
            vertices_to_consider.remove((new[1], new[0], new[2]))
        except ValueError: #deals with the case where the already added one isnt in vertices_to_consider
            pass
    return newG



newGraph = Graph()
newGraph.add("A", ("A", "B", 10))
newGraph.add("A", ("A", "D", 4))
newGraph.add("B", ("B", "A", 10))
newGraph.add("B", ("B", "C", 5))
newGraph.add("B", ("B", "E", 13))
newGraph.add("C", ("C", "B", 5))
newGraph.add("C", ("C", "D", 9))
newGraph.add("C", ("C", "E", 8))
newGraph.add("D", ("D", "A", 4))
newGraph.add("D", ("D", "C", 9))
newGraph.add("D", ("D", "E", 7))
newGraph.add("E", ("E", "B", 13))
newGraph.add("E", ("E", "D", 7))
newGraph.add("E", ("E", "C", 8))
prims(newGraph)
