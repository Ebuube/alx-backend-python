#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    '''Return the first element of the sequence if any'''
    if lst:
        return lst[0]
    else:
        return None
