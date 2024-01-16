#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def element_length(lst: typing.Iterable[typing.Sequence]) \
        -> typing.List[typing.Tuple[typing.Sequence, int]]:
    '''Return each iterable as well as its length in a list of tuples'''
    return [(i, len(i)) for i in lst]
