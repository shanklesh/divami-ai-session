from fastapi import APIRouter

from app.handlers.chat_handler import chat_handler
from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse


router = APIRouter(
    prefix="/chat",
    tags=["Chatbot"]
)

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return await chat_handler(request.prompt)
