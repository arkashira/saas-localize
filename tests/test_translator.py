from translator import Translator, TranslationRequest

def test_translate_happy_path():
    translator = Translator()
    request = TranslationRequest("hello world", "es")
    translated_text = translator.translate(request)
    assert translated_text == "hola mundo"

def test_translate_edge_case_unknown_word():
    translator = Translator()
    request = TranslationRequest("foo bar", "es")
    translated_text = translator.translate(request)
    assert translated_text == "foo bar"

def test_translate_edge_case_unknown_language():
    translator = Translator()
    request = TranslationRequest("hello world", "de")
    translated_text = translator.translate(request)
    assert translated_text == "hello world"
