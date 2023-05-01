import zmq
import random
import time

print("-------------SERVER STARTED------------=")

from server import Server

import sys
sys.path.append('../')
# from ds_features.LoadBalancer.round_robin import RoundRobinLoadBalancer ## find a way to get this
from ds_features.LoadBalancer.least_connection import LCServer, LeastConnectionLoadBalancer


# from ds_features.Coordination.ClockSynchronization.berkeley import *
# from ds_features.Coordination.ClockSynchronization.christian import *
# from ds_features.Coordination.ClockSynchronization.ntp import *

'''
    Centralized Message Queue for Monitoring a Distributed System.

    USAGE:
        socket.send_string(message)
'''

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:9876")

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
        return self.name
        print(f"User Name: {self.name} is assigned to Server: {self.server}")
        return f"User Name: {self.name} is assigned to Server: {self.server}"


users = []

def initial_users(num=4):
    names = ['USER0', 'USER1', 'USER2', 'USER3']
    for i in range(num):
        users.append(User(names[i]))
        socket.send_string("user_add" + " "+ users[-1].name)
initial_users()

def rrb():
    lb = RoundRobinLoadBalancer(list_of_servers)
    for user in users:
        assign_to_this_server = lb.next_server()
        socket.send_string("edge"+ " " + user.name + "," + str(assign_to_this_server)[1:-1])
        user.assign_server(assign_to_this_server)

def least_connections():
    '''
        Creating 3 servers from the "Server" class
    '''
    list_of_LC_servers = []
    for i, j in enumerate(list_of_servers):
        list_of_LC_servers.append(LCServer(f'{j.server_name}', i))

    '''
        Demo of how load is getting distributed
    '''
    lb = LeastConnectionLoadBalancer(list_of_servers)
    for user in users:
        assign_to_this_server = lb.get_least_connection_server()
        assign_to_this_server.active_connections +=1
        # socket.send_string("edge"+ " " + user.name + "," + str(assign_to_this_server)[1:-1])
        print("Name of server: ", assign_to_this_server)

least_connections()