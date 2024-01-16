#!/usr/bin/env python3
"""The basics of async"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """"Wait for a random period"""
    pause = random.randint(0, max_delay)
    asyncio.sleep(pause)
    return pause
