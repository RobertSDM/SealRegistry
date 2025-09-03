class AppError(Exception):
    def __init__(self, msg: str):
        super().__init__("[ERROR] " + msg)


class InputError(AppError):
    def __init__(self, msg: str):
        super().__init__(msg)
