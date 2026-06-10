from fastapi import APIRouter

from app.handlers.tool_calling_handler import tool_calling_handler
from app.schemas.chat_request import ChatRequest
from app.schemas.chat_response import ChatResponse


router = APIRouter(
    prefix="/toolcalling",
    tags=["Chatbot"]
)

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    return await tool_calling_handler(request.prompt)
