import json
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Glossary:
    terms: Dict[str, Dict[str, str]]

    @classmethod
    def from_json(cls, json_data: str):
        data = json.loads(json_data)
        return cls({term: translations for term, translations in data.items()})

    def validate(self):
        for term, translations in self.terms.items():
            if not isinstance(translations, dict):
                raise ValueError(f"Invalid glossary format: {term} is not a dictionary")
            for locale, translation in translations.items():
                if not isinstance(translation, str):
                    raise ValueError(f"Invalid glossary format: {term} -> {locale} is not a string")

    def translate(self, text: str, locale: str):
        for term, translations in self.terms.items():
            if term in text:
                text = text.replace(term, translations.get(locale, term))
        return text

def load_glossary(file_path: str) -> Glossary:
    with open(file_path, 'r') as file:
        json_data = file.read()
        glossary = Glossary.from_json(json_data)
        glossary.validate()
        return glossary
