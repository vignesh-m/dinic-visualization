""" Graph utility functions. """
"""
    Graphs are adjacency lists with vertices numbered from 0..n-1
    each element in the list indexed at u is a pair (v,c) denoting edge from
    u to v with capacity c
"""
import graphviz
import sys


def input_graph(input_file=sys.stdin):
    """ read graph from file.
    n = number of vertices
    m = number of edges
    input format
    n m
    u v c (m times)

    line u v c refers to edge from u to v with capacity c

    returns graph, vertices, edges
    """
    n, m = map(int, input_file.readline().split())
    graph = [[] for _ in range(n)]
    for i in range(m):
        u, v, c = map(int, input_file.readline().split())
        graph[u].append((v, c))

    # modified to return edges also
    return graph, n, m


def display_graph(graph, filename="graphviz_output"):
    """ simply displays a graph using graphviz.
    renders to filename.png
    """
    dot = graphviz.Digraph(comment="max flow graph", format='png')
    n = len(graph)
    for i in map(str, range(n)):
        dot.node(i)
    for i in range(n):
        for j, c in graph[i]:
            dot.edge(str(i), str(j), label=str(c))
    dot.render(filename)
