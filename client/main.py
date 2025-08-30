from sys import argv

from app.core import cli_action, interface_action
from app.utils import seal_api


def main():
    if len(argv) <= 1:
        interface_action(seal_api())
        return

    if len(argv) > 3:
        raise Exception("2 arguments are required but more were given")

    try:
        cli_action(
            seal_api(),
            int(argv[1]),
            int(argv[2]) if len(argv) == 3 else None,
        )

    except ValueError:
        print("The start or the end is not a valid number")

    print("All seals registered")


if __name__ == "__main__":
    main()
