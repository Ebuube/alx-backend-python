#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
import typing


async_comprehension: typing.Callable = \
        __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Return the run time for four parallel comprehensions
    """
    tasks: typing.List = []
    for i in range(4):
        tasks.append(asyncio.create_task(async_comprehension()))

    start_time: float = time.perf_counter()
    await asyncio.gather(*tasks)
    elapsed: float = time.perf_counter() - start_time
    return elapsed
