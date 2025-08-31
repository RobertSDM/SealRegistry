from enum import Enum

from app.constants import METHOD
from app.services.seal_api.automation_api import AutomationSealAPI
from app.services.seal_api.http_api import HTTPSealAPI


class MethodTypes(Enum):
    AUTO, API = range(1, 2 + 1)


def seal_api():
    return HTTPSealAPI if METHOD == MethodTypes.API.name else AutomationSealAPI


def validate_range_start_end(start: int, end: int | None = None):
    if end and end < start:
        raise ValueError("The end needs to be greater than the start")

    if end and end <= 0:
        raise ValueError("The end should be greater than '0'")

    if start <= 0:
        raise ValueError("The start should be greater than '0'")
