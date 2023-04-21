import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:55561")

def get_socket():
	return socket