from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    prompt: str = Field(...,min_lenght=1)