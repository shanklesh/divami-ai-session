from fastapi import FastAPI

from app.routers.chat_bot_router import router as chat_bot_router
from app.routers.hello_router import router as hello_router
from app.routers.tool_calling_router import router as tool_calling_router


app= FastAPI(
    title="ChatBot API",
    version="1.0.0"
)

app.include_router(hello_router)
app.include_router(chat_bot_router)
app.include_router(tool_calling_router)