from exceptions import BaseTyperException


class NotSeen(BaseTyperException):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Token '{self.value}' is never seen in the training set."
