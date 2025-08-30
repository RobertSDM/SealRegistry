import tkinter as tk

from app.exceptions import APIError
from app.seal_api.interface import SealAPI
from app.services.progressbar_service import CLIProgressBar
from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH


def check_not_valid_seals(
    seal_api: SealAPI, start: int, end: int | None = None
) -> list[int]:
    not_registered = list()
    pkg_size = 100

    try:

        end_metric = end + 1 if end else start + pkg_size
        for seal in range(start, end_metric):
            if not seal_api.check(seal):
                not_registered.append(seal)

            CLIProgressBar.plot(
                end - start if end else pkg_size,
                seal - start,
                seal == end_metric - 1,
            )

    except APIError as e:
        print(e.args[0])

    return not_registered


def cli_action(seal_api: SealAPI, start: int, end: int | None = None) -> list[int]:
    if end:
        if end < start:
            raise Exception("The end needs to be greater than the start")

        if end <= 0:
            raise Exception("The end should be greater than '0'")

    if start <= 0:
        raise Exception("The start should be greater than '0'")

    not_registered = check_not_valid_seals(seal_api, start, end)
    seal_error = list()

    for i, seal in enumerate(not_registered):
        if not seal_api.register(seal):
            seal_error.append(seal)

        CLIProgressBar.plot(
            len(not_registered) - 1,
            i + 1,
            i == len(not_registered) - 1,
        )

    return seal_error


def register_button(seal_api: SealAPI, start: str, end: str):
    try:
        start = int(start)
        end = int(end)

        if end and end < start:
            raise Exception("The end needs to be greater than the start")

        if end <= 0:
            raise Exception("The end should be greater than '0'")

        if start <= 0:
            raise Exception("The start should be greater than '0'")

        not_registered = check_not_valid_seals(seal_api, start, end)
        seal_error = list()

        for i, seal in enumerate(not_registered):
            if not seal_api.register(seal):
                seal_error.append(seal)

            CLIProgressBar.plot(
                len(not_registered) - 1,
                i + 1,
                i == len(not_registered) - 1,
            )

    except ValueError:
        print("The start or the end is not a valid number")


def interface_action(seal_api: SealAPI):
    root = tk.Tk()
    root.title = "Seal Registry"
    root.geometry(f"{INTERFACE_WIDTH}x{INTERFACE_HEIGHT}")

    label = tk.Label(root, text="Start: ")
    label.pack()

    start_input = tk.Entry(root)
    start_input.pack()

    label = tk.Label(root, text="End: ")
    label.pack()

    end_input = tk.Entry(root)
    end_input.pack()

    action_btn = tk.Button(
        root,
        text="Register Seals",
        command=lambda: register_button(seal_api, start_input.get(), end_input.get()),
    )
    action_btn.pack()

    root.mainloop()
