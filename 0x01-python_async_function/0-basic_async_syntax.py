#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """"Wait for a random period"""
    if max_delay != 0:
        pause = (random.random() * 10) % max_delay
    else:
        pause = 0
    # pause = random.uniform(0, max_delay)
    await asyncio.sleep(pause)
    return float(pause)
