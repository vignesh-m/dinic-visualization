""" Find a blocking flow of a graph.
    In a blocking flow, every source-sink path has atleast
    one saturated edge -> there is no such path in the residual graph.

    Finding a blocking flow in the level graph guarantees that the
    source-sink distance will decrease by atleast one.
"""
from graph import display_graph, input_graph
from gui.image_display import ImageSequence
import numpy as np


class BlockingFlowImageSequence(ImageSequence):
    """ find blocking flow from source to sink,
        given graph and distances array
    """
    def __init__(self, graph, nvertices, nedges, dist, source, sink):
        ImageSequence.__init__(self)
        self.graph = graph
        self.edges = nedges
        self.vertices = nvertices
        self.dist = dist
        self.source = source
        self.sink = sink

    def path_found(self):
        print "path found"

    def blocking_flow(self):
        """
        Finds a blocking flow of graph from source to sink.
        s - source, t - sink
        """
        graph = self.graph
        vert = self.vertices
        edges = self.edges
        source = self.source
        sink = self.sink
        # TODO check the complexity of below function
        # store the resulting graph
        final_graph_adj = np.zeros((vert, vert), dtype=np.int)
        final_graph = [[] for i in range(vert)]

        # Both adjacency list and adjacency matrix used.

        # Use sets as adjacency list so that queries are faster
        graph_sets = [set() for i in range(vert)]
        for i in range(vert):
            for j in range(len(graph[i])):
                temp1, temp2 = graph[i][j]
                graph_sets[i].add(temp1)

        # Adjacency Matrix ,A[i][j] stores residue of edge from i to j
        adj_matrix = np.zeros((vert, vert), dtype=np.int)
        for i in range(vert):
            for j in range(len(graph[i])):
                temp1, temp2 = graph[i][j]
                adj_matrix[i, temp1] = temp2

        # loop |E| times on modified DFS
        for i in range(edges):

            # TODO check if this is correct
            # exit if no edge from s
            if len(graph_sets[source]) == 0:
                break

            # initialize path and minimum weight along s-t path
            path = []
            path.append(source)

            min_wt = float('inf')
            # finds a single s-t path and updates residues along that path.
            while True:

                # if path is empty then exit and terminate the bfs
                # since above means no s-t path is there
                if len(path) == 0:
                    break

                # get last vertex in s-t path
                curr = path[-1]

                # Check if any vertices are adjacent to curr
                # If no, then no s-t path exists
                # Mark all incident edges for deletion next time they are seen
                # Achieve above by setting all adjacency matrix entries -1 for that vertex

                # Change to true if you find a child of curr
                child_exists = False

                # find the last available child of curr
                while (not child_exists) and len(graph_sets[curr]) != 0:
                    # get last vertex adjacent to curr
                    child = graph_sets[curr].pop()

                    # if valid child found
                    if adj_matrix[curr, child] != 0:
                        child_exists = True
                        # add back popped edge if it is a valid child
                        graph_sets[curr].add(child)

                # if no child node found, then set curr for deletion
                if len(graph_sets[curr]) == 0:
                    # set for deletion in adj_matrix
                    adj_matrix[:, curr] = 0
                    # remove vertex from path
                    path.pop()
                    continue

                # else path augmentation with child
                # update path and min_wt in path
                path.append(child)

                if min_wt > adj_matrix[curr, child]:
                    min_wt = adj_matrix[curr, child]

                # if s-t path is found
                if child == sink:
                    # Decrement path weight by minimum weight along entire path
                    # and update final_graph
                    self.path_found()
                    while len(path) > 1:
                        temp1 = path.pop()
                        temp2 = path[-1]
                        adj_matrix[temp2, temp1] = adj_matrix[temp2, temp1] - min_wt
                        final_graph_adj[temp2, temp1] = final_graph_adj[temp2, temp1] + min_wt
                    break

        # final_graph_adj stores the weights of each edge in the blocking flow graph
        # final_graph contains the blocking flow graph in reqd. format
        # process the final graph to required format
        for i in range(vert):
            for j in range(len(graph[i])):
                temp1, temp2 = graph[i][j]
                final_graph[i].append((temp1, final_graph_adj[i, temp1]))

        return final_graph


def test():
    # python block_flow < inp_file
    test_graph, edges, vertices = input_graph()
    v = len(test_graph)

    display_graph(test_graph)

    # assuming 0 is source and v-1 is sink
    block_graph = blocking_flow(test_graph, vertices, edges, 0, v - 1)

    display_graph(block_graph, "Block_flow")

# test()
