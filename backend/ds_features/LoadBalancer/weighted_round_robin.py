from typing import List, Tuple

class Server:
    def __init__(self, name: str, weight: int):
        self.name = name
        self.weight = weight
        self.current_weight = 0
    
    def __str__(self):
        return self.name
    
    def increment_weight(self, inc: int):
        self.current_weight += inc
    
    def get_weight(self):
        return self.weight
    
    def get_current_weight(self):
        return self.current_weight

class WeightedRoundRobin:
    def __init__(self, servers: List[Server]):
        self.servers = servers
    
    def get_next_server(self) -> Tuple[Server, int]:
        max_weight = 0
        selected_server = None
        
        for server in self.servers:
            server.increment_weight(server.get_weight())
            current_weight = server.get_current_weight()
            
            if current_weight > max_weight:
                max_weight = current_weight
                selected_server = server
        
        selected_server.increment_weight(-max_weight)
        print()
        for k in self.servers:
            print(k, k.get_current_weight(), k.get_weight())
        return selected_server, max_weight
    
'''
    ({Sum of the weights} divided by {GCD of all weights}) is the minimum time for attaining full assignment

    This method is has no flaws caused by randomness.
        The first idea that comes to mind when we want to do proportional assignment is giving each of the servers different probabilities of getting assigned.
        But it may so happen that, by chance, a particular server gets overloaded due to randomness. This is because the computers generate pseudo random numbers.
    
    ChatGPT:
        Yes, that is correct. Proportional assignment cannot be reliably achieved using randomness alone. Randomness can lead to certain servers being overloaded due to chance, and this can result in suboptimal load balancing. Instead, more deterministic algorithms like weighted round-robin can be used to achieve proportional assignment.
'''
servers = [
    Server("Server A", 4),
    Server("Server B", 2),
    Server("Server C", 1),
]

# servers = [
#     Server("Server A", 32),
#     Server("Server B", 16),
#     Server("Server C", 8),
# ]

lb = WeightedRoundRobin(servers)


for i in range(7):
    server, weight = lb.get_next_server()
    print(f"Request {i+1} is handled by {server}, weight = {weight}")
