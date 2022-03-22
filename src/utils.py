import typer


def print_classes(predict_class: str, right_class: str):
    predict_class_color = typer.colors.BLUE if predict_class == right_class else typer.colors.RED
    _predict_class = typer.style(predict_class, fg=predict_class_color, bold=True)
    _right_class = typer.style(right_class, fg=typer.colors.BLUE, bold=True)
    typer.echo(f'{_predict_class} {_right_class}')


def print_statitics(count, data_len):
    total_percent = (data_len / count) * 100 if count > 0 else 0
    typer.echo(f'{count} / {data_len}')
    typer.echo(f'{total_percent} %')