from weighted_edge import *
class WeightedNode:
    def __init__(self,name,data,edges=None):
        '''
        name is the identifier of the node. data is the weight of the route to our destination. and edges 
        is a list of weighted_edges that represent the neighbors
        '''
        self.name = name
        self.data = data
        self.edges = edges
        if(edges is None):
            self.edges = []



