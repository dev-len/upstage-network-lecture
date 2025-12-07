from fastapi import FastAPI

from dotenv import load_dotenv
from fastapi.params import Depends
from openai import OpenAI  # openai==1.52.2
import os

from starlette.responses import StreamingResponse

from app.api.route.chat_router import chat_router
from app.deps import get_chat_service
from app.models.schemas.chat import ChatRequest
from app.service.chat_service import ChatService

app = FastAPI()

app.include_router(router=chat_router)

load_dotenv()


@app.get("/hello")
async def hello():
    return {"message": "Hello FastAPI!"}


@app.post("/query")
async def query(message: ChatRequest):
    api_key = os.getenv("UPSTAGE_API_KEY")
    if not api_key:
        raise ValueError("UPSTAGE_API_KEY environment variable is required")
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.upstage.ai/v1"
    )
    response = client.embeddings.create(
        input=message.prompt,
        model="embedding-query"
    )

    return response.data[0].embedding

    # Use with stream=False
    # print(stream.choices[0].message.content)

