import typer


class BaseTyperException:
    def __init__(self, message: str):
        typer.echo(message, err=True)
        typer.Exit()


class NotFoundException:
    def __init__(self, filename: str):
        BaseTyperException(message=f'Файл не найден: {filename}')
