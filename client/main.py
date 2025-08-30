from sys import argv

from app.core import cli_action, interface_create


def main():
    if len(argv) <= 1:
        interface_create()
        return
    elif len(argv) > 3:
        raise Exception("2 arguments are required but more were given")

    cli_action(
        argv[1],
        argv[2] if len(argv) == 3 else None,
    )

    print("All seals registered")


if __name__ == "__main__":
    main()
