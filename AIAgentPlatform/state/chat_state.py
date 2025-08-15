#AIAgentPlatform/state/chat_state.py
import reflex as rx
import asyncio

class Message(rx.Base):
    """채팅 메시지를 위한 데이터 모델"""
    user: str
    text: str
    
class ChatState(rx.State):
    """채팅 앱의 서버 사이드 상태"""
    chat_history: list[Message] = []

    async def process_message(self, user_question: str):
        """사용자 질문을 처리하고 응답을 생성하는 이벤트 핸들러"""
        if not user_question.strip():
            return

        # 사용자 메시지를 채팅 기록에 추가
        self.chat_history.append(Message(user="Human", text=user_question))
        yield

        # AI 응답 시뮬레이션
        ai_response = f"'{user_question}'에 대한 AI의 응답입니다."
        self.chat_history.append(Message(user="AI", text=""))
        for char in ai_response:
            self.chat_history[-1].text += char
            await asyncio.sleep(0.03)
            yield
