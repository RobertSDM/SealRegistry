from time import sleep
import keyboard
import pyautogui
import pyperclip

from app.schemas import Cordinate, ErrorSeal, Point
from app.services.gui_service import InterGUI
from app.utils import pkg_range_from_random_position


class Automation:
    def __init__(self, gui: InterGUI):
        self._input_time = 2

        self._gui = gui

    def get_cordinates(self) -> Cordinate | None:
        """
        Static method to calibrate the mouse's cordinates in a range

        Returns
        ---

        The collected cordinates
        """

        self._gui.message_dialog(
            f"Após clicar em OK, você terá {self._input_time} segundos para posicionar o MOUSE na posição INICIAL da resposta do MINIFRAME"
        )

        sleep(self._input_time)
        start = tuple(pyautogui.position())
        self._gui.message_dialog("Posição INICIAL coletada com sucesso")

        self._gui.message_dialog(
            f"Clique em OK, após esse passo você terá {self._input_time} segundos para posicionar o mouse na posição FINAL da resposta do MINIFRAME"
        )

        sleep(self._input_time)
        end = tuple(pyautogui.position())
        self._gui.message_dialog("Posição FINAL coletada com sucesso\n\n")

        return Cordinate(Point(x=start[0], y=start[1]), Point(x=end[0], y=end[1]))

    def read_out(self, cord: Cordinate) -> str:
        """
        Reads content at the specified range

        Returns
        ---
        What was read in the range
        """

        pyautogui.moveTo(cord.start.x, cord.start.y)
        pyautogui.mouseDown(button="left")
        pyautogui.moveTo(cord.end.x, cord.end.y)
        pyautogui.mouseUp(button="left")

        with pyautogui.hold("ctrl"):
            pyautogui.press("c")

        pyautogui.press("esc")

        return pyperclip.paste()

    def automate(
        self, cord: Cordinate, start: int, end: int | None = None
    ) -> list[int]:
        """
        Initiates the seal registration process

        Args
        ---
        seal
            The seal where the package will be inferred from

        Returns
            A list containing the seals that couldn't be registered
        """

        self._gui.message_dialog("SELECIONE A JANELA E ESPERE 5 SEGUNDOS")

        sleep(5)
        not_registered = list()

        if not end:
            start, end = pkg_range_from_random_position(start)

        for seal in range(start, end + 1):
            if keyboard.is_pressed("f7"):
                break

            pyautogui.write(str(seal))

            # Confirming
            pyautogui.press("f9")

            sleep(0.04)

            out = self.read_out(cord)

            if "ja cadastrado" not in out.lower():
                not_registered.append(ErrorSeal(seal, reason="não cadastrado"))
            elif "utilizado" in out.lower():
                not_registered.append(ErrorSeal(seal, reason="ja foi utilizado"))

        return not_registered
