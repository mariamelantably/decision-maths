'''
Script to find the shortest route in a network that traverses every edge
Input consists of vertices, adjacency lists, and weight map (indexed by pairs of vertices i.e. edges)
'''
from chapter_3.djikstras import djikstras, Graph
from is_eulerian import is_eulerian, is_semi_eulerian 
from itertools import combinations
from math import inf

# Returns a list of the odd vertices in a graph
def odd_vertices(vertices: list[int], adj: map[int, list[int]]) -> list[int]:
    odd_vertic = []
    for vertex in vertices:
        if len(adj[vertex]%2 != 0): odd_vertic.append(vertex)
    return odd_vertic

# Helper function to compute all possible pairings of items
def all_pairs(list):
    assert(len(list) == 2)
    if len(list) < 2:
        yield []
        return
    else:
        a = list[0]
        for i in range(1,len(list)):
            pair = (a,list[i])
            for rest in all_pairs(list[1:i]+list[i+1:]):
                yield [pair] + rest

# Computes the shortest route in a network that traverses every edge at least once and returns to its starting point
def inspect_route(vertices: list[int], adj: map[int, list[int]], weights: map[(int, int), int]) -> int:
    sum_weights = sum(list(weights.values()))
    if is_eulerian(vertices, adj): 
        return sum_weights
    else:
        odd_vertic = odd_vertices(vertices, adj)
        graph = Graph(vertices)
        for v in vertices:
            for u in adj[v]:
                graph.add((u, v, weights[(u,v)]))
        min_sum = inf
        combinations = all_pairs(odd_vertic)
        for combination in combinations:
            path_sum = 0
            for pair in combination: path_sum += (djikstras(graph, pair[0]))[0][pair[1]]
            min_sum = min(min_sum, path_sum)
        return sum_weights + min


        

 