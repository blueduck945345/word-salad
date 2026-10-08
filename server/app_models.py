'''App models'''
from pydantic import BaseModel, Field

class LoadRequest(BaseModel):
    text: str = Field(max_length=1024 * 1024) ## less than 1MB of text, otherwise Redis will reject the request