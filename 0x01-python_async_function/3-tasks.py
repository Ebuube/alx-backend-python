#!/usr/bin/env python3
"""Tasks"""
import asyncio
import typing


wait_random: typing.Callable = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> typing.Any:
    """Return an asyncio task"""
    return asyncio.create_task(wait_random(max_delay))
