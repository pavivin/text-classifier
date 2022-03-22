import pymorphy2

from configs import config

morph = pymorphy2.MorphAnalyzer(lang='ru')


class Tokenizer:
    @staticmethod
    def tokenize(text: str):
        return text.lower().split(' ')

    @staticmethod
    def remove_stopwords(token):
        return '' if token in config.stopwords else token

    @staticmethod
    def remove_punctuation(token: str):
        return token.translate(str.maketrans('', '', config.punctuation))

    @staticmethod
    def remove_advb(token: str):
        return '' if 'ADVB' in morph.parse(token)[0].tag else token

    @staticmethod
    def remove_numeric(token: str):
        return '' if token.isnumeric() else token
