# ファイルのimport
from weather import weather_get

# 日記作成を開始する判断基準の単語リスト
blog = ["日記","思い出","出来事"]

# 日記作成をしてくれる関数
def making_blog():
    print("何月何日の日記ですか？")
    date = "日付:"+input("You:")
    
    if date == "日付:今日":
        weather = "天気:"+weather_get()
    else:
        weather = input("その日の天気を教えて。\nYou:")
    
    event = input("今日の出来事を教えて。\nYou:")
    
    # 入力をリスト化して保存し、それを返す
    blog = ["", date, "-"*20, weather, "-"*20,event]
    return blog
