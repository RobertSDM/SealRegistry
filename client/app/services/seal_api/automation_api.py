from ...interfaces.seal_api_interface import SealAPI


class AutomationSealAPI(SealAPI):

    @staticmethod
    def validate(seal: int) -> bool:
        pass

    @staticmethod
    def register(seal: int) -> bool:
        pass
