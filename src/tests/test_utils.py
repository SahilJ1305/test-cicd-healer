from src.utils import add, divide

def test_add():
    assert add(1, 2) == 3

def test_add_negative():
    assert add(-1, -2) == -3

def test_divide():
    assert divide(10, 2) == 5.0

def test_divide_zero():
    import pytest
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)