import asyncio
import zmq.asyncio

async def client():
    ctx = zmq.asyncio.Context.instance()
    socket = ctx.socket(zmq.REQ)
    socket.connect("tcp://192.168.137.1:5555")
    await socket.send(b"Hello")
    message = await socket.recv()
    print(f"Received message: {message}")


async def main():
    tasks = [
        asyncio.create_task(client()),
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())