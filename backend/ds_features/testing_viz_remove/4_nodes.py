import networkx as nx
import matplotlib.pyplot as plt

# create a new directed graph
G = nx.DiGraph()

# add two server nodes in the center
G.add_node('Server 1', pos=(0,0))
G.add_node('Server 2', pos=(0,1))

# add four client nodes outside the center
G.add_node('Client 1', pos=(-1,2))
G.add_node('Client 2', pos=(1,2))
G.add_node('Client 3', pos=(2,-1))
G.add_node('Client 4', pos=(-2,-1))

# add edges between the clients and the servers
G.add_edge('Client 1', 'Server 1')
G.add_edge('Client 2', 'Server 1')
G.add_edge('Client 3', 'Server 2')
G.add_edge('Client 4', 'Server 2')

# get the positions of all nodes
pos = nx.get_node_attributes(G, 'pos')

# draw the graph with labels
nx.draw(G, pos, with_labels=True)

manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()


