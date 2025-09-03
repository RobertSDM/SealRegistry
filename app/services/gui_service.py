import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showerror, showinfo, askokcancel
from tkinter.simpledialog import askinteger
from typing import Literal

from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH
from app.schemas import ErrorSeal


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

    def list_dialog(self, msg: str, list_: list[ErrorSeal]):
        root = tk.Tk()

        root.title(self._title)
        root.geometry(f"{INTERFACE_WIDTH}x{INTERFACE_HEIGHT}")

        main = ttk.Frame(root)

        label = ttk.Label(main, text=msg)

        listbox_frame = ttk.Frame(main)
        listbox = tk.Listbox(listbox_frame, background="white", width=50)

        scrollbar = ttk.Scrollbar(listbox_frame, command=listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        listbox.config(yscrollcommand=scrollbar.set)

        for i, err in enumerate(list_):
            listbox.insert(i + 1, f"{err.seal} -> {err.reason}")

        label.pack()
        scrollbar.pack()
        listbox.pack()

        listbox_frame.pack()
        main.pack(expand=True)

        root.mainloop()

    def int_input_dialog(self, msg: str) -> int | None:
        return askinteger(self._title, msg, initialvalue=0)
