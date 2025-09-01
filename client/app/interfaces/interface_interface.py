from abc import ABC


class Interface(ABC):
    async def start(self, start: int, end: int | None = None):
        """
        Starts the seal register process

        Args
        ---
        start
            The range's start
        end
            The range's end
        """

        pass
