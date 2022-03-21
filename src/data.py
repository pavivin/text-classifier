import pandas as pd

from configs import config


class Data:
    def __trim_text(df: pd.DataFrame):
        return df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    def __init__(self, filename: str):
        self.df = pd.read_excel(filename)

    def data_to_csv(self):
        df = pd.ExcelFile(config.xlsx_filename)

        train_data: pd.DataFrame = self.__trim_text(pd.read_excel(df, config.train_sheet_name))
        test_data: pd.DataFrame = self.__trim_text(pd.read_excel(df, config.test_sheet_name))

        train_data.to_csv(config.train_csv_filename)
        test_data.to_csv(config.test_csv_filename)

    @staticmethod
    def get_light_data():
        return pd.read_csv(config.light_train_filename)

    @staticmethod
    def get_train_data():
        return pd.read_csv(config.train_csv_filename)

    @staticmethod
    def get_test_data():
        return pd.read_csv(config.test_csv_filename)
