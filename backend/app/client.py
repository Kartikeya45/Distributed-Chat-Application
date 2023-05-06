# import zmq
# context = zmq.Context()
# socket = context.socket(zmq.PUSH)
# socket.bind("tcp://127.0.0.1:98776")

import assign
from user import User

list_of_users = []
corresponding_port_numbers = []

def create_users(socket, NUMBER_OF_USERS=10):
    global list_of_users
    global corresponding_port_numbers

    user_name = ['USER'+str(i) for i in range(NUMBER_OF_USERS)]
    print(user_name)
    for i in range(NUMBER_OF_USERS):
        current_server_port = assign.find_free_port()
        print(f"New client started at port {current_server_port}")

        u = User(user_name[i], current_server_port)

        list_of_users.append(u)
        corresponding_port_numbers.append(current_server_port)

        socket.send_string("user_add" + " "+ list_of_users[-1].name)
        # we can use multiple push protocols dw
        print(u)

    return list_of_users
    