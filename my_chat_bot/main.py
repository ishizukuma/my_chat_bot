# 必要なライブラリ、ファイルのimport
from my_chat_bot import respond_to_input
import scenario.res as re
import scenario.blog as sb
import scenario.booking as bk
import MeCab
import random

# res.pyから辞書型のメッセージを呼び出し、受け取る
responses = re.response()

# 分かち書きで入力されたメッセージを単語ごとに分割する関数の定義
def get_words(text):
    words = MeCab.Tagger("-Owakati").parse(text).split()
    return words

print("Welcome to my chatbot!")

# チャットボット
while True:
    user_input = input("You: ") # メッセージの受け取り
    
    if user_input in re.bye: # res.pyからbyeリストを呼び出し、
        print("またね！")    # そのリストにメッセージがあったら会話を終了する
        break
    else:
        prompt = tuple(get_words(user_input)) # 単語分割する関数を呼び出し
        flag = True # openaiを呼び出すかの判断をするためのもの
        for i in prompt:
            if i in responses:  # 辞書型の会話、辞書と一致する
                flag = False    # 単語が含まれていたらそれを返す
                bot_response = random.choice(responses[i])
                print("AI:", bot_response)
            elif i in sb.blog: # シナリオ型の会話、blogリストに
                flag = False   # 含まれてたら日記の作成を始める
                create = sb.making_blog() # 日記作成の関数呼び出し
                for b in create: # 作成された日記の出力
                    print(b)
            elif i in bk.bk:  # シナリオ型の会話、bkリストに
                flag = False  # 含まれてたら予約の開始をする
                reserve = bk.booking() # 予約の関数の呼び出し
                for r in reserve:
                    print(r) # 予約の確認の出力
                
        if flag: # シナリオ、辞書とマッチしなかった時に
            try: # flagがTrueのままとなりopenaiを呼び出す
                response = respond_to_input(user_input)
                print(f"AI: {response}")
            except Exception: # 認識できなかった時のエラー対応
                print(random.choice(re.no))
