import re
from typing import List, Optional

import pandas as pd
import typer

from case import ABCCase
from configs import config


class RegexCase(ABCCase):
    slots = ('df',)

    def classify_text(self, df: pd.DataFrame):
        count = 0

        data_len = df.shape[0]

        output_list: List[str] = []

        for i, df_item in enumerate(df[config.text_column_name]):

            local_count: int = 0
            local_class: Optional[str] = None

            theme = df[config.theme_column_name][i]

            for re_item, re_class in config.named_regex.items():
                if re.search(re_item, df_item):
                    if theme == re_class:
                        local_class = re_class
                        local_count += 1

            if local_count == 0:
                output_str = ''.join((str(i), ') ', 'default', ': ', df_item, ': ', theme))
                output_list.append(output_str)
            else:
                if local_class == theme:
                    count += 1
                else:
                    typer.echo(f'{i}) {local_class}: {df_item} : {theme}')

        total_percent = (data_len / count) * 100 if count > 0 else 0
        typer.echo(f'{count} / {data_len}')
        typer.echo(f'{total_percent} %')
