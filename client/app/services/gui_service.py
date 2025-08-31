from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from async_tkinter_loop import async_handler

from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH, PACKAGE_SIZE
from app.core import register_action, validate_action
from app.utils import validate_range_start_end
from app.exceptions import APIError
from app.services.progressbar_service import ProgressbarFrame


@dataclass
class Position:
    padx: int = 0
    pady: int = 0
    ipadx: int = 0
    ipady: int = 0
    expand: bool = False
    side: str = "top"


class App(tk.Tk):
    def __init__(self):
        super().__init__()


class GUI:
    def __init__(self, wind_title: str):
        # Stores all widgets in the GUI, for easy search
        self.__context = dict()
        self.app = App()

        self.app.title(wind_title)
        self.app.geometry(f"{INTERFACE_WIDTH}x{INTERFACE_HEIGHT}")

        self.create_ui()

    async def seal_registry_btn(self, start: int, end: int | None):
        try:
            validate_range_start_end(start, end)

            end_metric = end + 1 if end else start + PACKAGE_SIZE

            not_registered = await validate_action(
                self.context["progress_bar"], start, end_metric
            )
            await register_action(self.context["progress_bar"], not_registered)
        except APIError as e:
            print(e.args[0])
        except ValueError as e:
            print(e.args[0])

    def create_ui(self):
        form_frame = ttk.Frame(self.app)
        self.add_widget("form_frame", form_frame)
        form_frame.pack(expand=True)

        title_label = ttk.Label(form_frame, text="Seal Registry")
        self.add_widget("title_label", title_label)
        title_label.pack()

        field1 = ttk.Frame(form_frame)
        field2 = ttk.Frame(form_frame)

        self.add_widget("start_field", field1)
        self.add_widget("end_field", field2)

        field1.pack(pady=10)
        field2.pack()

        start_var = tk.IntVar()
        end_var = tk.IntVar()

        start_label = ttk.Label(field1, text="Start: ")
        end_label = ttk.Label(field2, text="End: ")

        self.add_widget("start_label", start_label)
        self.add_widget("end_label", end_label)

        start_label.pack(side="left")
        end_label.pack(side="left")

        start_entry = ttk.Entry(field1, textvariable=start_var)
        end_entry = ttk.Entry(field2, textvariable=end_var)

        self.add_widget("start_entry", start_entry)
        self.add_widget("end_entry", end_entry)

        start_entry.pack(side="right")
        end_entry.pack(side="right")

        async def btn_handler():
            await self.seal_registry_btn(start_var.get(), end_var.get())
            messagebox.showinfo(message="All seals registered")

        register_btn = ttk.Button(
            form_frame,
            text="Register Seals",
            command=async_handler(btn_handler),
        )
        self.add_widget("register_btn", register_btn)
        register_btn.pack(pady=10)

        progress_bar = ProgressbarFrame(self.context, form_frame)
        self.add_widget("progress_bar", progress_bar)

    def add_widget(self, id: str, widget: ttk.Widget):
        """
        Add the widget to the context, with an id name

        Args
        ---
        name
            The name id for the widget in the GUI
        widget
            The widget element, to store on the context
        """

        self.__context[id] = widget

    def find_widget(self, nameid: str):
        """
        Find and return the widget with the [nameid], if no widget is found an error is raised
        """

        widget = self.context.get(nameid, None)
        if not widget:
            raise Exception(f"The widget '{nameid}' is not in the context")

        return widget

        """
        The function to handle all ttk classes and styles
        """

        self.style = ttk.Style()

    @property
    def context(self):
        return self.__context
