from abc import ABC, abstractmethod
from typing import Any


class ABCCase(ABC):
    @abstractmethod
    def __call__(self, *args: Any, **kwds: Any):
        ...
