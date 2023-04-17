from typing import List


class Server:
    def __init__(self, server_id: int):
        self.server_id = server_id
        self.is_leader = False
        self.is_active = True

    def __repr__(self):
        return f"Server(server_id={self.server_id}, is_leader={self.is_leader}, is_active={self.is_active})"

    def deactivate(self):
        self.is_active = False
        self.is_leader = False
    
    def send_election_message(self, servers: List["Server"]):

        higher_servers = [s for s in servers if s.server_id > self.server_id and s.is_active]
        for server in higher_servers:
            print(f"Server {self.server_id} sends ELECTION message to Server {server.server_id}")
            server.receive_election_message(self)

        if not higher_servers:
            self.declare_leader(servers)

    def receive_election_message(self, sender: "Server"):
        print(f"Server {self.server_id} receives ELECTION message from Server {sender.server_id}")
        sender.send_ok_message()


        if sender.server_id > self.server_id:
            self.send_election_message([s for s in servers if s.is_active])

    def send_ok_message(self):
        print(f"Server {self.server_id} sends OK message")

    def declare_leader(self, servers: List["Server"]):
        print(f"Server {self.server_id} declares self as LEADER")
        self.is_leader = True
        for server in servers:
            if server.server_id != self.server_id and server.is_active:
                server.receive_coordinator_message(self)

    def receive_coordinator_message(self, sender: "Server"):
        # Set sender as leader and mark self as inactive
        print(f"Server {self.server_id} receives COORDINATOR message from Server {sender.server_id}")


# Create servers
server1 = Server(1)
server2 = Server(2)
server3 = Server(3)
server4 = Server(4)
servers = [server1, server2, server3, server4]

'''
    Call send_election_message from the highest ranked server
'''

server3.deactivate()
server4.send_election_message(servers)


server4.deactivate()
server2.deactivate()
server3.deactivate()
server1.send_election_message(servers)

print()
for i in servers:
    print(i)
