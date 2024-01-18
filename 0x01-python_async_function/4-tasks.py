#!/usr/bin/env python3
"""Tasks: creating tasks"""
import asyncio
import typing


wait_random: typing.Callable = __import__('0-basic_async_syntax').wait_random
task_wait_random: typing.Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> typing.List[float]:
    """
    Run these methods asynchronously

    Example
    tasks = []

    for iterations in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))

        wait_list = await asyncio.gather(*tasks)
        return sorted(wait_list)
    """
    tasks: typing.List = [task_wait_random(max_delay)
                          for i in range(n)]
    wait_list: typing.List = await asyncio.gather(*tasks)
    return sorted(wait_list)
