# AIAgentPlatform/AIAgentPlatform.py
import reflex as rx

from AIAgentPlatform.pages.index import chat_page
from AIAgentPlatform.state.chat_state import ChatState

app = rx.App()
app.add_page(chat_page, route="/")