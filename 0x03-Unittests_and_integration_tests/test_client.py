#!/usr/bin/env python3
"""Test GithubOrgClient
"""
import unittest
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock
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

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    def test_public_repos_url(self, org_name):
        """Ensure we can set the repos url
        """
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            url_fmt = 'https://api.github.com/orgs/{}/repos'
            mock_org.return_value = {
                    'payload': True,
                    'repos_url': url_fmt.format(org_name)
            }

            # Test the org property
            cli = GithubOrgClient(org_name)
            result = cli._public_repos_url

            self.assertEqual(result, mock_org()['repos_url'])

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_public_repos(self, org_name, mock_get_json):
        """Ensure client can access repos
        """
        # Create a mock object for the response
        mock_response = Mock()

        # Set the json method of the mock response to return the payload
        payload = {
                'repos_url': f"https://api.github.com/orgs/{org_name}/repos",
                'repos': [
                    {'name': 'WebNex'},
                    {'name': 'Envatim'},
                    {'name': 'Migo'}
                ]
        }
        mock_get_json.return_value = payload['repos']

        # Set the return value
        mock_get_json.return_value = mock_response

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_pru:
            mock_pru.return_value = payload['repos_url']

            # Test the public_repos method
            cli = GithubOrgClient(org_name)
            result = cli.public_repos()
            print(result)

            self.assertEqual(result, payload['repos'])

            mock_pru.assert_called_once()
        mock_get_json.assert_called_once()
