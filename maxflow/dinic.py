""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence


class DinicImageSequence(ImageSequence):
    """ subclass image sequence """
    def __init__(self, graph):
        ImageSequence.__init__(self)
        print "dinic with", graph
