""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence

INF = 1000000000


def find_distances(graph, source):
    """ Find distances using bfs """
    # TODO implement
    return [INF for _ in graph]


class DinicImageSequence(ImageSequence):
    """ subclass image sequence """
    def __init__(self, graph, source, sink):
        ImageSequence.__init__(self)
        self.graph = graph
        self.source = source
        self.sink = sink
        self.flow = 0
        self.done = False
        self.status = 0  # status=1 when blocking flow is in progress
        print "dinic with", graph
        # set init image

    def next(self):
        if self.status == 1:
            _next = self.blocking_flow.next()
            if self.blocking_flow.complete():
                self.status = 0
            return _next
        else:
            dist = find_distances(graph, source)
            if dist[sink] == INF:
                self.done = True
            else:
                # find blocking flow
                self.blocking_flow = BlockingFlowImageSequence(self.graph, dist, self.source, self.sink)
                self.status = 1
                return self.next()

    def complete(self):
        return self.done


class BlockingFlowImageSequence(ImageSequence):
    """ find blocking flow from source to sink,
        given graph and distances array
    """
    def __init__(self, graph, dist, source, sink):
        ImageSequence.__init__(self)
        print "blocking flow", graph, dist
