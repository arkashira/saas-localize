import argparse
import json
from dataclasses import dataclass

@dataclass
class TranslationRequest:
    text: str
    target_language: str

class Translator:
    def __init__(self):
        self.translations = {
            "hello": {"es": "hola", "fr": "bonjour"},
            "world": {"es": "mundo", "fr": "monde"},
        }

    def translate(self, request: TranslationRequest):
        text = request.text
        target_language = request.target_language
        translated_text = ""
        for word in text.split():
            if word in self.translations:
                translated_text += self.translations[word].get(target_language, word) + " "
            else:
                translated_text += word + " "
        return translated_text.strip()

def main():
    parser = argparse.ArgumentParser(description="Translate text")
    parser.add_argument("--text", help="Text to translate")
    parser.add_argument("--target-language", help="Target language")
    args = parser.parse_args()
    translator = Translator()
    request = TranslationRequest(args.text, args.target_language)
    translated_text = translator.translate(request)
    print(translated_text)

if __name__ == "__main__":
    main()
