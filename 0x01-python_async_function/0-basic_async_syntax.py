#!/usr/bin/env python3
"""
This module is an async function with default val
"""

import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    """
    async func that waits for a random delay btw 0 
    and max_delay
    """
    delay: float = random.uniform(0, max_delay)

    await asyncio.sleep(delay)

    return delay
