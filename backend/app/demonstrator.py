import zmq
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://127.0.0.1:9876")

from server import Server
import host
servers, port_numbers = host.create_servers(socket)


from user import User
import client
users = client.create_users(socket)

assigned_servers = {} #dict from server name to users connected to that server

'''
    LOAD BALANCING
'''
import sys
sys.path.append('../')
from ds_features.LoadBalancer.round_robin import RoundRobinLoadBalancer ## find a way to get this
def round_robin():
    lb = RoundRobinLoadBalancer(servers, port_numbers) # it wants the list of port numbers of the servers
    for user in users:
        assign_to_this_server = lb.next_server()
        socket.send_string("edge"+ " " + user.name + "," + str(assign_to_this_server.server_name))
        user.assign_server(assign_to_this_server)
        if(assign_to_this_server in assigned_servers):
            assigned_servers[assign_to_this_server].append(user)
            # print(assigned_servers)
        else:
            assigned_servers[assign_to_this_server] = [user]
            # print(assigned_servers)
        print(assign_to_this_server)

    print("After assigning servers!")

    for u in users:
        print(u)

from ds_features.LoadBalancer.least_connection import LeastConnectionLoadBalancer, LCServer ## find a way to get this
def least_connections():
    list_of_servers = []
    for i in servers:
        inp = input(f"Enter the current number of connections of SERVER: {i.server_name}: ")
        list_of_servers.append(LCServer(i.server_name, i, inp))

    lb = LeastConnectionLoadBalancer(list_of_servers, socket) # check if port number is needed

    for user in users:
        assign_to_this_server = lb.get_least_connection_server()
        assign_to_this_server.active_connections +=1
        print("Name of server: ", assign_to_this_server.name)
        socket.send_string("edge"+ " " + user.name + "," + str(assign_to_this_server.name))

# round_robin()
least_connections()

'''
    CLOCK-SYNCHRONIZATION ALGORITHMS
'''

from ds_features.Coordination.ClockSynchronization.berkeley import BerkeleyServer, BerkeleyClient
def berkeley():
    berkeley_servers = []
    for i in servers:
        berkeley_servers.append(BerkeleyServer(i))

    berkeley_clients = []
    for i in users:
        # Find the server that the user is connected to
        server_of_i = i.server
        b_server = None
        index=0
        for ind, j in enumerate(berkeley_servers):
            if(j.server is server_of_i):
                b_server = j
                index = ind
                break

        berkeley_clients.append(BerkeleyClient(i, b_server))
        berkeley_servers[index].add_client(berkeley_clients[-1])


    trial_server = berkeley_servers[0]
    for trial_server in berkeley_servers:
        # socket = None
        trial_server.synchronize_clocks(socket)
        print(f"Server time: {trial_server.get_time()}")

        for k in trial_server.clients:
            print(k.get_time())


def cristian():
    from ds_features.Coordination.ClockSynchronization.christian import CristianClient, CristianServer
    cristian_servers = []
    for i in servers:
        cristian_servers.append(CristianServer(i))

    cristian_clients = []
    for i in users:
        # Find the server that the user is connected to
        server_of_i = i.server
        c_server = None
        index=0
        for ind, j in enumerate(cristian_servers):
            if(j.server is server_of_i):
                c_server = j
                index = ind
                break
        print("LOOK THIS", i)
        cristian_clients.append(CristianClient(i, c_server, c_server.server))
        cristian_servers[index].add_client(cristian_clients[-1])

    for trial_client in cristian_clients:
        trial_client.synchronize_clock(socket)
        print(f"Client time time: {trial_client.get_time()}")

def ntp():
    from ds_features.Coordination.ClockSynchronization.ntp import NTPClient
    ntp_clients = []
    for server in servers:
        ntp_clients.append(NTPClient(server, socket))

    for user in users:
        ntp_clients.append(NTPClient(user, socket))
    
    for client in ntp_clients:
        client.update_time()
        print(f"Current time of {client}: ", client.get_current_time())

# ntp()
# cristian()
# berkeley()

