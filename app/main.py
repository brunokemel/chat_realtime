from fastapi import FastAPI
from app.websocket import router as ws_router
from app.routes import users

app = FastAPI()

app.include_router(users.router)
app.include_router(ws_router)

@app.get("/")
def root():
    return {"message": "Chat em tempo real ativo 🚀"}