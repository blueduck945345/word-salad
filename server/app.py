'''Main app routes'''
from fastapi import FastAPI, Query
from app_models import LoadRequest
from dependencies import RedisClient
from services import load, sample

app = FastAPI(title="Word Salad API")

@app.get("/sample")
async def sample_endpoint(
    r: RedisClient,
    size: int = Query(
        10, gt=0, le=100, description="Number of lines to sample" ## limit to 100 lines to avoid overloading Redis
    )
):
    return await sample(size, r)

@app.post("/load")
async def load_endpoint(
    request: LoadRequest,
    r: RedisClient,
):
    await load(request.text, r)
    return {"message": "Text processed"}