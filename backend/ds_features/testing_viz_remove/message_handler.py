import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:5555")

# while True:
#     message = socket.recv()
#     print(f"Received message: {message}")


def get_update():
    message = socket.recv().decode()
    command, data = message.split(' ')
    return command, data
