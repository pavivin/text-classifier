from typing import Dict
from .exceptions import NotSeen


class TrainedData:
    def __init__(self):
        self.docCountOfClasses = {}
        self.frequencies: Dict[str, dict] = {}

    def increaseClass(self, className):
        self.docCountOfClasses[className] = self.docCountOfClasses.get(className, 0) + 1

    def increaseToken(self, token, className):
        if not token in self.frequencies:
            self.frequencies[token] = {}

        self.frequencies[token][className] = self.frequencies[token].get(className, 0) + 1

    def getDocCount(self):
        return sum(self.docCountOfClasses.values())

    def getClasses(self):
        return self.docCountOfClasses.keys()

    def getClassDocCount(self, className):
        return self.docCountOfClasses.get(className, None)

    def getFrequency(self, token: str, className: str):
        if token in self.frequencies:
            foundToken = self.frequencies[token]
            return foundToken.get(className)
        else:
            raise NotSeen(token)
