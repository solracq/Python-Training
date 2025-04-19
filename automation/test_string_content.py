'''
@author: Solrac
'''
import unittest
import pytest

class TestClass:
    def test_one(self):
        s = "this"
        assert 'h' in s
        
    def test_two(self):
        s = 'hello'
        assert hasattr(s, 'hello')