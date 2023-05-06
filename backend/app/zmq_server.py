import asyncio
import zmq
import zmq.asyncio
import time
import sys

if sys.platform:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

ctx = zmq.asyncio.Context()

def async_process(msg):
    print(f"Received message: {msg}")
    
async def recv_and_process():
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://*:5968")
    while(True):
        msg = await sock.recv() # waits for msg to be ready
        async_process(msg.decode())
        

asyncio.run(recv_and_process())