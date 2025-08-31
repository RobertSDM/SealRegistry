import asyncio
from sys import argv

from app.core import cli_action


def init_cli(args: list[str]):
    start = int(args[1])
    end = int(args[2]) if len(argv) >= 3 else None

    asyncio.run(cli_action(start, end))
    print("All seals registered")
