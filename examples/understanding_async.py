"""
Understanding async programming
=============================================================================

Async programming is just running many things in a single loop that switches
amongst them as each explicitly yield by using `await`. An async function,
coroutine, can call a non-async function (blocking) but not the other way
around. Coroutine is short for concurrent routine based on how they run.

Example Run
-----------------------------------------------------------------------------
$ python3 understanding_async.py
<function coro_alpha at 0x10b638d90>
<coroutine object coro_alpha at 0x10b6430a0>
<Task pending coro=<coro_flasher() running at understanding_async.py:66>>
Alpha started
Beta started
!!! Flash !!!
Beta finished
Alpha finished with something from Beta: gift
All done!

References
-----------------------------------------------------------------------------
https://docs.python.org/3/library/asyncio.html
"""

import asyncio


def main():
    # Coroutines are run by a special event loop that switches amongst all
    # running coroutines
    loop = asyncio.get_event_loop()
    loop.run_until_complete(understand_async())


async def understand_async():
    """ Coroutine is declared using "async" method modifier """
    # <function coro_alpha at ...>
    print(coro_alpha)

    # Creates a coroutine object, but does not run until we yield / wait for
    # it using `await`
    alpha = coro_alpha()

    # <coroutine object coro_alpha at ...>
    print(alpha)

    # Run the coroutine as a background task
    task = asyncio.ensure_future(coro_flasher())

    # <Task pending coro=<coro_flasher() running at understanding_async.py:65
    print(task)

    # Now it starts to run
    await alpha

    print('All done!')


async def coro_alpha():
    print('Alpha started')

    ret = await coro_beta()

    print('Alpha finished with something from Beta:', ret)


async def coro_beta():
    print('Beta started')

    # Let other coroutine do work, then comes back without any delay
    await asyncio.sleep(0.002)

    print('Beta finished')

    return 'gift'


async def coro_flasher():
    await asyncio.sleep(0.001)
    print('!!! Flash !!!')


if __name__ == "__main__":
    main()
