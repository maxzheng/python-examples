from contextlib import contextmanager
from time import time


@contextmanager
def show_duration(title, extra_newline=False):
    """
    Print how long it took in seconds for enclosed code.

    :param str title: Title for what we are measuring
    :param bool extra_newline: Add an extra newline to make things look
                               separated
    """
    start_time = time()
    yield
    duration = time() - start_time
    print(f'{title} took {duration:.2f} seconds')

    if extra_newline:
        print()
