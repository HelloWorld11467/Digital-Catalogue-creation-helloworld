from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

def smart_assistant_reply(message: str) -> str:
    chat = ChatOpenAI()
    response = chat([
        HumanMessage(content=f"You're an assistant for rural sellers. Answer this: {message}")
    ])
    return response.content
