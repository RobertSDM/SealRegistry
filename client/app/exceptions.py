class AppError(Exception):
    def __init__(self, msg: str):
        super().__init__("[ERROR] " + msg)


class InputReadError(AppError):
    def __init__(self, msg: str):
        super().__init__(msg)
