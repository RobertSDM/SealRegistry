from async_tkinter_loop import async_mainloop


from app.services.gui_service import GUI


def init_gui():
    """
    Starts the GUI
    """

    gui = GUI("Seals Registry")

    async_mainloop(gui.app)
