import random
import matplotlib.image as mpimg
from networkx.drawing.nx_pydot import write_dot
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import networkx as nx

fig, ax = plt.subplots()

G = nx.MultiDiGraph()
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)

def update(i, add_node=False):
    if add_node:
        G.add_node(i)  # dynamically add new node
    pos = nx.spring_layout(G)  # update node positions
    ax.clear()  # clear the plot
    nx.draw(G, pos, with_labels=True, ax=ax)  # redraw the graph

def should_add_node():
    return True
    # your logic to check if a node should be added
    pass

import random

def get_new_node():
    # your logic to get the data of the new node
    return random.randint(1, 100)

def check_add_node(i):
    if should_add_node():
        anim.event_source.stop()  # stop animation
        new_node = get_new_node()  # get the new node data
        update(i, add_node=True)  # add the new node
        anim.event_source.start()  # restart animation

anim = FuncAnimation(fig, update, frames=range(100), repeat=True, interval=100)


for i in range(10):
    check_add_node(i)

plt.show()
