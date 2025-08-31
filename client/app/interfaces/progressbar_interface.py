from abc import ABC, abstractmethod


class ProgressbarInterface(ABC):
    @abstractmethod
    def plot(self, target: int, current: int, title: str, done: bool):
        pass
