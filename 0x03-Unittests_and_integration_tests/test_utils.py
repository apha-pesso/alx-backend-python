#!/usr/bin/env python3
'''Parameterized Testing'''
from parameterized import parameterized
import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''TestAccessNestedMap Class to test access_nested_map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        '''Test if the return from access_nested_map if as expected'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
