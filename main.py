""" Main driver """

from maxflow.dinic import DinicImageSequence
from maxflow.graph import input_graph, display_graph
from gui.image_display import start_gui

graph = input_graph()
imageSequence = DinicImageSequence(graph, source=0, sink=1)
start_gui(imageSequence)
