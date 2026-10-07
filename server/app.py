from fastapi import FastAPI
from models import LoadRequest
from datetime import datetime

app = FastAPI(title="Word Salad API")

@app.get("/")
def root():
    return {"time": datetime.now()}

@app.get("/sample")
def sample(size: int = 10):
    return {
        "message": "This is a sample endpoint",
        "size": size,
    }

@app.post("/load")
def load(request: LoadRequest):
    return {"status": "ok"}