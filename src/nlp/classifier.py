from __future__ import division

import operator
from functools import reduce

from configs import config

from .exceptions import NotSeen
from .tokenizer import Tokenizer
from .trained_data import TrainedData


class Classifier:

    __slots__ = (
        'data',
        'trained_data',
        'tokenizer',
    )

    def __init__(self, trained_data, tokenizer):
        self.data: TrainedData = trained_data
        self.tokenizer: Tokenizer = tokenizer

    def classify(self, text: str):
        classes = self.data.get_classes
        tokens = set(self.tokenizer.tokenize(text))
        probs_of_classes = {}

        for class_name in classes:
            tokens_probs = [self.get_token_prob(token, class_name) for token in tokens]

            try:
                token_set_prob = reduce(lambda a, b: a * b, (i for i in tokens_probs if i))
            except Exception:
                token_set_prob = 0

            probs_of_classes[class_name] = token_set_prob * self.get_prior(class_name)

        return sorted(probs_of_classes.items(), key=operator.itemgetter(1), reverse=True)[0]

    def get_prior(self, class_name):
        return self.data.get_class_doc_count(class_name) / self.data.get_doc_count

    def get_token_prob(self, token, class_name):
        class_document_count = self.data.get_class_doc_count(class_name)
        try:
            token_frequency = self.data.get_frequency(token, class_name)
        except NotSeen:
            return None

        if token_frequency is None:
            return config.default_prob

        probablity = token_frequency / class_document_count
        return probablity
