"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config
from AIAgentPlatform.pages.index import chat_page

class State(rx.State):
    """The app state."""


app = rx.App(
    theme=rx.theme(
        appearance="light",
        has_background=True,
        radius="large",
        accent_color="blue",
    ),
)

# 가져온 페이지를 앱에 추가합니다.
# 이 과정을 통해 '/' 경로와 chat_page 함수가 연결됩니다.
app.add_page(chat_page)
