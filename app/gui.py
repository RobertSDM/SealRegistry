from async_tkinter_loop import async_mainloop


from app.services.gui_service import InterGUI


def init_gui():
    """
    Starts the GUI
    """

    gui = InterGUI("Seals registration")

    async_mainloop(gui.app)
