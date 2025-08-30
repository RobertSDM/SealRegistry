from .interface import SealAPI


class AutomationSealAPI(SealAPI):

    @staticmethod
    def check(seal: int) -> bool:
        pass

    @staticmethod
    def register(seal: int) -> bool:
        pass
