from .trained_data import TrainedData
from .tokenizer import Tokenizer

class Trainer:

    def __init__(self, tokenizer):
        self.tokenizer: Tokenizer = tokenizer
        self.data = TrainedData()

    def train(self, text, className):
        self.data.increaseClass(className)

        tokens = self.tokenizer.tokenize(text)
        for token in tokens:
            token = self.tokenizer.remove_stop_words(token)
            token = self.tokenizer.remove_punctuation(token)
            self.data.increaseToken(token, className)
