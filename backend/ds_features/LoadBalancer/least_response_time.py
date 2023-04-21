from typing import List, Tuple

import sys
sys.path.append('../../..')
from backend.app.main_server import get_socket

socket = get_socket()

class Server:
    def __init__(self, name: str, response_time: int, capacity: int):
        self.name = name
        self.response_time = response_time
        self.capacity = capacity
        self.current_connections = 0
    
    def __str__(self):
        return f"Server {self.name}"
    
    def get_response_time(self):
        return self.response_time
    
    def get_capacity(self):
        return self.capacity
    
    def get_current_connections(self):
        return self.current_connections
    
    def increment_current_connections(self):
        self.current_connections += 1
    
    def decrement_current_connections(self):
        self.current_connections -= 1

class LeastResponseTimeBalancer:
    def __init__(self, servers: List[Server]):
        print("Init also ran")
        socket.send_string("Initializating LeastResponseTimeBalancer!")
        self.servers = servers
    
    def get_next_server(self) -> Tuple[Server, int]:
        selected_server = None
        min_response_time = float('inf')
        
        for server in self.servers:
            if server.get_capacity() > server.get_current_connections():
                response_time = server.get_response_time()
                if response_time < min_response_time:
                    min_response_time = response_time
                    selected_server = server
        
        if selected_server is None:
            return None
        
        selected_server.increment_current_connections()
        return selected_server, min_response_time
    
    def release_server(self, server: Server):
        server.decrement_current_connections()



# if __name__ == '__main__':
server1 = Server("Server 1", 10, 5)
server2 = Server("Server 2", 15, 5)
server3 = Server("Server 3", 20, 5)

list_of_servers = [
    server1,
    server2,
    server3,
]

balancer = LeastResponseTimeBalancer(list_of_servers)

for i in range(10):
    server, response_time = balancer.get_next_server()
    if server is not None:
        print(f"Request {i}: {server}, Response time: {response_time}")
        balancer.release_server(server)
    else:
        print(f"No server available for request {i}")
