#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import time

items = ['apple', 'banana', 'candy']

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def push_items(ws, path):
    for i in items:
        await ws.send(i)
        time.sleep(1)

start_server = websockets.serve(hello, "localhost", 8765)
# start_server = websockets.serve(push_items, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()