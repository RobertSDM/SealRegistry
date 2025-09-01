from app.interfaces.interface_interface import Interface
from app.core import register_seals, validate_seals
from app.services.progressbar_service import CLIProgressBar
from app.utils import pkg_range_from_random_position, validate_range_start_end


class CLI(Interface):
    def __init__(self):
        pass

    async def start(self, start, end=None):
        validate_range_start_end(start, end)

        progress_bar = CLIProgressBar()

        if not end:
            start, end_metric = pkg_range_from_random_position(start)
        else:
            end_metric = end + 1

        not_registered = await validate_seals(progress_bar, start, end_metric)
        seal_error = await register_seals(progress_bar, not_registered)

        return seal_error
