# ファイルのimport
from weather import weather_get

# 辞書型の会話の応答をしてくれる辞書を返す関数
def response():
    res = {
        "こんにちは": ["こんにちは！", "やあ！", "こんにちは。"],
        "おはよう": ["おはようございます！", "おはよう！", "朝だー！"],
        "こんばんは": ["こんばんは！", "こんばんはー！", "夜だー！"],
        "ありがとう": ["どういたしまして！", "いいえ、こちらこそ！", "何でもおっしゃってください。"],
        "天気": [weather_get()+"です。"], #天気についてはAPIを取得しています
    }
    return res

# 会話(プログラム)を終了する判断をするメッセージのリスト
bye = ["バイバイ","さようなら","またね"]
# openaiのエラーに対する応答のリスト
no = ["理解できませんでした。","理解不能！","もう一回言ってくれますか？"]
