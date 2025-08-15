import reflex as rx
from reflex.experimental import ClientStateVar

# 두 파일이 공통으로 사용하는 user_input 변수를 이곳으로 옮깁니다.
user_input = ClientStateVar.create("user_input", "")
