import requests
import json

def weather_get():
    # 気象庁データの取得
    jma_url = "https://www.jma.go.jp/bosai/forecast/data/forecast/130000.json"
    jma_json = requests.get(jma_url).json()

    # 取得
    jma_weather = jma_json[0]["timeSeries"][0]["areas"][0]["weathers"][0]
    jma_weather = jma_weather.replace('　', '') 

    return jma_weather