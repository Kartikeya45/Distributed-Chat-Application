import zmq
import asyncio
import zmq.asyncio

async def server():
    ctx = zmq.asyncio.Context.instance()
    socket = ctx.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    while True:
        message = await socket.recv()
        print(f"Received message: {message}")
        await socket.send(b"World")

async def main():
    tasks = [
        asyncio.create_task(server())
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())