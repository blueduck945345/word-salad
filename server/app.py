'''Main app routes'''
from pickle import load
from fastapi import FastAPI, Query
from app_models import LoadRequest
from dependencies import RedisClient
from services import load as load_service, sample as sample_service

app = FastAPI(title="Word Salad API")

@app.get("/sample")
async def sample(
    r: RedisClient,
    size: int = Query(
        10, gt=0, le=100, description="Number of lines to sample" ## limit to 100 lines to avoid overloading Redis
    )
) -> list[str]:
    return await sample_service(size, r)

@app.post("/load")
async def load(
    request: LoadRequest,
    r: RedisClient,
) -> dict[str, str]:
    await load_service(request.text, r)
    return {"message": "Text processed"}