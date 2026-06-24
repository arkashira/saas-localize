import pytest
from glossary import Glossary, load_glossary

def test_glossary_from_json():
    json_data = '{"hello": {"en": "hello", "fr": "bonjour"}}'
    glossary = Glossary.from_json(json_data)
    assert glossary.terms == {"hello": {"en": "hello", "fr": "bonjour"}}

def test_glossary_validate():
    json_data = '{"hello": {"en": "hello", "fr": "bonjour"}}'
    glossary = Glossary.from_json(json_data)
    glossary.validate()  # Should not raise an exception

def test_glossary_validate_invalid_format():
    json_data = '{"hello": "bonjour"}'
    glossary = Glossary.from_json(json_data)
    with pytest.raises(ValueError):
        glossary.validate()

def test_glossary_translate():
    json_data = '{"hello": {"en": "hello", "fr": "bonjour"}}'
    glossary = Glossary.from_json(json_data)
    text = "hello world"
    translated_text = glossary.translate(text, "fr")
    assert translated_text == "bonjour world"

def test_load_glossary():
    json_data = '{"hello": {"en": "hello", "fr": "bonjour"}}'
    with open("glossary.json", "w") as file:
        file.write(json_data)
    glossary = load_glossary("glossary.json")
    assert glossary.terms == {"hello": {"en": "hello", "fr": "bonjour"}}

def test_load_glossary_invalid_format():
    json_data = '{"hello": "bonjour"}'
    with open("glossary.json", "w") as file:
        file.write(json_data)
    with pytest.raises(ValueError):
        load_glossary("glossary.json")
