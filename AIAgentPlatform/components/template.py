#AIAgentPlatform/components/template.py
import reflex as rx
from typing import Callable

def main_template(page_content: Callable[[], rx.Component]) -> rx.Component:
    """모든 페이지를 위한 기본 템플릿"""
    return rx.hstack(
        # 왼쪽 사이드바
        rx.vstack(
            rx.heading("AI 에이전트", size="6"),
            rx.text("플랫폼 v0.1"),
            rx.divider(),
            rx.vstack(
                rx.link("채팅", href="/"),
                rx.link("설정", href="/settings"),
                spacing="4",
                align_items="start",
            ),
            rx.spacer(),
            rx.text("© 2025 AI Architect"),
            width="250px",
            height="100vh",
            padding="1em",
            bg="gray.100",
            border_right="1px solid #ddd",
        ),
        # 메인 컨텐츠 영역
        rx.box(
            page_content(),
            padding="2em",
            width="100%",
            height="100vh",
            overflow_y="auto",
        ),
        spacing="0",
        align="start",
    )
