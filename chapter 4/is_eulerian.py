'''
A file that detects whether a graph is eulerian, semi-eulerian, or netiher.
Graph representations are expected as vertices and adjacency list maps, indexed by individual vertices.
'''

# Recursive visiting function for DFS
def visit(vertex: int, adj: map[int, list[int]], visited):
    visited += vertex
    for v in adj[vertex]:
        if v not in visited:
            visited = visit(vertex, adj, visited)
    return visited

# Computes the visited vertices from arbitrary root using DFS and checks it is equal to the entire vertex set
def is_connected(vertices: list[int], adj: map[int, list[int]]):
    if len(vertices) == 0: return False
    visited = visit(vertices[0], adj, {})
    return visited == vertices 

# Counts the number of odd vertices in a graph
def number_odd(vertices: list[int], adj: map[int, list[int]]):
    odd_degree = 0
    for vertex in vertices:
        if len(adj[vertex]%2 != 0): odd_degree += 1
    return odd_degree

# Checks if a graph is eulerian
def is_eulerian(vertices: list[int], adj: map[int, list[int]]):
    return is_connected(vertices, adj) & (number_odd(vertices, adj) == 0)

# Checks if a graph is semi-eulerian
def is_semi_eulerian(vertices: list[int], adj: map[int, list[int]]):
    return is_connected(vertices, adj) & (number_odd(vertices, adj) == 2)
