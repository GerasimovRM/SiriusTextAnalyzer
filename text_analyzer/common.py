import time
from typing import Callable


def status_time(func: Callable) -> Callable:
    """
    Decorator for displaying working time

    :param func: Function for decorate
    :return: Decorated function
    """
    def func_with_status_time(*args, **kwargs):
        print(f">>> Function {func.__name__} from {func.__module__} is STARTING")
        start_time = time.clock()
        result = func(*args, **kwargs)
        finish_time = time.clock()
        print(f"<<< Function {func.__name__} from {func.__module__} is FINISHING in {finish_time - start_time} sec")
        return result
    return func_with_status_time
