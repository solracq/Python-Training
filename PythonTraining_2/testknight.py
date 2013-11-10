#!/usr/bin/env python3

import unittest

from knight import Knight

class TestKnight(unittest.TestCase):
    def test_arthurs_title_is_king(self):
        k = Knight('Arthur')
        self.assertEqual(k.Title, 'King')
        
    def test_lancelots_title_is_not_king(self):
        k = Knight('Lancelot')
        self.assertNotEqual(k.Title, 'King')

if __name__ == '__main__':
    unittest.main()