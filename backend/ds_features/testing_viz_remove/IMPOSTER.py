import random
import matplotlib.image as mpimg
from networkx.drawing.nx_pydot import write_dot
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import networkx as nx

fig, ax = plt.subplots()

G = nx.MultiDiGraph()
pos = nx.spring_layout(G)

G.add_nodes_from(['Server1', 'Server2'])
G.add_nodes_from(['Client1', 'Client2', 'Client3', 'Client4'])
pos.update({'Server1': (0, 0), 'Server2': (0, 2), 'Client1': (2, 0), 'Client2': (0, -2), 'Client3': (-2, 0), 'Client4': (0, 4)})

nx.draw(G, pos, with_labels=True)

def update(i):
    pass

from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, update, frames=range(1), repeat=False, interval=100)

G.add_node('Client5')
pos.update({'Client5': (-2, 2)})

plt.show()
