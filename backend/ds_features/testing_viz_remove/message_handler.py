import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://127.0.0.1:9876")

file = open("log.txt", "w")
file.write("")

# while True:
#     message = socket.recv()
#     print(f"EVENReceived message: {message}")


def get_update():
    message = socket.recv().decode()
    print("-> " + message)
    command, data = message.split(' ')

    file = open("log.txt", "a")
    file.write(message + "\n")
    file.close()

    return command, data
