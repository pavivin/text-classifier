import pandas as pd
import pymorphy2
import typer

from case import ABCCase
from configs import config

morph = pymorphy2.MorphAnalyzer(lang='ru')


class NLPCase(ABCCase):
    # @staticmethod
    # def __ngrams(words, n=2):
    #     for idx in range(len(words) - n + 1):
    #         yield tuple(words[idx: idx + n])

    @staticmethod
    def __clean_text(text: str):
        tokens = text.lower().translate(str.maketrans('', '', config.punctuation)).split(' ')
        tokens = [
            token
            for token in tokens
            if token not in config.stopwords
            and token
            and not token.isnumeric()
            and 'ADVB' not in morph.parse(token)[0].tag
        ]
        text = ' '.join(tokens)
        return text

    def classify_text(self, df: pd.DataFrame):
        # b = pd.read_csv(config.light_train_filename)

        text = 'кредит'

        count = 0
        _count = 0
        for i, df_item in enumerate(df[config.text_column_name]):
            norm_text = self.__clean_text(df_item)
            if text in norm_text:
                count += 1
                typer.echo(df[config.theme_column_name][i])
                break

        typer.echo(count)
        typer.echo(_count)
