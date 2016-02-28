""" Main driver """

from maxflow.dinic import DinicImageSequence
from maxflow.graph import input_graph, display_graph
from gui.image_display import start_gui, ImageSequence

graph = input_graph()
display_graph(graph)
imageSequence = ImageSequence(graph)
start_gui(imageSequence)
