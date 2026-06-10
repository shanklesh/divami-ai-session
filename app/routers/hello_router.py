from fastapi import APIRouter

from app.handlers.hello_handler import hello_handler
from app.schemas.response import HelloResponse

router = APIRouter(
    prefix="/hello",
    tags=["Hello"]
)

@router.get(
    "/",
    response_model=HelloResponse
)
async def hello():
    return await hello_handler()