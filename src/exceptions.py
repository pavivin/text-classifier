import typer


class BaseTyperException(Exception):
    def __init__(self, message: str):
        typer.echo(message, err=True)
        typer.Exit()


class NotFoundException:
    def __init__(self, filename: str):
        raise BaseTyperException(message=f'File not found: {filename}')
