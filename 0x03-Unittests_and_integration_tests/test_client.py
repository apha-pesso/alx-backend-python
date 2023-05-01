#!/usr/bin/env python3
'''Client test'''
from parameterized import parameterized
from client import GithubOrgClient
from unittest.mock import patch
import unittest


class TestGithubOrgClient(unittest.TestCase):
    '''TEsting GithubOrg'''
    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": True})])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, url_ext, expected, get_json_patch):
        '''Test method'''
        test_org = GithubOrgClient(url_ext)
        url = f"https://api.github.com/orgs/{url_ext}"

        # get_json_patch.return_value = expected

        # self.assertEqual(test_org.org, expected)
        self.assertEqual(test_org.org, get_json_patch.return_value)
        get_json_patch.assert_called_once

        # expected = requests.get(url).json()
        # self.assertEqual(test_org.org(), expected)
