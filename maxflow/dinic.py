""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence
from block_flow import BlockingFlowImageSequence
import matplotlib.image as mpimg
from graph import display_graph
import random

INF = 1000000000  # use double inf


class DinicImageSequence(ImageSequence):
    """ subclass image sequence """
    def __init__(self, graph, nvertices, nedges, source, sink):
        ImageSequence.__init__(self)
        self.graph = graph
        self.edges = nedges
        self.vertices = nvertices
        self.source = source
        self.sink = sink

        self.flow = 0
        self.done = False
        self.status = 0  # status=1 when blocking flow is in progress
        self.blocking_flow = None
        print "dinic with", graph
        # set init image

    def find_distances(self):
        """ Find distances using bfs """
        # TODO implement
        # return [random.choice([0, INF]) for _ in graph]
        return [0 for _ in self.graph]

    def init_image(self):
        # set init image
        display_graph(self.graph, 'dinic_init')
        return mpimg.imread('dinic_init.png')

    def next_image(self):
        if self.status == 1:
            print 'in blocking flow'
            _next = self.blocking_flow.next_image()
            if self.blocking_flow.complete():
                self.status = 0
            return _next
        else:
            dist = self.find_distances()
            if dist[self.sink] == INF:
                self.done = True
                print 'completed dinics'
                return None
            else:
                # find blocking flow
                print 'finding blocking flow'
                self.blocking_flow = BlockingFlowImageSequence(self.graph, self.vertices, self.edges, dist, self.source, self.sink)
                self.status = 1
                # update self.flow, self.graph(?)
                return self.blocking_flow.init_image()

    def complete(self):
        return self.done
