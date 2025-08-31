from app.exceptions import APIError
from app.services.progressbar_service import CLIProgressBar
from app.constants import PACKAGE_SIZE
from app.utils import seal_api, validate_range_start_end
from app.interfaces.progressbar_interface import ProgressbarInterface


async def validate_action(
    progress_bar: ProgressbarInterface, start: int, end: int
) -> list[int]:
    not_registered = list()

    for seal in range(start, end):
        if not await seal_api().validate(seal):
            not_registered.append(seal)

        progress_bar.plot(
            end - start if end else PACKAGE_SIZE,
            seal - start + 1,
            "Validating the seals",
            seal == end - 1,
        )

    return not_registered


async def register_action(
    progress_bar: ProgressbarInterface, seals: list[int]
) -> list[int]:
    seal_error = list()

    for i, seal in enumerate(seals):
        if not await seal_api().register(seal):
            seal_error.append(seal)

        progress_bar.plot(
            len(seals) - 1,
            i + 1,
            "Registering the seals",
            i == len(seals) - 1,
        )

    return seal_error


async def cli_action(start: str, end: str | None = None) -> list[int]:
    try:
        start = int(start)
        end = int(end)

        progress_bar = CLIProgressBar()

        validate_range_start_end(start, end)

        end_metric = end + 1 if end else start + PACKAGE_SIZE

        not_registered = await validate_action(progress_bar, start, end_metric)
        seal_error = await register_action(progress_bar, not_registered)

        return seal_error
    except APIError as e:
        print(e.args[0])
    except ValueError:
        print("The start or the end is not a valid number")
