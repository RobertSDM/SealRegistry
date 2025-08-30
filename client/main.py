from sys import argv

from app.core import cli_action, interface_action
from app.utils import seal_api

def main():
    if len(argv) <= 1:
        interface_action()
        return

    try:
        if len(argv) == 3:
            cli_action(
                seal_api(),
                int(argv[1]),
                int(argv[2]),
            )
        elif len(argv) == 2:
            cli_action(seal_api(), int(argv[1]))

    except ValueError:
        print("The start is not a valid number")

    print("All seals registered")


if __name__ == "__main__":
    main()
