from typing import List, Tuple
import requests

class Server:
    def __init__(self, ip: str, port: int, weight: int):
        self.ip = ip
        self.port = port
        self.weight = weight
        self.current_weight = 0
        self.response_time = 0

    def __str__(self):
        return f"Server {self.ip}:{self.port} with weight {self.weight} and response time {self.response_time}"

    def get_weight(self):
        return self.weight

    def get_current_weight(self):
        return self.current_weight

    def get_ip_port(self):
        return (self.ip, self.port)

    def increment_weight(self, value):
        self.current_weight += value

    def set_response_time(self, response_time):
        self.response_time = response_time

class DynamicLoadBalancer:
    def __init__(self, servers: List[Server]):
        self.servers = servers

    def get_next_server(self) -> Tuple[Server, int]:
        total_weight = sum(server.get_weight() for server in self.servers)
        fastest_response_time = float("inf")
        selected_server = None

        for server in self.servers:
            try:
                response = requests.get(f'http://{server.ip}:{server.port}/', timeout=1)
                response_time = response.elapsed.total_seconds()
                server.set_response_time(response_time)
                if response_time < fastest_response_time:
                    fastest_response_time = response_time
                    selected_server = server
            except:
                pass

        if selected_server is None:
            raise Exception("No server available")

        selected_server.increment_weight(-total_weight)
        return selected_server, fastest_response_time

if __name__ == "__main__":
    servers = [
        Server("192.168.1.100", 8000, 1),
        Server("192.168.1.101", 8000, 2),
        Server("192.168.1.102", 8000, 3)
    ]

    lb = DynamicLoadBalancer(servers)

    for i in range(10):
        server, response_time = lb.get_next_server()
        print(f"Request {i} served by {server}. Response time: {response_time} seconds.")
