from src.calculator import multiply, is_even, max_of_two

def test_multiply():
    assert multiply(3, 4) == 12

def test_multiply_zero():
    assert multiply(5, 0) == 0

def test_is_even_true():
    assert is_even(4) == True

def test_is_even_false():
    assert is_even(3) == False

def test_max_of_two_first():
    assert max_of_two(10, 5) == 10

def test_max_of_two_second():
    assert max_of_two(3, 7) == 7