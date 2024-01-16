#!/usr/bin/env python3
"""This module contains a type-annotated function"""
import typing


def sum_list(input_list: typing.List[float]) -> float:
    '''Return the sum of the inputs'''
    return float(sum(input_list))
