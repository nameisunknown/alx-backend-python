#!/usr/bin/env python3
"""This is a wait_n module that executes multiple caroutine"""

import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    this function takes in 2 int argument
    spawns the wait_random at an n time and
    returns a list of all the delays, which 
    should be in ascending order
    """

    todo = [wait_random(max_delay) for _ in range(n)]
    delay = [await delay for delay in asyncio.as_completed(todo)]
    return delay

