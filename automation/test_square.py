'''
@author: Solrac
'''
import math
import pytest

def suma(a, b):
    if b == 0:
        return a
    else:
        return suma(a^b, (a&b) << 1)

@pytest.mark.xfail
@pytest.mark.square
def test_sqrt():
    num = 25
    assert math.sqrt(num) == 5

@pytest.mark.square
def testsqre():
    num = 7
    assert num**2 == 40
    
@pytest.mark.others
def tesequality():
    assert 10 == 11

@pytest.mark.cuadrado
@pytest.mark.parametrize("val, res", [(suma(3, 5), 64), (suma(8, 9), 289), (suma(3, 3), 36), (suma(7, 1), 64)])    
def test_sqr(val, res):
    assert val**2 == res 