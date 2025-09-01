from abc import ABC, abstractmethod


class ProgressbarInterface(ABC):
    @abstractmethod
    def plot(self, target: int, current: int, title: str, done: bool):
        """
        Updates the progress in the progress bar

        Args
        ---
        target
            The progress bar limit
        current
            The current progress
        title
            Name for the progress bar
        done
            Boolean value to identify if the progress is finished
        """
        
        pass
