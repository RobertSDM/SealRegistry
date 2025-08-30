from app.services.progressbar_interface import Progressbar


class InterfaceProgressBar(Progressbar):
    def plot(target: int, current: int, done: bool):
        pass


class CLIProgressBar(Progressbar):
    @staticmethod
    def plot(target: int, current: int, done: bool):
        bar_size = 50
        percent_progress = current * 100 // target
        bar_size_percent = bar_size * percent_progress // 100

        bar = "["

        for _ in range(bar_size_percent):
            bar += "█"

        for _ in range(bar_size_percent, bar_size):
            bar += " "

        bar += "]"

        if done:
            print(" " * (len(bar) + 10), end="\r")
            return

        print(bar + f" ({percent_progress}%) {current}/{target}", end="\r")
