from app.services.tool_calling_service import generate_response

async def tool_calling_handler(prompt: str):
    response = await generate_response(prompt)

    return {
        "response": response
    }