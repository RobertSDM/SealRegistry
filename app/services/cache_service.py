import json
import os

from app.constants import CONFIG_FILE_PATH


class CacheService:
    def cache_exists() -> bool:
        """
        Returns
        ---
        A boolean value indicating if a cache file already exists
        """

        return os.path.exists(CONFIG_FILE_PATH)

    def save_cordinates(data: dict):
        """
        Saves a dictionary in cache

        Args
        ---
        data
            The dictionary to be saved in cache
        """

        with open(CONFIG_FILE_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps(data))

    def read_cordinates() -> dict:
        """
        Reads the cache file

        Returns
        ---
        The data extracted from the cache file
        """

        with open(CONFIG_FILE_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
