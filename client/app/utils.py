from enum import Enum

from app.constants import METHOD
from app.seal_api.automation_api import AutomationSealAPI
from app.seal_api.http_api import HTTPSealAPI


class MethodTypes(Enum):
    AUTO, API = range(1, 2 + 1)


def seal_api():
    return HTTPSealAPI if METHOD == MethodTypes.API.name else AutomationSealAPI
