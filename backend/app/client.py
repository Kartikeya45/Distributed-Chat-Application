import asyncio
import zmq
import zmq.asyncio

ctx = zmq.asyncio.Context()

async def send_messages():
    sock = ctx.socket(zmq.PUSH)
    sock.connect("tcp://192.168.137.1:5798")
    while True:
        msg = input("Enter a message: ")
        await sock.send_string(msg)

asyncio.run(send_messages())
