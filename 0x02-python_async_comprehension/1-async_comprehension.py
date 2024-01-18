#!/usr/bin/env python3
"""Asynchronous comprehension"""
import typing


async_generator: typing.Callable = \
        __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Return a list of 10 random numbers
    """
    return [i async for i in async_generator()]
