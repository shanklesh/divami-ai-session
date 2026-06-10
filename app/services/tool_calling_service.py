from groq import Groq
from tavily import TavilyClient

import json

from app.core.config import settings
from app.core.logger import logger

client = Groq(
    api_key=settings.GROQ_API_KEY
)

tavily_client = TavilyClient(api_key=settings.TAVILY_API_KEY)


async def webSearch(query: str) -> str:
    response = tavily_client.search(query)

    print(response)
    finaleResult =  "\n\n".join(result["content"] for result in response["results"])
    return finaleResult

async def generate_response(prompt: str) -> str:
    try:
        logger.info(f"Prompt received: {prompt}")
        messages= [
                {
                    "role": "system",
                    "content": """
                                You are a smart personal assistant who answers user questions.

                                You have access to the following tools:
                                1. webSearch(query: str) - Search the latest information on the internet.
                                """
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        completion = client.chat.completions.create(
            model=settings.GROQ_MODEL,
            temperature = 0,
            messages= messages,
            tools= [
                {
                "type": "function",
                "function": {
                    "name": "webSearch",
                    "description": "Search the laest informaon and realtime data from inernet",
                    "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "The Search query to perform search on."
                        }
                    },
                    "required": ["query"]
                    }
                }
                }
            ],
            tool_choice= "auto"
        )


        message = completion.choices[0].message

        messages.append(message)

        if message.tool_calls:
            tool_call = message.tool_calls[0]

            if tool_call.function.name == "webSearch":
                args = json.loads(tool_call.function.arguments)

                result = await webSearch(args["query"])
                messages.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": tool_call.function.name,
                    "content": result
                })
                 
                completion2 = client.chat.completions.create(
                    model=settings.GROQ_MODEL,
                    temperature = 0,
                    messages= messages,
                    tools= [
                        {
                        "type": "function",
                        "function": {
                            "name": "webSearch",
                            "description": "Search the laest informaon and realtime data from inernet",
                            "parameters": {
                            "type": "object",
                            "properties": {
                                "query": {
                                    "type": "string",
                                    "description": "The Search query to perform search on."
                                }
                            },
                            "required": ["query"]
                            }
                        }
                        }
                    ],
                    tool_choice= "auto"
                )
               
                return completion2.choices[0].message.content

        return message.content or ""



    except Exception as e:
        logger.exception("Groq API failed")
        raise e
