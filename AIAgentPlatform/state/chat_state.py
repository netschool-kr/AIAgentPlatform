import reflex as rx

class Message(rx.Base):
    user: str
    text: str

class ChatState(rx.State):
    """채팅 상태를 관리합니다."""
    chat_history: list[Message] = []
    input_text: str = ""  # Declare as state var here

    async def process_message(self, text: str):
        """메시지를 처리하는 내부 로직"""
        self.chat_history.append(Message(user="User", text=text))
        self.input_text = ""  # Clear input after processing
        yield
        self.chat_history.append(Message(user="AI", text=f"AI가 '{text}'에 응답합니다."))

    async def submit_message(self):
        if not self.input_text.strip():
            return
        return self.process_message(self.input_text)

    def handle_key_down(self, event):
        if event == "Enter":
            if not self.input_text.strip():
                return
            text = self.input_text
            self.chat_history.append(Message(user="User", text=text))
            self.input_text = ""  # Clear input after processing
            yield
            self.chat_history.append(Message(user="AI", text=f"AI가 '{text}'에 응답합니다."))
