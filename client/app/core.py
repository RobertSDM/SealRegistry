import tkinter as tk

from app.exceptions import APIError
from app.services.progressbar_service import CLIProgressBar, InterfaceProgressBar
from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH, PACKAGE_SIZE
from app.utils import seal_api, validate_range_start_end
from app.services.progressbar_interface import Progressbar


def check_action(progress_bar: Progressbar, start: int, end: int) -> list[int]:
    not_registered = list()

    for seal in range(start, end):
        if not seal_api().check(seal):
            not_registered.append(seal)

        progress_bar.plot(
            end - start if end else PACKAGE_SIZE,
            seal - start + 1,
            seal == end - 1,
        )


def register_action(progress_bar: Progressbar, seals: list[int]) -> list[int]:
    seal_error = list()

    for i, seal in enumerate(seals):
        if not seal_api().register(seal):
            seal_error.append(seal)

        progress_bar.plot(
            len(seals) - 1,
            i + 1,
            i == len(seals) - 1,
        )

    return seal_error


def cli_action(start: str, end: str | None = None) -> list[int]:
    try:
        start = int(start)
        end = int(end)

        validate_range_start_end(start, end)

        end_metric = end + 1 if end else start + PACKAGE_SIZE

        not_registered = check_action(CLIProgressBar, start, end_metric)
        seal_error = register_action(CLIProgressBar, not_registered)

        return seal_error
    except APIError as e:
        print(e.args[0])
    except ValueError:
        print("The start or the end is not a valid number")


def interface_action(start: str, end: str | None):
    try:
        start = int(start)
        end = int(end)

        validate_range_start_end(start, end)

        end_metric = end + 1 if end else start + PACKAGE_SIZE

        not_registered = check_action(InterfaceProgressBar, start, end_metric)
        register_action(InterfaceProgressBar, not_registered)
    except APIError as e:
        print(e.args[0])
    except ValueError:
        print("The start or the end is not a valid number")


def interface_create():
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
        command=lambda: interface_action(start_input.get(), end_input.get()),
    )
    action_btn.pack()

    root.mainloop()
