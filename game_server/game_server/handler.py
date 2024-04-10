# #!/usr/bin/env python
# # python3 -m pip install websockets

import asyncio
import json
import websockets
import gameStatus

currentStatus = gameStatus.GameStatus.begin_status()

async def handler(websocket, path):
    global currentStatus
    try:
        async for message in websocket:
            incomingStatus = gameStatus.parse_game_input_message(message)
            if incomingStatus:
                print("from client")
                gameStatus.print_game_status(incomingStatus)
                if incomingStatus:
                    currentStatus = incomingStatus
                    currentStatus.userID = 0
                    await send_to_ia(websocket)

    except websockets.exceptions.ConnectionClosedError:
        print("Conection closed by client")

async def send_to_ia(clientwebsocket):
    global currentStatus
    uri = "ws://localhost:8666"
    async with websockets.connect(uri) as websocket:
        await websocket.send(json.dumps(currentStatus.to_dict()))
        print('sended to ia')
        gameStatus.print_game_status(currentStatus)
        message = await websocket.recv()
        incomingStatus = gameStatus.parse_game_input_message(message)
        if incomingStatus:
            print("from ia")
            gameStatus.print_game_status(incomingStatus)
            currentStatus = incomingStatus
            currentStatus.userID = 0
            await clientwebsocket.send(json.dumps(currentStatus.to_dict()))

async def main():
    async with websockets.serve(handler, "localhost", 8766):
        print('WebSocket server running...')
        await asyncio.Future()

asyncio.run(main())


#!/usr/bin/env python
# python3 -m pip install websockets

# import asyncio
# import websockets
# import json
# import gameStatus

# currentStatus = gameStatus.GameStatus.begin_status()
# connected_clients = set()

# async def handler(websocket, path):
#     global currentStatus
#     try:
#         connected_clients.add(websocket)
#         async for message in websocket:
#             incomingStatus = gameStatus.parse_game_input_message(message)
#             if incomingStatus:
#                 print("11111from client")
#                 gameStatus.print_game_status(incomingStatus)
#                 currentStatus = incomingStatus
#                 currentStatus.userID = 0

#     except websockets.exceptions.ConnectionClosedError:
#         print("Connection closed by client")
#         connected_clients.remove(websocket)

# async def broadcast():
#     global currentStatus
#     while True:
#         if connected_clients:
#             message = json.dumps(currentStatus.__dict__)
#             await asyncio.wait([client.send(message) for client in connected_clients])
#         await asyncio.sleep(0.016)  # Espera 16 milisegundos antes de enviar la próxima actualización


# async def main():
#     server = websockets.serve(handler, "localhost", 8766)
#     broadcast_task = asyncio.create_task(broadcast())
#     print('WebSocket server running...')
#     await asyncio.gather(server, broadcast_task)

# asyncio.run(main())
