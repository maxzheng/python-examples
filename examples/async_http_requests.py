"""
Making HTTP requests asynchronously
=============================================================================

Asynchronous requests allows for many concurrent requests, which improves
performance and better than using threads.

Example Run
-----------------------------------------------------------------------------
$ pip install aiohttp_requests
$ python3 async_http_requests.py
Status: 200
Length: 11724
aiohttp took 0.35 seconds

Status:  200
Length:  10593
aiohttp_requests took 0.35 seconds

defaultdict(<class 'int'>, {200: 100})
100 concurrent requests took 0.54 seconds

References
-----------------------------------------------------------------------------
https://github.com/maxzheng/aiohttp-requests
"""

from collections import defaultdict

import aiohttp
from aiohttp_requests import requests
import asyncio

from utils import show_duration


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(request())


async def request():
    # Using plain aiohttp client
    with show_duration('aiohttp', extra_newline=True):
        async with aiohttp.ClientSession() as session:
            async with session.get('https://www.google.com') as response:
                content = await response.text()
                print('Status:', response.status)   # 200
                print('Length:', len(content))      # 10597

    # The above becomes a bit easier without indents using `aiohttp_requests`
    with show_duration('aiohttp_requests', extra_newline=True):
        response = await requests.get('https://www.google.com')
        content = await response.text()
        print('Status: ', response.status)          # 200
        print('Length: ', len(content))             # 10625

    # Now, let's do some concurrent requests
    with show_duration('100 concurrent requests'):
        status_count = defaultdict(int)
        get_futures = [requests.get('https://www.google.com')
                       for _ in range(1000)]
        for get_future in asyncio.as_completed(get_futures):
            response = await get_future
            status_count[response.status] += 1

        print(status_count)                         # {200: 100}

if __name__ == "__main__":
    main()
