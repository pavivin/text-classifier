from configs import config

from .tokenizer import Tokenizer
from .trained_data import TrainedData


class Trainer:
    def __init__(self, tokenizer):
        self.tokenizer: Tokenizer = tokenizer
        self.data = TrainedData()

    def train(self, text, class_name):
        self.data.increase_class(class_name)

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            token = self.tokenizer.remove_stopwords(token)
            token = self.tokenizer.remove_punctuation(token)
            token = self.tokenizer.remove_advb(token)
            token = self.tokenizer.remove_numeric(token)
            self.data.increase_token(token, class_name)
