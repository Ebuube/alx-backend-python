#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def safely_get_value(dct: typing.Mapping, key: typing.Any, default: typing.Optional[typing.Any] = None) -> typing.Optional[typing.Any]:
    '''Safely get a value from a mapping if it exists'''
    if key in dct:
        return dct[key]
    else:
        return default
