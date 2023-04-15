import random
import hashlib

class Server:
    def __init__(self, name: str, initial_connections: int=0):
        self.name = name
        self.active_connections = initial_connections
    
    def __str__(self):
        return self.name
    
    def get_active_connections(self):
        return self.active_connections

class IPHashLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
    
    def get_server(self, client_ip):
        '''
            Input: client_ip :- IPv4 Address of the client trying to connect to the server
            Output: Server URL, can be changed to Server object according to our convenience
                               Anyways, inside Server object we can store the URL of the server ## CHANGE OUTPUT
        '''
        hash = hashlib.md5(client_ip.encode('utf-8')).hexdigest()
        
        # Map the hash value to a server index
        server_index = int(hash, 16) % len(self.servers)
        
        return self.servers[server_index]


# servers = ["http://server1.com", "http://server2.com", "http://server3.com"]
# lb = IPHashLoadBalancer(servers)

# print(lb.get_server("192.168.1.100"))
# print(lb.get_server("192.168.1.101"))
# print(lb.get_server("192.168.2.100"))


'''
    Creating 3 servers from the "Server" class
'''
list_of_servers = []
for i in range(3):
    list_of_servers.append(Server(f'server{i}', i))




'''
    Demo of how load is getting distributed
'''

# List of 10 random IP addresses
ip_addresses = []
for i in range(10):
    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
    ip_addresses.append(ip)

print("IP Addresses: ", ip_addresses)

lb = IPHashLoadBalancer(list_of_servers)
for i in range(10):
    assign_to_this_server = lb.get_server(ip_addresses[i])
    assign_to_this_server.active_connections +=1
    print("Name of server: ", assign_to_this_server)
