"""
Code Reuse using Functions
=============================================================================

For better reuse and manageability, it is good practice to put code into
small functions that do one thing well. It will be easy to change and test.

Example Run
-----------------------------------------------------------------------------
$ python3 functions.py
Gonna clean the house
Done with clean the house in 1.00 seconds
Gonna eat lunch
Done with eat lunch in 0.01 seconds
"""

# Imports the "sleep" function from "time" module (file)
from time import sleep, time


def main():
    """ This is a global function visible in this module (file) """

    def do_task(name, duration=1):
        """
        This is a nested/private function visible inside "main" only.

        :param str name: Name of the task. Positional are required.
        :param int|float duration: Number of seconds to pretend to work.
                                   Keyword args are optional.
        """
        start_time = time()

        print('Gonna', name)
        sleep(duration)  # Pretend to do work

        print('Done with', name,
              'in {:.2f} seconds'.format(time() - start_time))

    do_task('clean the house')          # We clean like Flash
    """
    Gonna clean the house
    Done with clean the house in 1.00 seconds
    """

    do_task('eat lunch', duration=0.01)  # And eat like Flash
    """
    Gonna eat lunch
    Done with eat lunch in 0.01 seconds
    """


if __name__ == "__main__":
    main()
