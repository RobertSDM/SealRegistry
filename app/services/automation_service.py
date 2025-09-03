from dataclasses import dataclass
import json
import os
from time import sleep
import keyboard
import pyautogui
import pyperclip

from app.services.gui_service import InterGUI
from app.utils import pkg_range_from_random_position


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Cordinate:
    start: Point
    end: Point


class Automation:
    def __init__(self, gui: InterGUI):
        self._msgs = {
            "sucesso": "ja cadastrado",
            "disponivel": "disponível",
        }

        self._input_time = 2

        self._gui = gui

    def get_cordinates(self) -> Cordinate | None:
        """
        Static method to calibrate the mouse's cordinates in a range

        Returns
        ---

        The collected cordinates
        """

        if not self._gui.confirm_dialog(
            f"Após clicar em OK, você terá {self._input_time} segundos para posicionar o MOUSE na posição INICIAL da resposta do MINIFRAME"
        ):
            return None

        sleep(self._input_time)
        start = tuple(pyautogui.position())
        self._gui.message_dialog("Posição INICIAL coletada com sucesso")

        if not self._gui.confirm_dialog(
            f"Clique em OK, após esse passo você terá {self._input_time} segundos para posicionar o mouse na posição FINAL da resposta do MINIFRAME"
        ):
            return None

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

        pyautogui.click(cord.start.x, cord.start.y)
        with pyautogui.hold("shift"):
            pyautogui.click(cord.end.x, cord.end.y)

        with pyautogui.hold("ctrl"):
            pyautogui.press("c")

        pyautogui.press("esc")

        return pyperclip.paste()

    def save_cordinates(self, cord: Cordinate):
        """
        Saves the cordinates into a cache file

        Args
        ---
        cord
            The cordinate instance to be saved in cache
        """
        
        with open("cache.json", "w", encoding="utf-8") as f:
            f.write(
                json.dumps(
                    {
                        "start": {"x": cord.start.x, "y": cord.start.y},
                        "end": {"x": cord.end.x, "y": cord.end.y},
                    }
                ),
            )

    def read_cordinates(self) -> Cordinate:
        """
        Reads the cache file

        Returns
        ---
        The cordinates extracted from the cache file
        """
        
        with open("cache.json", "r", encoding="utf-8") as f:
            jcord = json.load(f)

            return Cordinate(
                start=Point(
                    x=jcord["start"]["x"],
                    y=jcord["start"]["y"],
                ),
                end=Point(
                    x=jcord["end"]["x"],
                    y=jcord["end"]["y"],
                ),
            )

    def cache_exists(self) -> bool:
        """
        Returns
        ---
        A boolean value indicating if a cache file already exists
        """

        return os.path.exists("cache.json")

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

        if not self._gui.confirm_dialog("SELECIONE A JANELA E ESPERE 5 SEGUNDOS"):
            return []

        sleep(5)
        not_registered = list()

        if not end:
            start, end = pkg_range_from_random_position(start)

        for seal in range(start, end + 1):
            if keyboard.is_pressed("f7"):
                break

            pyautogui.write(str(seal))

            # Comfirming
            pyautogui.press("f9")

            sleep(0.02)

            out = self.read_out(cord)

            if self._msgs["sucesso"] not in out or self._msgs["disponivel"] not in out:
                not_registered.append(seal)
            
        return not_registered
