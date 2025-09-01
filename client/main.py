from sys import argv

from app.cli import init_cli
from app.gui import init_gui
from app.repository.automation_api import Automation


def main():
    if "--auto" in argv:
        cord = Automation.get_cordinates()
        auto = Automation(cord)

        auto.automate([int(seal) for seal in argv[1:] if not seal.startswith("-")])

    # if len(argv) <= 1:
    #     init_gui()
    # else:
    #     init_cli(argv)


if __name__ == "__main__":
    main()
