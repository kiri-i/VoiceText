#!usr/bin/env python3

import os
from dotenv import load_dotenv
import requests
from requests.auth import HTTPBasicAuth
import pprint
import pathlib
import json
from datetime import datetime

# .envを読み込んで環境変数を設定
load_dotenv()
# 環境変数からAPIキーを取得
API_KEY = os.getenv("VOICE_TEXT_APIKEY")

# 共通
output_dir = pathlib.Path("output")
url = "https://api.voicetext.jp/v1/tts"

auth = HTTPBasicAuth(API_KEY,"")
headers = {
    # "Authorization" : API_KEY
}


def save_json(json_dic, filename):
    output_dir.mkdir(exist_ok=True)
    filepath = output_dir / pathlib.Path(filename)
    with open(filepath, "w") as f:
        json.dump(json_dic, f, ensure_ascii=False, indent=4)


def tts(text,speaker="hikari"):
    payload = { "text": text,
                "speaker": speaker}
    r = requests.post(url, data=payload, auth=auth)
    r.raise_for_status()
    saveFileName = datetime.now().strftime("%Y%m%d_%H%M%S_") + ".wav"
    saveFilePath = output_dir / saveFileName
    with open(saveFilePath, 'wb') as saveFile:
        saveFile.write(r.content)


def main():
    text = input("テキストを入力")
    tts(text)
    print("完了")

if __name__ == "__main__":
    main()