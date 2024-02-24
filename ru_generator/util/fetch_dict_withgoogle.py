import requests
import json
import os
import io
import zipfile
import mimetypes


LINGUA_DICT_URL = "https://fastapi.metacpan.org/source/MASH/Lingua-JA-Yomi-0.01/lib/Lingua/JA/bep-eng.dic"
GOOGLE_DICT_URL = "https://github.com/KEINOS/google-ime-user-dictionary-ja-en/archive/master.zip"
en_kana_dict = dict()



def get_lingua_dict():
    res = requests.get(LINGUA_DICT_URL)
    res.encoding = res.apparent_encoding

    for row in res.text.split("\n"):
        if row.startswith("#"):
            continue
        if len(row.split(" ")) != 2:
            continue
        en_word, jp_word = row.split(" ")
        lower_en_word = en_word.lower()
        en_kana_dict[lower_en_word] = jp_word

def get_google_dict():
    # mk tmp dir
    if not os.path.exists("tmp"):
        os.makedirs("tmp")

    # download zip
    with (
        requests.get(GOOGLE_DICT_URL) as res,
        io.BytesIO(res.content) as bytes_io,
        zipfile.ZipFile(bytes_io) as zip,
    ):
        zip.extractall("tmp")
    
    # tmp内の全てのファイルを読み込む
    for root, dirs, files in os.walk("tmp/google-ime-user-dictionary-ja-en-master/Google-ime-jp-カタカナ英語辞典"):
        for file in files:
            # MIMEタイプがtext/plainのファイルを読み込む
            mime_type = mimetypes.guess_type(file)[0]
            if mime_type != "text/plain":
                continue
            
            # ファイルを読み込む
            with open(os.path.join(root, file), mode="r",encoding="utf-8_sig") as f:
                try:
                    for row in f.readlines():
                        if len(row.split("\t")) < 4:
                            #print(f"invalid format: {file}")
                            continue
                        splited_row = row.split("\t")
                        en_word = splited_row[1]
                        jp_word = splited_row[3]
                        if splited_row[1].find(" ") != -1:
                            #print(f"invalid en word: {file}")
                            continue
                        lower_en_word = en_word.lower()
                        
                        en_kana_dict[lower_en_word] = jp_word
                        #print(f"add: {lower_en_word} -> {jp_word}")
                except UnicodeDecodeError:
                    #print(f"UnicodeDecodeError: {file}")
                    continue

def export_json():
    os.makedirs("src", exist_ok=True)
    with open("src/dict.json", mode="w") as file:
        json.dump(en_kana_dict, file, indent=2)

def main():
    get_google_dict()
    get_lingua_dict()
    export_json()

if __name__ == "__main__":
    main()
