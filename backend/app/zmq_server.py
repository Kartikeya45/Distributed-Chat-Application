import asyncio
import zmq
import zmq.asyncio

import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

ctx = zmq.asyncio.Context()

def async_process(msg):
    print(f"Received message: {msg}")
    reply = [b"Thanks for your message!"]



async def recv_and_process():
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://192.168.137.1:5798")
    while(True):
        msg = await sock.recv() # waits for msg to be ready
        async_process(msg)

asyncio.run(recv_and_process())