import zmq
import random
import time

print("-------------SERVER STARTED-------------")

from server import Server

import sys
sys.path.append('../')
from ds_features.LoadBalancer.round_robin import RoundRobinLoadBalancer ## find a way to get this
from ds_features.Coordination.ClockSynchronization.berkeley import *

'''
    Centralized Message Queue for Monitoring a Distributed System.

    USAGE:
        socket.send_string(message)
'''

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:5678")
# message = input("Enter message to be sent: ")
# socket.send_string(message)


'''
    Round-Robin Load Balancer   
        # Currently, inheriting from Server class {should it inherit Server or not?}
            If it doesnt inherit, then every update to the number of servers, we need to update to RoundRobinLoadBalancer

'''
import collections

# class RoundRobinLoadBalancer(Server):
#     def __init__(self, servers):
#         super().__init__()
#         self.servers = collections.deque(servers)
#         self.num_servers = len(servers)
    
#     def add_server(self):
#         new_server = Server()
#         self.servers.append(new_server)
#         Server.counter += 1
#         self.num_servers += 1
#         self.display_servers()

#     def next_server(self):
#         self.servers.rotate(-1)

#         return self.servers[0]
    
#     def remove_server(self, server):
#         try:
#             self.servers.remove(server)
#             self.num_servers -= 1
#         except ValueError:
#             print(f"{server} not found in the workers list")
    
#     def display_servers(self):
#         for i in self.servers:
#             print(i)

'''
    Testing Load Balancer from main_server.py
'''

list_of_servers = []

def initial_servers(num=2):
    for _ in range(num):
        list_of_servers.append(Server())
        socket.send_string("server_add" + " "+ str(list_of_servers[-1])[1:-1])
initial_servers()

'''
    Demo of how load is getting distributed
'''
lb = RoundRobinLoadBalancer(list_of_servers)

'''
    Basic User class
'''
class User:
    def __init__(self, name):
        self.name = name
        self.server = None
    
    def assign_server(self, server):
        self.server = server

    def __repr__(self):
        print(f"User Name: {self.name} is assigned to Server: {self.server}")
        return f"User Name: {self.name} is assigned to Server: {self.server}"


users = []

def initial_users(num=4):
    names = ['USER0', 'USER1', 'USER2', 'USER3']
    for i in range(num):
        users.append(User(names[i]))
        socket.send_string("user_add" + " "+ users[-1].name)
initial_users()

for user in users:
    assign_to_this_server = lb.next_server()
    socket.send_string("edge"+ " " + user.name + "," + str(assign_to_this_server)[1:-1])
    user.assign_server(assign_to_this_server)



print("Server done")

# ------------------- CLOCK SYNCHRONIZATION ----------------------------------
print("Clock Synchronization started")

berkeley_servers = []
for i in list_of_servers:
    berkeley_servers.append(BerkeleyServer(i))

berkeley_clients = []
for i in users:
    # Find the server that the user is connected to
    server_of_i = i.server
    b_server = None
    index=0
    for ind, j in enumerate(berkeley_servers):
        if(j.server is server_of_i):
            b_server = j
            index = ind
            break

    berkeley_clients.append(BerkeleyClient(i, b_server))
    berkeley_servers[index].add_client(berkeley_clients[-1])


trial_server = berkeley_servers[0]
for trial_server in berkeley_servers:
    trial_server.synchronize_clocks(socket)
    print(f"Server time: {trial_server.get_time()}")

    for k in trial_server.clients:
        print(k.get_time())