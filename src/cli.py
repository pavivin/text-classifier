from enum import Enum
from typing import Callable, Optional

import typer

from _regex import RegexCase
from ml import MLCase
from nlp_clean import NLPCase
from case import ABCCase
from exceptions import NotFoundException

class AppMode(Enum):
    FILE = 'file'
    STR = 'str'


class TextBuild(Enum):
    TRUE = True
    FALSE = False


class AppMethod(Enum):
    REGEX = RegexCase
    TEXT_PROCESSING = NLPCase
    ML = MLCase


class App:
    def __init__(self, case: ABCCase) -> None:
        self._print = typer.echo
        self._case = case


def main(
    mode: AppMode = typer.Option('', help="file mode: read test data from file, str mode read data from input"),
    filename: Optional[str] = typer.Option('', help="filename [xlsx]"),
    input_str: Optional[str] = typer.Option('', help="string with testing text"),
    # method: AppMethod = typer.Option('', help="string with testing text"),
    # build: TextBuild = typer.Option('', help="string with testing text"),
):
    NotFoundException(param='')
    # mode.value(filename=filename, input_str=input_str, method=method, build=build)


if __name__ == "__main__":
    typer.run(main)
