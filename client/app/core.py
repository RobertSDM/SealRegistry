from app.constants import PACKAGE_SIZE
from app.utils import seal_api
from app.interfaces.progressbar_interface import ProgressbarInterface


async def validate_seals(
    progress_bar: ProgressbarInterface, start: int, end: int
) -> list[int]:
    """
    Validade the seals calling the [SealAPI.validate] method

    Args
    ---
    progress_bar
        A class that extends [ProgressbarInterface]. The [ProgressbarInterface.plot] method is called every interation to update the progress
    start:
        The range's start
    end:
        The range's end

    Returns
    ---
    The not registered seals
    """

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


async def register_seals(
    progress_bar: ProgressbarInterface, seals: list[int]
) -> list[int]:
    """
    Validade the seals calling the [SealAPI.validate] method

    Args
    ---
    progress_bar
        A class that extends [ProgressbarInterface]. The [ProgressbarInterface.plot] method is called every interation to update the progress
    seals
        The seals to be registered

    Returns
    ---
    The seals that could not be registered
    """

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
