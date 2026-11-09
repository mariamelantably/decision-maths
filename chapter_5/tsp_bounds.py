'''
A file to compute upper and lower bounds for the travelling salesman problem using various methods
To be used alongside an accurate TSP solver. 
Uses adjacency list representation of graphs
'''

from chapter_3.prims import Graph, prims
from chapter_3.nearest_neighbour import nearest_neighbour
from math import inf
from heapq import nlargest


def construct_graph(vertices: list[int], adj: map[int, list[int]], weights: map[(int, int), int]) -> Graph:
    new_graph = Graph()
    for vertex in vertices:
        for outgoing in adj[vertex]:
            new_graph.add(vertex, (vertex, outgoing, weights[(vertex, outgoing)]))
    return new_graph

# Computes lower bound via MSTs
def upper_bound_MST(vertices: list[int], adj: map[int, list[int]], weights: map[(int, int), int]) -> int:
    return prims(construct_graph(vertices, adj, weights)).get_weight() * 2

def lower_bound_RMST(vertices: list[int], adj: map[int, list[int]], weights: map[(int, int), int]) -> int:
    lower_bound = -1*inf
    for vertex in vertices:
        new_vertices = vertices.remove(vertex)
        new_adj = {k:v for k,v in adj.items() if k != vertex}
        rmst_weight = prims(construct_graph(new_vertices, new_adj, weights)).get_weight()
        connection_weight = sum(nlargest([weights[(vertex, u)] for u in adj[vertex]], 2))
        lower_bound = max(lower_bound, rmst_weight + connection_weight)
    return lower_bound

def upper_bound_NN(vertices: list[int], adj: map[int, list[int]], weights: map[(int, int), int]) -> int:
    graph = construct_graph(vertices, adj, weights)
    min_weight_tour = inf
    for vertex in vertices:
        min_weight_tour = min(nearest_neighbour(graph, vertex))
    return min_weight_tour



