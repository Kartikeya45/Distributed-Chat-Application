import time

from server import Server

# inherit Server maybe
class BerkeleyServer:
    def __init__(self, server):
        print("\nBerkeley server\n")
        self.server = server
        self.clients = []

    def __repr__(self):
        return f"BerkeleyServer - {self.server}"

    def add_client(self, client):
        print("THis hsas to change", self.clients)
        self.clients.append(client)
        print("THis hsas to change", self.clients)

    def remove_client(self, client):
        self.clients.remove(client)

    def synchronize_clocks(self, socket):
        # Step 1: Get the current time from all clients
        client_times = []
        print(self.clients)
        print()
        for client in self.clients:
            # handle the name of the server properly, and send properly in the below line
            socket.send_string("highlight_edge_direction " + str(client) + "," + str(self.server.server_name))
            client_times.append(client.get_time())
        
        print(client_times, "waht")

        # Step 2: Calculate the average time difference
        time_diff = 0
        for client_time in client_times:
            time_diff += client_time - self.get_time()
        
        avg_time_diff = time_diff / len(client_times)

        # Step 3: Adjust the server's clock
        self.adjust_time(avg_time_diff)

        # Step 4: Send the new time to all clients
        for client in self.clients:
            socket.send_string("highlight_edge_direction_green " + str(client) + "," + str(self.server.server_name))
            client.adjust_time(avg_time_diff)

    def get_time(self):
        return time.time()

    def adjust_time(self, time_diff):
        current_time = self.get_time()
        new_time = current_time + time_diff
        # Set the new time as the server's time
        # You can use any method to set the time, such as adjusting the system clock
        pass


class BerkeleyClient:
    def __init__(self, client, server):
        print("\nBerkeley client\n")
        self.cumulative_time_error = 0
        self.server = server
        self.client = client

    def get_time(self):
        return self.server.get_time() + self.cumulative_time_error

    def adjust_time(self, time_diff):
        current_time = self.get_time()
        new_time = current_time + time_diff
        self.cumulative_time_error += time_diff
        # Set the new time as the client's time
        # You can use any method to set the time, such as adjusting the system clock
        pass

    def __repr__(self):
        return self.client.name

if(__name__=="__main__"):
    # Example usage
    server = Server()
    client1 = BerkeleyClient(server)
    client2 = BerkeleyClient(server)
    client3 = BerkeleyClient(server)

    server.add_client(client1)
    server.add_client(client2)
    server.add_client(client3)

    # Sync the clocks a few times
    for i in range(3):
        server.synchronize_clocks()
        print(f"Server time: {server.get_time()}")
        print(f"Client 1 time: {client1.get_time()}")
        print(f"Client 2 time: {client2.get_time()}")
        print(f"Client 3 time: {client3.get_time()}")
