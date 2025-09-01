from tkinter import ttk
from typing import Any

from app.interfaces.progressbar_interface import ProgressbarInterface


class GUIProgressbar(ttk.Frame, ProgressbarInterface):
    def __init__(self, context: dict, master: Any):
        super().__init__(master)

        self.progress_bar = ttk.Progressbar(self)
        context["progress_bar"] = self.progress_bar
        self.progress_bar.pack()

        self.label = ttk.Label(self)
        context["progress_bar-label"] = self.label
        self.label.pack()

        self.progress_bar.configure(length=200, value=0)

    def plot(self, target: int, current: int, title: str, done: bool):
        self.pack()

        percent_progress = current * 100 // target

        self.label.configure(text=title + f" - ({percent_progress})%")

        if done:
            self.pack_forget()
            return

        self.progress_bar.configure(value=percent_progress)


class CLIProgressBar(ProgressbarInterface):
    def plot(self, target: int, current: int, title: str, done: bool):
        bar_size = 30
        percent_progress = current * 100 // target
        bar_size_percent = bar_size * percent_progress // 100

        max_title_size = 30

        bar = (
            f"{title[:max_title_size]}{'...'if len(title) > max_title_size else ""} - ["
        )

        for _ in range(bar_size_percent):
            bar += "█"

        for _ in range(bar_size_percent, bar_size):
            bar += " "

        bar += "]"

        if done:
            print(" " * (len(bar) + 50), end="\r")
            return

        print(bar + f" ({percent_progress}%) {current}/{target}", end="\r")
