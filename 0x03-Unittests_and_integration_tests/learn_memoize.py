#!/usr/bin/env python3
"""Memoize - remember
"""
import functools


# Define a memoization decorator
def memoize(func):
    """Decorator for memoized function
    """
    cache = {}

    @functools.wraps(func)
    def memoized_func(*args):
        """Actual execution script for memoized function
        """
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return memoized_func


# Using memoize to optimize a function
@memoize
def fibonacci(n):
    """Return the fibonacci value of a number
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return fibonacci(n - 1) * n

# Example
print("Fibonacci series")
for n in range(0, 1000):
    print("{}! = {}".format(n, fibonacci(n)))
