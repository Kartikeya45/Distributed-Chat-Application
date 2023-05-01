import sys
import message_handler
from pprint import pprint
import random
import matplotlib.image as mpimg
from networkx.drawing.nx_pydot import write_dot
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import networkx as nx
import time

global edge_colors

print("------------- GRAPHER STARTED-------------")

fig, ax = plt.subplots()
G = nx.DiGraph()

global counter
counter = 0
start = time.time()

all_servers = []
all_users = []

def process_command(G, command, data, c):
    if(command=="server_add"):
        if(data=='NTP'):
            G.add_node(data, node_label=data)
        else:
            G.add_node("S"+str(len(all_servers)),node_label=data)
        all_servers.append(data)
    elif(command=="user_add"):
        G.add_node("U"+str(len(all_users)), node_label=data)
        all_users.append(data)
    elif(command=="edge"):
        first, second = data.split(',')
        use_label = f"{first} -> {second}"
        if(len(first)==2 and second=="NTP"):
            pass
        else:
            use_label = f"{first} -> {second}"
            first = "U" + str(all_users.index(first))
            second = "S" + str(all_servers.index(second))

        G.add_edge(first, second, label=use_label)
    elif(command=="highlight_edge_direction"):
        first, second = data.split(',')
        if(first=="NTP"):
            colors = [(second, first), 'red']
            return colors
        elif(second=="NTP"):
            colors = [(first, second), 'red']
            return colors
        first = first[0].upper() + first[-1]
        second = second[0].upper() + second[-1]
        colors = [(second, first), 'red']
        return colors
    elif(command=="highlight_edge_direction_green"):
        first, second = data.split(',')
        if(first=="NTP"):
            colors = [(second, first), 'orange']
            return colors
        elif(second=="NTP"):
            colors = [(first, second), 'orange']
            return colors
        first = first[0].upper() + first[-1]
        second = second[0].upper() + second[-1]
        colors = [(second, first), 'orange']
        return colors
    elif(command=="close_edge"):
        first, second = data.split(',')
        if(first=="NTP"):
            second, first = first, second
        G.remove_edge(first, second)
    elif(command=="sleep"):
        time.sleep(float(data))
        

def update(i):
    time.sleep(0.5) # to visibly see the updates
    global counter

    command, data = message_handler.get_update()
    print(command, data, time.time()-start)

    ret = process_command(G, command, data, counter)
    counter += 1

    user_pos = {node: (-1, j) for j, node in enumerate(["U"+str(k) for k in range(len(all_users))])}
    server_pos = {node: (1, j) for j, node in enumerate(["S"+str(k) for k in range(len(all_servers))])}
    ntp_pos = {}


    ntp_pos = {"NTP": (0,0)}
    
    pos = {**user_pos, **server_pos, **ntp_pos}

    ax.clear()
    colors = {edge: 'black' for edge in G.edges()}
    
    if(ret is not None):
        colors[ret[0]] = ret[1]
    pprint(colors)

    nx.set_edge_attributes(G, colors, 'color')
    nx.draw(G, pos=pos, with_labels=True, ax=ax, edge_color=[G.edges[e]['color'] for e in G.edges()])

anim = FuncAnimation(fig, update, frames=range(1000), repeat=False, interval=100)

counter +=1 ## This part happens only once, If we want to update more, then put it inside update()
manager = plt.get_current_fig_manager()
manager.full_screen_toggle()
plt.show()


## Make it such that message_handler continuously gives empty strings so that matplotlib doesnt hang
    ## and immediately return