import asyncio
import zmq
import zmq.asyncio

ctx = zmq.asyncio.Context()

async def send_messages():
    sock = ctx.socket(zmq.PUSH)
    sock.connect("tcp://127.0.0.1:9876")
    while True:
        msg = input("Enter a message: ")
        await sock.send_string(msg)

asyncio.run(send_messages())
