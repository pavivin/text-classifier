from typing import Dict

from .exceptions import NotSeen


class TrainedData:
    __slots__ = (
        'doc_count_of_classes',
        'frequencies',
    )

    def __init__(self):
        self.doc_count_of_classes = {}
        self.frequencies: Dict[str, dict] = {}

    def increase_class(self, class_name):
        self.doc_count_of_classes[class_name] = self.doc_count_of_classes.get(class_name, 0) + 1

    def increase_token(self, token, class_name):
        if not token in self.frequencies:
            self.frequencies[token] = {}

        self.frequencies[token][class_name] = self.frequencies[token].get(class_name, 0) + 1

    @property
    def get_doc_count(self):
        return sum(self.doc_count_of_classes.values())

    @property
    def get_classes(self):
        return self.doc_count_of_classes.keys()

    def get_class_doc_count(self, class_name):
        return self.doc_count_of_classes.get(class_name)

    def get_frequency(self, token: str, class_name: str):
        if token in self.frequencies:
            found_token = self.frequencies[token]
            return found_token.get(class_name)
        raise NotSeen(token)
