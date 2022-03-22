from enum import Enum
from typing import Dict, Optional, Type

import typer

from case import ABCCase
from configs import config
from data import Data
from ml import MLCase
from nlp import NLPCase
from regexp import RegexCase


class AppMethod(Enum):
    REGEX = 'regex'
    NLP = 'nlp'
    ML = 'ml'


APP_METHOD: Dict[str, Type[ABCCase]] = {
    'regex': RegexCase,
    'nlp': NLPCase,
    'ml': MLCase,
}

# TODO: rewrite pandas to csv reader
class App:
    def __init__(
        self,
        filename: Optional[str] = typer.Option(config.input_filename, help="filename [xlsx]"),
        method: AppMethod = typer.Option(AppMethod.ML.value, case_sensitive=False, help="string with testing text"),
        build: bool = False,
    ):
        data = Data()
        if build:
            data.data_to_csv()
        if filename:
            df = data.read_dataframe(filename=filename)
        app_method: ABCCase = APP_METHOD[method.value]()

        app_method.classify_text(df=df)


if __name__ == "__main__":
    typer.run(App)
