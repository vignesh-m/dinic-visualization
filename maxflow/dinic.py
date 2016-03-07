""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence
from block_flow import BlockingFlowImageSequence
import matplotlib.image as mpimg
from graph import display_graph
import random
import numpy as np
from Queue import Queue

INF = float('inf')  # use double inf


def find_distances(graph, source):
    """ Find distances using bfs """
    dist = [INF for _ in graph]
    q = Queue()
    dist[source] = 0
    q.put(source)
    while(q.empty() == 0):
        current = q.get()
        for t in graph[current]:
            if dist[t[0]] == INF:
                dist[t[0]] = dist[current] + 1
                q.put(t[0])
    return dist


class DinicImageSequence(ImageSequence):
    """ dinic image sequence """
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

    def init_image(self):
        # set init image
        display_graph(self.graph, 'dinic_init')
        return mpimg.imread('dinic_init.png')

    def find_level_graph(self):
        self.level_graph = [[] for _ in self.graph]
        for i, l in enumerate(self.graph):
            for j, c in l:
                if self.dist[j] - self.dist[i] == 1:
                    self.level_graph[i].append((j, c))

    def next_image(self):
        if self.status == 1:
            print 'in blocking flow'
            _next = self.blocking_flow.next_image()
            if self.blocking_flow.complete():
                self.status = 0
            return _next
        else:
            self.dist = find_distances(self.graph, self.source)
            self.find_level_graph()
            if self.dist[self.sink] == INF:
                self.done = True
                print 'completed dinics'
                return None
            else:
                # find blocking flow
                print 'finding blocking flow'
                self.blocking_flow = BlockingFlowImageSequence(self.level_graph, self.vertices, self.edges, self.dist, self.source, self.sink)
                self.status = 1
                # update self.flow, self.graph(?)
                return self.blocking_flow.init_image()

    def complete(self):
        return self.done

    def residual(self, wt_graph):

        # capacity_graph gives a graph with all the maximum capacity of the edges

        vert = self.vertices

        # Residual graph
        res_graph = [[] for i in range(vert)]
        res_adj_matrix = np.zeros((vert, vert), dtype=np.int)

        # Capacity graph adj matrix
        wt_adj_matrix = np.zeros((vert, vert), dtype=np.int)

        # original graph adjacency matrix
        adj_matrix = np.zeros((vert, vert), dtype=np.int)

        for i in range(vert):
            for j in range(len(self.graph[i])):
                temp1, temp2 = self.graph[i][j]
                adj_matrix[i, temp1] = temp2

        for i in range(self.vertices):
            for j in range(len(wt_graph[i])):
                temp1, temp2 = wt_graph[i][j]
                wt_adj_matrix[i, temp1] = temp2

        # Find residual graph
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                res_adj_matrix[i, j] = (adj_matrix[i, j] - wt_adj_matrix[i, j]) + wt_adj_matrix[j, i]
                res_adj_matrix[j, i] = (adj_matrix[j, i] - wt_adj_matrix[j, i]) + wt_adj_matrix[i, j]

                # Store also as matrix and as a adjacency list form
                if res_adj_matrix[i, j] != 0:
                    res_graph[i].append((j, res_adj_matrix[i, j]))

                if res_adj_matrix[j, i] != 0:
                    res_graph[j].append((i, res_adj_matrix[j, i]))

        return res_graph


    def dinic_algo():

        vert = self.vertices
        graph_wt = [[] for i in range(vert)]

        for i in range(vert):
            for j in range(len(graph[i])):
                temp1, temp2 = graph[i][j]
                graph_zero_wt[i].append((temp1, 0))

        
        wt_adj_matrix = np.asmatrix(np.zeros((vert, vert), dtype=np.int))

        for v in range(vert):
            

            


        



