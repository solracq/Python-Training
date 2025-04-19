'''
@author: Solrac
'''
import pytest

@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11*num == output

@pytest.mark.multiplicacion
@pytest.mark.parametrize("a, b, c",[(2,3,6),(5,5,25),(3,6,12)])
def test_multiplication(a, b, c):    
    assert multiplication(a, b) == c

def multiplication(a, b):
    mult = 0
    if abs(a) != 0 or abs(b) != 0:
        if abs(a) < abs(b):
            for i in range(abs(a)):
                mult += abs(b)
        else:
            for i in range(abs(b)):
                mult += abs(a)
        return mult
    else:
        return 0