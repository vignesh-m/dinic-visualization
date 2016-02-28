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

    # stores the augmenting path

    # loop |E| times on modified DFS
    for i in range(edges):

        path = []
        path.append(source)
        
        min_wt = float('inf')

        while True:

            # if path is empty then exit and terminate the bfs
            # since no s-t path is there
            if len(path)==0:
                break

            # get last vertex in s-t path
            curr = path[-1]

            # Check if any vertices are adjacent to curr
            # If yes then no s-t path exists
            # Mark all incident edges for deletion next time they are seen
            # Then adjacency matrix entries are all set to -1 for that vertex
           
            # Change to true if you find a child
            child_exists = False


            while ((not child_exists) and len(graph_sets[curr])!=0):
                #get random adjacent edge to current edge
                child = graph_sets[curr].pop()

                # if valid child found
                if adj_matrix[curr,child]!=0:
                    child_exists =True    
                    graph_sets[curr].add(child)


            # if no child node found, then set curr for deletion
            if len(graph_sets[curr])==0:
                adj_matrix[:,curr] = 0 
                path.pop()
                continue

            #else path augmentation:

            if min_wt >  adj_matrix[curr,child]:
                min_wt = adj_matrix[curr,child] 


            if child == sink:
                
                while( len(path) > 1 ):
                    temp1 = path.pop()
                    temp2 = path[-1]
                    adj_matrix[temp2,temp1] =  adj_matrix[temp2,temp1] - min_wt

                break
                




    
          
#============Function end===========================



#===== Program testing ===================

# give input_graph as file input
# Display both full capacity graph and blocking flow graph
test_graph,edges,vertices = input_graph()
v = len(test_graph)

display_graph(test_graph)
#assuming 0 is source and v-1 is sink
blocking_flow(test_graph, edges,vertices, 0 ,v-1)

display_graph(test_graph,"Block_flow")


