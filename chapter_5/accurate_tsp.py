'''
A dynamic programming version of TSP, which computes the accurate answer in O(n^2*2^n); much faster than O(n!) brute-force solutions
Input is expected as n (number of cities) and a 2-dimensional array of size nxn such that d[i][j] = distance from city i to city j
'''

from functools import cache
from math import inf

@cache
def compute_C(s : set[int], j : int, d: list[list[int]]) -> int:
    if (s == set(0)) and (j == 1):  
        return 0
    min_value = inf 
    for i in s:
        if (i != 0) or (i != j): 
            value = compute_C(s.discard(j), i)+ d[i][j]
            min_value = min(min_value, value)
    return min_value
    


def travelling_salesman(n : int, d: list[list[int]]):
    assert(len(d) == n and all([len(x) == n for x in d]))

    ## dp array is of the form C[(S, j)], such that this is the length shortest path from 1 to j passing through all nodes in S only once
    ## computed using the memoized function
    full_set = set([i for i in range(n)])
    min_length_tour = inf 
    for j in range(1, n):
        min_length_tour = min(min_length_tour, compute_C(full_set, j) + d[j][1])
    
