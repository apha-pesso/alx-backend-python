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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        '''Test if the return from access_nested_map if as expected'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)
