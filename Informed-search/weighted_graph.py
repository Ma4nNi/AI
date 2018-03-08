from weighted_edge import *

class WeightedGraph:
    def __init__(self, root):
        '''
        root should be a weighted_node 
        '''
        self.root = root

    def addNeighbors(self,node, *weighted_edges):
        '''
        weigted_edges is any amount of WeightedEdge objects. This method adds the edges from node to all the destination origin pointing to that original node.
        and the edges to the original node.
        '''
        for edge in weighted_edges:
            node.edges.append(edge)
            edge.destination.edges.append(WeightedEdge(node,edge.weight))
            
    def greedySearch(self, verbose=False):
        visited_node_list = []
        shortes_path  = []
        current_node = self.root
        shortes_path.append(current_node.name)
        visited_node_list.append(current_node.name)
        while(current_node.data > 0 and len(current_node.edges)>0): #current_node.data> 0 is if we arent on the goal city
            lowest_cost_node = None
            visited_node_amount = 0
            if(verbose):
                print("Checking ", current_node.name, current_node.data)
                print("visited nodes:", visited_node_list)
            for edge in current_node.edges:
                if(verbose):
                    print("\tEdge: ",edge.destination.name)
                if(edge.destination.name in visited_node_list):#node exists
                    if(verbose):
                        print("\twas already visited")
                    visited_node_amount+=1
                    continue
                if(lowest_cost_node is None): #first node visited
                    if(verbose):
                        print("\twas the first node visited")
                    lowest_cost_node = edge.destination
                elif(lowest_cost_node.data > edge.destination.data):
                    if(verbose):
                        print("\t had a better cost than", lowest_cost_node.name)
                    lowest_cost_node = edge.destination
                visited_node_list.append(edge.destination.name)
            if(visited_node_amount == len(current_node.edges)):
                return shortes_path
            shortes_path.append(lowest_cost_node.name)
            current_node = lowest_cost_node
        return shortes_path

    def aStarSearch(self, verbose=False):
        visited_node_list = []
        shortes_path  = []
        current_node = self.root
        shortes_path.append(current_node.name)
        visited_node_list.append(current_node.name)
        while(current_node.data > 0 and len(current_node.edges)>0): #current_node.data> 0 is if we arent on the goal city
            lowest_cost_node = None
            visited_node_amount = 0
            if(verbose):
                print("Checking ", current_node.name, current_node.data)
                print("visited nodes:", visited_node_list)
            routeCost=0
            for edge in current_node.edges:
                if(verbose):
                    print("\tEdge: ",edge.destination.name)
                if(edge.destination.name in visited_node_list):#node exists
                    if(verbose):
                        print("\twas already visited")
                    visited_node_amount+=1
                    continue
                if(lowest_cost_node is None): #first node visited
                    if(verbose):
                        print("\twas the first node visited")
                    lowest_cost_node = edge.destination
                    routeCost = edge.weight
                elif(lowest_cost_node.data+routeCost > edge.destination.data+edge.weight):
                    if(verbose):
                        print("\t had a better cost than", lowest_cost_node.name)
                    lowest_cost_node = edge.destination
                visited_node_list.append(edge.destination.name)
            if(visited_node_amount == len(current_node.edges)):
                return shortes_path
            shortes_path.append(lowest_cost_node.name)
            current_node = lowest_cost_node
        return shortes_path
        
            
