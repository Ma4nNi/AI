class WeightedEdge:
    '''
    This edge is for edges with direction
    '''
    def __init__(self, destination, weight):
        '''
        destination and origin are weighted_node objects. weight is the cost between them
        '''
        self.destination= destination
        self.weight = weight