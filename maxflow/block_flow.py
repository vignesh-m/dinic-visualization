from graph import display_graph,input_graph 
import numpy as np

# TODO check the complexity of below function

def blocking_flow(graph , edges,vert, source, sink):

    # store the resulting graph
    final_graph_adj = np.zeros( (vert,vert) , dtype = np.int )
    final_graph = [ [] for i in range(vert) ] 

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
            temp1,temp2 = graph[i][j] 
            adj_matrix[i , temp1] = temp2


    #================================================


    # loop |E| times on modified DFS
    for i in range(edges):

        #initialize path and minimum weight along s-t path
        path = []
        path.append(source)

        min_wt = float('inf')

        while True:

            # if path is empty then exit and terminate the bfs
            # since above means no s-t path is there
            if len(path)==0:
                break

            # get last vertex in s-t path
            curr = path[-1]

            # Check if any vertices are adjacent to curr
            # If no, then no s-t path exists
            # Mark all incident edges for deletion next time they are seen
            # Achieve above by setting all adjacency matrix entries -1 for that vertex
           
            # Change to true if you find a child
            child_exists = False

             
            
            # loop while child is not yet found, and there exists unvisited edge from "curr"
            while ((not child_exists) and len(graph_sets[curr])!=0):

                #get random adjacent edge to current edge
                child = graph_sets[curr].pop()

                # if valid child found
                if adj_matrix[curr,child]!=0:
                    child_exists =True    
                    # add back popped edge if it is a valid child
                    graph_sets[curr].add(child)


            # if no child node found, then set curr for deletion
            if len(graph_sets[curr])==0:
                # set for deletion in adj_matrix
                adj_matrix[:,curr] = 0 
                # remove vertex from path
                path.pop()
                continue


        # else path augmentation:
            # update path and min_wt in path
            path.append(child)

            if min_wt >  adj_matrix[curr,child]:
                min_wt = adj_matrix[curr,child] 


            # if s-t path is found
            if child == sink:
                
                # Decrement path weight by minimum weight along entire path

                while( len(path) > 1 ):
                    temp1 = path.pop()
                    temp2 = path[-1]
                    adj_matrix[temp2,temp1] =  adj_matrix[temp2,temp1] - min_wt
                    final_graph_adj[temp2,temp1] = final_graph_adj[temp2,temp1] + min_wt

                break
                

    # final_graph_adj stores the weights of each edge in the blocking flow graph
    # final_graph contains the blocking flow graph in reqd. format 
    #process the final graph to required format
    for i in range(vert):
        for j in range( len(graph[i])):
            temp1,temp2 = graph[i][j]
            final_graph[i].append( (temp1, final_graph_adj[i,temp1] ))

    return final_graph
          
#============Function end===========================



#===== Program testing ===================
# run: python block_flow < inp_file

# give input_graph as file input
test_graph,edges,vertices = input_graph()
v = len(test_graph)

display_graph(test_graph)

#assuming 0 is source and v-1 is sink
block_graph = blocking_flow(test_graph, edges,vertices, 0 ,v-1)

display_graph(block_graph,"Block_flow")


