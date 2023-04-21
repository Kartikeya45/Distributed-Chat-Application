from typing import List

# import os

# current_dir = os.path.abspath(os.getcwd())
# parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

# os.chdir(parent_dir)

import sys
sys.path.append('../../..')

from backend.app.server_ds_features_import_testing import *

from backend.app.main_server import socket

class RoundRobinLoadBalancer:
    '''
        When the Distributed System is initiated or when we want to change the "LoadBalancerAlgorithm" used to "RoundRobinLoadBalancer", 
            create an instance of this class.

        When a new request comes, (the request which we want to "load balance"), 
            call the next_server function to assign the request to a particular server

        
    '''
    def __init__(self, servers: List[Server]):
        self.servers = servers                 # Need to handle server crashing here
        self.current = 0                       # When a server crashes, indexing can get messed up, NEED TO HANDLE IT
        
    def next_server(self) -> Server:
        if self.current == len(self.servers):  
            self.current = 0
        server = self.servers[self.current]
        self.current += 1
        return server


'''
    Creating 3 servers from the "Server" class
'''
list_of_servers = []
for _ in range(3):
    list_of_servers.append(Server())

'''
    Demo of how load is getting distributed
'''
lb = RoundRobinLoadBalancer(list_of_servers)
for i in range(10):
    assign_to_this_server = lb.next_server()
    print("Name of server: ", assign_to_this_server.server_name)
