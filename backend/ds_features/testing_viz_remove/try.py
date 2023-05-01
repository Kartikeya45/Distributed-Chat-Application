import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4)])

# Set edge color attribute
colors = {edge: 'red' for edge in G.edges()}
print(G.edges())
nx.set_edge_attributes(G, colors, 'color')

# Draw the graph with edge colors
pos = nx.spring_layout(G)
nx.draw(G, pos=pos, with_labels=True, edge_color=[G.edges[e]['color'] for e in G.edges()], node_color='lightblue')
plt.show()
