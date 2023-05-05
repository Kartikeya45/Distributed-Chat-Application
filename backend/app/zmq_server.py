import asyncio
import zmq
import zmq.asyncio

import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

ctx = zmq.asyncio.Context()

async def async_process(msg):
    print(f"Received message: {msg}")
    reply = [b"Thanks for your message!"]



async def recv_and_process():
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://127.0.0.1:9876")
    msg = await sock.recv_multipart() # waits for msg to be ready

asyncio.run(recv_and_process())