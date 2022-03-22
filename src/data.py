import csv

import pandas as pd

from configs import config
from exceptions import NotFoundException


class Data:
    @staticmethod
    def __trim_text(df: pd.DataFrame):
        return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    @staticmethod
    def read_dataframe(filename: str):
        try:
            return pd.read_excel(filename)
        except FileNotFoundError:
            NotFoundException(filename)

    def data_to_csv(self):
        df = pd.ExcelFile(config.xlsx_filename)

        train_data: pd.DataFrame = self.__trim_text(pd.read_excel(df, config.train_sheet_name))
        test_data: pd.DataFrame = self.__trim_text(pd.read_excel(df, config.test_sheet_name))

        train_data.to_csv(config.train_csv_filename, index=False)
        test_data.to_csv(config.test_csv_filename, index=False)

    @staticmethod
    def get_csv_data(filename: str):
        df = {config.text_column_name: [], config.theme_column_name: []}
        for item in csv.DictReader(open(filename)):
            df[config.text_column_name].append(item[config.text_column_name])
            df[config.theme_column_name].append(item[config.theme_column_name])
        return df

    def get_train_data(self):
        return self.get_csv_data(config.train_csv_filename)

    def get_test_data(self):
        return self.get_csv_data(config.test_csv_filename)
