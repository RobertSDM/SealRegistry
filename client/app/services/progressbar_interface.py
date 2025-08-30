from abc import ABC, abstractmethod


class Progressbar(ABC):
    @abstractmethod
    def plot(target: int, current: int, done: bool):
        pass
