'''
@author: Solrac
'''
import pytest

#@pytest.fixture
#def input_value():
#    input = 39
#    return input

@pytest.mark.divby
def test_divisible_by_3(input_value):
    assert input_value % 3 == 0
    
@pytest.mark.divby
def test_divisible_by_6(input_value):
    assert input_value % 6 == 0