from  weighted_edge import * 
from weighted_graph import *
from weighted_node import *


#Here are all the basic nodes mentioned in the book Artificial intelligence a modern approach page-93
#the goal node will be bucharest which is why it has 0 as its data
#All the other nodes have data indicatig its euclidean distance to bucharest
arad = WeightedNode("Arad",366)
bucharest = WeightedNode("bucharest",0)
craiova = WeightedNode("craiova",160)
drobeta = WeightedNode("drobeta",242)
eforie = WeightedNode("eforie",161)
fagaras = WeightedNode("fagaras",176)
giurgiu = WeightedNode("giurgiu",77)
hirsova = WeightedNode("hirsova",151)
iasi  = WeightedNode("iasi",226)
lugoj = WeightedNode("lugoj",244)
mehadia = WeightedNode("mehadia",241)
neamt = WeightedNode("neamt",234)
oradea = WeightedNode("oradea",380)
pitesti = WeightedNode("pitesti",100)
rimnicuVilcea = WeightedNode("rimnicuVilcea",193)
sibiu = WeightedNode("sibiu",253)
timisoara = WeightedNode("timisoara",329)
urziceni = WeightedNode("urziceni",80)
vaslui = WeightedNode("vaslui",199)
zerind = WeightedNode("zerind",374)

#here we set the root node which can be any node but in the book it's arad
graph = WeightedGraph(arad)

#HERE WE SET ALL THE NEIGHBORS FOR EACH CITY BASED ON 
graph.addNeighbors(arad, WeightedEdge(zerind,75), WeightedEdge(sibiu,140), WeightedEdge(timisoara,118))
graph.addNeighbors(zerind, WeightedEdge(oradea,20))
graph.addNeighbors(oradea, WeightedEdge(sibiu,151))
graph.addNeighbors(sibiu,WeightedEdge(fagaras,99), WeightedEdge(rimnicuVilcea,80))
graph.addNeighbors(fagaras, WeightedEdge(bucharest,211))
graph.addNeighbors(rimnicuVilcea, WeightedEdge(pitesti,97), WeightedEdge(craiova,146))
graph.addNeighbors(pitesti, WeightedEdge(bucharest,101))
graph.addNeighbors(timisoara, WeightedEdge(lugoj,111))
graph.addNeighbors(lugoj,WeightedEdge(mehadia,70))
graph.addNeighbors(mehadia, WeightedEdge(drobeta,75))
graph.addNeighbors(drobeta, WeightedEdge(craiova,120))
graph.root = zerind 


print("Greedy search: ",graph.greedySearch())
print("AStar search: ", graph.aStarSearch())