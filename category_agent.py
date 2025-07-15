import os
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

def categorize_product(product_name: str) -> str:
    try:
        chat = ChatOpenAI()
        prompt = f"Suggest the most suitable e-commerce product category for the following product: '{product_name}'. Reply with only the category name."
        response = chat([HumanMessage(content=prompt)])
        return response.content.strip()
    except Exception as e:
        return f"Category detection failed: {e}"
