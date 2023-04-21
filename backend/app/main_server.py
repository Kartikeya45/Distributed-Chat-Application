import zmq

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:5835")

print("This code ran")
socket.send_string("message")

def get_socket():
	return socket