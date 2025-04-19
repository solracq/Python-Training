'''
@author: Carlos Q.
'''
import pytest
import logging

@pytest.fixture
def log():
    log = logging.getLogger(__name__)
    return log

@pytest.fixture
def setup():
    a = 5
    b = 8
    c = 3
    return [a, b, c]

def mod(a, b):
    # a/b = c  6/3=2 c*b-a
    if b != 0:
        result = abs((a//b) * b - a)
        return result
    else:
        raise Exception("No zero division!")

@pytest.mark.parametrize("a, b, result", [(6, 3, 0), (25, 5, 0), (7, 3, 1)], ids=["first", "second", "third"])
@pytest.mark.operations
def test_mod(log, a, b, result):
    log.info("Result of mod operation")
    assert mod(a, b) == result, "Wrong result!"

@pytest.mark.xfail
def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, 'Test Failed'
    assert x == y, 'Test Failed because x=' + str(x) + ' y=' + str(y)
    
@pytest.mark.set2
def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, 'Test Failed'

@pytest.mark.skip
def test_file1_method2a():
    x = 8
    y = 9
    assert x < y, 'Test Failed'
    
@pytest.mark.set4
def test_file1_method2b():
    x = 7
    y = 7
    assert x == y, 'Test Failed'

@pytest.mark.set5
def test_testarrosa(setup):
    x = 1
    assert x > setup[0], "test failed as x=" + str(x) + " and setup[0]=" + str(setup[0]) 
    
@pytest.mark.set6
def test_testarrosa2(setup):
    x = 3
    assert x == setup[2], "test failed"
    
@pytest.mark.parametrize('input1, input2, output', [(5, 5, 10), (3, 5, 1)])
def test_add(input1, input2, output):
    assert input1 + input2 == output, 'failed'

@pytest.fixture(params=[True, False])
def p_check_status(request):
    return request.param

@pytest.mark.status
def test_returning_status(p_check_status):
    assert p_check_status == True, "It is equal to False"
    
    
    