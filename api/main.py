from fastapi import FastAPI
from api.routes import chat, upload

app = FastAPI(title="AWS Data Platform")

app.include_router(chat.router)
app.include_router(upload.router)


@app.get("/")
def home():
    return {"message": "API AWS Data Platform rodando"}