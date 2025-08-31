from sys import argv

from app.cli import init_cli
from app.gui import init_gui


def main():
    if len(argv) <= 1:
        init_gui()
    else:
        init_cli(argv)


if __name__ == "__main__":
    main()
