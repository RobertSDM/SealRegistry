from enum import Enum

from app.constants import METHOD
from app.exceptions import AppError
from app.interfaces.seal_api_interface import SealAPI
from app.repository.automation_api import AutomationSealAPI
from app.repository.http_api import HTTPSealAPI


class MethodTypes(Enum):
    AUTO, API = range(1, 2 + 1)


def seal_api() -> SealAPI:
    """
    Returns
    ---
    A [SealAPI] corresponding to the environment variable METHOD
    """

    if not METHOD:
        raise AppError("The environment variable 'METHOD' is not defined")

    return HTTPSealAPI if METHOD == MethodTypes.API.name else AutomationSealAPI


def validate_range_start_end(start: int, end: int | None = None):
    """
    Validate if the start and the end, are valid to create a range
    """

    if end and end < start:
        raise ValueError("The end needs to be greater than the start")

    if end and end <= 0:
        raise ValueError("The end should be greater than '0'")

    if start <= 0:
        raise ValueError("The start should be greater than '0'")
