import zmq
import random
import sys
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://127.0.0.1:55561")

while True:
    message = input("Enter message to be sent: ")
    socket.send_string(message)