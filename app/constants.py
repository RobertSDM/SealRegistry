from math import floor

from dotenv import load_dotenv
import pyautogui

load_dotenv()

WINDOW_RATIO = 9 / 16
INTERFACE_WIDTH = 400
INTERFACE_HEIGHT = floor(INTERFACE_WIDTH * WINDOW_RATIO)

PACKAGE_SIZE = 100

APP_TITLE = "Cadastramento de Lacres"

CONFIG_FILE_PATH = "config.json"

pyautogui.PAUSE = 0.03

