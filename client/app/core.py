from app.exceptions import APIError
from app.seal_api.interface import SealAPI


def check_not_valid_seals(
    seal_api: SealAPI, start: int, end: int | None = None
) -> list[int]:
    not_registered = list()
    pkg_size = 100

    try:

        for seal in range(start, end + 1 if end else start + pkg_size):
            if not seal_api.check(seal):
                not_registered.append(seal)

    except APIError as e:
        print(e.args[0])

    return not_registered


def cli_action(seal_api: SealAPI, start: int, end: int | None = None) -> list[int]:
    if end:
        if end < start:
            raise Exception("The end needs to be greater than the start")

        if end <= 0:
            raise Exception("The end should be greater than '0'")

    if start <= 0:
        raise Exception("The start should be greater than '0'")

    not_registered = check_not_valid_seals(seal_api, start, end)
    seal_error = list()

    for seal in not_registered:
        if not seal_api.register(seal):
            seal_error.append(seal)

    return seal_error


def interface_action():
    pass
