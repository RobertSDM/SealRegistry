from typing import Generator


class CLIProgressBar:
    def plot(
        target: int,
        progress: Generator[int, None, None] | list[int] | set[int] | tuple[int],
    ):
        pass
