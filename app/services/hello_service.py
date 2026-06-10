from app.core.logger import logger

async def get_hello_message():
    logger.info("Hello endpoint called")

    return {
        "message": "Hello World"
    }