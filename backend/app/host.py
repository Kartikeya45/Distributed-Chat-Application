# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.PUSH)
# socket.bind("tcp://127.0.0.1:49065")


import assign
from server import Server


list_of_servers = []
corresponding_port_numbers = []

def create_servers(socket, NUMBER_OF_SERVERS=3):
    
    global list_of_servers
    global corresponding_port_numbers

    for i in range(NUMBER_OF_SERVERS):
        current_server_port = assign.find_free_port()
        print(f"New server started at port {current_server_port}")

        s = Server(current_server_port)

        list_of_servers.append(s)
        corresponding_port_numbers.append(current_server_port)

        socket.send_string("server_add" + " "+ str(list_of_servers[-1].server_name))

    return list_of_servers, corresponding_port_numbers






print("<<<<<<<<<<<<<<<<<<< Success! >>>>>>>>>>>>>>>>>>")