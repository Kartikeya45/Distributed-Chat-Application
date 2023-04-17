from typing import List


class Server:
    def __init__(self, server_id: int, successor: "Server"):
        self.server_id = server_id
        self.successor = successor
        self.is_leader = False
        self.is_active = True

    def __repr__(self):
        return f"Server(server_id={self.server_id}, is_leader={self.is_leader}, is_active={self.is_active})"

    def send_election_message(self):
        print(f"Server {self.server_id} sends ELECTION message to Server {self.successor.server_id}")
        self.successor.receive_election_message(self.server_id, [self.server_id])

    def receive_election_message(self, origin_id: int, message_list: List[int]):        
        if self.server_id not in message_list:
            message_list.append(self.server_id)
            print(f"Server {self.server_id} receives ELECTION message from Server {origin_id} and message_list is {message_list}")
            print()
            self.successor.receive_election_message(self.server_id, message_list)
        else:
            print("REPETITION")
            print(f"Server {max(message_list)} is elected as COORDINATOR with members: {message_list}")
            self.successor.leadership_acceptance(max(message_list), message_list)
            

    def leadership_acceptance(self, leader_id, message_list):
        if(self.server_id == leader_id):
            self.is_leader = True
            print(f"Server {self.server_id} sends COORDINATOR message to members: {message_list}")
            self.send_coordinator_message(message_list)
        else:
            self.successor.leadership_acceptance(max(message_list), message_list)


    def send_coordinator_message(self, message_list: List[int]):
        print("Inside SEND COORDINATOR MESSAGE", message_list)
        for server_id in message_list:
            if(server_id != self.server_id):
                self.get_server_by_id(server_id).receive_coordinator_message()

    def receive_coordinator_message(self):
        # Mark self as inactive if not coordinator
        if not self.is_leader:
            print(f"Server {self.server_id} receives COORDINATOR message")

    def get_server_by_id(self, server_id: int) -> "Server":
        # Get server by server_id
        if self.server_id == server_id:
            return self
        else:
            return self.successor.get_server_by_id(server_id)


# Create servers
server1 = Server(1, None)
server2 = Server(2, server1)
server3 = Server(3, server2)
server4 = Server(4, server3)
server1.successor = server4
servers = [server1, server2, server3]


server2.send_election_message()

# Print final state of servers
print(servers)
