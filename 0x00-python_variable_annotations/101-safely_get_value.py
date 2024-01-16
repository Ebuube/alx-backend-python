#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


T = typing.TypeVar('T')

def safely_get_value(dct: typing.Mapping, key: typing.Any, default: typing.Union[T, None] = None) -> typing.Union[typing.Any, T]:
    '''Safely get a value from a mapping if it exists'''
    if key in dct:
        return dct[key]
    else:
        return default
