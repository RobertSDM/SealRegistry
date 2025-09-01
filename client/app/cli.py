import asyncio
from sys import argv

from app.services.cli_service import CLI


def init_cli(args: list[str]):
    """
    Starts the CLI
    """

    start = int(args[1])
    end = int(args[2]) if len(argv) >= 3 else None

    cli = CLI()

    asyncio.run(cli.start(start, end))
    print("All seals registered")
