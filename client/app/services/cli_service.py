from app.interfaces.interface_interface import Interface
from app.core import register_seals, validate_seals
from app.services.progressbar_service import CLIProgressBar
from app.utils import validate_range_start_end
from app.constants import PACKAGE_SIZE


class CLI(Interface):
    def __init__(self):
        pass

    async def start(self, start, end=None):
            validate_range_start_end(start, end)

            progress_bar = CLIProgressBar()

            end_metric = end + 1 if end else start + PACKAGE_SIZE

            not_registered = await validate_seals(progress_bar, start, end_metric)
            seal_error = await register_seals(progress_bar, not_registered)

            return seal_error
