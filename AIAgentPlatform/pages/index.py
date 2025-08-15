import reflex as rx
from AIAgentPlatform.components.template import main_template
from AIAgentPlatform.state.chat_state import ChatState, Message

def message_bubble(message: Message) -> rx.Component:
    is_ai = message.user == "AI"
    return rx.box(
        rx.markdown(message.text),
        align_self=rx.cond(is_ai, "start", "end"),
        bg=rx.cond(is_ai, "gray.100", "blue.100"),
        padding="1em",
        border_radius="lg",
        max_width="70%",
    )

@rx.page(route="/")
def chat_page() -> rx.Component:
    def content() -> rx.Component:
        return rx.vstack(
            rx.vstack(
                rx.foreach(ChatState.chat_history, message_bubble),
                spacing="4",
                width="100%",
                flex_grow=1,
                overflow_y="auto",
                padding_bottom="1em",
            ),
            rx.hstack(
                rx.input(
                    placeholder="메시지를 입력하세요...",
                    value=ChatState.input_text,
                    on_change=ChatState.set_input_text,
                    on_key_down=ChatState.handle_key_down,  # Use defined handler
                    flex_grow=1,
                ),
                rx.button(
                    "전송",
                    on_click=ChatState.submit_message,  # Use defined submit
                ),
                width="100%",
            ),
            height="calc(100vh - 4em)",
            width="100%",
            align="stretch",
            spacing="4",
        )
    return main_template(content)