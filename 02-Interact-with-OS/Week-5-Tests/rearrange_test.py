#!/usr/bin/env python3

# Unit test for rearrange.py
# import the func

from rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Kennedy, John F."
        expected = "John F. Kennedy"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Dolphy"
        expected = "Dolphy"
        self.assertEqual(rearrange_name(testcase), expected)


unittest.main()
