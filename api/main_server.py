import asyncio
from fastapi import FastAPI, WebSocket
from game_of_life import game_of_life
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS
origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello welcome to the game of life"}


@app.websocket("/ws/game-of-life")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        initial_state = data["initial_state"]
        steps = data["steps"]
        delay = data.get("delay", 1)

        for _ in range(steps):
            initial_state = game_of_life(initial_state)
            await websocket.send_json({"current_state": initial_state})
            await asyncio.sleep(delay)
