#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> None:
    """Run these methods asynchronously"""
    tasks = []

    for iterations in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

        return asyncio.gather(tasks)
