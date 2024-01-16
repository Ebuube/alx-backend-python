#!/usr/bin/env python3
"""This module contains a type-annotated function"""


def floor(n: float) -> int:
    """Return the floor of a float"""
    floored = int(n)
    
    if floored > n:
        return floored - 1
    else:
        return floored
