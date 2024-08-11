#!/usr/bin/env python3
"""This module contains task_wait_random() function (Coroutine)"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Returns a asyncio.Task"""
    return asyncio.create_task(wait_random(max_delay))

