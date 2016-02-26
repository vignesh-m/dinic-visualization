""" Main driver """

from maxflow.dinic import DinicImageSequence
from gui.image_display import start_gui

graph = []
imageSequence = DinicImageSequence(graph)
start_gui(imageSequence)
