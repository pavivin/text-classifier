from abc import ABC, abstractmethod

import pandas as pd


class ABCCase(ABC):
    @abstractmethod
    def classify_text(self, df: pd.DataFrame):
        ...
