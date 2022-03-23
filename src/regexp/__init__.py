import re
from typing import List, Optional

import pandas as pd

from case import ABCCase
from utils import print_classes, print_statitics
from configs import config


class RegexCase(ABCCase):
    slots = ('df',)

    def classify_text(self, df: pd.DataFrame):
        count = 0

        data_len = len(df[config.text_column_name])

        output_list: List[str] = []

        for i, df_item in enumerate(df[config.text_column_name]):

            local_count: int = 0
            predict_class: Optional[str] = None

            theme = df[config.theme_column_name][i]

            for re_item, right_class in config.named_regex.items():
                if re.search(re_item, df_item) and theme == right_class:
                    predict_class = right_class
                    local_count += 1

            print_classes(predict_class=predict_class, right_class=right_class)

            if local_count == 0:
                output_str = ''.join((str(i), ') ', 'default', ': ', df_item, ': ', theme))
                output_list.append(output_str)
            else:
                if predict_class == theme:
                    count += 1

        print_statitics(data_len=data_len, count=count)
