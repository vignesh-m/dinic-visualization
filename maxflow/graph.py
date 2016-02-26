""" Graph utility functions. """
"""
    Graphs are adjacency lists with vertices numbered from 0..n-1
    each element in the list indexed at u is a pair (v,c) denoting edge from
    u to v with capacity c
"""
import sys


def input_graph(input_file=sys.stdin):
    """ read graph from file.
    n = number of vertices
    m = number of edges
    input format
    n m
    u v c (m times)

    line u v c refers to edge from u to v with capacity c
    """
    n, m = map(int, raw_input().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, c = map(int, raw_input().split())
        graph[u].append((v, c))
    return graph
