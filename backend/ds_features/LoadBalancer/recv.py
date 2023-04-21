import sys
import zmq

port = "5556"
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect('tcp://127.0.0.1:55561')
socket.setsockopt_string(zmq.SUBSCRIBE, "")

while(True):
    message = socket.recv_string()
    print("Received message: ", message)
    if(message=='close'):
        break