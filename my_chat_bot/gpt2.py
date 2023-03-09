# 必要なライブラリのimport
import openai
import os

# 環境変数にopenaiのAPIkeyを設定し取得
openai.api_key = os.environ.get('OPEN_AI_KEY')
# 設定が分からない場合は直書きでも可能ですが、漏洩に注意！
# イメージ: openai.api_key = "xxxxx... "

# openaiに問い合わせを送信し、応答を取得する関数
def generate_response(prompt):
    response = openai.Completion.create(   
        engine="davinci",  # 使用するOpenAIのモデルを指定
        prompt=prompt,     # 生成された文章の前に与えるテキストを指定
        temperature=0.7,   # 生成されたテキストの多様性を制御
        max_tokens=2000,   # 生成されたテキストの長さを制御
        n=1,               #生成された文章の数を指定
        stop=["。", "?", "!"],  # 生成された文章が終了するトークンを指定
        frequency_penalty=0.9,  # 生成された文章で使用される単語の頻度を制御
        presence_penalty=0.9,   # 生成された文章で使用される単語の重複を制御
    )
    
    # メッセージの調整
    # 今回はopenaiの応答があまりうまくいかなかったため、
    # ある程度の調整をしました。
    text = response.choices[0].text.strip()
    res_text = ""
    replace = ["「","」","　"," ","[","]"]
    for t in text:
        if t not in replace:
            res_text += t
    res_text.replace('\n', '')
    
    return res_text
