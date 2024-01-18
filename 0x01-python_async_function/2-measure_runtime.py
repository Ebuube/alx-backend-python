#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
import typing
import time

wait_n: typing.Callable = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measure the runtime"""
    start_time: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed: float = float((time.perf_counter() - start_time) / n)
    return elapsed
