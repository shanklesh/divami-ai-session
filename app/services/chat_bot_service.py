from groq import Groq

from app.core.config import settings
from app.core.logger import logger

client = Groq(
    api_key=settings.GROQ_API_KEY
)

async def generate_response(prompt: str) -> str:
    try:
        logger.info(f"Prompt received: {prompt}")

        completion = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages= [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        answer = completion.choices[0].message.content

        logger.info("Response generaed successfully")

        return answer


    except Exception as e:
        logger.exception("Groq API failed")
        raise e
