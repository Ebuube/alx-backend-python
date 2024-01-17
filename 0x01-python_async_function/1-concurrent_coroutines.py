#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import asyncio
import typing


wait_random: typing.Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Run these methods asynchronously

    Example
    tasks = []

    for iterations in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

        wait_list = await asyncio.gather(*tasks)
        return sorted(wait_list)
    """
    tasks: typing.List = [asyncio.create_task(wait_random(max_delay))
                          for i in range(n)]
    wait_list: typing.List = await asyncio.gather(*tasks)
    return sorted(wait_list)
