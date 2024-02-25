#!/usr/bin/env python3
"""Test access_nested_map function
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A set of tests for the access_nested_map function
    """

    @parameterized.expand([
        ({"a": 1}, ["a"], 1),
        ({"a": {"b": 2}}, ["a"], {"b": 2}),
        ({"a": {"b": 2}}, ["a", "b"], 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """Ensure test satisfies the required conditions"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)
