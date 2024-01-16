#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    '''Return a function that multiplies a float by multiplier'''

    def multiply(n: float) -> float:
        '''Multiply a float by mulitplier'''
        return n * multiplier

    return multiply
