from typing import List

from server import Server
import collections

'''
    Round-Robin Load Balancer   
        # Currently, inheriting from Server class {should it inherit Server or not?}
            If it doesnt inherit, then every update to the number of servers, we need to update to RoundRobinLoadBalancer

'''

class RoundRobinLoadBalancer(Server):
    '''
        When the Distributed System is initiated or when we want to change the "LoadBalancerAlgorithm" used to "RoundRobinLoadBalancer", 
            create an instance of this class.

        When a new request comes, (the request which we want to "load balance"), 
            call the next_server function to assign the request to a particular server
    '''
    def __init__(self, servers, port_numbers):
        print("Round robin just initialized from main_server")
        self.port_numbers = port_numbers
        self.servers = collections.deque(servers)
        self.num_servers = len(servers)
    
    def add_server(self):
        new_server = Server()
        self.servers.append(new_server)
        Server.counter += 1
        self.num_servers += 1
        self.display_servers()

    def next_server(self):
        self.servers.rotate(-1)

        return self.servers[0]
    
    def remove_server(self, server):
        try:
            self.servers.remove(server)
            self.num_servers -= 1
        except ValueError:
            print(f"{server} not found in the workers list")
    
    def display_servers(self):
        for i in self.servers:
            print(i)


if(__name__=='__main__'):
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

