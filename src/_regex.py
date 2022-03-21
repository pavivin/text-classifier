import re
from typing import List

import pandas as pd

from configs import config

from case import ABCCase


class RegexCase(ABCCase):
    slots = ('df',)

    def __call__(self, df: pd.DataFrame):
        count = 0

        data_len = df.shape[0]

        output_list: List[str] = []

        for i, df_item in enumerate(df[config.text_column_name]):
            # кредитная карта - кредитная карта, кредитка
            # дебетовая карта - !кредитная карта
            # кредит - деньги, займ, кредит

            local_count = 0
            local_class = 0

            for re_item, re_class in config.named_regex.items():
                if re.search(re_item, df_item):
                    if df[config.theme_column_name][i] == re_class:
                        local_class = re_class
                        local_count += 1

            if local_count == 0:
                output_str = ''.join((str(i), ') ', 'default', ': ', df_item, ': ', df[config.theme_column_name][i]))
                output_list.append(output_str)
            else:
                if local_class == df[config.theme_column_name][i]:
                    count += 1
                else:
                    print(i, ') ', local_class, ': ', df_item, ': ', df[config.theme_column_name][i])

        print(count, '/', data_len)
        print((data_len / count) * 100, '%')
