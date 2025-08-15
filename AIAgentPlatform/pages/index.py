#AIAgentPlatform/pages/index.py
import reflex as rx
from reflex.experimental import ClientStateVar
from AIAgentPlatform.components.template import main_template
from AIAgentPlatform.state.chat_state import ChatState, Message

# 사용자 입력을 위한 클라이언트 사이드 상태
user_input = ClientStateVar.create("user_input", "")

def message_bubble(message: Message) -> rx.Component:
    """개별 메시지 버블을 렌더링하는 컴포넌트"""
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
    """메인 채팅 페이지"""
    def content() -> rx.Component:
        return rx.vstack(
            # 채팅 기록
            rx.vstack(
                rx.foreach(ChatState.chat_history, message_bubble),
                spacing="4",
                width="100%",
                flex_grow=1,
                overflow_y="auto",
                padding_bottom="1em",
            ),
            # 입력 폼
            rx.hstack(
                rx.input(
                    placeholder="메시지를 입력하세요...",
                    value=user_input.value,
                    on_change=user_input.set_value,
                    on_key_down=lambda key: rx.cond(
                        key == "Enter",
                        ChatState.process_message(user_input.value),
                        rx.console_log("")  # No-op
                    ),
                    flex_grow=1,
                ),
                rx.button(
                    "전송",
                    on_click=ChatState.process_message(user_input.value),
                ),
                width="100%",
            ),
            height="calc(100vh - 4em)",  # 전체 높이에서 패딩 제외
            width="100%",
            align="stretch",
            spacing="4",
        )
    return main_template(content)

