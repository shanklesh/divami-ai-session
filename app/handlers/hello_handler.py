from app.services.hello_service import get_hello_message

async def hello_handler():
    return await get_hello_message()