import pytest

def test_demo():
    assert 'siddhant' == 'siddhant', 'both strings are equal'

@pytest.mark.test1
def test_demo2():
    assert 'siddhant mishra' == 'siddhant', 'both strings are not equal'