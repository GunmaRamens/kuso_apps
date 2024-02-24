import requests
import json
import os

LINGUA_DICT_URL = "https://fastapi.metacpan.org/source/MASH/Lingua-JA-Yomi-0.01/lib/Lingua/JA/bep-eng.dic"
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

def export_json():
    os.makedirs("src", exist_ok=True)
    with open("src/dict.json", mode="w") as file:
        json.dump(en_kana_dict, file, indent=2)

def main():
    get_lingua_dict()
    export_json()

if __name__ == "__main__":
    main()
