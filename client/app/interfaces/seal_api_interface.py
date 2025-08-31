from abc import ABC, abstractmethod


class SealAPI(ABC):
    @abstractmethod
    def validate(seal: int) -> bool:
        pass

    @abstractmethod
    def register(seal: int):
        pass
