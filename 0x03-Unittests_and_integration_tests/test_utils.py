#!/usr/bin/env python3
"""Test access_nested_map function
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


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

    @parameterized.expand([
        ({}, ['a'], None),
        ({"a": 1}, ["a", "b"], None)
    ])
    def test_access_nested_map_exception(self, nested_map,
                                         path, expected_result):
        """Ensure expection is raised"""
        with self.assertRaises(KeyError) as context:
            result = access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """A set of tests for the get_json function
    """

    @parameterized.expand([
        ('http://example.com', {'payload': True}),
        ('http://holberton.io', {'payload': False})
    ])
    @patch('requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Ensure test works with mock"""
        # Create a mock object for the response
        mock_response = Mock()

        # Set the json method of the Mock response to return the test_payload
        mock_response.json.return_value = test_payload

        # Set the return value of the patched requests.get to the Mock response
        mock_get.return_value = mock_response

        # Call the get_json function with the test_url
        result = get_json(test_url)

        # Assert the requests.get was called with the correct URL once
        mock_get.assert_called_once_with(test_url)

        # Assert the result matches the test_payload
        self.assertEqual(result, test_payload)


class TestMemoize(unittest.TestCase):
    """A set of tests for the memoize decorator
    """

    def test_memoize(self):
        """Test the memoize decorator
        """
        class TestClass:
            """Test method for the decorator
            """

            def a_method(self):
                """Return 42
                """
                return 42

            @memoize
            def a_property(self):
                """A memoized version of a_method
                """
                return self.a_method()

        with patch.object(TestClass, 'a_method',
                          return_value=lambda: 42) as memoized_func:
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            memoized_func.assert_called_once()
