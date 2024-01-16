#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def sum_mixed_list(mxd_list: typing.List[typing.Union[int, float]]) -> float:
    '''Return the sum of the arguments'''
    return float(sum(mxd_list))
