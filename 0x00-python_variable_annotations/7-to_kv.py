#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    '''Return a string and the square of the numerical argument'''
    return (k, v * v)
