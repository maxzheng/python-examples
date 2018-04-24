"""
Cron Clone: Run commands at set times
=============================================================================

Like cron that runs arbitrary shell commands in scheduled time.

Example Run
-----------------------------------------------------------------------------
$ python3 examples/cron.py

Press CTRL+C to exit
11:57 AM
  Running echo Commands are run concurrently
  Running echo Cron started at this time
Commands are run concurrently
Cron started at this time
^C

References
-----------------------------------------------------------------------------
https://docs.python.org/3/library/asyncio-subprocess.html
https://docs.python.org/2/library/datetime.html#strftime-strptime-behavior

"""

import asyncio
from datetime import datetime


def main():
    schedule = {
        '6:00 AM': ['ls -l', 'pwd'],
        '7:00 PM': ['ps'],
        _current_time(): ['echo Cron started at this time',
                          'echo Commands are run concurrently'],
    }

    loop = asyncio.get_event_loop()

    try:
        loop.run_until_complete(cron(schedule))

    except KeyboardInterrupt:
        pass


async def cron(schedule):
    """
    Run the commands based on the given schedule

    :param dict schedule: Map of time to list of commands to run.
    """
    print('Press CTRL+C to exit')

    while True:
        current_time = _current_time()

        if current_time in schedule:
            print(current_time)
            await asyncio.wait([_run_command(c)
                                for c in schedule[current_time]])

        await asyncio.sleep(60)


async def _run_command(cmd):
    """ Run the given shell command """
    print('  Running', cmd)
    await asyncio.create_subprocess_shell(cmd)


def _current_time():
    """ Returns the current time in HH:MM AM/PM format. """
    return datetime.today().strftime('%I:%M %p').lstrip('0')


if __name__ == "__main__":
    main()
