class CLIProgressBar:
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

        print(bar + f" ({percent_progress}%)", end="\r")
