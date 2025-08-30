from sys import argv
import requests

from .constants import API_ENDPOINT


def check_seals(start: int, end: int) -> list[str]:
    """
    Receives a range to interate and check the seals

    Args
    ---
    start
        The start of the range
    end
        The end of the range, defaults to "None"
    """

    if end < start:
        raise Exception("The end needs to be greater than the start")

    not_registered = list()

    for i in range(start, end + 1):
        resp = requests.get(API_ENDPOINT + f"/transport/seal/check?seal={i}")
        if resp.status_code == 404:
            not_registered.append(i)

    return not_registered


def register_seals(seals: list[str]):
    for seal in seals:
        resp = requests.post(API_ENDPOINT + f"/transport/seal/register?seal={seal}")

        if not resp.ok:
            print(resp.text)


def main():
    if len(argv) == 3:
        seals = check_seals(int(argv[1]), int(argv[2]))
        register_seals(seals)
    else:
        raise Exception("You should provide the start and the end for the seals range")


if __name__ == "__main__":
    main()
