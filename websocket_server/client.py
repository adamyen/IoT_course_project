#!/usr/bin/env python

# WS client example

import asyncio
import websockets

async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        name = input("What's your name? ")

        await websocket.send(name)
        print(f"> {name}")

        greeting = await websocket.recv()
        print(f"< {greeting}")

async def get_scanned_item():
    async with websockets.connect("ws://localhost:8765") as websocket:
        while True:
            item = await websocket.recv()
            print(f"< {item}")


# asyncio.get_event_loop().run_until_complete(get_scanned_item())
asyncio.get_event_loop().run_until_complete(hello())