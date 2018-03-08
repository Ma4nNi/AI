import copy
class FlappyNode:
    def __init__(self,name, neighbors, game_state):
        self.neighbors=neighbors
        self.node_name=name
        self.data=game_state
 

horizontal_frame_displacement = 4 #amount of horizontal pixels moved per frame
jumping_power=8 #the speed obtained when jumping
def depth_first_search(graph, node, visited_nodes):
    if node not in visited_nodes:
        visited_nodes.append(node)
        for neighbor in graph[node].neighbors:
            try:
                depth_first_search(graph,neighbor, visited_nodes)
            except:
                print("No node found with identifier ",neighbor)
    return visited_nodes

def create_test_graph():
    flappy_graph = {
        'R' : FlappyNode('R',['a1','a6'],[]),
        'a1': FlappyNode('a1',['R'],[]),
        'a2': FlappyNode('a2',['a3','a4','a5','a6'],[]),
        'a6': FlappyNode('a6',['R','a2','a7'],[]),
        'a3': FlappyNode('a3',['a2'],[]),
        'a4': FlappyNode('a4',['a6','a1'],[]),
        'a5': FlappyNode('a5',['a3','R'],[])
    }
    return flappy_graph 

def create_next_nodes(graph,current_node,steps, frame):
    if(frame>15):
        return
    nodes_name = current_node.node_name+str(frame)
    idle_game_state = copy.deepcopy(current_node.data)
    jumping_game_state = copy.deepcopy(current_node.data)
    idle_game_state['player_vel']+=1
    idle_game_state['next_pipe_dist_to_player']-=horizontal_frame_displacement
    jumping_game_state['player_vel']= -1*jumping_power
    jumping_game_state['next_pipe_dist_to_player']-=horizontal_frame_displacement
    node_idle = FlappyNode(nodes_name+'I',[],idle_game_state)
    node_jump = FlappyNode(nodes_name+'J',[],idle_game_state)
    current_node.neighbors.append(node_idle.node_name)
    current_node.neighbors.append(node_jump.node_name)
    graph[node_idle.node_name] = node_idle
    graph[node_jump.node_name] = node_jump
    create_next_nodes(graph,node_idle,steps,frame+1)
    create_next_nodes(graph,node_jump,steps,frame+1)

def generate_flappy_graph(game_state):
    flappy_graph={
        'R' : FlappyNode('R',[],game_state)
    }
    #distance_to_next_pipe = game_state['next_pipe_dist_to_player']
    current_frame = 1
    create_next_nodes(flappy_graph, flappy_graph['R'],[],current_frame)
    print("This is the current GRAPH:")
    for key, value in flappy_graph.items() :
        print (key, value.neighbors)
    return flappy_graph
        

def get_steps_by_frame(original_state):
    flappy_graph = create_test_graph()
    flappy_graph2 = generate_flappy_graph(original_state)
    visited_nodes = depth_first_search(flappy_graph,'R', [])
    print("visited_nodes order: " , visited_nodes)
    return visited_nodes
