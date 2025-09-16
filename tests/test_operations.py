import pytest
from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(7, 6) == 42

def test_divide():
    assert divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
