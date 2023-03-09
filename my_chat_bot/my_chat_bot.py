# ファイル先の関数のimport
from gpt2 import generate_response

# main.pyから呼び出される関数
# 入力されたメッセージをopenaiに送る
def respond_to_input(user_input):
    prompt = user_input
    response = generate_response(prompt)
    return response
