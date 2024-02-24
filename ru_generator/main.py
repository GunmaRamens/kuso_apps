import json
from janome.tokenizer import Tokenizer
from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='ja',target='en')

with open("src/dict.json", mode="r") as file:
    en_kana_dict = json.load(file)
tokenizer = Tokenizer()

input_string = input(">>> ")
tokens = tokenizer.tokenize(input_string)

rued_string = ""
for index, token in enumerate(tokens):
    print(f"ruing {index + 1}th token")
    if token.part_of_speech.split(',')[0] == '名詞':
        en_noun = translator.translate(token.surface)
        ru_noun = en_kana_dict.get(en_noun.lower())
        if ru_noun is None:
            ru_noun = en_noun
        rued_string += ru_noun

        print(f"{token.surface}*{en_noun}*{ru_noun}")
    else:
        rued_string += token.surface

print("Rued string: ", rued_string)
