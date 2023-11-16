import asyncio
import websockets
import json
from game_of_life import game_of_life  # Import your game_of_life function


async def game_of_life_server(websocket, path):
    try:
        initial_message = await websocket.recv()
        data = json.loads(initial_message)
        initial_state = data["initial_state"]
        print("Initial state: ", initial_state, sep="\n")
        steps = data["steps"]
        delay = data["delay"]

        current_state = initial_state

        for _ in range(steps):
            current_state = game_of_life(current_state)

            await websocket.send(json.dumps(current_state))

            await asyncio.sleep(delay)
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed normally")
    except websockets.exceptions.ConnectionClosedError as e:
        print("Connection closed with error:", e)



if __name__ == "__main__":

    start_server = websockets.serve(game_of_life_server, "localhost", 8000)
    print("Server started at localhost:8000")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
