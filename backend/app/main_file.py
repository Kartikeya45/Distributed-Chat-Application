import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:64666")

while True:
    message = input("Enter a message to send: ")
    socket.send_string(message)
