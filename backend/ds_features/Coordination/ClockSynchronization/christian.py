import time
from server import Server
class CristianServer:
    def __init__(self, server):
        self.server = server
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def get_time(self):
        return time.time()

class CristianClient:
    def __init__(self, client, server, base_server):
        self.client = client
        self.server = server
        self.base_server = base_server
        self.time_delta = 0

    def synchronize_clock(self, socket):
        # Step 1: Send a request to the server for the current time
        socket.send_string("highlight_edge_direction " + str(self) + "," + str(self.base_server.server_name))
        server_time = self.server.get_time()
        socket.send_string("highlight_edge_direction_green " + str(self) + "," + str(self.base_server.server_name))

        # Step 2: Calculate the time it takes for the request to travel to the server and back
        time_diff = (self.get_time() - server_time) / 2

        self.time_delta = (server_time - time_diff) - self.get_time()

        # Step 3: Adjust the client's clock
        return server_time - time_diff

    def __repr__(self):
        return self.client.name
    
    def get_time(self):
        return time.time() + self.time_delta

if __name__ == "__main__":
    # Example usage
    server = CristianServer()
    client1 = CristianClient("USER0", server)
    client2 = CristianClient("USER1", server)
    client3 = CristianClient("USER2", server)

    server.add_client(client1)
    server.add_client(client2)
    server.add_client(client3)

    clients = [
        client1,
        client2,
        client3,
    ]
    # Sync the clocks a few times
    # for i in range(3):
    #     print(f"Server time: {server.get_time()}")
    #     print(f"Client 1 time: {client1.get_time()}")
    #     print(f"Client 2 time: {client2.get_time()}")
    #     print(f"Client 3 time: {client3.get_time()}")

    for client in clients:
        print(client.synchronize_clock())