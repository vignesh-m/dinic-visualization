""" Main driver """

from maxflow.dinic import DinicImageSequence, find_distances
from maxflow.graph import input_graph, display_graph
from maxflow.block_flow import BlockingFlowImageSequence
from gui.image_display import start_gui

import pdb

graph, v, e = input_graph()
display_graph(graph)
print graph

# pdb.set_trace()


def dinic_test():
    b = DinicImageSequence(graph, v, e, 0, v - 1)
    start_gui(b)


def blocking_flow_test():
    b = BlockingFlowImageSequence(graph, v, e, [], 0, v - 1)
    block_graph = b.blocking_flow()
    print "blocking flow", block_graph
    display_graph(block_graph, "Block_flow")


def residual_test():
    graph_zero_wt = [[] for i in range(v)]

    for i in range(v):
        for j in range(len(graph[i])):
            temp1, temp2 = graph[i][j]
            graph_zero_wt[i].append((temp1, 0))

    b = DinicImageSequence(graph, v, e, 0, v - 1)
    res_graph = b.find_residual()

    display_graph(res_graph, "residual_graph")


def bfs_test():
    print find_distances(graph, 0)

# bfs_test()
dinic_test()
# residual_test()
