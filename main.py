""" Main driver """

from maxflow.dinic import DinicImageSequence
from maxflow.graph import input_graph, display_graph
from gui.image_display import start_gui

#temp holds edges
graph,temp = input_graph()
display_graph(graph)
imageSequence = DinicImageSequence(graph)
start_gui(imageSequence)
