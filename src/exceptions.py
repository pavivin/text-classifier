from typing import Optional
import typer


class BaseException:
    def __init__(self, message: str, param: Optional[str]):
        typer.echo(f'{message} {param}')
        typer.Exit()


class NotFoundException:
    def __init__(self, param: Optional[str]):
        BaseException(message='Параметр не найден', param=param)
