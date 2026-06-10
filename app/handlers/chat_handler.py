from app.services.chat_bot_service import generate_response

async def chat_handler(prompt: str):
    response = await generate_response(prompt)

    return {
        "response": response
    }