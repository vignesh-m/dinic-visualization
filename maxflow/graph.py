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


def display_graph(graph, filename="graphviz_output", highlight_path=None, capacities=None):
    """ simply displays a graph using graphviz.
    renders to filename.png
    """
    def label(edge, weight, capacities):
        if capacities is not None:
            return str(weight) + ' / ' + str(capacities[edge])
        else:
            return str(weight)
    dot = graphviz.Digraph(comment="max flow graph", format='png')
    n = len(graph)
    for i in map(str, range(n)):
        dot.node(i)
    if highlight_path:
        path_edges = zip(highlight_path, highlight_path[1:])
    for i in range(n):
        for j, c in graph[i]:
            if highlight_path and (i, j) in path_edges:
                print 'got path edge', (i, j)
                dot.edge(str(i), str(j), label=label((i, j), c, capacities), color='red')
            else:
                dot.edge(str(i), str(j), label=label((i, j), c, capacities))
    dot.render(filename)
