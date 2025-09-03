from email import message
from enum import Enum
import tkinter as tk
from tkinter import IntVar, TclError, ttk
from tkinter.messagebox import askyesno, showerror, showinfo, askokcancel
from tkinter.simpledialog import askinteger
from typing import Literal

from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH


class MsgDialogType(Enum):
    INFO, ERROR = range(1, 3)


class InterGUI:
    def __init__(self, title):
        self._title = title

    def confirm_dialog(self, msg: str, type: Literal["ok", "yesno"] = "ok") -> bool:
        if type == "ok":
            return askokcancel(self._title, msg)
        else:
            return askyesno(self._title, msg)

    def message_dialog(self, msg: str, type: Literal["error", "info"] = "info"):

        if type == "info":
            showinfo(self._title, msg)
        else:
            showerror(self._title, msg)

    def list_dialog(self, msg: str, list_: list):
        root = tk.Tk()

        root.title(self._title)
        root.geometry(f"{INTERFACE_WIDTH}x{INTERFACE_HEIGHT}")

        main = ttk.Frame(root)

        label = ttk.Label(main, text=msg)
        listbox = tk.Listbox(main)

        for i, text in enumerate(list_):
            listbox.insert(i + 1, text)

        label.pack()
        listbox.pack()

        main.pack(expand=True)

        root.mainloop()

    def int_input_dialog(self, msg: str) -> int | None:
        return askinteger(self._title, msg, initialvalue=0)
