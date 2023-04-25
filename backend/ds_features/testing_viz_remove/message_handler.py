import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:9876")

# while True:
#     message = socket.recv()
#     print(f"Received message: {message}")


def get_update():
    message = socket.recv().decode()
    print("-> " + message)
    command, data = message.split(' ')
    return command, data
