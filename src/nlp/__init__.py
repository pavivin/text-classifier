import pandas as pd

from case import ABCCase
from utils import print_classes, print_statitics
from configs import config
from data import Data
from nlp.classifier import Classifier
from nlp.tokenizer import Tokenizer
from nlp.trainer import Trainer


class NLPCase(ABCCase):
    def classify_text(self, df: pd.DataFrame):
        _tokenizer = Tokenizer()
        class_trainer = Trainer(_tokenizer)

        data_len = len(df[config.text_column_name])
        count = 0

        for i, df_item in enumerate(df[config.text_column_name]):

            right_class = df[config.theme_column_name][i]

            reader = Data().get_train_data()
            theme_list, text_list = reader[config.theme_column_name], reader[config.text_column_name]
            for theme, text in zip(theme_list, text_list):
                class_trainer.train(theme, text)

            text_classifier = Classifier(class_trainer.data, _tokenizer)

            classification = text_classifier.classify(df_item)

            predict_class, probability = classification
            if probability == 0.00:
                predict_class = 'не определено'

            if predict_class == right_class:
                count += 1

            print_classes(predict_class=predict_class, right_class=right_class)

        print_statitics(data_len=data_len, count=count)
