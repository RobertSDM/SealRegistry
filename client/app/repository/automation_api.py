from dataclasses import dataclass
from time import sleep
import pyautogui
import pyperclip

from app.utils import pkg_range_from_random_position


@dataclass
class Cordinate:
    start: tuple[int, int]
    end: tuple[int, int]


class Automation:
    def __init__(self, out_cord: Cordinate):
        self.__success_msg = "ja cadastrado"

        self.__out_cord = out_cord

    def get_cordinates() -> Cordinate:
        """
        Static method to calibrate the mouse's cordinates in a range

        Returns
        ---

        The collected cordinates
        """

        print("Get the mouse into the start position, in 5 seconds")

        sleep(5)
        start = tuple(pyautogui.position())
        print("Start position collected successfully")

        print("\nGet the mouse into the end position")
        sleep(5)
        end = tuple(pyautogui.position())
        print("End position collected successfully")

        return Cordinate(start, end)

    def __clean_input(self):
        """
        Cleans the seal text on the input
        """

        with pyautogui.hold("ctrl"):
            pyautogui.press("end")

    def read_out(self) -> str:
        """
        Reads content at the specified range

        Returns
        ---
        What was read in the range
        """

        with pyautogui.hold("shift"):
            pyautogui.mouseDown(self.__out_cord.start[0], self.__out_cord.start[1])
            pyautogui.mouseUp(self.__out_cord.end[0], self.__out_cord.end[1])

        with pyautogui.hold("ctrl"):
            pyautogui.press("c")

        return pyperclip.paste()

    def automate(self, seals: tuple[int, int]) -> list[int]:
        """
        Initiates the seal registration process

        Args
        ---
        seal
            The seal where the package will be inferred from

        Returns
            A list containing the seals that couldn't be registered
        """

        print("SELECT THE WINDOW! in 5 seconds")
        sleep(5)

        not_registered = list()

        if len(seals) == 1:
            start, end = pkg_range_from_random_position(seals[0])
        else:
            start, end = seals[0], seals[1]

        for seals in range(start, end + 1):
            self.__clean_input()

            pyautogui.write(str(seals))
            pyautogui.press("f9")

            out = self.read_out()

            if self.__success_msg not in out.lower() and str(seals) not in out:
                not_registered.append(seals)

            sleep(1)

        return not_registered
