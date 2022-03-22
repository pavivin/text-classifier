import re
from dataclasses import dataclass
from typing import Tuple


@dataclass(frozen=True)
class Config:
    @staticmethod
    def _get_stopwords(stopwords_filename: str):
        with open(stopwords_filename, encoding='UTF-8') as file:
            return tuple(file.read().split('\n'))

    data_folder: str = 'data/'
    xlsx_filename: str = ''.join((data_folder, 'data.xlsx'))
    test_csv_filename: str = ''.join((data_folder, 'test.csv'))
    train_csv_filename: str = ''.join((data_folder, 'train.csv'))
    light_train_filename: str = ''.join((data_folder, 'light_train.csv'))
    stopwords_filename: str = ''.join((data_folder, 'stopwords.txt'))
    input_filename: str = ''.join((data_folder, 'input_data.xlsx'))
    train_sheet_name: str = 'train'
    test_sheet_name: str = 'test'
    text_column_name: str = 'Запрос'
    theme_column_name: str = 'Тема'
    sheet_names: Tuple[str, str] = (train_sheet_name, test_sheet_name)

    punctuation: str = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
    stopwords: Tuple[str] = _get_stopwords(stopwords_filename)

    re_credit_cart = re.compile(
        r'кредитк|((кред[итное]{0,3}|[ыаяуюом]{0,2}) * '
        r'(карт[аыочк]{0,4}))|карт[аыочк]{0,4} * '
        r'кред[итное]{0,3}|[ыаяуюом]{0,2}'
    )
    re_debet_cart = re.compile(r'карт')
    re_credit = re.compile(r'ден|займ|кред')

    # кредитная карта - кредитная карта, кредитка
    # дебетовая карта - !кредитная карта
    # кредит - деньги, займ, кредит

    named_regex = {
        re_credit_cart: 'кредитная карта',
        re_debet_cart: 'дебетовая карта',
        re_credit: 'кредит',
    }

    default_prob = 0.000000001


config = Config()
