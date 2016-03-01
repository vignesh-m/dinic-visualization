""" Main driver """

from maxflow.dinic import DinicImageSequence
from maxflow.graph import input_graph, display_graph
from maxflow.block_flow import blocking_flow
from gui.image_display import start_gui

graph, v, e = input_graph()
display_graph(graph)
print graph
block_graph = blocking_flow(graph, v, e, 0, v - 1)
print "blocking flow", block_graph
display_graph(block_graph, "Block_flow")
