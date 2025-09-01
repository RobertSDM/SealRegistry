import tkinter as tk
from tkinter import TclError, ttk
from tkinter import messagebox
from async_tkinter_loop import async_handler

from app.constants import INTERFACE_HEIGHT, INTERFACE_WIDTH
from app.core import register_seals, validate_seals
from app.utils import pkg_range_from_random_position, validate_range_start_end
from app.exceptions import AppError
from app.services.progressbar_service import GUIProgressbar
from app.interfaces.interface_interface import Interface


class App(tk.Tk):
    def __init__(self):
        super().__init__()


class GUI(Interface):
    def __init__(self, wind_title: str):
        # Stores all widgets in the GUI, for easy search
        self.__context = dict()
        self.app = App()

        self.app.title(wind_title)
        self.app.geometry(f"{INTERFACE_WIDTH}x{INTERFACE_HEIGHT}")

        self.create_ui()

    async def start(self, start: int, end: int | None):
        try:
            validate_range_start_end(start, end)

            if not end:
                start, end_metric = pkg_range_from_random_position(start)
            else:
                end_metric = end + 1

            not_registered = await validate_seals(
                self.find_widget("progress_bar"), start, end_metric
            )
            await register_seals(self.find_widget("progress_bar"), not_registered)
        except AppError as e:
            print(e.args[0])

    def create_ui(self):
        """
        Creates the UI
        """

        form_frame = ttk.Frame(self.app)
        self.add_widget("form_frame", form_frame)
        form_frame.pack(expand=True)

        title_label = ttk.Label(
            form_frame, text="Seal registration", font=("Arial", 12)
        )
        self.add_widget("title_label", title_label)
        title_label.pack(pady=20)

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
            try:
                await self.start(start_var.get(), end_var.get())
                messagebox.showinfo(message="All seals registered")
            except (TclError, ValueError) as e:
                messagebox.showerror(message=e.args[0])

        register_btn = ttk.Button(
            form_frame,
            text="Register Seals",
            command=async_handler(btn_handler),
        )
        self.add_widget("register_btn", register_btn)
        register_btn.pack(pady=10)

        progress_bar = GUIProgressbar(self.context, form_frame)
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

    def find_widget(self, nameid: str) -> ttk.Widget:
        """
        Find and return the widget with the [nameid], if no widget is found an error is raised

        Returns
        ---
        The found widget
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
