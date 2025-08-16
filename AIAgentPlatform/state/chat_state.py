import reflex as rx

class Message(rx.Base):
    user: str
    text: str

class ChatState(rx.State):
    """채팅 상태를 관리합니다."""
    chat_history: list[Message] = []
    input_text: str = ""

    async def process_message(self):
        """입력된 메시지를 처리하고 AI 응답을 생성합니다."""
        if not self.input_text.strip():
            return

        # 사용자의 메시지를 리스트 맨 앞에 추가하고 입력창을 비웁니다.
        text = self.input_text
        self.chat_history.insert(0, Message(user="User", text=text))
        self.input_text = ""
        yield # UI를 업데이트하여 사용자 메시지를 즉시 표시합니다.

        # AI 응답을 리스트 맨 앞에 추가하여 가장 최신 메시지로 만듭니다.
        self.chat_history.insert(0, Message(user="AI", text=f"AI가 '{text}'에 응답합니다."))

    def submit_message(self):
        """전송 버튼 클릭을 처리합니다."""
        # process_message를 호출하도록 수정합니다.
        return self.process_message()

    def handle_key_down(self, event):
        """입력 필드에서 Enter 키 입력을 처리합니다."""
        if event == "Enter":
            # process_message를 호출하도록 수정합니다.
            return self.process_message()
