from googletrans import Translator, LANGUAGES

def TransLate(str, lang):
    translator = Translator()
    try:
        result = translator.translate(str, dest=lang)
        return result.text
    except Exception as e:
        return str(e)

def LangDetect(txt):
    translator = Translator()
    try:
        result = translator.detect(txt)
        return result.lang, result.confidence
    except Exception as e:
        return str(e)

def CodeLang(lang):
    lang = lang.lower()
    if lang in LANGUAGES.values():
        return list(LANGUAGES.keys())[list(LANGUAGES.values()).index(lang)]
    elif lang in LANGUAGES.keys():
        return LANGUAGES[lang]
    else:
        return "Language not found"

txt = "Привіт! Як Справи?"
lang = "en"
print(txt)
print(LangDetect(txt))
print(TransLate(txt, lang))
print(CodeLang(lang))
