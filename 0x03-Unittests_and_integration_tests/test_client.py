#!/usr/bin/env python3
"""Test GithubOrgClient
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch
from utils import get_json
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """A set of tests for the Github org client
    """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Ensure it can access an organization
        """
        # Create a mock object for the response
        mock_response = Mock()

        # Set the json method of the Mock response to return the payload
        mock_response.json.return_value = {'payload': True}

        # set the return value
        mock_get_json.return_value = mock_response

        # Retrieve the org property
        cli = GithubOrgClient(org_name)

        org = cli.org
        mock_get_json.assert_called_once_with(
                f'https://api.github.com/orgs/{org_name}')
