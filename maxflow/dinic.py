""" Implementation of Dinic's algorithm for max flow """
from gui.image_display import ImageSequence
from block_flow import BlockingFlowImageSequence
import matplotlib.image as mpimg
from graph import display_graph
import random
import numpy as np
from Queue import Queue
from copy import deepcopy

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

        # Self.graph is initialized to graph with all weights as zero
        self.graph = [[] for i in range(nvertices)]
        for i in range(nvertices):
            for j in range(len(graph[i])):
                temp1, temp2 = graph[i][j]
                self.graph[i].append((temp1, 0))
        # Stores maximum capcities
        self.graph_capacity = graph

        # Store edges,vertices,source and sink vertex
        self.edges = nedges
        self.vertices = nvertices
        self.source = source
        self.sink = sink

        self.flow = 0
        self.done = False
        # status=1 when blocking flow is in progress
        self.status = 0
        self.blocking_flow = None
        print "dinic with", graph
        # set init image

    def init_image(self):
        # set init image
        display_graph(self.graph, 'dinic_init')
        return mpimg.imread('dinic_init.png')

    def find_level_graph(self):
        self.find_residual()
        self.level_graph = [[] for _ in self.graph]
        for i, l in enumerate(self.residual_graph):
            for j, c in l:
                if self.dist[j] - self.dist[i] == 1:
                    self.level_graph[i].append((j, c))

    def next_image(self):

        print "graph weights",self.graph
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

                image = self.blocking_flow.init_image()
                self.block_flow_graph = self.blocking_flow.block_flow
                print self.block_flow_graph
                self.update_flow()
                print self.graph
                return image

    def complete(self):
        return self.done

    def find_residual(self):

        vert = self.vertices

        # Residual graph
        res_graph = [[] for i in range(vert)]
        res_adj_matrix = np.zeros((vert, vert), dtype=np.int)

        # Capacity graph adj matrix
        cap_adj_matrix = np.zeros((vert, vert), dtype=np.int)

        # original graph adjacency matrix
        adj_matrix = np.zeros((vert, vert), dtype=np.int)

        for i in range(vert):
            for j in range(len(self.graph[i])):
                temp1, temp2 = self.graph[i][j]
                adj_matrix[i, temp1] = temp2

        for i in range(vert):
            for j in range(len(self.graph_capacity[i])):
                temp1, temp2 = self.graph_capacity[i][j]
                cap_adj_matrix[i, temp1] = temp2

        # Find residual graph
        for i in range(self.vertices):
            for j in range(i + 1, self.vertices):
                res_adj_matrix[i, j] = (cap_adj_matrix[i, j] - adj_matrix[i, j]) + adj_matrix[j, i]
                res_adj_matrix[j, i] = (cap_adj_matrix[j, i] - adj_matrix[j, i]) + adj_matrix[i, j]

                # Store also as matrix and as a adjacency list form
                if res_adj_matrix[i, j] != 0:
                    res_graph[i].append((j, res_adj_matrix[i, j]))

                if res_adj_matrix[j, i] != 0:
                    res_graph[j].append((i, res_adj_matrix[j, i]))

        self.residual_graph = res_graph
        return res_graph, res_adj_matrix

    def update_flow(self):
        """
        Update self.graph etc, after getting a blocking_flow
        """
        for i in range(len(self.graph)):
            for j in range(len(self.graph[i])):
                if i < range(len(self.block_flow_graph)) and j < range(len(self.block_flow_graph[i])):
                    self.graph[i][j] = (self.graph[i][j][0], self.graph[i][j][1] + self.block_flow_graph[i][j][1])

    def dinic_algo():

        # TODO alter function for using in visualization
        vert = self.vertices

        adj_matrix = (np.zeros((vert, vert), dtype=np.int))
        cap_adj_matrix = np.zeros((vert, vert), dtype=np.int)

        # Initialize adjacency matrices for capacity and current graph
        for i in range(vert):
            for j in range(len(self.graph[i])):
                temp1, temp2 = self.graph[i][j]
                adj_matrix[i, temp1] = temp2

        for i in range(vert):
            for j in range(len(self.graph_capacity[i])):
                temp1, temp2 = wt_graph[i][j]
                cap_adj_matrix[i, temp1] = temp2

        for v in range(vert):
            """
             TODO :     why is level graph being calculate on self.graph(suggestion : create self.res_graph ??
                        New class for residual graph ??

                        create a self.adj_matrix object instead of recreating the object?
            """
# loop start:
            # keep a copy of capacity and original graph

            # compute residual graph
            # Compute level_graph
            # Computer blocking flow

            # Subtract the weights of graph with blocking flow graph
            # ?? Use adjacency_matrix for above? (since will be much faster)
            # also create adjacency list since it is require for graphviz

            # if no change in flow after update exit loop(i.e. no blocking flow
            # loop again(i.e)

            block = BlockingFlowImageSequence(self.level_graph, self.vertices, self.edges, dist, self.source, self.sink)

            block_graph = block.blocking_flow()
            block_graph_adj = block.get_block_flow_adj()
