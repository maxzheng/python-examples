"""
Feature: Using asyncio to run tasks concurrently in the background

Sample output::

    $ python3 complete-python.py
    [0 running tasks]
    Running "Task 2"
    Running "Task 1"
    Running "Task 0"
    [3 running tasks]
    [2 running tasks]
    Done with Task 2 after 1 seconds!
    [1 running tasks]
    Done with Task 1 after 2 seconds!
    [0 running tasks]
    Done with Task 0 after 3 seconds!
    IDs for tasks done: 0, 1, 2
"""

# Imports are at the top, and generally have 3 groups separated by blank line: built-in, 3rd party on PyPI, and internal
import asyncio                      # Import a package
from asyncio import get_event_loop  # Import a single item from a package

# Constants are capitalized by convention
COMPLETED_TASKS_FILE = "completed_tasks.log"


class AsyncManager:
    """
    A class that demos how to run tasks concurrently using asyncio.

    .. code-block:: python

        manager = AsyncManager(3)
        asyncio.run_until_complete(manager.do_things_concurrently())
    """

    def __init__(self, tasks):
        """
        Initialize instance variables
        :param int tasks: Number of concurrent tasks to run
        """
        #: Number of tasks to run concurrently. Notice there is a colon after # to indicate this is an attribute doc
        #: This is a public attribute so use special '#:' attribute docstring marker for API doc
        self.tasks = tasks

        # Number of currently running tasks. This is just a normal comment for private stuff and not an attribute docstring.
        self._running_tasks = 0

    async def _run_background_task(self, name, delay=1):
        """
        Run a task in the background

        :param str name: Name of the task
        :param int delay: Number of seconds to wait before completing the task
        """
        self._running_tasks += 1

        print('Running "{}"'.format(name))
        await asyncio.sleep(delay)

        self._running_tasks -= 1
        return 'Done with {n} after {d} seconds!'.format(n=name, d=delay)

    async def do_things_concurrently(self):
        """ Run all tasks concurrently """
        task_ids = range(self.tasks)   # Creates a range iterator that returns a number per iteration from: 0, 1, 2
        task_futures = []

        # Run the coroutine in the background without waiting for it (like daemonize)
        show_task = asyncio.ensure_future(self._show_running_tasks())

        # Create the coroutine objects
        for task_id in task_ids:
            delay = 3 - task_id
            coro = self._run_background_task("Task " + str(task_id), delay=delay)
            task_futures.append(coro)

        # Start running all coroutines and wait for each to complete
        for future in asyncio.as_completed(task_futures):
            result = await future
            print(result)

        show_task.cancel()  # Terminate the background task

        return list(task_ids)  # Converts the range object into a normal list of ints

    async def _show_running_tasks(self):
        last_running_tasks = None

        while True:
            if last_running_tasks != self._running_tasks:
                print("[{} running tasks]".format(self._running_tasks))
                last_running_tasks = self._running_tasks

            await asyncio.sleep(0)  # Let's other coroutines do work instead of blocking


def do_things_serially():
    loop = get_event_loop()
    manager = AsyncManager(3)
    task_ids = loop.run_until_complete(manager.do_things_concurrently())

    with open(COMPLETED_TASKS_FILE, "w") as fp:
        fp.write("IDs for tasks done: {}".format(', '.join([str(i) for i in task_ids])))

    print(open(COMPLETED_TASKS_FILE).read())


if __name__ == "__main__":
    do_things_serially()
