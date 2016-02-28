from graph import display_graph,input_graph 
import numpy as np

def blocking_flow(graph , edges,vert, source, sink):


    # ====convert to sets and an adjacency matrix======
        
    # Convert to sets so that queries are faster
    graph_sets = [ set() for i in range(vert) ]

    for i in range(vert): 
        for j in range(len(graph[i])):
            temp1,temp2 = graph[i][j] 
            graph_sets[i].add(temp1)


    # Adjacency Matrix
    # A[i][j] stores weight of the vertex from i to j

    adj_matrix = np.zeros( (vert,vert) , dtype = np.int )
    
    for i in range(vert):
        for j in range(len(graph[i])):
            print temp1,temp2
            temp1,temp2 = graph[i][j] 
            adj_matrix[i , temp1] = temp2

#     print graph_sets
#     print adj_matrix

    #================================================

    # loop |E| times on modified DFS

    # For each DFS
    
    # Augment path
    # Make deletion of vertex
    
          
#============Function end===========================



#===== Program testing ===================

# give input_graph as file input
# Display both full capacity graph and blocking flow graph
test_graph,edges,vertices = input_graph()
v = len(test_graph)

display_graph(test_graph)
#assuming 0 is source and v-1 is sink
blocking_flow(test_graph, edges,vertices, 0 ,v-1)

# display_graph(test_graph,"Block_flow")


