class APIError(Exception):
    def __init__(self, msg: str):
        super().__init__("[ERROR] " + msg)