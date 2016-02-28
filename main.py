""" Main driver """

from maxflow.dinic import DinicImageSequence,BlockingFlowImageSequence
from maxflow.graph import input_graph, display_graph
from gui.image_display import start_gui, ImageSequence

graph = input_graph()
display_graph(graph)
# imageSequence = ImageSequence(graph)
imageSequence = DinicImageSequence(graph, source=0, sink=1)
# imageSequence = BlockingFlowImageSequence(graph, source=0, sink=1, dist=[])
start_gui(imageSequence)
