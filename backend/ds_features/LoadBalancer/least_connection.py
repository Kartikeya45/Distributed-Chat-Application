from typing import List

class Server:
    def __init__(self, name: str, initial_connections: int=0):
        self.name = name
        self.active_connections = initial_connections
    
    def __str__(self):
        return self.name
    
    def get_active_connections(self):
        return self.active_connections

class LeastConnectionLoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers
    
    def get_least_connection_server(self) -> Server:
        least_conn_server = None
        for server in self.servers:
            if least_conn_server is None or server.get_active_connections() < least_conn_server.get_active_connections():
                least_conn_server = server
        return least_conn_server
    
    def add_active_connection(self, server: Server):
        server.active_connections += 1
    
    def remove_active_connection(self, server: Server):
        server.active_connections -= 1


'''
    Creating 3 servers from the "Server" class
'''
list_of_servers = []
for i in range(3):
    list_of_servers.append(Server(f'server{i}', i))

'''
    Demo of how load is getting distributed
'''
lb = LeastConnectionLoadBalancer(list_of_servers)
for i in range(10):
    assign_to_this_server = lb.get_least_connection_server()
    assign_to_this_server.active_connections +=1
    print("Name of server: ", assign_to_this_server)
