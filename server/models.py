from pydantic import BaseModel

class LoadRequest(BaseModel):
    text: str