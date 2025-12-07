from app.models.schemas.chat import ChatRequest
from app.repository.client.upstage_client import UpstageClient


class ChatService:
    def __init__(self, upstage_client: UpstageClient):
        self.client = upstage_client

    def upstage_chat(self, message: ChatRequest):
        stream = self.client.chat_streaming(message)
        return stream
