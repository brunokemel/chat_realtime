from fastapi import FastAPI
from app.websocket import router as ws_router

app = FastAPI()

app.include_router(ws_router)

@app.get("/")
def root():
    return {"message": "Welcome to the FastAPI WebSocket Chat!"}