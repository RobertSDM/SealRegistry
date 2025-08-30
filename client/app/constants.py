from math import floor
import os
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = os.getenv("API_ENDPOINT")
METHOD = os.getenv("METHOD")


WINDOW_RATIO = 9 / 16
INTERFACE_WIDTH = 800
INTERFACE_HEIGHT = floor(INTERFACE_WIDTH * WINDOW_RATIO)

PACKAGE_SIZE = 100
