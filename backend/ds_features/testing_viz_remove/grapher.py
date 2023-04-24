import sys
import message_handler

import random
import matplotlib.image as mpimg
from networkx.drawing.nx_pydot import write_dot
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import networkx as nx
import time

fig, ax = plt.subplots()
G = nx.DiGraph()

global counter
counter = 0
start = time.time()

all_servers = []
all_users = []

def process_command(G, command, data, c):
    if(command=="server_add"):
        G.add_node("S"+str(len(all_servers)),node_label=data)
        all_servers.append(data)
    elif(command=="user_add"):
        G.add_node("U"+str(len(all_users)), node_label=data)
        all_users.append(data)
    elif(command=="edge"):
        print(all_servers)
        print(all_users)
        print()
        first, second = data.split(',')
        use_label = f"{first} -> {second}"
        first = "U" + str(all_users.index(first))
        second = "S" + str(all_servers.index(second))

        G.add_edge(first, second, label=use_label)

def update(i):
    time.sleep(2) # to visibly see the updates
    global counter

    command, data = message_handler.get_update()
    print(command, data, time.time()-start)

    process_command(G, command, data, counter)
    counter += 1

    user_pos = {node: (-1, j) for j, node in enumerate(["U"+str(k) for k in range(len(all_users))])}
    server_pos = {node: (1, j) for j, node in enumerate(["S"+str(k) for k in range(len(all_servers))])}
    pos = {**user_pos, **server_pos}

    ax.clear()
    nx.draw(G, pos=pos, with_labels=True, ax=ax)

anim = FuncAnimation(fig, update, frames=range(10), repeat=False, interval=100)

counter +=1 ## This part happens only once, If we want to update more, then put it inside update()
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()


## Make it such that message_handler continuously gives empty strings so that matplotlib doesnt hang
    ## and immediately return