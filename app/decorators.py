import time
from typing import Callable


def timer(minus: int = 0):
    def deco(func: Callable):
        def wrapper(self, *args, **kwargs):
            start = time.perf_counter()
            res = func(self, *args, **kwargs)
            print(
                f"A função demorou {((time.perf_counter() - start - minus)/1000):.3f}s"
            )
            return res

        return wrapper

    return deco
