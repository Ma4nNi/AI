from FlappyNode import FlappyNode
import copy

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
    if(frame>5):
        return
    nodes_name = 'N'+str(frame)
    idle_game_state = copy.deepcopy(current_node.data)
    jumping_game_state = copy.deepcopy(current_node.data)
    idle_game_state['player_vel']+=1
    idle_game_state['dist_to_next_pipe']-=horizontal_frame_displacement
    jumping_game_state['player_vel']= -1*jumping_power
    node_idle = FlappyNode(nodes_name+'I',[],idle_game_state)
    node_jump = FlappyNode(nodes_name+'J',[],idle_game_state)

def generate_flappy_graph(game_state):
    flappy_graph={
        'R' : FlappyNode('R',[],game_state)
    }
    distance_to_next_pipe = game_state['dist_to_next_pipe']
    current_frame = 1
    create_next_nodes(flappy_graph, flappy_graph['R'],[],current_frame)
        


flappy_graph = create_test_graph()
visited_nodes = depth_first_search(flappy_graph,'R', [])
print("visited_nodes order: " , visited_nodes)
