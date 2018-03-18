"""
<TOPIC>
=============================================================================

Example Run
-----------------------------------------------------------------------------


References
-----------------------------------------------------------------------------

"""

import asyncio


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test())


async def test():
    print('This is a template')


if __name__ == "__main__":
    main()
