#!/usr/bin/env python3
"""This module defines an asynchronous generator"""
import asyncio
import typing
import random


async def async_generator() -> typing.Generator[float, None, None]:
    """
    Yield random numbers
    Yields float but returns None
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
