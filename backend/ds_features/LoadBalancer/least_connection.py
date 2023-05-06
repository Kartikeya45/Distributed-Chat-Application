from typing import List

class LCServer:
    def __init__(self, name: str, server, initial_connections: int=0):
        self.server = server
        self.name = name
        self.active_connections = initial_connections
    
    def __str__(self):
        return self.name
    
    def get_active_connections(self):
        return self.active_connections

from server import Server

class LeastConnectionLoadBalancer:
    def __init__(self, servers: List[LCServer], socket):
        self.servers = servers
        self.socket = socket
    
    def get_least_connection_server(self) -> LCServer:
        least_conn_server = None
        for server in self.servers:
            if least_conn_server is None or server.get_active_connections() < least_conn_server.get_active_connections():
                least_conn_server = server
        return least_conn_server
    
    def add_active_connection(self, server: LCServer):
        server.active_connections += 1
    
    def remove_active_connection(self, server: LCServer):
        server.active_connections -= 1

if(__name__=="__main__"):
    '''
        Creating 3 servers from the "Server" class
    '''
    list_of_servers = []
    for i in range(3):
        list_of_servers.append(LCServer(f'server{i}', i))

    '''
        Demo of how load is getting distributed
    '''
    lb = LeastConnectionLoadBalancer(list_of_servers)
    for i in range(10):
        assign_to_this_server = lb.get_least_connection_server()
        assign_to_this_server.active_connections +=1
        print("Name of server: ", assign_to_this_server)
