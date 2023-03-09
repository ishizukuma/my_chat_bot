# 仮想環境の準備
python.exe -m virtualenv venv
.\venv\Scripts\activate

# 必要なライブラリ
python.exe -m pip install -U pip
python.exe -m pip install mecab-python3 unidic-lite
python.exe -m pip install openai
python.exe -m pip install sentence-transformers

# 実行コマンド
python.exe main.py