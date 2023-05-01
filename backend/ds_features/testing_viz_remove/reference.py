import random
import matplotlib.image as mpimg
from networkx.drawing.nx_pydot import write_dot
from matplotlib.animation import FuncAnimation
import time
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

fig, ax = plt.subplots()
number_of_nodes = 3
current_position = 0

def menu_for_auto_or_manual():
    global Q
    global number_of_nodes

    number_of_nodes = int(input("Enter the number of nodes: "))
    choice = int(input("Auto or Manual or Sparse? (1 / 2 / 3): "))
    if(choice==1):
        tpm = np.random.rand(number_of_nodes, number_of_nodes)  # generate a random matrix of shape (n, n)
        Q = tpm / tpm.sum(axis=1, keepdims=True)
    elif(choice==2):
        Q = []
        for i in range(number_of_nodes):
            Q.append(list(map(float, input(f"Enter the row elements for {i}th row: ").split())))
    elif(choice==3):
        Q = np.zeros((number_of_nodes, number_of_nodes))
        a,b,c = list(map(float, input().split()))
        a,b = int(a), int(b)
        while(True):
            Q[a][b] = c
            try:
                a,b,c = list(map(float, input().split()))
                a,b = int(a), int(b)
            except:
                break
    for i in range(number_of_nodes):
        if(abs(np.sum(Q[i]) - 1 )>0.01):
            print(np.sum(Q[i]))
            print("Sum of the rows of transition probability matrix must be 1 !")
            exit()
    print("\nTRANSITION PROBABILTIY MATRIX: \n", Q, "\n")

def choose_initial_position():
    pi = np.zeros(number_of_nodes)
    print("Enter the initial probability distribution:")
    choice = int(input("Auto or Manual or Sparse: (1 / 2 / 3)"))
    if(choice==1):
        for i in range(number_of_nodes):
            pi[i] = random.random()
        pi = pi / sum(pi)
    elif(choice==2):
        pi = list(map(float, input().split()))
    elif(choice==3):
        a, b = list(map(float, input().split()))
        a = int(a)
        while(a!=-1 and b!=-1):
            pi[a] = b
            a, b = list(map(float, input().split()))
            a = int(a)
    if(abs(sum(pi) - 1) > 0.01):
        print("Sum of initial probabilites must be 1!")
        exit()
    print("INITIAL PROBABILTIY DISTRIBUTION :", pi)

def update(i):
    global current_position
    # choose a random node to change color
    node_colors = ['red' for i in range(number_of_nodes)]
    current_position = random.choices(range(number_of_nodes), Q[current_position], k=1)[0]
    node_colors[current_position] = 'green'
    
    # redraw the graph with updated colors
    ax.clear()
    nx.set_node_attributes(G, dict(zip(range(number_of_nodes), node_colors)), 'color')
    nx.draw(G, pos, with_labels=True, node_color=node_colors)
    write_dot(G, 'mc.dot')

    from subprocess import check_call
    nfile = 'w.png' 
    check_call(['dot', '-Tpng', 'mc.dot', '-o', nfile])
    
    img = mpimg.imread(nfile)
    plt.imshow(img)

def adding_edges():
    states = range(number_of_nodes)

    labels={}
    edge_labels={}

    for i, origin_state in enumerate(states):
        for j, destination_state in enumerate(states):
            rate = Q[origin_state][destination_state]
            if rate > 0:
                G.add_edge(origin_state, destination_state, weight=rate, label="{:.02f}".format(rate))
                edge_labels[(origin_state, destination_state)] = label="{:.02f}".format(rate)


G = nx.MultiDiGraph()

menu_for_auto_or_manual()
choose_initial_position()
adding_edges()

pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True)

from matplotlib.animation import FuncAnimation
anim = FuncAnimation(fig, update, frames=range(1000), repeat=True, interval=100)

print(Q)
plt.show()
